# FileX - Universal File Renaming Tool

![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux%20%7C%20Termux-lightgrey.svg)

A simple yet powerful Python script to batch rename files with sequential numbering. Perfect for organizing photos, documents, or any files!

## 📦 What's Included

- `FileX.py` - The main Python script
- `README.md` - This documentation file

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher (usually pre-installed on most systems)
- No additional installations needed!

### How to Run

1. **Download** the `FileX.py` file to your computer
2. **Open Terminal** (Mac/Linux) or **Command Prompt** (Windows)
3. **Navigate** to where you saved the file:
   ```bash
   cd path/to/your/folder
   ```

1. Run the script:
   ```bash
   python FileX.py
   ```

🎯 Step-by-Step Guide (What to Expect)

When you run FileX, here's exactly what will happen:

Step 1: Welcome Screen

```
📁 Universal File Renamer Tool 📁
========================================
```

Step 2: Choose Folder

```
Enter directory path [current folder]: 
```

· Press Enter to use current folder
· Or type a path like        C:\Users\YourName\Pictures or 
/home/username/photos

Step 3: Name Your Files

```
Enter base name (e.g., 'photos'): 
```

· Type a name like vacation, project, scans
· This becomes the base for all renamed files

Step 4: Starting Number

```
Start from number [1]: 
```

· Press Enter to start from 1
· Or type any number like 5 to start from 5

Step 5: Number Format

```
Number of digits (e.g., 2 for 01,02) [2]: 
```

· Press Enter for 2-digit format (01, 02, 03...)
· Or type:
  · 1 for 1, 2, 3...
  · 3 for 001, 002, 003...
  · 4 for 0001, 0002, 0003...

Step 6: Filter Files (Optional)

```
File pattern (e.g., '*.jpg' for only JPG files) [all files]: 
```

· Press Enter to rename ALL files
· Or type:
  · *.jpg - only JPG images
  · *.png - only PNG images
  · *.pdf - only PDF documents
  · *.mp4 - only MP4 videos
  · * - all files (same as pressing Enter)

Step 7: Preview Changes

```
🔍 Preview of changes (5 files):
------------------------------------------------------------
📄 IMG_1234.jpg → vacation_01.jpg
📄 photo.png → vacation_02.png
📄 document.pdf → vacation_03.pdf
📄 video.mp4 → vacation_04.mp4
📄 notes.txt → vacation_05.txt
```

Step 8: Confirm Renaming

```
⚠️  Proceed with renaming? (y/N): 
```

· Type y or yes to continue
· Type anything else or press Enter to cancel

Step 9: See Results

```
🔄 Renaming files...
✅ IMG_1234.jpg → vacation_01.jpg
✅ photo.png → vacation_02.png
✅ document.pdf → vacation_03.pdf
✅ video.mp4 → vacation_04.mp4
✅ notes.txt → vacation_05.txt

🎉 Done! 5 files renamed successfully!
```

📝 Real Examples

Example 1: Renaming Vacation Photos

Before:

```
DSC_0001.jpg
DSC_0002.jpg
DSC_0003.jpg
```

Command:

```
Enter directory path [current folder]: ./vacation_photos
Enter base name (e.g., 'photos'): hawaii
Start from number [1]: 1
Number of digits (e.g., 2 for 01,02) [2]: 3
File pattern (e.g., '*.jpg' for only JPG files) [all files]: *.jpg
```

After:

```
hawaii_001.jpg
hawaii_002.jpg
hawaii_003.jpg
```

Example 2: Organizing Documents

Before:

```
scan1.pdf
scan2.pdf
scan3.pdf
document_old.pdf
```

Command:

```
Enter directory path [current folder]: ./
Enter base name (e.g., 'photos'): contract
Start from number [1]: 10
Number of digits (e.g., 2 for 01,02) [2]: 2
File pattern (e.g., '*.jpg' for only JPG files) [all files]: *.pdf
```

After:

```
contract_10.pdf
contract_11.pdf
contract_12.pdf
contract_13.pdf
```

⚠️ Important Notes :-

1. FileX shows you a preview of all changes before renaming, making it completely safe to use.
2. The tool will never automatically overwrite existing files to prevent accidental data loss.
3. FileX works on all major platforms including Windows, macOS, Linux, and Android (via Termux).
4. It supports all file types including images, documents, videos, and files without extensions.
5. If you make a mistake, FileX shows a preview first and you can cancel at the confirmation step.
6. FileX currently only works in one folder at a time and cannot rename files in subfolders.
7. Files without extensions are handled perfectly and will be renamed like base_name_01, base_name_02, etc.
8. you can use FileX on your phone by installing Termux (Android) and Python, then running the script.
9. Ensure Python is installed by typing "python --version" in your terminal or command prompt.
10. Verify that you're in the correct folder when running the script by checking your current directory.
11. The target folder must contain files to rename - empty folders will not work with FileX.

📜 License

MIT License - feel free to use and modify for any purpose!
