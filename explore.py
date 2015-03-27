#!/usr/local/bin/python3

import argparse
from pathlib import Path
import xml.etree.ElementTree as ET


def prefix(tags):
    prefixes = [
        '{http://www.topografix.com/GPX/1/1}',
        '{http://www.topografix.com/GPX/1/1}',
        ]

    for tag in tags:
        yield tag
        for prefix in prefixes:
            yield prefix + tag


def main():
    parser = argparse.ArgumentParser(description='Explore GPX data.')

    parser.add_argument('-T', '--top', action='store_true', help='show top-level fields (default: %(default)d)')

    parser.add_argument('file', nargs='+', help='a .gpx file to explore')
    args = parser.parse_args()

    for pattern in args.file:
        for infile in Path('.').glob(pattern):
            root = ET.parse(str(infile)).getroot()
            for child in root:
                if args.top:
                    if child.tag not in prefix(['trk', 'wpt']):
                        ET.dump(child)



if __name__ == "__main__":
    main()