import os
import shutil


def copy_static_to_public(src: str, dest: str):
    if not os.path.exists(dest):
        os.mkdir(dest)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):
            print(f"Copying: {src_path} -> {dest_path}")
            shutil.copy(src_path, dest_path)

        elif os.path.isdir(src_path):
            os.mkdir(dest_path)
            copy_static_to_public(src_path, dest_path)


def main():
    if os.path.exists("public"):
        shutil.rmtree("public")

    copy_static_to_public("static", "public")


if __name__ == "__main__":
    main()