import tomllib


from jinja2 import Template
from pathlib import Path
from typing import Dict, List

from readme_builder.utilities.base_class import BaseClass


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

    def _load_context(self) -> dict:
        context_file: Path = self.user_templates / "context.toml"

        if not context_file.exists():
            print("No context.toml found. Using default context.")
            return {}

        with context_file.open("rb") as f:
            return tomllib.load(f)

    def create_context_file(self):
        context_path: Path = self.user_templates / "context.toml"

        if not context_path.exists():
            self.user_templates.mkdir(exist_ok=True)
            context_path.write_text(
                'project_name = "Markdowner"\n'
                'author = "Your Name"\n'
                'description = "A modular markdown tool."\n'
            )
        else:
            print(f"context.toml already exists at: {context_path}")

    def build_readme(self) -> None:
        if not self.template_path.exists():
            raise FileNotFoundError(
                f"README template not found: {self.template_path}"
            )

        lines: List[str] = self.template_path.read_text().splitlines()
        processed_lines: List[str] = self._process_lines(lines)
        joined_text: str = "\n".join(processed_lines)
        context: Dict = self._load_context()
        template: Template = Template(joined_text)
        rendered: str = template.render(**context)

        self.output_path.write_text(rendered)

        print(f"README built at: {self.output_path}")
