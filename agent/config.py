"""Configuration management for the agent"""

import json
import os
from pathlib import Path
from typing import Dict, Any


class Config:
    """Configuration manager"""

    def __init__(self, config_file="config.json"):
        self.config_file = Path(config_file)
        self.config = self._load_config()
        self._load_env_vars()

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from JSON file"""
        if self.config_file.exists():
            with open(self.config_file, "r") as f:
                return json.load(f)
        return {}

    def _load_env_vars(self):
        """Load environment variables"""
        self.github_token = os.getenv("GITHUB_TOKEN", "")
        self.github_repo = os.getenv("GITHUB_REPOSITORY", "")
        self.anthropic_key = os.getenv("ANTHROPIC_API_KEY", "")
        self.debug = os.getenv("AGENT_DEBUG", "false").lower() == "true"
        self.verbose = os.getenv("AGENT_VERBOSE", "true").lower() == "true"

    def get(self, key: str, default=None) -> Any:
        """Get configuration value"""
        keys = key.split(".")
        value = self.config
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        
        return value if value is not None else default

    def set(self, key: str, value: Any):
        """Set configuration value"""
        keys = key.split(".")
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value

    def save(self):
        """Save configuration to file"""
        with open(self.config_file, "w") as f:
            json.dump(self.config, f, indent=2)

    @property
    def is_github_configured(self) -> bool:
        """Check if GitHub is configured"""
        return bool(self.github_token and self.github_repo)

    @property
    def is_anthropic_configured(self) -> bool:
        """Check if Anthropic is configured"""
        return bool(self.anthropic_key)


# Global config instance
config = Config()
