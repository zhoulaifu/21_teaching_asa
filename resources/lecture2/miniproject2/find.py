import os
import pprint
import logging
import argparse
from itertools import dropwhile
import re

def findAllFP(curline):
    myre="[0-9]*\.[0-9]+"
    return re.findall(myre,curline)

#is_comment or is_print
def isCommentOrHasPrint(s):
    return s.startswith('#') or s.startswith('//') or 'print' in s or 'scanf' in s

def getFiles2FP(rootdir):
    fp={}
    files_cpp=[]
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".cpp") or filepath.endswith(".c"):
                files_cpp.append(filepath)

    logging.debug("number of cpp files = {}".format(len(files_cpp)))
    files_cpp_main=[]
    for file_cpp in files_cpp:
        with open(file_cpp, encoding='utf-8',errors='ignore') as f:
            u=re.findall('\sint\smain\s*\(', f.read())
            if len(u)>0:
                files_cpp_main.append(file_cpp)
                logging.debug(file_cpp)
    logging.debug ("number of cpp files with main = {}".format(len(files_cpp_main)))

    logging.info("="*20)
    for f in files_cpp_main:
        with open(f,'r',encoding='utf-8',errors='ignore') as myfile:
            found_fp=[]
            for curline in dropwhile(isCommentOrHasPrint, myfile):
                if 'print' not in curline:
                    found_fp += findAllFP(curline)
                    if len(found_fp)>0:
                        fp[f]=found_fp
    return fp

if __name__=="__main__":
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('--path',default=".")
    args = parser.parse_args()
    rootdir= os.path.abspath(args.path)
    fp=getFiles2FP(rootdir)
    logging.info("file -> fpnumbers for those including main")
    logging.info(pprint.pformat(fp))
    logging.info("number of found cpp files with main and fp decimals = {}".format(len(fp)))
