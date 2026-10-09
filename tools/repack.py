#! /usr/bin/env python3
import os
import shutil
import subprocess
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Configure the project")
    parser.add_argument(
        "rom_file",
        help="built game",
    )
    parser.add_argument(
        "iso_file",
        help="iso game",
    )
    args = parser.parse_args()

    version_path = os.path.dirname(args.rom_file)
    volume_path = f"{version_path}/volume/"

    if os.path.exists(volume_path):
        shutil.rmtree(volume_path)
    shutil.copytree("volume/", volume_path)
    elf_bytes = None
    with open(f"{volume_path}FILES/SLES_519.33", "rb") as f:
        elf_bytes = f.read()[:0x80]
        f.close()
    write_bytes = None
    with open(args.rom_file, "rb") as x:
        write_bytes = x.read()
        x.close()
    with open(f"{volume_path}FILES/SLES_519.33", "wb") as f:
        f.write(elf_bytes+write_bytes)
        f.close()

    subprocess.run(["./tools/ps2iso", "pack", f"{volume_path}METADATA.json"])
    os.rename(f"{volume_path}OUTPUT.iso", args.iso_file)
    print(f"ISO created at {args.iso_file}!")
