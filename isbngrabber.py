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

isbnReader = csv.DictReader(open('isbnlist.csv'), delimiter=',', quotechar='"')

for row in isbnReader:
    while len(row['isbn']) < 10:
        row['isbn'] = "0" + row['isbn']

    outname = "images/" + row['isbn'] + ".jpg"
    
    if (not (os.path.isfile(outname))):
        url = "http://www.textbooksrus.com/viewimg.ashx?ft=medium&isbn=" + row['isbn'];
        #url = "http://images.textbooks.com/TextbookInfo/Covers/" + row['isbn'] + ".gif"
        
        try:
            f = urllib.request.urlopen(url)
            time.sleep(0.2)
        except urllib.error.URLError:
            print("HTTP 404 Error")
            time.sleep(0.2)
        else:
            outp = io.FileIO(outname, 'w')
            if (str(f.info()).find('jpeg') != -1):
                outp.write(f.read())
            



