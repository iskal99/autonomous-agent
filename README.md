# 🤖 Autonomous Agent

An AI-powered autonomous development agent that can analyze, plan, and execute development tasks autonomously.

## 🎯 Features

- **Task Analysis**: Automatically detect and classify development tasks
- **Task Decomposition**: Break complex tasks into manageable subtasks
- **Autonomous Execution**: Execute tasks without human intervention
- **Git Integration**: Automatic branch creation, commits, and pull requests
- **GitHub Integration**: Create issues and pull requests on GitHub
- **Code Generation**: Generate code, tests, and documentation
- **Comprehensive Logging**: JSON-based logging for all operations
- **Configuration Management**: Flexible configuration system

## 📋 Prerequisites

- Python 3.11+
- Git
- GitHub account with token (for GitHub integration)
- Anthropic API key (for AI capabilities)

## 🚀 Installation

```bash
git clone https://github.com/iskal99/autonomous-agent.git
cd autonomous-agent
pip install -r requirements.txt
cp .env.example .env
```

## 🔧 Configuration

### Environment Variables

```bash
GITHUB_TOKEN=your_github_token
GITHUB_REPOSITORY=owner/repo
ANTHROPIC_API_KEY=your_api_key
AGENT_DEBUG=false
AGENT_VERBOSE=true
```

## 💻 Usage

```python
from agent.core import AutonomousAgent

agent = AutonomousAgent()
result = agent.run("Create a new feature for user authentication")
```

## 🧪 Testing

```bash
pytest tests/ -v --cov=agent
```

## 📄 License

MIT License

---

**Made with ❤️ by iskal99**
