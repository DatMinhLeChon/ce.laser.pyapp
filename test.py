from xml.dom.minidom import parse
import xml.dom.minidom

# Mo mot tai lieu XML document boi su dung minidom parser
def parse_xml(file_name, worksheet, sheet_size):
    
    DOMTree = xml.dom.minidom.parse(file_name)
    collection = DOMTree.documentElement
    if collection.hasAttribute("shelf"):
        collection.getAttribute("shelf")

    # Lay tat ca phim trong bo suu tap
    tags = collection.getElementsByTagName("tag")

    # in chi tiet ve moi phim.
    for tag in tags:
        for i in range(sheet_size):
        if movie.hasAttribute("title"):
            worksheet[i][7] == movie.getAttribute("title")
            
        type = movie.getElementsByTagName('type')[0]
        print "The loai: %s" % type.childNodes[0].data
        format = movie.getElementsByTagName('format')[0]
        print "Dinh dang: %s" % format.childNodes[0].data
        rating = movie.getElementsByTagName('rating')[0]
        print "Rating: %s" % rating.childNodes[0].data
        description = movie.getElementsByTagName('description')[0]
        print "Gioi thieu: %s" % description.childNodes[0].data

def parseXML(xmlfile):
      
    # create element tree object
    tree = ET.parse(xmlfile)
  
    # get root element
    root = tree.getroot()
  
    # create empty list for news items
    newsitems = []
  
    # iterate news items
    for item in root.findall('./channel/item'):
  
        # empty news dictionary
        news = {}
  
        # iterate child elements of item
        for child in item:
  
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
  
        # append news dictionary to news items list
        newsitems.append(news)
      
    # return news items list
    return newsitems
  
  
def savetoCSV(newsitems, filename):
  
    # specifying the fields for csv file
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media']
  
    # writing to csv file
    with open(filename, 'w') as csvfile:
  
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames = fields)
  
        # writing headers (field names)
        writer.writeheader()
  
        # writing data rows
        writer.writerows(newsitems)
     
# main procesing function

file_name = "P3C globals.xml"

parse_xml(file_name, worksheet, 366)

