import sys
import os
import shutil
import json
from datetime import datetime

# Default categories
DEFAULT_MAPPING = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"],
    "Code": [".py", ".js", ".java", ".c", ".cpp", ".cs", ".html", ".css", ".php", ".rb", ".go", ".rs"],
    "Installers": [".exe", ".msi", ".apk", ".dmg"],
    "Others": []
}

def load_config(folder):
    """Load file_organizer_config.json if present to override categories."""
    config_path = os.path.join(folder, "file_organizer_config.json")
    if os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            normalized = {}
            for k, v in data.items():
                normalized[k] = [ext.lower() if ext.startswith(".") else f".{ext.lower()}" for ext in v]
            return normalized
        except Exception as e:
            print(f"Warning: Failed to load config file: {e}")
    return None

def build_extension_map(mapping):
    ext_map = {}
    for folder, exts in mapping.items():
        for ext in exts:
            ext_map[ext] = folder
    return ext_map

def ensure_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def unique_target_path(dest_folder, filename):
    """Ensures no overwrite by renaming duplicates."""
    base, ext = os.path.splitext(filename)
    candidate = filename
    counter = 1
    while os.path.exists(os.path.join(dest_folder, candidate)):
        candidate = f"{base} ({counter}){ext}"
        counter += 1
    return os.path.join(dest_folder, candidate)

def organize(folder):
    config = load_config(folder)
    mapping = DEFAULT_MAPPING.copy()
    if config:
        for k, v in config.items():
            if k in mapping:
                mapping[k] = list(set(mapping[k] + v))
            else:
                mapping[k] = v

    ext_map = build_extension_map(mapping)
    items = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    total = len(items)
    if total == 0:
        print("No files found to organize in", folder)
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_lines = [f"File Organizer run at {timestamp}", f"Target folder: {folder}", "-"*40]
    moved_count = 0

    for idx, filename in enumerate(items, 1):
        src = os.path.join(folder, filename)
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        dest_folder_name = ext_map.get(ext, "Others")
        dest_folder = os.path.join(folder, dest_folder_name)
        ensure_folder(dest_folder)

        target_path = unique_target_path(dest_folder, filename)
        try:
            shutil.move(src, target_path)
            moved_count += 1
            log_lines.append(f"MOVED: {filename} -> {dest_folder_name}/{os.path.basename(target_path)}")
            print(f"[{idx}/{total}] Moved: {filename} -> {dest_folder_name}")
        except Exception as e:
            log_lines.append(f"FAILED: {filename} -> {e}")
            print(f"[{idx}/{total}] Failed to move {filename}: {e}")

    log_lines.append("-"*40)
    log_lines.append(f"Total files processed: {total}")
    log_lines.append(f"Total files moved: {moved_count}")

    log_filename = os.path.join(folder, f"organizer_log_{timestamp}.txt")
    try:
        with open(log_filename, "w", encoding="utf-8") as lf:
            lf.write("\n".join(log_lines))
        print("\nDone. Log saved to:", log_filename)
    except Exception as e:
        print("Warning: Could not save log file:", e)

def default_downloads_folder():
    home = os.path.expanduser("~")
    candidates = [os.path.join(home, "Downloads"), os.path.join(home, "downloads")]
    for c in candidates:
        if os.path.exists(c):
            return c
    return home

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = default_downloads_folder()

    if not os.path.exists(target):
        print("Error: target folder does not exist:", target)
        sys.exit(1)

    print("Organizing folder:", target)
    organize(target)
