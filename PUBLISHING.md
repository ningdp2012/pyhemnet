# Publishing to PyPI Guide

This guide will help you publish the PyHemnet package to PyPI.

## Package Overview

This package includes:
- **Hemnet Data Access**: Access property sales data from Hemnet.se
- Clean Python API for accessing listings and sold properties
- Support for filtering by location and property types

## Prerequisites

1. Create accounts on:
   - [PyPI](https://pypi.org/account/register/)
   - [Test PyPI](https://test.pypi.org/account/register/) (recommended for testing)

2. Install required tools:
   ```bash
   pip install --upgrade build twine
   ```

## Before Publishing

1. **Update package metadata** in `pyproject.toml`:
   - Verify `authors` name and email
   - Update the GitHub repository URLs if needed
   - Update version number (currently 0.1.0)

2. **Update** `pyhemnet/__init__.py`:
   - Verify `__author__` matches your info
   - Update `__version__` if needed

3. **Update** `LICENSE`:
   - Verify copyright holder name

4. **Run tests**:
   ```bash
   pytest tests/ -v
   ```

## Building the Package

1. Navigate to the project directory:
   ```bash
   cd /home/denin1/swedish-scraper
   ```

2. Clean old builds:
   ```bash
   rm -rf dist/ build/ *.egg-info
   ```

3. Build the distribution packages:
   ```bash
   python -m build
   ```

   This will create:
   - `dist/pyhemnet-0.1.0.tar.gz` (source distribution)
   - `dist/pyhemnet-0.1.0-py3-none-any.whl` (wheel distribution)

## Testing on Test PyPI (Recommended)

1. Upload to Test PyPI:
   ```bash
   python -m twine upload --repository testpypi dist/*
   ```

2. Enter your Test PyPI credentials when prompted

3. Test installation in a new virtual environment:
   ```bash
   python -m venv test_env
   source test_env/bin/activate  # On Windows: test_env\Scripts\activate
   pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pyhemnet
   ```

4. Test the package:
   ```python
   from pyhemnet import HemnetScraper, HemnetItemType
   ```

5. Clean up:
   ```bash
   deactivate
   rm -rf test_env
   ```

## Publishing to PyPI

Once you've tested on Test PyPI and everything works:

1. Upload to PyPI:
   ```bash
   python -m twine upload dist/*
   ```

2. Enter your PyPI credentials when prompted

3. Your package is now live! Install it with:
   ```bash
   pip install pyhemnet
   ```

## Using API Tokens (Recommended)

Instead of username/password, use API tokens:

1. Generate a token on PyPI:
   - Go to Account Settings → API tokens
   - Click "Add API token"
   - Set scope to the entire account or specific project

2. Create `~/.pypirc`:
   ```ini
   [pypi]
   username = __token__
   password = pypi-YOUR-API-TOKEN-HERE

   [testpypi]
   username = __token__
   password = pypi-YOUR-TEST-API-TOKEN-HERE
   ```

3. Upload without prompts:
   ```bash
   python -m twine upload dist/*
   ```

## Updating the Package

When you need to release a new version:

1. Update version in `pyproject.toml` and `pyhemnet/__init__.py`
2. Update `README.md` with any new features or changes
3. Run tests: `pytest tests/ -v`
4. Delete old builds: `rm -rf dist/ build/ *.egg-info`
5. Build: `python -m build`
6. Check: `python -m twine check dist/*`
7. Upload: `python -m twine upload dist/*`

## Checking the Package

Before uploading, check if everything is correct:

```bash
python -m twine check dist/*
```

## Project Structure

```
pyhemnet/  (or swedish-scraper/ - local directory name)
├── pyhemnet/                   # Main package
│   ├── __init__.py             # Package initialization & exports
│   ├── hemnet.py               # Hemnet scraper implementation
│   ├── constants.py            # Constants (URLs, enums)
│   └── __pycache__/            # Python cache (ignored by git)
├── tests/                      # Test suite
│   ├── __init__.py
│   └── test_hemnet.py          # Hemnet scraper tests
├── pyproject.toml              # Package metadata & dependencies
├── README.md                   # Documentation
├── LICENSE                     # MIT License
├── MANIFEST.in                 # Include additional files
├── .gitignore                  # Git ignore rules
└── PUBLISHING.md               # This file
```

## Useful Commands

- Install in develop tests/ -v`
- Run tests with coverage: `pytest tests/ --cov=swedish_scraper`
- Format code: `black swedish_scraper/ tests/`
- Lint code: `flake8 swedish_scraper/ tests/`
- Check package: `python -m twine check dist/*`

## Important Notes

- Package name "swedish-scraper" must be available on PyPI
- If taken, consider alternatives: "hemnet-scraper", "swedish-property-scraper", etc.
- Update in pyproject.toml's `name` field
- Version numbers should follow [semantic versioning](https://semver.org/):
  - MAJOR.MINOR.PATCH (e.g., 1.2.3)
  - Increment MAJOR for breaking changes
  - Increment MINOR for new features
  - Increment PATCH for bug fixes
- Always test on Test PyPI first before publishing to PyPI
- **Important**: This package is for educational/learning purposes only
- Always respect Hemnet.se's terms of service and robots.txt
- Consider rate limiting and caching to minimize server load

## Legal & Ethical Considerations

⚠️ **Disclaimer**: This package is created for exploring web scraping technologies and learning purposes only. It is **not intended for production use** or commercial applications.

- Web scraping may be subject to legal restrictions in your jurisdiction
- Always review and comply with website terms of service
- Respect robots.txt directives
- Implement rate limiting and be considerate of server resources
- Cache results when possible to minimize requests
- Use at your own risk and responsibility
- Legal: Ensure compliance with Hemnet.se and Qasa.se's terms of service

## Resources

- [Python Packaging Guide](https://packaging.python.org/)
- [PyPI](https://pypi.org/)
- [Test PyPI](https://test.pypi.org/)
- [Twine Documentation](https://twine.readthedocs.io/)
