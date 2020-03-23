"""
    parser class to convert XML to JSON and vice versa
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
import pprint
import xml.etree.cElementTree
import xml.etree.cElementTree as ET
import xml.etree.cElementTree as ET
from collections import OrderedDict
from pprint import pprint

import pymongo
import pymongo
import xmltodict
from DB.MongoDB import MongoDB
from DB.MongoDB import MongoDB


class parser:
    """
    """

    def __init__(self):
        print 'inside init of parser'

    def strip_tag(self, tag):
        strip_ns_tag = tag
        split_array = tag.split('}')
        if len(split_array) > 1:
            strip_ns_tag = split_array[1]
            tag = strip_ns_tag
        return tag

    def elem_to_internal(self, elem, strip_ns=1, strip=1):
        # Convert an Element into an internal dictionary (not JSON!).

        d = OrderedDict()
        elem_tag = elem.tag
        if strip_ns:
            elem_tag = self.strip_tag(elem.tag)
        for key, value in list(elem.attrib.items()):
            d['@' + key] = value

        # loop over subelements to merge them
        for subelem in elem:
            v = self.elem_to_internal(subelem, strip_ns=strip_ns, strip=strip)

            tag = subelem.tag
            if strip_ns:
                tag = self.strip_tag(subelem.tag)

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

        # Convert an internal dictionary (not JSON!) into an Element.
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

    def elem2json(self, elem, options, strip_ns=1, strip=1):

        # Convert an ElementTree or Element into a JSON string.

        if hasattr(elem, 'bulkCmConfigDataFile'):
            elem = elem.getroot()

        if options == "xml2json":
            return json.dumps(self.elem_to_internal(elem, strip_ns=strip_ns, strip=strip), indent=4, separators=(',', ': '))
        else:
            return json.dumps(self.elem_to_internal(elem, strip_ns=strip_ns, strip=strip))

    def json2elem(json_data, factory=ET.Element):

        # Convert a JSON string into an Element
        return internal_to_elem(json.loads(json_data), factory)

    def xml2json(self, xmlstring, options, strip_ns=1, strip=1):

        # Convert an XML string into a JSON string.

        elem = ET.fromstring(xmlstring)
        return self.elem2json(elem, options, strip_ns=strip_ns, strip=strip)

    def json2xml(json_data, factory=ET.Element):

        """Convert a JSON string into an XML string."""

        if not isinstance(json_data, dict):
            json_data = json.loads(json_data)

        elem = internal_to_elem(json_data, factory)
        return ET.tostring(elem)
