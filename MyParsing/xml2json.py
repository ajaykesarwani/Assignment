"""xml2json.py
http://www.xml.com/pub/a/2006/05/31/converting-between-xml-and-json.html
XML                              JSON
<e/>                             "e": null
<e>text</e>                      "e": "text"
<e name="value" />               "e": { "@name": "value" }
<e name="value">text</e>         "e": { "@name": "value", "#text": "text" }
<e> <a>text</a ><b>text</b> </e> "e": { "a": "text", "b": "text" }
<e> <a>text</a> <a>text</a> </e> "e": { "a": ["text", "text"] }
<e> text <a>text</a> </e>        "e": { "#text": "text", "a": "text" }
"""


import json
import optparse
import sys
import os
from collections import OrderedDict

import xml.etree.cElementTree as ET
from PARSE.parser import parser
from DB.MongoDB import MongoDB
import pymongo
from pprint import pprint
import json


def readDB(uri):
    # read data from mongodb
    print "inside readDB"

    try:
        uri =""
        db = MongoDB(uri,"mylib")#pymongo.MongoClient('localhost', 27017)
        print "Connected Successfully!!!"
    except:
        print "Could not connect to MongoDB"
    #database
    #db_cm.remove()
    data = db.get()
    print "data type"
    print type(data)
    print 'data fetched successfully'
    response = []
    for doc in data:
        #print doc
        response.append(doc)

    print type(response)
    return json.dumps(response)


def storeDB(data, uri):
    # store data into mongodb
    print 'inside storeDB'
    document = json.loads(data)

    try:
        db = MongoDB(uri, "mylib")#pymongo.MongoClient('localhost', 27017)
        print "Connected Successfully!!!"
    except:
        print "Could not connect to MongoDB"
    #database
    #db_cm.remove()
    db.insert(document)
    print " Data is successfully stored in DB"


def strip_tag(tag):
    strip_ns_tag = tag
    split_array = tag.split('}')
    if len(split_array) > 1:
        strip_ns_tag = split_array[1]
        tag = strip_ns_tag
    return tag


def elem_to_internal(elem, strip_ns=1, strip=1):
    #Convert an Element into an internal dictionary (not JSON!).

    d = OrderedDict()
    elem_tag = elem.tag
    if strip_ns:
        elem_tag = strip_tag(elem.tag)
    for key, value in list(elem.attrib.items()):
        d['@' + key] = value

    # loop over subelements to merge them
    for subelem in elem:
        v = elem_to_internal(subelem, strip_ns=strip_ns, strip=strip)

        tag = subelem.tag
        if strip_ns:
            tag = strip_tag(subelem.tag)

        value = v[tag]

        try:
            # add to existing list for this tag
            d[tag].append(value)
        except AttributeError:
            # turn existing entry into a list
            d[tag] = [d[tag], value]
        except KeyError:
            # add a new non-list entry
            d[tag] = value
    text = elem.text
    tail = elem.tail
    if strip:
        # ignore leading and trailing whitespace
        if text:
            text = text.strip()
        if tail:
            tail = tail.strip()

    if tail:
        d['#tail'] = tail

    if d:
        # use #text element if other attributes exist
        if text:
            d["#text"] = text
    else:
        # text is the value if no attributes
        d = text or None
    return {elem_tag: d}


def internal_to_elem(pfsh, factory=ET.Element):

    #Convert an internal dictionary (not JSON!) into an Element.
    attribs = OrderedDict()
    text = None
    tail = None
    sublist = []
    tag = list(pfsh.keys())
    if len(tag) != 1:
        raise ValueError("Illegal structure with multiple tags: %s" % tag)
    tag = tag[0]
    value = pfsh[tag]
    if isinstance(value, dict):
        for k, v in list(value.items()):
            if k[:1] == "@":
                attribs[k[1:]] = v
            elif k == "#text":
                text = v
            elif k == "#tail":
                tail = v
            elif isinstance(v, list):
                for v2 in v:
                    sublist.append(internal_to_elem({k: v2}, factory=factory))
            else:
                sublist.append(internal_to_elem({k: v}, factory=factory))
    else:
        text = value
    e = factory(tag, attribs)
    for sub in sublist:
        e.append(sub)
    e.text = text
    e.tail = tail
    return e


def elem2json(elem, options, strip_ns=1, strip=1):

    #Convert an ElementTree or Element into a JSON string.

    if hasattr(elem, 'bulkCmConfigDataFile'):
        elem = elem.getroot()

    if options == "xml2json":
        return json.dumps(elem_to_internal(elem, strip_ns=strip_ns, strip=strip), indent=4, separators=(',', ': '))
    else:
        return json.dumps(elem_to_internal(elem, strip_ns=strip_ns, strip=strip))


def json2elem(json_data, factory=ET.Element):

    #Convert a JSON string into an Element
    return internal_to_elem(json.loads(json_data), factory)


def xml2json(xmlstring, options, strip_ns=1, strip=1):

    #Convert an XML string into a JSON string.

    elem = ET.fromstring(xmlstring)
    return elem2json(elem, options, strip_ns=strip_ns, strip=strip)


def json2xml(json_data, factory=ET.Element):

    """Convert a JSON string into an XML string."""

    if not isinstance(json_data, dict):
        json_data = json.loads(json_data)

    elem = internal_to_elem(json_data, factory)
    return ET.tostring(elem)


def main():
    inputstream = sys.stdin
    source = "C:\\Users\\ajkesarw\\PycharmProjects\\MyParsing\\venv\\file.xml"
    source1 = "C:\\Users\\ajkesarw\\PycharmProjects\\MyParsing\\venv\\XML\\ericsson_lte_enm_son_lte_discovery_v17A.xml"
    try:
        inputstream = open(source1)
    except:
        sys.stderr.write("Problem in opening the xml file")
        sys.exit(-1)

    #read xml file
    input = inputstream.read()

    options = "xml2json"
    strip_ns = 1
    strip = 1
    uri = ""
    if (options == "xml2json"):
        print "xml2json is called"
        out = xml2json(input, options, strip_ns, strip)
        storeDB(out,uri)

    print "data is successfully stored in DB "

    input = readDB(uri)
    #print input
    print 'data is fetched'
    options = "json2xml"
    print type(input)
    if (options == "json2xml"):
        print 'inside json2xml'
        out = json2xml(input)
        file = open(Test.xml, 'w')
        file.write(out)
        file.close()

if __name__ == "__main__":
    main()
