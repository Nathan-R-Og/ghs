import os
import shutil
import subprocess
from glob import glob

if __name__ == "__main__":
    if os.path.exists("volume/"):
        shutil.rmtree("volume/")

    all_isos = [f for f in glob("*.iso") if os.path.isfile(f)]
    use_iso = all_isos[0]
    subprocess.run(["./tools/ps2iso", "unpack", use_iso])
    use_iso = os.path.basename(use_iso)
    os.rename(f"UNPACK_{use_iso}/", "volume/")
    shutil.copy("volume/FILES/SLES_519.33", "SLES_519.33")