# Comment Shrinker v0.1

## Description
Comment Shrinker is a small Python script meant for shrinking comment lines down to a desired length. It automatically inserts newlines after the last word before the maximum line length. By default, Comment Shrinker shrinks all lines to 79 or less characters (according to PEP-8 standard).

## Usage
```
python comments.py inFile outFile
```
Simply type the above into any Unix terminal with Python installed. The Comment Shrinker will take inFile and output the fixed script to outFile. Additionally, a sample script, **sample1.py** is provided. **sample2.py** shows what sample1.py looks like after it has been passed through Comment Shrinker.
