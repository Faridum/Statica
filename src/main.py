import os
import shutil
import sys

from generate_page import generate_page


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


def generate_pages_recursive(
    dir_path_content: str,
    template_path: str,
    dest_dir_path: str,
    basepath: str,
):
    for item in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)

        if os.path.isfile(content_path):
            if content_path.endswith(".md"):
                dest_path = dest_path.replace(".md", ".html")

                generate_page(
                    content_path,
                    template_path,
                    dest_path,
                    basepath,
                )

        elif os.path.isdir(content_path):
            generate_pages_recursive(
                content_path,
                template_path,
                dest_path,
                basepath,
            )


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    if os.path.exists("docs"):
        shutil.rmtree("docs")

    copy_static_to_public("static", "docs")

    generate_pages_recursive(
        "content",
        "template.html",
        "docs",
        basepath,
    )


if __name__ == "__main__":
    main()