import xml.dom.minidom
import urllib.request



#isbnDBKey = "9KD2QLOO"
#baseURL = "http://isbndb.com/api/books.xml"
#suffixURL = "?access_key=" + isbnDBKey + "&index1=isbn&value1="
#
#request = urllib.request.urlopen(baseURL+suffixURL+"0205615597")
#
#
#document = xml.dom.minidom.parseString(request.read())
#
#print(document.getElementsByTagName("Title").item(0).childNodes[0].nodeValue)
#print(document.getElementsByTagName("AuthorsText").item(0).childNodes[0].nodeValue)
#print(document.getElementsByTagName("PublisherText").item(0).childNodes[0].nodeValue)
#print(document.getElementsByTagName("BookList").item(0).getAttribute("total_results"))
#
#document.unlink
#
baseURL = "http://books.google.com/books/feeds/volumes"
suffixURL = "?max-results=1&q=isbn:"

request = urllib.request.urlopen(baseURL+suffixURL+"0205615597")

document = xml.dom.minidom.parseString(request.read())

print(document.getElementsByTagName("dc:title").item(0).childNodes[0].nodeValue)
print(document.getElementsByTagName("dc:creator").item(0).childNodes[0].nodeValue)
print(document.getElementsByTagName("dc:publisher").item(0).childNodes[0].nodeValue)
print(document.getElementsByTagName("openSearch:totalResults").item(0).childNodes[0].nodeValue)

document.unlink