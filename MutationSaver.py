#SOL Parasite Mutation Saver

#urllib.request is a Python module for fetching URLs
import urllib.request
imgURL = "https://sol-parasites.s3.us-west-2.amazonaws.com/img/4021.jpg"

#Get current date
from datetime import date
today = date.today()

path = 'D:/SOL_Parasite_Mutations/'
parasite = '4021-'
filetype = '.jpg'

filename = path + parasite + str(today) + filetype
urllib.request.urlretrieve(imgURL, filename)
