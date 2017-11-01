# Copyright 2017 mengxi wang wmx@bu.edu
import sys

for i in sys.argv[1:5]:
	sys.stdout.write(i+"\n")
for j in sys.argv[5:len(sys.argv)]:
	sys.stderr.write(j+"\n")
