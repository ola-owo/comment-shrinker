#!/usr/bin/env python3
import sys, re

lines = []
newLines = []
docString = False # current line is a docstring
M = 79 # max line length, according to PEP-8 standard

with open(sys.argv[1], 'rt') as f:
#with open('sample1.py', 'rt') as f: #for use while debugging
    lines = f.readlines() #list of lines in the file

def fixline(line, typeof):
    comment = ''
    if typeof == 'docstring':
        findComment = line.find('#')
        if findComment != -1: #if it's a docstring w/a comment at the end
            # comment = line[findComment:]
            comment = re.search(r'\s*#.*$', line).group(0)
            line = line[:line.find(comment)]
        quoteChar = line.strip()[0] #either ['] or ["]
        if not line.strip().startswith(quoteChar * 3): #one-liner string
            stringStart = line.find(quoteChar)
            line = line[:stringStart] + quoteChar * 2 + line.strip() + quoteChar * 2
    endpoint = M - line[M-1::-1].find(' ') # last space on the line before column M
    if endpoint == M + 1: # str.find returned -1 (error)
        newLines.append(line)
        return
    splitA = line[:endpoint - 1] + '\n'
    splitB = line[endpoint:]
    if len(comment) and not len(splitB):
        newLines.append(splitA.strip('\n') + comment + '\n')
        return
    else:
        newLines.append(splitA)

    while len(splitB) > M:
        endpoint = M - splitB[M-1::-1].find(' ') # last space on the line before column M
        if endpoint == M + 1: # str.find returned -1 (error)
            break
        if typeof == 'docstring':
            splitA = splitB[:endpoint - 1] + '\n'
        else:
            splitA = '# ' + splitB[:endpoint - 1] + '\n'
        splitB = splitB[endpoint:]
        newLines.append(splitA)
    if typeof == 'comment':
        newLines.append('# ' + splitB)
    else:
        newLines.append(splitB.strip('\n') + comment + '\n')

for i in range(len(lines)):
    line = lines[i]
    if line.strip().startswith('#') and len(line) > M:
        fixline(line, 'comment')
    elif line.strip().startswith('def ') or line.strip().startswith('class '):
        if lines[i+1].strip().startswith('"') or lines[i+1].strip().startswith("'"):
            docString = not docString
            newLines.append(line)
    elif docString:
        docString = not docString
        fixline(line, 'docstring')
    else:
        newLines.append(line)

with open(sys.argv[2], 'wt') as f:
#with open('sample2.py', 'w+t') as f: #for use while debugging
    f.writelines(newLines)
