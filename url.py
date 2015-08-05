# -*- coding: utf-8 -*-

import urllib2
import time


def openUrl(url, index, email):
    print 'Open Url', index, url
    try:
        ret = urllib2.Request(url)
        data = urllib2.urlopen(ret).read()
    except Exception as e:
        print 'Failed with open url', e
        f = open('error_list.txt', 'a')
        f.write(email)
        f.close()


def main():
    fread = open('unsubscribe.txt', 'r')
    url = "http://www.epubor.com/codes/subscript.aspx?Action=Unsubscribe&Type=Order&Mail="
    email = fread.readline()
    line = url + email
    openUrl(line, 1, email)
    index = 1
    while line:
        index += 1
        time.sleep(2)
        email = fread.readline()
        line = url + email
        openUrl(line, index, email)

if __name__ == '__main__':
    main()

