# 🎬 SRT Turkish Character Fixer

This Python script fixes corrupted Turkish characters in `.srt` subtitle files and also cleans up formatting issues. It’s useful when dealing with subtitles that were saved in incorrect encodings or transferred between systems that don’t support Turkish characters properly.

## 🧰 Features

- Detects file encoding automatically
- Replaces broken Turkish characters with correct ones
- Cleans subtitle formatting (e.g., replaces dots with commas in timestamps)
- Saves fixed subtitles into a separate folder in UTF-8 format

## 📦 Requirements

- Python 3.x  
- `chardet` library  
  Install via pip:

  ```bash
  pip install chardet

## ▶️ How to Use
- Place all .srt files to be fixed into a folder named subtitles
- Run the script:

  ```bash
  python fix_srt.py
- Fixed subtitles will be saved in a folder named subtitles_fixed

## 📁 What It Does

- Automatically detects the encoding of each subtitle file

- Fixes corrupted Turkish characters such as:

- ý → ı, þ → ş, ð → ğ, etc.

- Replaces timestamp dots with commas (00:01:10.500 → 00:01:10,500)

- Saves cleaned files in UTF-8 encoding

## 🗂️ Output Folder Structure

  ```bash
  subtitles/
├── movie1.srt
├── movie2.srt

subtitles_fixed/
├── movie1.srt
└── movie2.srt
