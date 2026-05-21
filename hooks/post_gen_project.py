"""Open the generated project folder after Cookiecutter finishes."""

import os
import platform
import subprocess
import sys
from pathlib import Path


def main() -> int:
    project_dir = Path.cwd()
    system = platform.system().lower()

    try:
        if system == "windows":
            os.startfile(str(project_dir))
        elif system == "darwin":
            subprocess.run(["open", str(project_dir)], check=False)
        else:
            subprocess.run(["xdg-open", str(project_dir)], check=False)
    except Exception as exc:
        print(f"Warning: could not open generated folder: {exc}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
