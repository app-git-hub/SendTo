import sublime, sublime_plugin

class SelectedExample(sublimeplugin.TextCommand):
	def run(self, view, args):
		for region in view.sel():
			if not region.empty():
				s = view.substr(region)	# get the selected text
		# do processing on var s here
		view.replace(region, s)







r"""sublime selected text plugin OR api
sublimetext.com/docs/plugin-examples"""