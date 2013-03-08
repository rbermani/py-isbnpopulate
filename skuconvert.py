# Copyright (c) 2007 Robert Bermani (bobbermani@gmail.com)
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


import csv

skuReader = csv.DictReader(open('skulist.csv'), delimiter=',', quotechar='"')


fieldnames = ['sku']
skuWriter = csv.DictWriter(open('skuout.csv', 'w'), fieldnames, delimiter=',', quotechar='"',lineterminator='\n')

for row in skuReader:
    while len(row['sku']) < 10:
        row['sku'] = "0" + row['sku']
    
    d = {"sku":row['sku']}
    skuWriter.writerow(d)
