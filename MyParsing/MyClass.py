
import os
import sys

from PARSE.parser import parser
from Utility.utility import utility


def main():
    """
    """
    inputstream = sys.stdin
    source1 = "C:\\Users\\ajkesarw\\PycharmProjects\\MyParsing\\venv\\XML\\ericsson_lte_enm_son_lte_discovery_v17A.xml"
    try:
        inputstream = open(source)
    except:
        sys.stderr.write("Problem in opening the xml file")
        sys.exit(-1)

    #read xml file
    input = inputstream.read()

    options = "xml2json"
    strip_ns = 1
    strip = 1
    uri = ""
    p = parser()
    u = utility()
    #data = t.parse1(source1, uri)

    if (options == "xml2json"):
        print "xml2json is called"
        out = p.xml2json(input, options, strip_ns, strip)
        u.storeDB(out,uri)

    print "data is successfully stored in DB "

    input = u.readDB(uri)
    #print input
    print 'data is fetched'
    options = "json2xml"
    print type(input)
    if (options == "json2xml"):
        print 'inside json2xml'
        out = p.json2xml(input)
        file = open(Test.xml, 'w')
        file.write(out)
        file.close()

if __name__ == "__main__":
    main()
