import os
import json

root = "assets/images/"
data = []

for dirpath, dirnames, filenames in os.walk(root):
    for filename in filenames:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            rel_path = os.path.relpath(os.path.join(dirpath, filename), '.')  # 相对路径
            category = os.path.basename(os.path.dirname(rel_path))  # 取图片的上一级文件夹作为类别
            data.append({
                "category": category,
                "filename": filename,
                "path": rel_path.replace('\\', '/')  # 替换为网页可用的正斜杠
            })

with open("images.json", "w") as f:
    json.dump(data, f, indent=2)

print(f"✅ 共生成 {len(data)} 个图像条目")
