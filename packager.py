import os
import json
import shutil
import subprocess

current_build = os.environ.get("BUILD_PLATFORM")
with open("platforms.json", "r") as f:
    platforms = json.load(f)

if not os.path.exists("out"):
    os.mkdir("out")
shutil.copytree("pico_launcher", "out", dirs_exist_ok=True)
shutil.copytree("pico_loader", "out", dirs_exist_ok=True)

if "miniboot_paths" in platforms[current_build]:
    for i in platforms[current_build]["miniboot_paths"]:
        subprocess.run(f"cp -rf miniboot/{i} out", shell=True)
