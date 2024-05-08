---
runme:
  id: 01HXCP9T32MB8P6770TB4EC4TF
  version: v3
---

# Mkdocs Runme Plugin

## Features:

1. Automatically Creates Badge for Runme
2. Secures Fenced Code Blocks for flawless rendering

## Setup

### Virtual Environment (venv)

To create a virtual environment for your Mkdocs project, you can follow these steps:

1. Open a terminal or command prompt.
2. Navigate to your project directory:
3. Create a new virtual environment:

```sh {"id":"01HXCP9T32MB8P6770SXWQAYBH","name":"venv-new"}
python3 -m venv venv
```

4. Activate the virtual environment:

- On macOS and Linux:

```sh {"id":"01HXCP9T32MB8P6770SYDK3A3K","name":"venv-activate"}
source venv/bin/activate
```

- On Windows:

```sh {"id":"01HXCP9T32MB8P6770T1WK2WCM","name":"venv-activate-win"}
venv\Scripts\activate
```

5. Install the required packages:

```sh {"id":"01HXCP9T32MB8P6770T5D7S3D9","name":"dependencies"}
pip install -r requirements.txt
```

6. Now you can proceed with running the Mkdocs server or building the documentation.
7. When you're done, you can deactivate the virtual environment:

```sh {"id":"01HXCP9T32MB8P6770T73T5M6K","name":"venv-deactivate"}
deactivate
```

That's it! You have successfully set up a virtual environment for your Mkdocs project.

### Installing

Install python module

```sh {"id":"01HXCP9T32MB8P6770T8HZ2SEA","name":"pip-install"}
pip install git+https://github.com/stateful/mkdocs-runme-plugin.git
```

Configuration

```yaml {"id":"01HXCPZGGV9Z5P545RQ11HGHDW"}
plugins:
  - runme:
      # Repository URL for generated badges
      repository: https://github.com/stateful/mkdocs-runme-plugin.git
```