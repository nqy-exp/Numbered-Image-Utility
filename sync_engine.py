import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image 

class ThumbnailSyncHandler(FileSystemEventHandler):
    def __init__(self, source_dir, target_dir):
        self.source_dir = source_dir
        self.target_dir = target_dir
        # 确保目标文件夹存在
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir)

    def _generate_thumb(self, file_path):
        """生成高质量、真 WebP 格式的缩略图"""
        try:
            # 1. 获取不带后缀的文件名 (例如 "T01.jpg" -> "T01")
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            # 2. 强制构建以 .webp 结尾的新路径
            thumb_path = os.path.join(self.target_dir, f"{base_name}.webp")

            if not os.path.exists(thumb_path):
                with Image.open(file_path) as img:
                    img.thumbnail((300, 300)) 
                    # 保存为 WebP 格式
                    img.save(thumb_path, "WEBP", quality=75, method=6)
                print(f"[同步引擎] ✅ 已生成新缩略图: {base_name}.webp")
        except Exception as e:
            print(f"[同步引擎] ❌ 生成失败 {file_path}: {e}")

    def on_created(self, event):
        """当有新文件进入 images 文件夹时触发"""
        if not event.is_directory and event.src_path.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            print(f"[事件] 检测到新文件: {event.src_path}")
            time.sleep(0.5) # 稍微缓冲，等待文件写入完成
            self._generate_thumb(event.src_path)

    def on_deleted(self, event):
        """当有文件从 images 文件夹被删除时触发"""
        if not event.is_directory and event.src_path.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            # 1. 获取不带后缀的文件名
            base_name = os.path.splitext(os.path.basename(event.src_path))[0]
            # 2. 构建对应的缩略图路径
            thumb_path = os.path.join(self.target_dir, f"{base_name}.webp")
            
            if os.path.exists(thumb_path):
                try:
                    os.remove(thumb_path)
                    print(f"[同步引擎] 🗑️ 已清理对应的缩略图: {base_name}.webp")
                except PermissionError:
                    # 如果文件被占用，不崩溃，打印提示即可（等待下次启动自动清理）
                    print(f"[同步引擎] ⚠️ 无法删除缩略图 (文件可能正被浏览器占用): {base_name}.webp")
                except Exception as e:
                    print(f"[同步引擎] ❌ 删除缩略图出错 {base_name}.webp: {e}")

    def on_moved(self, event):
        """当文件被重命名或移动时触发"""
        if not event.is_directory:
            # 处理旧路径的删除逻辑 (通过伪造一个 src_path 对象)
            old_event = type('obj', (object,), {'src_path': event.src_path, 'is_directory': False})
            self.on_deleted(old_event)
            
            # 处理新路径的创建逻辑
            new_event = type('obj', (object,), {'src_path': event.dest_path, 'is_directory': False})
            self.on_created(new_event)

    def _cleanup_orphans(self):
        """【核心新增】反向清理：检查并删除没有对应原图的缩略图"""
        print(f"[系统] 🧹 正在扫描冗余缩略图...")
        if not os.path.exists(self.source_dir) or not os.path.exists(self.target_dir):
            return

        # 1. 获取源目录下所有图片文件的“不带后缀的名字”集合
        # 例如 images 里有 T01.jpg, T02.png -> source_bases = {"T01", "T02"}
        source_bases = set()
        for f in os.listdir(self.source_dir):
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                name_without_ext = os.path.splitext(f)[0]
                source_bases.add(name_without_ext)

        # 2. 遍历缩略图目录
        orphan_count = 0
        for thumb_file in os.listdir(self.target_dir):
            if thumb_file.lower().endswith('.webp'):
                thumb_base = os.path.splitext(thumb_file)[0]
                
                # 3. 如果缩略图的名字不在原图名字集合里，说明它是“孤儿”
                if thumb_base not in source_bases:
                    thumb_full_path = os.path.join(self.target_dir, thumb_file)
                    try:
                        os.remove(thumb_full_path)
                        print(f"[同步引擎] 🧹 已自动清理冗余缩略图 (无原图对应): {thumb_file}")
                        orphan_count += 1
                    except Exception as e:
                        print(f"[同步引擎] ⚠️ 清理冗余失败 {thumb_file}: {e}")
        
        if orphan_count > 0:
            print(f"[系统] 🧹 清理完成，共移除 {orphan_count} 个冗余文件。")
        else:
            print(f"[系统] 🧹 未发现冗余缩略图。")

def start_sync_service(source, target):
    """启动监听服务的入口函数"""
    event_handler = ThumbnailSyncHandler(source, target)
    observer = Observer()
    observer.schedule(event_handler, source, recursive=False)
    observer.start()

    # --- 【启动时的全量同步逻辑】 ---
    print(f"\n[系统] 🚀 正在进行初始同步扫描...")
    print(f"[系统] 监控目录: {os.path.abspath(source)}")
    print(f"[系统] 目标目录: {os.path.abspath(target)}\n")

    # 第一步：先执行反向清理（解决“僵尸缩略图”问题）
    event_handler._cleanup_orphans()

    # 第二步：进行正向扫描（补齐缺失的缩略图）
    count = 0
    if os.path.exists(source):
        for filename in os.listdir(source):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                full_path = os.path.join(source, filename)
                event_handler._generate_thumb(full_path)
                count += 1
    
    print(f"[系统] 初始扫描完成，共检查了 {count} 个原图文件。\n")
    return observer
