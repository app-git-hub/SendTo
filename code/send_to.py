import sublime, sublime_plugin
import os

openFiles = list()

generateOpenFileList = lambda : [view.file_name() for view in sublime.activewindows().views() if view and view.file_name()]




"""the folloing function has been beautifully resolved by os.commonpath seek `path1()` and `path2()` functions in all code"""
# def chopCommonParts(pathList):	# defaults to trailing uncommonness, change user.setting to set it to leading
# 	div = os.sep
# 	newList = pathList
# 	uncommons = ["" for _ in newList]	# cuz newList is same as pathList
# 	while True:	# no 2 paths can be exactly same, so loop ain't infinite. still set it to count<max([len(_) for _ in pathList])
# 		for i in range(len(newList)):
# 			uncommons[i] = os.path.pardir(newList[i]) + div + uncommons[i]
# 		if len(uncommons) == set(uncommons).__len__():
# 			break
# 		else:
# 			newList = [div.join(_.split(div).pop()) for _ in newList]	# pop() will remove last value but return a string THEREFORE use list.remove(-1)
# 	for i in range(len(pathList)):
# 		uncommons[i] = os.path.basename(pathList[i]) + " in <" + uncommons[i] + ">"
# 	return uncommons

# def chopCommonParts(pathList, fromHead=True):
# 	frag = [[_.split(os.sep)] for _ in pathList]	# ["c:/a/z","c:/b/z"]-->[["c:","a","z"],["c:","b","z"]]
# 	if fromHead:
# 		fetchPoint = 0
# 		chopFrom, chopTo = 1, None
# 	else:
# 		fetchPoint = -1
# 		chopFrom, chopTo = None, -1
# 	while True:
# 		x = set([_[fetchPoint] for _ in frag])
# 		if len(x) > 1:
# 			break
# 		frag = [_[chopFrom:chopTo] for _ in frag]	# it should be--   [[_[1:]] for _ in frag] ??
# 	final = list()
# 	[final.append(os.sep.join(_)) for _ in frag]
# 	return final




























def resolveFileListRedundancy(pathList):
	betterFileList = list()
	for key, val in commons.items():
		if type(val) is list:
			temp = chopCommonParts(val)
			betterFileList+= [os.path.basename(val[i]) + " in <" + temp[i] + ">" for i in range(len(pathList))]
			del temp
		else:
			betterFileList.append(val)
	return betterFileList	#.sort()?

def refreshFileList():
	commons = dict()
	noDuplicateFileNames = True
	for _ in openFiles:
		fileName = os.path.basename(_)
		try:
			commons[fileName].append(_)	# call not ctor # commons.get(basename(x)).append(x)
		except TypeError:
			temp = commons[fileName]	# hold previous string value
			commons[fileName] = [temp]	# re-assign string value as 0th element in list
			commons[fileName].append(_)	# now append the new value
			noDuplicateFileNames = False
		except KeyError:
			commons[fileName] = _	# ctor not call
	if noDuplicateFileNames:
		return [_ for _ in commons.keys()]	# no need to execute reolveFi... portion
	else:
		return resolveFileListRedundancy(commons)

def detectChanges():
	global openFiles
	new = generateOpenFileList()
	# WHAT happens when a list is shuffled and then compared with its original form using "is"
	if new is openFiles:	# implies no file closed or new file opened since last scan
		return None
	else:
		openFiles = new
		return refreshFileList()

def rewriteContextMenu(fileList):
	''' populate `Context-Menu > Send To >` with values in fileList '''
	if fileList is None:
		return
	for i, aFile in enumerate(fileList):	# post-assumption--  betterFileList is perfectly parallel to global openFiles
		fileList[i] = r'{"caption": %(aFile)s, "command": "send_to", \
						"args": {"fileIndex": %d(i)}}' % locals()
	x = os.sep
	cm = x.join(os.path.abspath(".").split(x)[:-1]) + x + "Context.sublime-menu" # get path to `Browse Packages > User" folder
	with open(cm, mode="at+", encoding="UTF-8") as fh:
		fh.seek(172)
		fh.write(",".join(fileList) + "\n\t]\n}]\n\n\n\n")
	return

rewriteContextMenu(detectChanges())>>>THREAD, runs continuously at regular intervals, independently i.e. irrespective of command call
init-- run full rewriteContextMenu with refresh fileList
instead of processing entire file list compare it to old one
do processing only on the things that have changes
OR
why not jst ask sublimetext to alert me everytime a file is opened or closed


class SendToCommand(sublime_plugin.TextCommand):
	# append selected text to file pointed by user & prompt to save
	def run(self, fileIndex):	# what about view & args argument?
		if len(view.sels()) > 1:
			# open buffer before pasting so that multi-selections (some/most of which can be unintentionally selected) aren't sent
		for region in view.sel():
			if not region.empty():
				s = view.substr(region)	# get the selected text
		with open(openFiles[fileIndex], mode="at", encoding="UTF-8") as fh:
			fh.seek(END)
			fh.write("\n\n\n\n")
			fh.write(s)
		return











r"""
def resolveDuplicates(l):
	from collections import defaultdict
	commons = defaultdict()
	for i, val in enumerate(l):	commons[i].append(val)

class SendSel...
	def resolveFileList(self):
		openFiles = [basename(view.file_name()) for view in \
			sublime.active_windows().views() if view and view.file_name()]
		if len(openFiles) - len(list(set(openFiles))):
			openFiles = resolveDuplicates(openFiles)
		return openFiles
"""
r"""
		for view in sublime.activewindows().views():
			x = view.file_name()
			if view and x:
				try:
					commons[basename(x)].append(x)	# call not ctor # commons.get(basename(x)).append(x)
				except:
					commons[basename(x)] = [x]	# ctor not call
"""
r"""
for _ in [view.file_name() for view in sublime.activewindows().views() if view and view.file_name()]:
			fileName = os.path.basename(_)
			try:
				commons[fileName].append(_)	# call not ctor # commons.get(basename(x)).append(x)
			except TypeError:
				temp = commons[fileName]	# hold strng
				commons[fileName] = [temp]	# replace strng as list-of-string
				commons[fileName].append(_)	# append new path
			except KeyError:
				commons[fileName] = _	# ctor not call
"""
r"""
def resolve(paths):
	depth = 0
	a, b = max(enumerate(paths), key=operator.itemgetter(1))	#bit.do/bB3Qk
	old = b.count(os.sep) + 5
	for i, x in paths:
		new = x.split(os.sep)
		if len(new) < len(old):
			for _ in new:
				if _ in old:	continue
				else:	depth = new.index(_)	# break here?
		else:	pass
		old = new
	for i, x in paths:
		paths[i] = os.path.basename(x) + "in <" \
				os.sep.join(x.split(os.sep)[depth:]) + ">"
	return paths
"""
r"""

class PrepareContextMenuCommand():	#(sublime_plugin.TextCommand):
	global openFiles
	openFiles = [view.file_name() for view in sublime.activewindows().views() if view and view.file_name()]

	def resolveFileList(self):
		commons = dict()
		noDuplicateFileNames = True
		for _ in openFiles:
			fileName = os.path.basename(_)
			try:
				commons[fileName].append(_)	# call not ctor # commons.get(basename(x)).append(x)
				noDuplicateFileNames = False
			except KeyError:
				commons[fileName] = [_]	# ctor not call
		if noDuplicateFileNames:
			return [_ for _ in commons.keys()]	# no need to execute following portion
		betterFileList = list()
		for key, val in commons.items():
			try:
				val[1]
			except IndexError:
				betterFileList.append(val)
			betterFileList+= _resolve(val)
		return betterFileList	#.sort()?

	# populate `Context-Menu > Send To >` with values in betterFileList
	def populate(self, betterFileList):
		temp = list()
		for i, aFile in enumerate(betterFileList):	# post-assumption--  betterFileList is perfectly parallel to global openFiles
			temp.append(
				r'{"caption": %(aFile)s, "command": "send_to", "args": {"fileIndex": %d(i)}}' \
				% locals()
			)
		final = ",".join(temp) + "\n\t]\n}]" + "\n\n\n\n"
		del temp
		here = os.sep.join(os.path.abspath(".").split(os.sep)[:-1]) # get path to `Browse Packages > User" folder
		with open(here+"Context.sublime-menu", mode="at+", encoding="UTF-8") as fh:
			fh.seek(172)
			fh.write(final)
		return
	
	def run(self):
		populate(resolveFileList())
		return
"""