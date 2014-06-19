import string
import urllib2
import os
import urllister


opener = urllib2.build_opener()
opener.addheaders = [("User-Agent",
                      "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6")]
urllib2.install_opener(opener)


def get_tieba_page(page):
    req = urllib2.Request(page)
    web = urllib2.urlopen(req)
    praser = urllister.URLLister()
    praser.feed(web.read())
    web.close()
    praser.close()
    return praser


def catch_baidu(tieba_name, begin, end):
    if end % 50 == 0:
        pageindex = end
    else:
        pageindex = int(end / 50) * 50

    posturls = []
    for x in range(0, pageindex + 1, 50):
        page = 'http://tieba.baidu.com/f?kw=' + tieba_name + '&pn=' + str(x)
        print page
        pagepraser = get_tieba_page(page)

        for url in pagepraser.urls:
            if url[:3] == r'/p/':
                posturls.append(url)
    print len(posturls)

    for i in range(begin, end + 1):
        pagename = 'tieba\\' + string.zfill(i, 6) + '.html'
        print 'now loading Page: ' + tieba_name + ' and save to: ' + pagename
        f = open(pagename, 'w+')
        posturl = 'http://tieba.baidu.com' + posturls[i - 1]
        tieba_content = urllib2.urlopen(posturl).read()
        f.write(tieba_content)
        f.close()


if __name__ == "__main__":
    tieba_name = raw_input(u'input tieba name:\n')
    begin = int(raw_input(u'input begin page:\n'))
    end = int(raw_input(u'input end page:\n'))
    if not os.path.isdir('tieba'):
        os.makedirs('tieba')
    catch_baidu(tieba_name, begin, end)
