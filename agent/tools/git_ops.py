"""Git operations for the agent"""

import subprocess
from pathlib import Path
from agent.logger import setup_logger

logger = setup_logger(__name__)


class GitOps:
    """Handle git operations"""

    def __init__(self, repo_path="."):
        self.repo_path = Path(repo_path)

    def create_branch(self, branch_name: str):
        """Create a new branch"""
        try:
            subprocess.run(
                ["git", "checkout", "-b", branch_name],
                cwd=self.repo_path,
                check=True,
                capture_output=True,
                text=True
            )
            logger.info(f"✅ Branch created: {branch_name}")
        except subprocess.CalledProcessError as e:
            logger.error(f"❌ Failed to create branch: {e.stderr}")
            raise

    def commit(self, message: str, files: list = None):
        """Commit changes"""
        try:
            if files:
                subprocess.run(
                    ["git", "add"] + files,
                    cwd=self.repo_path,
                    check=True,
                    capture_output=True
                )
            else:
                subprocess.run(
                    ["git", "add", "-A"],
                    cwd=self.repo_path,
                    check=True,
                    capture_output=True
                )
            
            subprocess.run(
                ["git", "commit", "-m", message],
                cwd=self.repo_path,
                check=True,
                capture_output=True,
                text=True
            )
            logger.info(f"✅ Committed: {message}")
        except subprocess.CalledProcessError as e:
            logger.error(f"❌ Failed to commit: {e.stderr}")
            raise

    def push(self, branch_name: str):
        """Push branch to remote"""
        try:
            subprocess.run(
                ["git", "push", "origin", branch_name],
                cwd=self.repo_path,
                check=True,
                capture_output=True,
                text=True
            )
            logger.info(f"✅ Pushed: {branch_name}")
        except subprocess.CalledProcessError as e:
            logger.error(f"❌ Failed to push: {e.stderr}")
            raise
