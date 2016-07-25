try:
	from setuptools import setup
except ImportError:
	from disutils.core import setup
	
config = {
	'description' : 'My Project',
	'author' : 'George R Richardson',
	'url' : 'URL',
	'download_url' : 'DOWNLOAD'
	'author_email' : 'g.raymond.richardson@gmail.com',
	'version': '0.1',
	'install_requires' : ['nose'],
	'packages' : ['NAME'],
	'scripts' : [],
	'name' : 'projectname'
	}
	
setup(**config)