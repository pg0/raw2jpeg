#!/usr/bin/python
import sys, getopt
import os
import rawpy

def main(argv):
    opts, args = getopt.getopt(argv,"h")
    for opt, arg in opts:
        if opt == '-h':
            helpMsg()
            sys.exit()

    if (len(args) < 1):
        helpMsg()
        sys.exit()

    inputfile = args[0]

    filename, _ = os.path.splitext(inputfile)
    with rawpy.imread(inputfile) as raw:
        try:
            thumb = raw.extract_thumb()
        except rawpy.LibRawNoThumbnailError:
            print('no thumbnail found')
        else:
            if thumb.format in [rawpy.ThumbFormat.JPEG, rawpy.ThumbFormat.BITMAP]:
                if thumb.format is rawpy.ThumbFormat.JPEG:
                    thumb_filename = filename + '_thumb.jpg'
                    with open(thumb_filename, 'wb') as f:
                        f.write(thumb.data)
                        print('"' + thumb_filename +'" saved successfully')
            else:
                print('unknown thumbnail format')

def helpMsg():
    print ('test.py <rawfile>')


if __name__ == "__main__":
   main(sys.argv[1:])
