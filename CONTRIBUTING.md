# Contributing to NeuroPulse Intelligence System

We welcome contributions from researchers, developers, and anyone interested in emergent AI and swarm intelligence! This document provides guidelines for contributing to the NeuroPulse project.

## Table of Contents

- [Getting Started](#getting-started)
- [How to Fork and Set Up](#how-to-fork-and-set-up)
- [Branch Naming Conventions](#branch-naming-conventions)
- [Commit Style Guidelines](#commit-style-guidelines)
- [Development Workflow](#development-workflow)
- [Code Style and Standards](#code-style-and-standards)
- [Testing Requirements](#testing-requirements)
- [Opening Issues](#opening-issues)
- [Pull Request Checklist](#pull-request-checklist)
- [Types of Contributions](#types-of-contributions)
- [Code of Conduct](#code-of-conduct)

## Getting Started

### Prerequisites

Before contributing, ensure you have:
- **Python 3.11+** installed via pyenv
- **Git** for version control
- **Basic understanding** of the NeuroPulse system (see README.md)
- **Development environment** set up as described in the main README

### Development Environment Setup

1. **Install pyenv** (if not already installed):
   ```bash
   # macOS
   brew install pyenv
   
   # Linux
   curl https://pyenv.run | bash
   ```

2. **Add pyenv to your shell profile**:
   ```bash
   echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
   echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
   echo 'eval "$(pyenv init -)"' >> ~/.bashrc
   source ~/.bashrc
   ```

## How to Fork and Set Up

### 1. Fork the Repository

1. Visit the NeuroPulse repository on GitHub
2. Click the **"Fork"** button in the top-right corner
3. Choose your GitHub account as the destination

### 2. Clone Your Fork

```bash
# Clone your fork locally
git clone https://github.com/YOUR_USERNAME/NeuralNetDisplay.git
cd NeuralNetDisplay

# Add the original repository as upstream remote
git remote add upstream https://github.com/ORIGINAL_OWNER/NeuralNetDisplay.git

# Verify remotes
git remote -v
```

### 3. Set Up Development Environment

```bash
# Install and set Python version
pyenv install 3.11.7
pyenv local 3.11.7

# Verify Python version
python3 --version

# Upgrade pip and install dependencies
python3 -m pip install --upgrade pip
pip3 install pygame numpy matplotlib pytest

# Verify installation
python3 -c "import pygame; print('Pygame version:', pygame.version.ver)"
```

### 4. Keep Your Fork Updated

```bash
# Fetch latest changes from upstream
git fetch upstream

# Switch to main branch and merge upstream changes
git checkout main
git merge upstream/main

# Push updates to your fork
git push origin main
```

## Branch Naming Conventions

Use descriptive branch names that follow these patterns:

### Feature Branches
```bash
feature/description-of-feature
feature/enhanced-pattern-matching
feature/gpu-acceleration
feature/3d-maze-navigation
```

### Bug Fix Branches
```bash
bugfix/description-of-fix
bugfix/memory-leak-in-pulses
bugfix/maze-boundary-collision
bugfix/pattern-adaptation-overflow
```

### Documentation Branches
```bash
docs/description-of-documentation
docs/api-reference-update
docs/installation-guide-improvements
docs/contributing-guidelines
```

### Experiment/Research Branches
```bash
experiment/description-of-experiment
experiment/genetic-algorithm-optimization
experiment/swarm-communication-protocols
experiment/hierarchical-pattern-matching
```

### Examples
```bash
# Good branch names
git checkout -b feature/multi-layer-neurobit-networks
git checkout -b bugfix/pulse-ttl-counter-reset
git checkout -b docs/performance-benchmarking-guide

# Avoid these patterns
git checkout -b fix        # Too vague
git checkout -b new-stuff  # Not descriptive
git checkout -b patch      # Unclear purpose
```

## Commit Style Guidelines

We follow the **Conventional Commits** specification for clear, structured commit messages.

### Commit Message Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer]
```

### Commit Types

- **feat**: New feature or enhancement
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, no logic changes)
- **refactor**: Code refactoring without feature changes
- **perf**: Performance improvements
- **test**: Adding or modifying tests
- **chore**: Maintenance tasks, dependency updates
- **experiment**: Experimental features or research

### Examples of Good Commit Messages

```bash
# Feature commits
feat(neurobit): add 16-bit pattern support for complex environments
feat(visualization): implement real-time 3D maze rendering
feat(pulse): add genetic algorithm for pattern evolution

# Bug fix commits
fix(maze): resolve boundary collision detection in sparse graphs
fix(memory): prevent memory leak in pulse population management
fix(pattern): correct bit mask application in trigger logic

# Documentation commits
docs(readme): add installation troubleshooting section
docs(api): update Neurobit class documentation with examples
docs(contributing): add branch naming conventions

# Performance commits
perf(pulse): optimize neighbor lookup algorithm for large mazes
perf(neurobit): reduce memory footprint from 32 to 16 bytes
perf(simulation): implement parallel processing for pulse populations

# Refactoring commits
refactor(graph): extract spatial encoding into separate utility class
refactor(tests): consolidate test fixtures for better maintainability
refactor(pulse): simplify TTL management logic

# Multi-line commit example
feat(adaptation): implement multi-modal learning mechanisms

- Add Hebbian learning for pattern reinforcement
- Implement anti-Hebbian learning for harmful pattern weakening
- Add homeostatic plasticity for system balance
- Include structural plasticity for connection modification

Closes #42, #45
Co-authored-by: Research Partner <partner@email.com>
```

### Commit Best Practices

1. **Use the imperative mood**: "Add feature" not "Added feature"
2. **Limit the first line to 50 characters** when possible
3. **Provide context in the body** for complex changes
4. **Reference issues and PRs** when relevant
5. **Co-author when collaborating**: Use `Co-authored-by:` footer
6. **Make atomic commits**: Each commit should represent one logical change

## Development Workflow

### 1. Start with an Issue

- Check existing issues before starting work
- Create a new issue if one doesn't exist
- Discuss approach in the issue before major changes

### 2. Create a Feature Branch

```bash
# Ensure you're on main and up-to-date
git checkout main
git pull upstream main

# Create and switch to your feature branch
git checkout -b feature/your-feature-name
```

### 3. Develop and Test

```bash
# Make your changes
# ... development work ...

# Run tests frequently
python3 -m pytest test_pulse.py -v

# Test the maze demo
python3 testMaze.py

# Check code style (if using linting tools)
# flake8 your_modified_files.py
```

### 4. Commit Your Changes

```bash
# Stage your changes
git add .

# Commit with descriptive message
git commit -m "feat(neurobit): add adaptive learning rate mechanism"

# Push to your fork
git push origin feature/your-feature-name
```

### 5. Create Pull Request

- Go to your fork on GitHub
- Click "New Pull Request"
- Fill out the PR template (see below)
- Link to related issues

## Code Style and Standards

### Python Code Style

Follow **PEP 8** guidelines with these specifics:

```python
# Good examples
def calculate_pattern_fitness(neurobit: Neurobit, 
                             environment_data: List[int],
                             success_threshold: float = 0.7) -> float:
    """Calculate fitness score based on environmental performance.
    
    Args:
        neurobit: The neurobit to evaluate
        environment_data: Binary patterns from environment
        success_threshold: Minimum success rate for positive fitness
        
    Returns:
        Fitness score between 0.0 and 1.0
    """
    if not environment_data:
        return 0.0
        
    matches = sum(
        1 for data in environment_data 
        if neurobit.trigger(data)
    )
    success_rate = matches / len(environment_data)
    
    return max(
        0.0, 
        (success_rate - success_threshold) / (1.0 - success_threshold)
    )
```

### Key Style Requirements

1. **Use descriptive variable names**:
   ```python
   # Good
   activation_threshold = 0.7
   neurobit_population = []
   
   # Avoid
   thresh = 0.7
   nb_pop = []
   ```

2. **Add comprehensive docstrings**:
   ```python
   def trigger_pattern_match(self, input_data: int) -> bool:
       """Check if input data matches neurobit's pattern.
       
       Args:
           input_data: 8-bit binary input to match against
           
       Returns:
           True if pattern matches after applying mask
           
       Example:
           >>> nb = Neurobit(pattern=0b11110000, mask=0b11110000)
           >>> nb.trigger_pattern_match(0b11110001)
           True
       """
   ```

3. **Use type hints** where helpful:
   ```python
   from typing import List, Optional, Dict, Tuple
   
   def create_pulse_population(size: int, 
                              patterns: List[int],
                              maze_graph: Dict[Tuple[int, int], List[Tuple[int, int]]]) -> List[NeuroPulse]:
   ```

4. **Keep functions focused** on single responsibilities
5. **Use constants** for magic numbers:
   ```python
   # Good
   DEFAULT_TTL = 50
   MAX_PATTERN_VALUE = 0xFF
   EXPLORATION_RATE = 0.15
   
   # Avoid inline magic numbers
   pulse = NeuroPulse(pos, neurobit, graph, ttl=50)  # What is 50?
   ```

## Testing Requirements

### Running Tests

```bash
# Run all tests
python3 -m pytest test_pulse.py -v

# Run specific test
python3 -m pytest test_pulse.py::TestNeurobit::test_pattern_matching -v

# Run with coverage (if installed)
python3 -m pytest --cov=neurobit_walker test_pulse.py
```

### Writing Tests

Add tests for all new functionality:

```python
import pytest
from neurobit_walker import Neurobit, NeuroPulse

class TestNewFeature:
    """Test suite for new feature implementation."""
    
    def test_basic_functionality(self):
        """Test basic feature behavior."""
        # Arrange
        neurobit = Neurobit(id=1, pattern=0b11110000)
        
        # Act
        result = neurobit.new_method(input_data=0b11110001)
        
        # Assert
        assert result is True
        assert neurobit.state == 1
    
    def test_edge_cases(self):
        """Test edge cases and error conditions."""
        neurobit = Neurobit(id=1, pattern=0b00000000)
        
        # Test with invalid input
        with pytest.raises(ValueError):
            neurobit.new_method(input_data=-1)
    
    def test_performance_requirements(self):
        """Test that performance requirements are met."""
        import time
        
        neurobit = Neurobit(id=1, pattern=0b11111111)
        
        start_time = time.time()
        for _ in range(1000):
            neurobit.new_method(input_data=0b11111111)
        duration = time.time() - start_time
        
        assert duration < 0.1  # Should complete in less than 100ms
```

### Test Categories

1. **Unit Tests**: Test individual functions and methods
2. **Integration Tests**: Test component interactions
3. **Performance Tests**: Verify speed and memory requirements
4. **System Tests**: End-to-end functionality tests

## Opening Issues

### Issue Types

Use these templates when creating issues:

#### Bug Report
```markdown
**Bug Description**
A clear description of what the bug is.

**Steps to Reproduce**
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior**
What you expected to happen.

**Actual Behavior**
What actually happened.

**Environment**
- OS: [e.g. macOS 13.0]
- Python Version: [e.g. 3.11.7]
- Pygame Version: [e.g. 2.1.0]

**Additional Context**
Add any other context about the problem here.
```

#### Feature Request
```markdown
**Feature Description**
A clear description of the feature you'd like to see.

**Use Case**
Describe the problem this feature would solve.

**Proposed Solution**
Describe how you envision this feature working.

**Alternatives Considered**
Describe alternatives you've considered.

**Additional Context**
Add any other context or screenshots about the feature request.
```

#### Research Question
```markdown
**Research Question**
What aspect of the NeuroPulse system would you like to investigate?

**Background**
What existing research or observations motivate this question?

**Proposed Approach**
How might we investigate this question?

**Expected Outcomes**
What insights do you hope to gain?

**Resources Needed**
What tools, data, or expertise would be helpful?
```

### Issue Labels

We use these labels to categorize issues:

- **Type Labels**: `bug`, `feature`, `documentation`, `research`, `performance`
- **Priority Labels**: `critical`, `high`, `medium`, `low`
- **Difficulty Labels**: `beginner-friendly`, `intermediate`, `advanced`, `research-level`
- **Component Labels**: `neurobit`, `pulse`, `maze`, `visualization`, `testing`
- **Status Labels**: `needs-discussion`, `ready-to-implement`, `in-progress`, `needs-review`

## Pull Request Checklist

Before submitting a pull request, ensure you've completed all applicable items:

### Pre-Submission Checklist

#### Code Quality
- [ ] **Code follows PEP 8 style guidelines**
- [ ] **All functions have descriptive docstrings**
- [ ] **Type hints are included where appropriate**
- [ ] **Variable names are descriptive and meaningful**
- [ ] **No commented-out code or debug print statements**
- [ ] **Code is properly organized into logical functions/classes**

#### Testing
- [ ] **All existing tests pass**: `python3 -m pytest test_pulse.py -v`
- [ ] **New functionality includes unit tests**
- [ ] **Edge cases are tested**
- [ ] **Performance requirements are met**
- [ ] **Manual testing completed**: `python3 testMaze.py`

#### Documentation
- [ ] **README.md updated if new features added**
- [ ] **Docstrings added for new functions/classes**
- [ ] **Code comments explain complex logic**
- [ ] **USAGE.md updated if user interface changes**

#### Git Practices
- [ ] **Commits follow conventional commit format**
- [ ] **Commit messages are descriptive**
- [ ] **Branch is up-to-date with main**: `git rebase upstream/main`
- [ ] **No merge commits in feature branch**
- [ ] **Branch name follows naming conventions**

#### Performance Considerations
- [ ] **Memory usage impact considered**
- [ ] **No performance regressions introduced**
- [ ] **Scalability implications assessed**
- [ ] **Profiling completed for performance-critical changes**

### Pull Request Template

When creating a PR, use this template:

```markdown
## Description

Brief description of the changes in this pull request.

## Type of Change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Related Issues

- Closes #[issue_number]
- Relates to #[issue_number]

## Changes Made

- List the main changes made
- Include any new files created
- Note any files deleted or significantly modified

## Testing

- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing completed
- [ ] Performance impact assessed

Describe the testing you've performed:

## Performance Impact

- Memory usage: [increase/decrease/no change]
- Execution speed: [faster/slower/no change]
- Scalability: [impact on large populations/mazes]

## Screenshots/Demos

If applicable, add screenshots or demo output showing the changes.

## Checklist

- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, particularly hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or my feature works
- [ ] New and existing unit tests pass locally with my changes

## Additional Notes

Any additional information that reviewers should know.
```

## Types of Contributions

We welcome various types of contributions:

### 1. Core Development
- **Algorithm Improvements**: Enhanced pattern matching, learning mechanisms
- **Performance Optimization**: Memory efficiency, computational speed
- **New Features**: 3D navigation, genetic algorithms, swarm communication
- **Bug Fixes**: Memory leaks, logic errors, edge cases

### 2. Research Contributions
- **Theoretical Analysis**: Mathematical models of neurobit behavior
- **Experimental Validation**: Comparisons with other AI approaches
- **Novel Applications**: Creative uses in robotics, games, cybersecurity
- **Performance Studies**: Scalability analysis and benchmarking

### 3. Documentation and Education
- **API Documentation**: Comprehensive function/class documentation
- **Tutorials**: Step-by-step guides for specific use cases
- **Examples**: Demonstration scripts for different scenarios
- **Educational Content**: Explanations of underlying concepts

### 4. Community Building
- **Issue Triage**: Helping categorize and prioritize issues
- **Code Review**: Reviewing pull requests from other contributors
- **Mentoring**: Helping new contributors get started
- **Discussion Leadership**: Facilitating technical discussions

### 5. Infrastructure and Tooling
- **CI/CD Improvements**: Automated testing and deployment
- **Development Tools**: Linting, formatting, debugging utilities
- **Packaging**: PyPI distribution, Docker containers
- **Monitoring**: Performance tracking and alerting systems

## Code of Conduct

### Our Commitment

We are committed to fostering an inclusive, respectful, and collaborative community where all contributors can participate safely and productively.

### Our Standards

**Positive behaviors include:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members
- Collaborating effectively across different backgrounds and expertise levels

**Unacceptable behaviors include:**
- Use of sexualized language or imagery and unwelcome sexual attention
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment of any kind
- Publishing others' private information without explicit permission
- Conduct which could reasonably be considered inappropriate in a professional setting
- Dismissing or attacking requests for support on diversity and inclusion

### Enforcement

Project maintainers are responsible for clarifying standards and will take appropriate corrective action in response to any instances of unacceptable behavior.

**Consequences may include:**
1. **Warning**: A private, written warning explaining the violation
2. **Temporary Suspension**: Temporary loss of interaction privileges
3. **Permanent Ban**: Permanent removal from all project spaces

### Reporting

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported to the project maintainers. All complaints will be reviewed and investigated promptly and fairly.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant](https://www.contributor-covenant.org/), version 2.1.

---

## Getting Help

If you need help with contributing:

1. **Read the Documentation**: Start with README.md and this contributing guide
2. **Check Existing Issues**: Someone might have already asked your question
3. **Join Discussions**: Participate in issue discussions and pull request reviews
4. **Ask Questions**: Create an issue with the `question` label
5. **Start Small**: Begin with `beginner-friendly` labeled issues

## Recognition

We value all contributions and will recognize contributors in:
- **README.md Contributors Section**: All contributors listed
- **Release Notes**: Major contributions highlighted
- **Research Papers**: Co-authorship for significant research contributions
- **Conference Presentations**: Speaking opportunities for major contributors

---

Thank you for contributing to the NeuroPulse Intelligence System! Together, we're pioneering the future of emergent AI through biomimetic pattern recognition.
