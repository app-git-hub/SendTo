import sublime, sublime_plugin
from os.path import basename

class ListOpenFilesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = sublime.active_windows()
		views = window.views()
		fileNames = ""
		for view in views:
			if view and view.file_name():
				fileNames+= basename(view.file_name()) + '\n'
		window.new_file().insert(edit, 0, "List of open files:\n\n"+fileNames)




r"""
"\n".join(
			[basename(view.file_name()) for view in \
			sublime.active_windows().views() if view and view.file_name()]
		)
"""
r"""
[
	{"keys": ["ctrl+alt+l"], "command": "list_open_files"}
]
"""