import string
import urllib2
import os
import re


opener = urllib2.build_opener()
opener.addheaders = [("User-Agent",
                      "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6")]
urllib2.install_opener(opener)


def catch_baidu(tieba_name, begin, end):
    if end % 50 == 0:
        pageindex = end
    else:
        pageindex = int(end / 50) * 50

    posturls = []
    getpostpattern = re.compile(r'[^m]/p/\d{10}')  #strings without beginning with m
                                                   #and /p/ + ten numbers
    for x in range(0, pageindex + 1, 50):
        pages = 'http://tieba.baidu.com/f?kw=' + tieba_name + '&pn=' + str(x)
        print pages
        page = urllib2.urlopen(pages)
        posturls = posturls + getpostpattern.findall(page.read())
        page.close()
    print len(posturls)

    for i in range(begin, end + 1):
        pagename = 'tieba\\' + string.zfill(i, 6) + '.html'
        print 'now loading Page: ' + tieba_name + ' and save to: ' + pagename
        f = open(pagename, 'w+')
        posturl = 'http://tieba.baidu.com' + posturls[i][1:]
        tieba_content = urllib2.urlopen(posturl).read()
        f.write(tieba_content)
        f.close()


def main():
    tieba_name = raw_input(u'input tieba name:\n')
    begin = int(raw_input(u'input begin page:\n'))
    end = int(raw_input(u'input end page:\n'))
    if not os.path.isdir('tieba'):
        os.makedirs('tieba')
    catch_baidu(tieba_name, begin, end)


if __name__ == "__main__":
    main()
