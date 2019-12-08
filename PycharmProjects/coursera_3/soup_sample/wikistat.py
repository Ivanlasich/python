from bs4 import BeautifulSoup
import requests
import re
import os
import codecs

def parse(start, end, path):


    A = [start, end]
    out={}
    for a1 in A:
        start1 = path + "//" + a1
        fileObj = codecs.open(start1, "r", "utf_8_sig")
        html = fileObj.read()
        fileObj.close()
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, "lxml")
        soup = soup.find(id="bodyContent")
        tags = soup('img')
        j = 0
        for a in tags:
            if (int(a['width']) > 199):
                j = j + 1


        k1 = 0;
        all = soup.findAll(name=re.compile(r'^(h1)|(h2)|(h3)|(h4)|(h5)|(h6)'))
        for i in all:
            if i.text[0] in 'ETC':
                k1 = k1 + 1

        max1 = 0
        k = 0
        link = soup.find_next('a')

        maxl = 0
        link = soup.find_next('a')
        while link:
            k = 1
            for i in link.find_next_siblings():
                if i.name == 'a':
                    k = k + 1
                else:
                    break
            if k > max1:
                max1 = k
            link = link.find_next('a')

        p = 0
        lnk = soup.findAll(name=['ul', 'ol'])
        for i in lnk:
            if i.find_parents(['ul', 'ol']):
                continue
            else:
                p = p + 1
        out[a1] = [j, k1, max1, p]

    return out
