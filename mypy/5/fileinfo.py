#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys

class FileInfo(object):
    """docstring for FileInfo"""
    def __init__(self, arg):
        super(FileInfo, self).__init__()
            self.arg = arg

def listDirectory(directory, fileExtList):
    """ get list of file info obj for file of particular extentsions"""
    fileList = [os.path.normcase(f)
            for f in os.listdir(directory)]
    fileList = [ os.path.join(directory, f)
            for f in fileList
            if os.path.splitext(f)[1] in fileExtList ]
    #print fileList
    def getFileInfoClass(filename, module=sys.modules[FileInfo.__module__]):
        """docstring for getFileInfoClass"""
            subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]
            return hasattr(module, subclass) and getattr(module, subclass) or FileInfo
    return [getFileInfoClass(f)(f) for f in fileList]

def main():
    project_path = os.path.realpath('.')
    listDirectory(project_path, [".py"])

if __name__ == '__main__':
    main()
