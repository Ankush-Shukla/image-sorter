import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from collections import defaultdict
from datetime import datetime

# Set your folder paths
input_folder = "./input images"      
output_folder = "sorted_media"

# Supported formats
image_exts = ('.jpg', '.jpeg', '.png')
video_exts = ('.mp4', '.mov', '.avi', '.mkv')  # Add more as needed

# Get EXIF "DateTimeOriginal" from image
def get_image_date(path):
    try:
        img = Image.open(path)
        exif = img.getexif()
        for tag_id, val in exif.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag == "DateTimeOriginal":
                return val
    except:
        pass
    return None

# Fallback: get modified file date
def get_file_date(path):
    timestamp = os.path.getmtime(path)
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

# Format to YYYY-MM
def extract_month_year(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y:%m:%d %H:%M:%S")  # EXIF format
    except:
        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")  # fallback format
    return dt.strftime("%Y-%m")

# Grouping
groups = defaultdict(list)

# Recursively walk through input_folder
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.lower().endswith(image_exts + video_exts):
            full_path = os.path.join(root, file)

            # Try EXIF (for images)
            date = get_image_date(full_path) if file.lower().endswith(image_exts) else None

            # Fallback to file timestamp
            if not date:
                date = get_file_date(full_path)

            folder_name = extract_month_year(date)
            groups[folder_name].append(full_path)

# Move files into output folder (by month)
for folder, files in groups.items():
    dest = os.path.join(output_folder, folder)
    os.makedirs(dest, exist_ok=True)
    for f in files:
        try:
            shutil.move(f, dest)  # Move instead of copy
            print(f"→ Moved: {f} → {dest}")
        except Exception as e:
            print(f"Error moving {f}: {e}")

print("\n Done! Files organized by month & moved.")
