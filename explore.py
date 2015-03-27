#!/usr/local/bin/python3

import argparse
from pathlib import Path
import xml.etree.ElementTree as ET
import sys


def prefix(tags):
    prefixes = [
        '{http://www.topografix.com/GPX/1/0}',
        '{http://www.topografix.com/GPX/1/1}',
        '{http://www.trimbleoutdoors.com/WebServices/Api/1/0}',
        ]

    for tag in tags:
        yield tag
        for prefix in prefixes:
            yield prefix + tag


def main():
    parser = argparse.ArgumentParser(description='Explore GPX data.')

    parser.add_argument('-T', '--top', action='store_true', help='show top-level fields (default: %(default)d)')
    parser.add_argument('-t', '--track', action='store_true', help='show track metadata (default: %(default)d)')
    parser.add_argument('-w', '--waypoint', action='store_true', help='show waypoint metadata (default: %(default)d)')

    parser.add_argument('file', nargs='+', help='a .gpx file to explore')
    args = parser.parse_args()

    for pattern in args.file:
        for infile in Path('.').glob(pattern):
            try:
                root = ET.parse(str(infile)).getroot()
                
                for child in root:
                    if args.top:
                        if child.tag not in prefix(['trk', 'wpt']):
                            ET.dump(child)
                    if args.track:
                        if child.tag in prefix(['trk']):
                            for subchild in child:
                                if subchild.tag not in prefix(['name', 'trkseg']):
                                    ET.dump(subchild)
                    if args.waypoint:
                        if child.tag in prefix(['wpt']):
                            for subchild in child:
                                if subchild.tag not in prefix(['ele', 'time', 'name', 'desc', 'cmt', 'lat', 'lon', 'ltime']):
                                    ET.dump(subchild)

            except Exception:
                print('Error: could not parse {}'.format(infile), file=sys.stderr)

if __name__ == "__main__":
    main()