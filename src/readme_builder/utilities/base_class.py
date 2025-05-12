import shutil
import os

from pathlib import Path
from typing import List


class BaseClass:
    """
    Contains functions shared acrosss multiple classes in the project.
    """
    def __init__(self, output_path: Path = Path("README.md")):
        self.project_root: Path = self.find_project_root()
        self.templates: Path = self.project_root / "project_templates"
        self.user_templates: Path = self.project_root / "templates"
        self.output_path: Path = output_path or self.project_root / "README.md"

    def find_project_root(
        self,
        start: Path = Path.cwd(),
        markers: List[str] = [
            ".git", "pyproject.toml", "README.md"
        ]
    ) -> Path:
        current: Path = start.resolve()

        for parent in [current] + list(current.parents):
            if any((parent / marker).exists() for marker in markers):
                return parent

        raise RuntimeError(f"Could not determine project root from: {current}")

    def get_template_file(self, template_name: str) -> None:
        """
        Moves the static template file (pre-commit or pre-push) from the
        `project_templates` directory into the user's `templates` directory.
        """

        template: Path = self.templates / template_name
        destination: Path = self.user_templates / template_name

        os.makedirs(self.user_templates, exist_ok=True)
        shutil.copy2(template, destination)

        print(f"Generated {template_name} template at: {destination}")
