"""Tests for agent tools"""

import pytest
from agent.tools.code_generator import CodeGenerator
from agent.tools.git_ops import GitOps


class TestCodeGenerator:
    """Test code generation"""

    def setup_method(self):
        self.generator = CodeGenerator()

    def test_generate_python_module(self):
        """Test Python module generation"""
        code = self.generator.generate_python_module("test_module", "Test module")
        assert "class" in code
        assert "Test module" in code

    def test_generate_test_file(self):
        """Test file generation"""
        code = self.generator.generate_test_file("test_module")
        assert "def test_" in code
        assert "pytest" in code


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
