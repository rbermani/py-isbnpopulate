# Copyright (c) 2007 Robert Bermani (bobbermani@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import urllib.request
import io
import csv
import os.path
import time
import xml.dom.minidom


isbnReader = csv.DictReader(open('isbnlist.csv'), delimiter=',', quotechar='"')
isbnDBKey = "AHDEZKOE"
baseURL = "http://isbndb.com/api/books.xml"
suffixURL = "?access_key=" + isbnDBKey + "&index1=isbn&value1="

isbnWriter = csv.DictWriter(open('isbn_output.csv', 'w'), ['isbn','author','title','publisher'], delimiter=',', quotechar='"')

for row in isbnReader:
    while len(row['isbn']) < 10:
        row['isbn'] = "0" + row['isbn']

    request = urllib.request.urlopen(baseURL+suffixURL+row['isbn'])
    document = xml.dom.minidom.parseString(request.read())

    reply = document.getElementsByTagName("BookList").item(0).getAttribute("total_results")
    if (reply != '0'):
    #        print(document.getElementsByTagName("BookList").item(0).getAttribute("total_results"))
    #        print(row['isbn'])
        try:
            row['author'] = document.getElementsByTagName("AuthorsText").item(0).childNodes[0].nodeValue
        except IndexError:
            print("Author List Indexing Error")
        
        
        row['title'] = document.getElementsByTagName("Title").item(0).childNodes[0].nodeValue
        try:
            row['publisher'] = document.getElementsByTagName("PublisherText").item(0).childNodes[0].nodeValue
        except IndexError:
            print("Publisher Indexing Error")
            
        isbnWriter.writerow(row)

            
document.unlink


