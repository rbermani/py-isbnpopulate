py-isbnpopulate
===============

A quick python hack for page scraping a text book website to provide cover art images

isbnpopulate.py

Based on a CSV list containing ISBN numbers, this script extrapolates 
text book information, such as author, publisher, and title and saves
the output to a csv file. The data set used is pulled from 
http://isbndb.com

googleisbnpop.py

Serves the same function as above, but uses google as a dataset

isbngrabber.py

This script takes a csv file containing ISBN numbers as input and 
populates a directory with text book art of the respective ISBNs
