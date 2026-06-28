from pathlib import Path
import shutil
import sys

CATEGORY_MAP = {
    "images": {"jpg", "jpeg", "png", "gif", "bmp", "svg", "webp"},
    "documents": {"pdf", "doc", "docx", "txt", "xls", "xlsx", "ppt", "pptx"},
    "audio": {"mp3", "wav", "aac", "flac", "ogg"},
    "video": {"mp4", "mov", "avi", "mkv", "wmv", "flv"},
    "archives": {"zip", "rar", "7z", "tar", "gz", "bz2"},
    "code": {"py", "js", "ts", "java", "c", "cpp", "cs", "html", "css", "json", "xml"},
    "executables": {"exe", "msi", "bat", "cmd", "sh"},
}


def get_target_category(filepath: Path) -> str:
    """Return the category folder name for a file based on its extension."""
    if not filepath.is_file():
        return "others"

    extension = filepath.suffix.lower().lstrip(".")
    for category, extensions in CATEGORY_MAP.items():
        if extension in extensions:
            return category
    return "others"


def organize_download_folder(download_folder: Path) -> None:
    """Move files from the download folder into category subfolders."""
    if not download_folder.exists() or not download_folder.is_dir():
        raise ValueError(f"The path '{download_folder}' is not a valid directory")

    for item in download_folder.iterdir():
        if item.is_dir():
            continue

        category = get_target_category(item)
        destination_folder = download_folder / category
        destination_folder.mkdir(exist_ok=True)

        destination = destination_folder / item.name
        if destination.exists():
            destination = destination_folder / f"{item.stem}_1{item.suffix}"

        shutil.move(str(item), str(destination))
        print(f"Moved {item.name} -> {category}/{destination.name}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        downloads_path = Path(sys.argv[1])
    else:
        downloads_path = Path.home() / "Downloads"

    try:
        organize_download_folder(downloads_path)
        print("Download folder organization complete.")
    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)
