import os
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".java", ".c", ".cpp"],
    "Others": []
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print(" Folder does not exist.")
        return

    for category in FILE_CATEGORIES.keys():
        category_path = os.path.join(folder_path, category)
        os.makedirs(category_path, exist_ok=True)
        
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            moved = False

            for category, extensions in FILE_CATEGORIES.items():
                if ext.lower() in extensions:
                    shutil.move(file_path, os.path.join(folder_path, category, filename))
                    print(f" Moved: {filename} → {category}")
                    moved = True
                    break

            if not moved:  # Uncategorized files
                shutil.move(file_path, os.path.join(folder_path, "Others", filename))
                print(f" Moved: {filename} → Others")

    print("\n File organization complete!")


if __name__ == "__main__":
    print("=== File Organizer Tool ===")
    folder = input("Enter the folder path to organize: ").strip()
    organize_files(folder)
