import os
import shutil
import stat

from pathlib import Path
from setuptools import setup
from setuptools.command.install import install


class PostInstallCommand(install):
    """Custom install command to install git hooks automatically."""

    def run(self) -> None:
        install.run(self)  # Run the regular install first

        try:
            git_dir: Path = self.find_git_root()
            hooks_dir: Path = git_dir / ".git" / "hooks"

            hook_templates: Path = Path(
                __file__
            ).parent / "src" / "readme_builder" / "templates" / "git_hooks"
            for hook_name in ["pre-commit", "pre-push"]:
                src_hook: Path = hook_templates / hook_name
                dest_hook: Path = hooks_dir / hook_name

                if not dest_hook.exists():
                    shutil.copy(src_hook, dest_hook)
                    os.chmod(
                        dest_hook, os.stat(dest_hook).st_mode | stat.S_IEXEC
                    )
                    print(f"Installed {hook_name} hook.")
                else:
                    print(f"{hook_name} hook already exists. Skipping...")

        except Exception as e:
            print(f"Failed to install Git hooks: {e}")

    def find_git_root(self) -> Path:
        current = Path.cwd().resolve()
        for parent in [current] + list(current.parents):
            if (parent / ".git").exists():
                return parent
        raise RuntimeError("Not inside a Git repository.")


setup(
    name="readme-builder",
    version="0.1.0",
    packages=["readme_builder"],
    package_dir={"": "src"},
    include_package_data=True,
    cmdclass={
        'install': PostInstallCommand,
    },
    # other setup metadata here
)
