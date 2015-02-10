#!/usr/bin/env python
import glob

from xml.etree import ElementTree

TABLE = \
"""\
==={schema}===
====Search Fields====
The [[{schema}]] index contains the following fields you can search
{{| border=\"1\" class=\"wikitable sortable\"
|-
! Field !! Description
"""

COLUMN = \
"""\
|-
| {fieldname} ||
"""

schemafiles = glob.glob("[a-z]*/conf/schema.xml")
schemafiles.sort()

for _file in schemafiles:
    parser = ElementTree.XMLParser()
    parser.entity["fieldtypes"] = "fieldtypes"
    schemaname = ""
    columns = []

    for _, elem in ElementTree.iterparse(_file, parser=parser):
        if elem.tag == "schema":
            schemaname = elem.attrib["name"].capitalize()
        elif elem.tag == "field":
            fieldname = elem.attrib["name"]
            if not fieldname[0] == "_":
                columns.append(COLUMN.format(fieldname=fieldname))
    print(TABLE.format(schema=schemaname))
    print("".join(columns))
    print("|}")
