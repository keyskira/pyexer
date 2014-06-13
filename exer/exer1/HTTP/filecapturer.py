# coding=utf-8
import urllib
import urllib2
import urllister

usock = urllib.urlopen("https://yande.re/post") #自行修改URL
parser = urllister.URLLister()
parser.feed(usock.read())
usock.close()
parser.close()

jpglist = []


def callbackfunc(blocknum, blocksize, totalsize):
    """回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    """
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print "%.2f%%" % percent


for url in parser.urls:
    if url[-3:] == "jpg":#自行修改扩展名
        jpglist.append(url)
for i in range(len(jpglist)):
    file_name = urllib2.unquote(jpglist[i]).decode('utf8').split('/')[-1]
    local = str("D:\\catch\\" + file_name) #自行修改目录
    urllib.urlretrieve(jpglist[i], local, callbackfunc)

