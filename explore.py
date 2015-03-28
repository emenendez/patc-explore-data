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


def dump_excluding(element, exclude):
    if element.tag not in prefix(exclude):
        ET.dump(element)


def dump_subchildren(element, include, exclude):
    if element.tag in prefix(include):
        for child in element:
            dump_excluding(child, exclude)

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
                        dump_excluding(child, ['trk', 'wpt'])
                    if args.track:
                        dump_subchildren(child, ['trk'], ['name', 'trkseg'])
                    if args.waypoint:
                        dump_subchildren(child, ['wpt'], ['ele', 'time', 'name', 'desc', 'cmt', 'lat', 'lon', 'ltime'])

            except Exception:
                print('Error: could not parse {}'.format(infile), file=sys.stderr)

if __name__ == "__main__":
    main()