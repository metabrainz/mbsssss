#!/usr/bin/env python
from __future__ import print_function

import glob
import argparse

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

IGNORED_FIELDS = set(['mbid', 'ngram', 'ref_count'])

parser = argparse.ArgumentParser()
parser.add_argument("-l", action="store_true", help="Display fields as a python list")
args = parser.parse_args()

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
            if not fieldname[0] == "_" and fieldname not in IGNORED_FIELDS:
                if args.l:
                    columns.append(fieldname)
                else:
                    columns.append(COLUMN.format(fieldname=fieldname))
    if args.l:
        print("'%s': [" % schemaname.lower(), end="")
        print(", ".join(["'%s'" % c for c in sorted(columns)]), end="")
        print("]")
    else:
        print(TABLE.format(schema=schemaname))
        print("".join(columns))
        print("|}")
