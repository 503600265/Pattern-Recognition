import PIL 
import numpy as numpy
import os

from os import listdir
from matplotlib import image
from PIL import Image


# define a function that read an address of the directory 
def read_picture_data_set(adress):

	temp = [None]*(len(next(os.walk(adress))[1]))
	i = 0

	for foldername in listdir(adress):
	    loaded_images = list()
	    for filename in listdir(adress + "\\" +foldername):
	        
	        # check the image first 
	        # there are some files that are borken, we want to import them as a place holding matrix
	        size = os.stat(adress + "\\"+ foldername + "\\" + filename).st_size
	        if size != 0 : 
	            # load image
	            img_data = image.imread(adress + "\\"+ foldername + "\\" + filename)
	       
	        else: 
	            # if file is broken, just fill a place holding image
	            img_data = [  [[0,0,0] , [0,0,0]], [[0,0,0] , [0,0,0] ]]
	            
	        # store loaded image
	        loaded_images.append(numpy.array(img_data))
	        # print('> loaded %s %s' % (filename, img_data.shape))
	        
	    temp[i] = loaded_images
	    print('> loaded %s ' % (foldername))
	    i=i+1

# read all the folders of files in temp directory
# This should be the actual address of where you store the dataset in your computer
adress_temp = r"C:\Users\Administrator\Desktop\PRML\Project\fabric_data\temp"
read_picture_data_set(adress_temp)
print("Finish importing temp directory")

# read all the folders of files in trgt directory
# This should be the actual address of where you store the dataset in your computer
adress_trgt = r"C:\Users\Administrator\Desktop\PRML\Project\fabric_data\temp"
read_picture_data_set(adress_trgt)
print("Finish importing trgt directory")



import json
import glob, os

def load_fabric_data(path):
    '''
    Loads data from fabric_data folder.
    Returns:
        (list, list)
        A list of id in the file name
        A list of dictionary file containing data from json (flaw_type, bbox)

    Sample usage: fid, fdata = load_fabric_data('fabric_data/label_json/**/**.json')
    '''
    fid = []
    fdata = []
    for filename in glob.iglob(path, recursive=True):
        fid.append(filename.split('/')[-1].split('.')[0])
        with open(filename) as f:
            fdata.append(json.load(f))
    return (fid, fdata)
