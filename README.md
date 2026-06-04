# About

This folder can be accessed locally at `Personal Processes\Generic Notes\Quick Notes.code-workspace`

# On Usage

This repository can be retrieve via the following command:

```powershell
cookiecutter gh:BenWS/cookiecutter-generic --output-dir "$story_file_path"
```

# Post-Generation Hook

Cookiecutter automatically runs hook scripts from the `hooks/` folder.

This template includes `hooks/post_gen_project.py`, which opens the generated project folder in File Explorer after creation.
