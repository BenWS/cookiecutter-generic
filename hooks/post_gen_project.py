"""Open the generated project folder after Cookiecutter finishes."""

import os
import platform
import subprocess
import sys
from pathlib import Path


def main() -> int:
    project_dir = Path.cwd()
    system = platform.system().lower()

    # try:
    #     if system == "windows":
    #         subprocess.run(["code", str(project_dir)], check=False)
    #     elif system == "darwin":
    #         subprocess.run(["code", str(project_dir)], check=False)
    #     else:
    #         subprocess.run(["code", str(project_dir)], check=False)
    # except Exception as exc:
    #     print(f"Warning: could not open generated folder: {exc}")
    
    print(f"Project generated at: {project_dir}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
