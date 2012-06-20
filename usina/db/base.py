from fabric.api import *

class SGBD(object):

	def __init__():
		self.command_start_client = ''
		self.command_select_db = 'use %(db_name)s;'

	@task
	def create():
		pass
	@task
	def drop():
		pass

