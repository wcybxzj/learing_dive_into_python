#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
from UserDict import UserDict

def __private_func():
	"""docstring for __private_func"""
	return '__private_func'

def stripnulls():
	"""docstring for stripnulls"""
	return data.replace("\00", "").strip()

class FileInfo(UserDict):
	"""store file meta"""
	def __init__(self, filename=None):
		UserDict.__init__(self)
		self["name"] = filename

class MP3FileInfo(FileInfo):
	"""docstring for MP3FileInfo"""
	__private_var = 'yangbingxi'
	__public_var__ = 'a pulic var'
	tagDataMap = {"title"   : (  3,  33, stripnulls),
			"artist"  : ( 33,  63, stripnulls),
			"album"   : ( 63,  93, stripnulls),
			"year"    : ( 93,  97, stripnulls),
			"comment" : ( 97, 126, stripnulls),
			"genre"   : (127, 128, ord)}
	#私有方法
	def __parse(self, filename):
		self.clear()
		try:
			fsock = open(filename, "rb", 0)
			try:
				fsock.seek(-128, 2)
				tagdata = fsock.read(128)
			finally:
				fsock.close()
			if tagdata[:3] == "TAG":
				for tag, (start, end, parseFunc) in self.tagData.items():
					self[tag] = parseFunc(tagdata[start:end])
		except IOError:
			pass

	def __setitem__(self, key, item):
		"""docstring for __setitem__"""
		if key == "name" and item:
			self.__parse(item)
		FileInfo.__setitem__(self, key , item)

	def test(self):
		"""docstring for __functest__"""
		return 'a public func'

	def __public_func(self):
		"""docstring for private_func"""
		return 'a private method'

	def __private_func2__(self):
		"""docstring for private_func"""
		return 'a public method'

def listDirectory(directory, fileExtList):
	""" get list of file info obj for
		file of particular extentsions"""
	fileList = [os.path.normcase(f)
			for f in os.listdir(directory)]
	#print fileList
	fileList = [ os.path.join(directory, f) \
			for f in fileList \
			if os.path.splitext(f)[1] in fileExtList ]
	#print fileList

	def getFileInfoClass(filename, \
			module=sys.modules[FileInfo.__module__]):
		"""docstring for getFileInfoClass"""
		#print module
		subclass = "%sFileInfo" % \
				os.path.splitext(filename)[1].upper()[1:]
		#print subclass
		return hasattr(module, subclass) \
				and getattr(module, subclass) or FileInfo
	return [getFileInfoClass(f)(f) for f in fileList]

if __name__ == '__main__':
	project_path = os.path.realpath('.')
	for info in listDirectory(project_path, [".mp3"]):
		print info
		print
