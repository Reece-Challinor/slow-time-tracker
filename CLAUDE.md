# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

- **Run app**: `python3 src/app.py`
- **Build static site**: `python3 src/freeze.py` 
- **Deploy to S3**: `python3 scripts/deploy_s3.py`
- **Install dependencies**: `pip install -r requirements.txt`
- **Tests**: `python3 -m unittest discover tests/`
- **Run single test**: `python3 -m unittest tests/test_file.py`

## Code Guidelines

- **Imports**: Group standard library, third-party, and local imports with a blank line between groups
- **Formatting**: Use 4-space indentation, 79-character line limit
- **Type hints**: Use Python type annotations (PEP 484) for function parameters and return values
- **Docstrings**: Include docstrings for all modules, classes, and functions (follow PEP 257)
- **Error handling**: Use try/except blocks with specific exception types
- **Naming**: Use snake_case for variables/functions, PascalCase for classes
- **File organization**: Keep related functionality in appropriate subdirectories (calculator/, visualizations/)
- **Constants**: Define constants in config/constants.py