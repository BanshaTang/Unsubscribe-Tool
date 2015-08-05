# -*- coding: utf-8 -*-

import urllib2
import time
error_list = []

def openUrl(url, index):
    global error_list
    print 'Open Url', index, url
    try:
        ret = urllib2.Request(url)
        data = urllib2.urlopen(ret).read()
    except Exception as e:
        error_list.append(e)
        print 'Failed with open url', e
        

def main():
    fread = open('unsubscribe.txt', 'r')
    line = "http://www.epubor.com/codes/subscript.aspx?Action=Unsubscribe&Type=Order&Mail=" + fread.readline()
    openUrl(line, 1)
    index = 1
    while line:
        index += 1
        time.sleep(5)
        line = "http://www.epubor.com/codes/subscript.aspx?Action=Unsubscribe&Type=Order&Mail=" + fread.readline()
        openUrl(line, index)


if __name__ == '__main__':
    main()

