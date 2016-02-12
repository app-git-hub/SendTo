import sublime, sublime_plugin

class SaveAllExistingFilesCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		for w in sublime.windows():
			self._save_files_in_window(w)
	def _save_files_in_window(self, w):
		for v in w.views():
			self._save_existing_file_in_view(v)
	def _save_existing_file_in_view(self, v):
		if v.file_name() and v.is_dirty():
				v.run_command("save")






r"""
append to file sublime plugin OR api
sublime save dirty file plugin stackoverflow
"""