from setuptools import setup, find_packages

setup(
	name='mkdocs-runme-plugin',
	version='0.0.1',
	packages=find_packages(),
	install_requires=[
		'beautifulsoup4>=4.12.3',
	],
	entry_points={
		'mkdocs.plugins': [
			'runme = runme_plugin.plugin:RunmePlugin',
		]
	}
)
