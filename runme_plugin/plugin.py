from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options as c, Config
import os
import re
import json

class RunmeConfig(Config):
	repository = c.Type(str)
	docs_dir = c.Type(str, default="docs")

class RunmePlugin(BasePlugin[RunmeConfig]):
	def __init__(self):
		pass

	def on_page_markdown(self, markdown, files, page, config, **kwards):
		path = f"{self.config.docs_dir}{os.sep}{page.file.src_path}"
		# Find the first heading using regular expression
		match = re.search(r"^(#+)(.*)", markdown, flags=re.MULTILINE)

		# remove annotations in code blocks to avoid rendering issues
		markdown = clean_runme_blocks(markdown)

		# Check if a heading is found
		if match:
			# Capture the heading and its following text
			heading = match.group(0)

			# Create the markdown to inject
			injected_markdown = f"[![](https://badgen.net/badge/Run%20with/Runme/5B3ADF?icon=https://runme.dev/img/logo.svg)](https://runme.dev/api/runme?repository={self.config.repository}&fileToOpen={path})"

			# Inject the markdown after the heading
			new_markdown = markdown.replace(heading, f"{heading}\n{injected_markdown}\n")
			return new_markdown
		else:
			# No heading found, return original markdown
			return markdown


def clean_runme_blocks(markdown):
	lines = markdown.split('\n')
	corrected_lines = []
	for line in lines:
		if line.startswith('```') and ' {' in line:
			lang_identifier, metadata_str = line.split(' {')
			lang = lang_identifier[3:].strip()  # Extract language identifier
			metadata = json.loads('{' + metadata_str)  # Parse JSON metadata
			corrected_lines.append(f'```{lang}')
		else:
			corrected_lines.append(line)
	return '\n'.join(corrected_lines)
