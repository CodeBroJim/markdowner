## Project Templates

Stores static files, examples and other template like files that users can rely on or that the project uses during the various file generation steps.

---

### Templates
1. context.toml
    - A context file used to parse values using Jinja. This is helpful for things like `project_name`, etc that are used in the actual user's project `README.md` file.
2. main.md
    - main.md serves as a template file that provides an example to users that helps them incorporate this package into their project with ease.
3. pre-commit
    - Used to generate the user level pre-commit .git file. This will allow users to run Markdowner every time they commit changes using `git commit`
4. pre-push
    - Used to generate the user level pre-commit .git file. This will allow users to run Markdowner every time they commit changes using `git push`

---
