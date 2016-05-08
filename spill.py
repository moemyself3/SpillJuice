#!/usr/bin/python
import os

with open("images.lis") as f:
    image = f.readlines()

listlen = len(image)

errsize = 2
errsize = str(errsize)

# mkdir for cleanup
newdir = "juice/matched_cats"
os.system("mkdir -p juice/matched_cats")

for num in range(0, listlen):
	catname = "juice/juice_cats/catalog" + str(num) + ".cat"
	image[num] = image[num].replace("\n","")
	exportname = image[num]+"_matched.cat"
	spillin = "ds9 %s -catalog cds II/336 -catalog import starbase %s -catalog match error %s arcsec -catalog match function 1and2 -catalog match unique no -catalog match return 1and2 -catalog match cds tool -catalog export tsv %s -exit" % (image[num], catname, errsize, exportname)

	os.system(spillin)

	# Move new cat to new dir
	cleanspill = "mv %s %s" % (exportname, newdir)
	os.system(cleanspill)

#	print(catname)
#	print(exportname)
#	print(cleanspill)
