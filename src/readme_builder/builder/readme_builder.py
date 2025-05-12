import os

from pathlib import Path
from typing import List

from src.readme_builder.utilities.base_class import BaseClass


class ReadmeBuilder(BaseClass):
    """
    Builds user's project level README.md file using a templates directory
    and user generated markdown files.
    """

    def __init__(self) -> None:
        super().__init__()
        self.template_path: Path = self.user_templates / "main.md"

    def _parse_include_line(self, line: str) -> str:
        """Extract the relative include path from the comment line."""
        return line.strip().split("<!-- INCLUDE:")[1].split("-->")[0].strip()

    def _process_lines(self, lines: List[str]) -> List[str]:
        """Build the README content, injecting included markdown files."""
        output_lines: List[str] = []

        for line in lines:
            if line.strip().startswith("<!-- INCLUDE:"):
                rel_path: str = self._parse_include_line(line)
                include_path: Path = self.project_root / rel_path

                output_lines.append(f"<!-- BEGIN {rel_path} -->\n")
                if include_path.exists():
                    output_lines.append(include_path.read_text().strip())
                else:
                    output_lines.append(f"Missing file: {rel_path}")
                output_lines.append(f"\n<!-- END {rel_path} -->")
            else:
                output_lines.append(line)

        return output_lines

    def build_readme(self) -> None:
        if not self.template_path.exists():
            raise FileNotFoundError(
                f"README template not found: {self.template_path}"
            )

        lines: List[str] = self.template_path.read_text().splitlines()
        final_content: List[str] = self._process_lines(lines)

        self.output_path.write_text("\n".join(final_content))
        print(f"README built at: {self.output_path}")

    def create_templates_dir(self) -> None:
        if not self.user_templates.exists():
            os.makedirs(self.user_templates)
