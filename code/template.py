import sublime, sublime_plugin

class $1Command(sublime_plugin.$2Command):
	def run(self$3):
		print("preliminary test>>\n\n\tIts Working! :)")
		$4





r"""
$1--- camelCase, starting with uppercase (as is the class naming
		convention), word describing what it does, say
		`HipHopCommand`. will be exposed to api as `hip_hop()`
		to call it use`view.run_command(hip_hop)`
$2--- either `Text` or `Application` or `
$3--- parameter list, if required
"""