"""Code generation utilities"""

from agent.logger import setup_logger

logger = setup_logger(__name__)


class CodeGenerator:
    """Generate code snippets and files"""

    def generate_python_module(self, name: str, description: str) -> str:
        """Generate a Python module"""
        code = f'''"""
{description}
"""


class {name.title()}:
    """Implementation of {name}"""

    def __init__(self):
        """Initialize {name}"""
        pass

    def run(self):
        """Run the {name}"""
        pass
'''
        logger.info(f"✅ Generated Python module: {name}")
        return code

    def generate_test_file(self, module_name: str) -> str:
        """Generate test file"""
        code = f'''"""Tests for {module_name}"""

import pytest


def test_{module_name}_basic():
    """Test basic functionality"""
    # TODO: Add tests
    pass
'''
        logger.info(f"✅ Generated test file: {module_name}")
        return code
