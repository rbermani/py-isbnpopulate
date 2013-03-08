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
baseURL = "http://books.google.com/books/feeds/volumes"
suffixURL = "?max-results=1&q=isbn:"

isbnWriter = csv.DictWriter(open('isbn_output.csv', 'a',encoding='utf-8'), ['isbn','author','title','publisher','price'], dialect='excel',quoting=csv.QUOTE_ALL,lineterminator='\n')

for row in isbnReader:
    time.sleep(0.4)
    while len(row['isbn']) < 10:
        row['isbn'] = "0" + row['isbn']

    rownew = {}
    rownew['isbn'] = row['isbn']
    rownew['price'] = row['price']
    try:
        request = urllib.request.urlopen(baseURL+suffixURL+row['isbn'])
        document = xml.dom.minidom.parseString(request.read())
    except:
        print("HTTPError")
        continue
    
    reply = document.getElementsByTagName("openSearch:totalResults").item(0).childNodes[0].nodeValue
    if (reply != '0'):
    #        print(document.getElementsByTagName("BookList").item(0).getAttribute("total_results"))
    #        print(row['isbn'])
        print(row['isbn'])
        try:
            rownew['author'] = str(document.getElementsByTagName("dc:creator").item(0).childNodes[0].nodeValue)
        except:
            print("Author List Indexing Error")
        
        
        rownew['title'] = str(document.getElementsByTagName("dc:title").item(0).childNodes[0].nodeValue)
        try:
            rownew['publisher'] = str(document.getElementsByTagName("dc:publisher").item(0).childNodes[0].nodeValue)
        except:
            print("Publisher Indexing Error")
        
            
        isbnWriter.writerow(rownew)
        
    

            
document.unlink


