"""Tests for autonomous agent core functionality"""

import pytest
from agent.core import AutonomousAgent, TaskPlanner, TaskExecutor


class TestTaskPlanner:
    """Test task planning"""

    def setup_method(self):
        self.planner = TaskPlanner()

    def test_detect_feature_task(self):
        """Test feature task detection"""
        task_type = self.planner.detect_task_type("Create new API endpoint")
        assert task_type == "feature"

    def test_detect_bugfix_task(self):
        """Test bugfix task detection"""
        task_type = self.planner.detect_task_type("Fix authentication bug")
        assert task_type == "bugfix"

    def test_detect_test_task(self):
        """Test detection of test tasks"""
        task_type = self.planner.detect_task_type("Improve test coverage")
        assert task_type == "test"

    def test_decompose_task(self):
        """Test task decomposition"""
        subtasks = self.planner.decompose_task("feature", "Create new feature")
        assert len(subtasks) > 0
        assert isinstance(subtasks, list)


class TestTaskExecutor:
    """Test task execution"""

    def setup_method(self):
        self.executor = TaskExecutor()

    def test_executor_initialization(self):
        """Test executor initialization"""
        assert self.executor is not None
        assert self.executor.results == []


class TestAutonomousAgent:
    """Test main agent functionality"""

    def setup_method(self):
        self.agent = AutonomousAgent()

    def test_agent_initialization(self):
        """Test agent initialization"""
        assert self.agent is not None
        assert self.agent.planner is not None
        assert self.agent.executor is not None

    def test_analyze_task(self):
        """Test task analysis"""
        analysis = self.agent.analyze_task("Create a new feature")
        assert "type" in analysis
        assert "subtasks" in analysis
        assert analysis["type"] == "feature"
        assert len(analysis["subtasks"]) > 0

    def test_task_complexity_estimation(self):
        """Test complexity estimation"""
        simple = self.agent.analyze_task("Simple fix")
        complex_task = self.agent.analyze_task("Large feature with many components")
        
        assert simple["estimated_time_minutes"] <= complex_task["estimated_time_minutes"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
