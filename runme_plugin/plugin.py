from bs4 import BeautifulSoup, element
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options as c, Config
import os
import re
import json

class RunmeConfig(Config):
	repository = c.Type(str)
	docs_dir = c.Type(str, default="docs")
	badge_image = c.Type(str, default="https://badgen.net/badge/Run%20with/Stateful/67a88e")
	link_url = c.Type(str, default="https://runme.dev/api/runme")

class RunmePlugin(BasePlugin[RunmeConfig]):
	def __init__(self):
		pass

	def on_page_content(self, html, page, config, **kwargs):
		path = self.resolve_path(page)
		soup = BeautifulSoup(html, 'html.parser')
		runme_paragraphs = soup.find_all("p", string="run-with-runme")
		index = 0
		for paragraph in runme_paragraphs:
			anchor = soup.new_tag('a')

			anchor['href'] = f"{self.config.link_url}?repository={self.config.repository}&fileToOpen={path}&command=demo&cell={index}"
			anchor.string = '▶️'
			anchor['title'] = 'Run with runme'
			anchor['style'] = 'text-decoration: none; font-size: 1.5em; position: absolute; right: 1.6em; top: 0'

			next_sibling = paragraph.next_sibling
			while next_sibling and not isinstance(next_sibling, element.Tag):
				next_sibling = next_sibling.next_sibling

			lines_col, code_col = next_sibling.find_all('pre')
			if code_col:
				index += 1
				code_col.insert(0, anchor)


		modified_html = str(soup)
		modified_html = re.sub(r"<p>run-with-runme</p>", "", modified_html)
		return modified_html

	def on_page_markdown(self, markdown, files, page, config, **kwards):
		path = self.resolve_path(page)
		match = re.search(r"^(#+)(.*)", markdown, flags=re.MULTILINE)
		markdown = clean_runme_blocks(markdown)
		if match:
			heading = match.group(0)
			injected_markdown = f"[![]({self.config.badge_image})]({self.config.link_url}?repository={self.config.repository}&command=setup&fileToOpen={path})"
			new_markdown = markdown.replace(heading, f"{heading}\n{injected_markdown}\n", 1)
			return new_markdown
		else:
			return markdown

	def resolve_path(self, page):
		return f"{self.config.docs_dir}{os.sep}{page.file.src_path}"

def clean_runme_blocks(markdown):
	lines = markdown.split('\n')
	corrected_lines = []
	for line in lines:
		if line.startswith('```') and ' {' in line:
			lang_identifier, metadata_str = line.split(' {')
			lang = lang_identifier[3:].strip()
			metadata = json.loads('{' + metadata_str)
			corrected_lines.append("\nrun-with-runme\n")
			corrected_lines.append(f'```{lang}')
		else:
			corrected_lines.append(line)
	return '\n'.join(corrected_lines)
