import os
import re
import chardet

def detect_encoding(file_path):
    with open(file_path, "rb") as f:
        raw_data = f.read()
        return chardet.detect(raw_data)['encoding']

def fix_turkish_chars(text):
    replacements = {
        "ý": "ı", "Ý": "İ", "þ": "ş", "Þ": "Ş", "ð": "ğ", "Ð": "Ğ"
    }
    for wrong, correct in replacements.items():
        text = text.replace(wrong, correct)
    return text

def clean_srt_format(text):
    text = re.sub(r"(\d{2}:\d{2}:\d{2})\.(\d{3})", r"\1,\2", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text

def fix_srt_file(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".srt"):
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename)
            
            encoding = detect_encoding(input_file_path)
            
            with open(input_file_path, "r", encoding=encoding) as f:
                content = f.read()
            
            content = fix_turkish_chars(content)
            content = clean_srt_format(content)
            
            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(content)
            
            print(f"Fixed file saved: {output_file_path}")

if __name__ == "__main__":
    input_folder = "subtitles"
    output_folder = "subtitles_fixed"
    fix_srt_file(input_folder, output_folder)
