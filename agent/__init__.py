"""Autonomous Agent Package"""

__version__ = "1.0.0"
__author__ = "iskal99"
__description__ = "AI-powered autonomous agent for development automation"

from agent.core import AutonomousAgent
from agent.logger import setup_logger

__all__ = ["AutonomousAgent", "setup_logger"]
