"""

"""
import pymongo
import xml.etree.cElementTree
import xml.etree.cElementTree as ET
from DB.MongoDB import MongoDB
import xmltodict
import pprint
import json

class parser:

    def __init__(self):
        print 'inside init of parser'

    def parse(self,source,uri):
        print 'inside parse'
        inBulkCmConfigDataFile = False
        inConfigData = False

        for event, elem in ET.iterparse(source, events=("start", "end")):
            if event == 'start' and elem.tag == "bulkCmConfigDataFile":
                inBulkCmConfigDataFile = True
            if event == 'end' and elem.tag == "bulkCmConfigDataFile":
                inBulkCmConfigDataFile = False
                elem.clear()
            if inBulkCmConfigDataFile:
                if event == 'start' and elem.tag == 'configData':
                    inConfigData = True
                    cvss = ''
                if event == 'start' and inConfigData:
                    if event == 'start' and elem.tag == 'cvss_base_score':
                        cvss = elem.text
                if event == 'end' and elem.tag == 'configData':
                    print cvss
                    inConfigData = False
        data =""
        self.storeDB(data,uri)

    def parse1(self,source,uri):
        file = open(source);
        doc = xmltodict.parse(file.read(), process_namespaces=True)
        print(type(doc))
        #self.storeDB(doc, uri)
        pp = pprint.PrettyPrinter(indent=4)
        print "data is"
        data = json.dumps(doc)
        datajson = json.loads(data)
        #print datajson
        print(type(datajson))
        self.storeDB(data, uri)

    def storeDB(self, data,uri):
        print 'inside storeDB'
        db = MongoDB(uri, "mylib")
        print " Connection to MongoDB successful"

       #data converted into document
        db.insert(data)

        print " Data is successfully stored in DB"