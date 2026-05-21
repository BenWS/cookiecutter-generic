"""Open the generated project folder after Cookiecutter finishes."""

import os
import platform
import subprocess
import sys
from pathlib import Path


def main() -> int:
    project_dir = Path.cwd()
    
    command = "code ."

    return 0


if __name__ == "__main__":
    sys.exit(main())
