# Image and Video Date Sorter

A simple Python script that automatically sorts your photos and videos into folders based on the date they were taken.

## 📂 What It Does

- Recursively scans a given folder (and all subfolders)
- Extracts the "Date Taken" from EXIF metadata for images
- Falls back to the file's last modified time if EXIF data is missing (useful for videos)
- Groups and moves media files into folders by **Year-Month** format (e.g., `2025-07`)
- Supports both images and videos:
  - Images: `.jpg`, `.jpeg`, `.png`
  - Videos: `.mp4`, `.mov`, `.avi`, `.mkv` (customizable)

## 🛠 Technologies Used

- Python 3
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/) for reading EXIF data
- `os`, `shutil`, and `datetime` modules

## ✅ Example

If your input folder contains:

```
trip_photos/
├── IMG_001.jpg  (taken on 2025-07-10)
├── IMG_002.jpg  (taken on 2025-08-03)
├── VIDEO_001.mp4 (created on 2025-07-10)
```

After running the script, you'll get:

```
sorted_media/
├── 2025-07/
│   ├── IMG_001.jpg
│   └── VIDEO_001.mp4
├── 2025-08/
│   └── IMG_002.jpg
```

## 📌 How to Use

1. **Install dependencies**  
   ```bash
   pip install Pillow
   ```

2. **Edit the script**  
   Set the `input_folder` variable to the path of your unsorted media folder.

3. **Run the script**  
   ```bash
   python sorter.py
   ```

4. Your media will be moved into organized folders inside `sorted_media/`.

> **Note:** To keep the original files instead of moving them, replace `shutil.move()` with `shutil.copy()` in the script.

## 💡 Customization

- Add more extensions in `image_exts` or `video_exts` as needed.
- Change the folder naming format (`%Y-%m`) to group by year only, or even by day.

## 📬 Suggestions & Feedback

This was a personal utility built to manage my own travel media more efficiently. If you have ideas for improvements, feel free to open an issue or submit a pull request.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
