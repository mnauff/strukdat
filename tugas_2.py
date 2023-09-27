import os

# ANSI escape codes for color formatting
COLOR_RESET = "\x1b[0m"
COLOR_BOLD = "\x1b[1m"
COLOR_RED = "\x1b[31m"
COLOR_GREEN = "\x1b[32m"
COLOR_BLUE = "\x1b[34m"


def print_file_tree(path, indent=""):
    if not os.path.exists(path):
        print(
            f"{indent}{COLOR_RED}Error: Path tidak ada - {path}{COLOR_RESET}")
        return

    # Cek folder
    if os.path.isdir(path):
        print(
            f"{indent}{COLOR_BOLD}{COLOR_BLUE}>{os.path.basename(path)}{COLOR_RESET}")
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            print_file_tree(item_path, indent + "|   ")

    # Cek file
    else:
        print(f"{indent}{COLOR_GREEN}-{os.path.basename(path)}{COLOR_RESET}")


# Get the disk choice from the user
while True:
    disk_choice = input(
        "Masukkan disk (C, D, atau E) atau 'exit' untuk keluar: ").strip().upper()

    if disk_choice == 'EXIT':
        break
    elif disk_choice in ('C', 'D', 'E'):
        root_path = f"{disk_choice}:\\"
        folder_choice = input(
            f"Apakah Anda ingin memilih folder di dalamn {disk_choice}? (y/n): ").strip().lower()
        if folder_choice == 'y':
            while True:
                folder_choice = input(
                    f"Masukkan folder didalam {disk_choice}: ").strip()
                folder_path = os.path.join(root_path, folder_choice)
                if os.path.exists(folder_path) and os.path.isdir(folder_path):
                    print_file_tree(folder_path)
                    break
                else:
                    print(
                        f"Folder {disk_choice} tidak ditemukan.")
        elif folder_choice == 'n':
            print_file_tree(root_path)
        else:
            print("Pilihan tidak valid. Silakan masukkan 'y', 'n', or 'exit'.")
    else:
        print("Pilihan tidak valid. Silakan masukkan 'C', 'D', 'E', or 'exit'.")
