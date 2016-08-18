import  urllib,re
for page in range(1, 51):
    listurl = re.findall(r'data-mp4="(.*?)">', urllib.urlopen('http://www.budejie.com/video/%s' %page).read())
    for i in listurl:
        urllib.urlretrieve(i, 'F:/script_video/%s.mp4' %(i.split('/')[-1]))