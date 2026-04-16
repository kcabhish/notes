# uv Command Reference (Python Package Management)

This document lists commonly used **uv** commands for managing Python projects, dependencies, and environments. The commands are grouped by use case and presented in a tabular format for quick reference.

---

## Project & Environment Management

| Command                 | Description                                  | Example                  |
| ----------------------- | -------------------------------------------- | ------------------------ |
| `uv init`               | Initialize a new Python project              | `uv init my-project`     |
| `uv venv`               | Create a virtual environment                 | `uv venv`                |
| `uv venv --python 3.12` | Create a venv with a specific Python version | `uv venv --python 3.12`  |
| `uv run <cmd>`          | Run a command inside the project environment | `uv run python main.py`  |
| `uv python install`     | Install Python versions                      | `uv python install 3.11` |
| `uv python list`        | List available and installed Python versions | `uv python list`         |
| `uv python pin`         | Pin a Python version for the project         | `uv python pin 3.12`     |

---

## Dependency Installation

| Command               | Description                              | Example                   |
| --------------------- | ---------------------------------------- | ------------------------- |
| `uv add <pkg>`        | Add a dependency to the project          | `uv add requests`         |
| `uv add <pkg> --dev`  | Add a development dependency             | `uv add pytest --dev`     |
| `uv add <pkg>==<ver>` | Add a dependency with a specific version | `uv add fastapi==0.110.0` |
| `uv remove <pkg>`     | Remove a dependency                      | `uv remove requests`      |
| `uv sync`             | Sync environment with lockfile           | `uv sync`                 |
| `uv sync --dev`       | Sync including dev dependencies          | `uv sync --dev`           |

---

## Lockfile & Reproducibility

| Command                           | Description                         | Example                            |
| --------------------------------- | ----------------------------------- | ---------------------------------- |
| `uv lock`                         | Generate or update the lockfile     | `uv lock`                          |
| `uv lock --upgrade`               | Upgrade all dependencies and relock | `uv lock --upgrade`                |
| `uv lock --upgrade-package <pkg>` | Upgrade a specific dependency       | `uv lock --upgrade-package django` |

---

## Package Execution & Tooling

| Command                    | Description                                   | Example                  |
| -------------------------- | --------------------------------------------- | ------------------------ |
| `uv tool run <tool>`       | Run a Python tool without installing globally | `uv tool run black .`    |
| `uv tool install <tool>`   | Install a CLI tool managed by uv              | `uv tool install ruff`   |
| `uv tool list`             | List installed uv tools                       | `uv tool list`           |
| `uv tool uninstall <tool>` | Remove an installed tool                      | `uv tool uninstall ruff` |

---

## pip-Compatible Commands

| Command                              | Description                        | Example                              |
| ------------------------------------ | ---------------------------------- | ------------------------------------ |
| `uv pip install <pkg>`               | Install a package (pip-compatible) | `uv pip install numpy`               |
| `uv pip install -r requirements.txt` | Install from requirements file     | `uv pip install -r requirements.txt` |
| `uv pip uninstall <pkg>`             | Uninstall a package                | `uv pip uninstall numpy`             |
| `uv pip list`                        | List installed packages            | `uv pip list`                        |
| `uv pip freeze`                      | Output installed packages          | `uv pip freeze`                      |

---

## Caching & Performance

| Command          | Description          | Example          |
| ---------------- | -------------------- | ---------------- |
| `uv cache dir`   | Show cache directory | `uv cache dir`   |
| `uv cache clean` | Clear the uv cache   | `uv cache clean` |

---

## Diagnostics & Info

| Command             | Description                 | Example        |
| ------------------- | --------------------------- | -------------- |
| `uv --version`      | Show uv version             | `uv --version` |
| `uv help`           | Show help information       | `uv help`      |
| `uv help <command>` | Help for a specific command | `uv help add`  |

---

## Notes

* `uv` is designed to be a **fast, modern replacement** for `pip`, `pip-tools`, `virtualenv`, and parts of `pyenv`.
* It uses a **lockfile-first** approach for reproducible builds.
* Most `pip` workflows can be replaced with `uv add`, `uv sync`, and `uv lock`.

---

