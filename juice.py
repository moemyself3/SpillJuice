#!/usr/bin/python
import os

with open("images.lis") as f:
    content = f.readlines()

listlen = len(content)

### For Testing ###
#print content[1]
#cmdstring = "sex %s" % (content[1])
#print cmdstring
#os.system(cmdstring)
##################

newdir = "juice/juice_cats"
newdir2 = "juice/juice_sex"
os.system("mkdir -p juice/juice_cats; mkdir -p juice/juice_sex;")
for num in range(0,listlen): 
	newsex = 'test' + str(num) + '.sex'
	newcat = 'catalog'+str(num)+'.cat'
	f1 = open('default.sex', 'r')
	f2 = open(newsex, 'w')
	for line in f1:
	    f2.write(line.replace('test.cat', newcat))
	f1.close()
	f2.close()
	
	cmdstring = "sex -c %s %s" % (newsex, content[num])
	os.system(cmdstring)
	cmdstring2 = "mv %s %s; mv %s %s" % (newcat, newdir, newsex, newdir2)
	os.system(cmdstring2)
