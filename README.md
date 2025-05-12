# Markdowner

A Python command-line tool designed to automate the generation of `README.md` files from modular Markdown templates. Ideal for projects that maintain documentation in separate files and require a streamlined method to compile them into a single and structured `README` file.

---

## Installation

Install the package using pip:

```bash
pip install markdowner
```

---

## Usage

After installation, you can use the CLI tool to build your project's README.md from all specified .md files in your project:

```bash
downer build-readme
```

This command will:
    - Locate your project's root directory.
    - Search for a `main.md` template in the `templates/` directory.
    - Compile the template and included Markdown files into a single `README.md` at the project root.

---
