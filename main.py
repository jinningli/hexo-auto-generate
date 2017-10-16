#!/usr/bin/python
# -*- coding: UTF-8 -*-

import codecs
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

import imghdr

import re
global compressRate
compressRate = 0.3
global res
res = ""
global rootdir
rootdir = os.getcwd()
global head
head = ""
global headflag
headflag = False
global subcnt
subcnt = 0

def collectPicName(dir, namearr):
    # k = 0
    global head
    global headflag
    for root, dirs, files in os.walk(dir):
        for file in files:
            pos = file.find(".jpg")
            if pos == -1:
                continue
            if file == "head.jpg":
                head = os.path.join(root, file).replace(rootdir + "/", '')
                headflag = True
                continue
            # k += 1
            # os.system("mv " + os.path.join(root, file) + " " + os.path.join(root, str(k) + ".jpg"))
            fileabsdir = os.path.join(root, file).replace(rootdir+"/", '')
            namearr.append(fileabsdir)

def compressSinglePic(inputdir, outputdir, cpsrate):
    im = Image.open(inputdir)
    w,h = im.size
    if w<800 or h<800:
        os.system("cp " + inputdir + " " + outputdir)
        print("Compress: "+inputdir.replace(rootdir,"") + "\nSkip: "+str(w)+"x"+str(h)+"\n")
        return
    towidth = int(w * cpsrate)
    toheight = int(h * cpsrate)

    im.thumbnail((towidth,toheight))
    print("Compress: "+inputdir.replace(rootdir,"") + "\nsize: "+str(w)+"x"+str(h)+"\t->\t"+str(towidth)+"x"+str(toheight)+"\n")
    # im.thumbnail((500, 500))

    # im.resize((towidth,toheight),Image.ANTIALIAS)

    im.save(outputdir,optimize=True,quality=100)
    return


def compressBkgQto():
    for root, dirs, files in os.walk(os.path.join(rootdir,"background")):
        for file in files:
            pos = file.find(".jpg")
            if pos == -1:
                continue
            compressSinglePic(os.path.join(root, file),
                              os.path.join(root, file).replace(".jpg", "_cpsed.jpg")
                              , compressRate)
            os.system("rm -f " + os.path.join(root, file))
            os.system("mv " + os.path.join(root, file).replace(".jpg", "_cpsed.jpg") + " " + os.path.join(root, file))
    for root, dirs, files in os.walk(os.path.join(rootdir,"QuoteImage")):
        for file in files:
            pos = file.find(".jpg")
            if pos == -1:
                continue
            compressSinglePic(os.path.join(root, file),
                              os.path.join(root, file).replace(".jpg", "_cpsed.jpg")
                              , compressRate)
            os.system("rm -f " + os.path.join(root, file))
            os.system("mv " + os.path.join(root, file).replace(".jpg", "_cpsed.jpg") + " " + os.path.join(root, file))

def compressProcess():
    os.system("rm -rf Galary_Compressed")
    os.system("mkdir Galary_Compressed")
    os.system("cp -r Galary/* Galary_Compressed")
    for root, dirs, files in os.walk(rootdir+"/Galary_Compressed"):
        for file in files:
            pos = file.find(".jpg")
            if pos == -1:
                continue
            if file == "head.jpg":#compress head.jpg
                compressSinglePic(os.path.join(root, file),
                                  os.path.join(root, file).replace(".jpg","_cpsed.jpg")
                                  ,compressRate)
                os.system("rm -f "+os.path.join(root, file))
                os.system("mv " + os.path.join(root, file).replace(".jpg","_cpsed.jpg") + " " + os.path.join(root, file))
                continue
            compressSinglePic(os.path.join(root, file),
                              os.path.join(root, file).replace(".jpg", "_cpsed.jpg")
                              , compressRate)
            os.system("rm -f " + os.path.join(root, file))



def appendfile(filename):
    constantdir = os.path.join(rootdir, "IndexConstant")
    global res
    htmlhead = codecs.open(constantdir + "/" + filename, "r", "utf-8")
    while 1:
        line = htmlhead.readline()
        if line == '':
            break
        res += line

def generateBackground():
    ret = "\n"
    backgrounddir = rootdir + "/background"
    for root, dirs, files in os.walk(backgrounddir):
        for file in files:
            pos = file.find(".jpg")
            if pos == -1:
                continue
            ret += "<li style=\"background-image: url(" + "background/" \
                  + file + ");\" data-stellar-background-ratio=\"0.5\"></li>\n"
    return ret

def append(str):
    global res
    res += str

def readFromFile(filename):
    constantdir = os.path.join(rootdir, "SubIndexConstant")
    ret = ""
    htmlhead = codecs.open(constantdir + "/" + filename, "r", "utf-8")
    while 1:
        line = htmlhead.readline()
        if line == '':
            break
        ret += line
    return ret

# def generatePic(namearr):
#     ret = ''
#     for namedir in namearr:
#         ret += "\n<figure class=\"animate-box\">\n<img src=\""
#         ret += namedir
#         ret += "\" alt=\"Sorry, something wrong happened... Please refresh " \
#                "the webpage...\" class=\"img-responsive\">\n</figure>\n"
#     return ret

def generatePic(namearr, tit):
    ret = ''
    for namedir in namearr:
        ret += "<div class=\"col-md-4 col-sm-4 col-xs-6 col-xxs-12 animate-box\">\n\t<div class=\"img-grid\">\n\t<img src=\""
        ret += namedir
        ret += "\" alt=\"Something wrong happened...\" class=\"img-responsive\">\n\t<a href=\""
        ret += namedir.replace("Galary_Compressed","Galary").replace("_cpsed.jpg",".jpg")
        ret += "\" >\n\t<div>\n\t<span class=\"fh5co-meta\">Click for Original Image </span>\n\t<h2 class=\"fh5co-title\">"
        ret += tit
        ret += "</h2>\n\t</div>\n\t</a>\n\t</div>\n\t</div>\n\n"
    return ret


def buildSubIndex(namearr, title, content):
    ret = ""
    global subcnt
    subcnt += 1
    filename = "subindex" + str(subcnt) + ".html"
    output = codecs.open(filename, "w", "utf-8")
    ret += readFromFile("SubHead.txt")
    ret += title
    ret += readFromFile("SubAfterTitle.txt")
    if headflag:
        ret += head
    else:
        ret += namearr[0]
    ret += readFromFile("SubBeforePic.txt")
    ret += content
    ret += readFromFile("SubAfterContent.txt")
    ret += generatePic(namearr, title)
    ret += readFromFile("SubAfterPic.txt")
    output.write(ret)
    return filename


def generaterGalary(Galarydir):
    info = codecs.open(Galarydir + "/info.txt", "r", "utf-8")
    galarytitle = info.readline()
    galarycontent = ""
    while 1:
        line = info.readline()
        if line == '':
            break
        galarycontent += " <p> " + line + "</p>\n"
    ret = ""
    namearray = []
    collectPicName(Galarydir, namearray)
    ret += "<div class=\"col-md-4 col-sm-4 col-xs-6 col-xxs-12 animate-box\">\n<div class=\"img-grid\">\n<img src=\""
    if headflag:
        ret += head
    else:
        ret += namearray[0]
    ret += "\" alt=\"Something wrong happened...\" class=\"img-responsive\">" \
           "\n<a href=\""
    ret += buildSubIndex(namearray, galarytitle, galarycontent)
    ret += "\" class=\"transition\"><div>\n<span class=\"fh5co-meta\">"
    ret += str(namearray.__len__())
    ret +=  " images</span>\n<h2 class=\"fh5co-title\">"
    ret += galarytitle
    ret += "</h2>\n</div>\n</a>\n</div>\n</div>\n"
    return ret



def main():
    print("\n-----------------------\nHTML Building Process Start\n-----------------------\n")
    print("\n-----------------------\nCompressing Image...\n-----------------------\n")
    compressBkgQto()
    compressProcess()
    print("\n-----------------------\nCompressing Image Finish\n-----------------------\n")
    appendfile("IndexHead.txt")
    appendfile("IndexBeforeBackground.txt")
    append(generateBackground())
    appendfile("IndexBeforeGalary.txt")
    print("\nGenerated Galary:\n-----------------------")
    for root, dirs, files in os.walk(rootdir + "/Galary_Compressed"):
        for dir in dirs:
            print(dir)
            append(generaterGalary(os.path.join(root, dir)))
    print("-----------------------\n")
    appendfile("IndexAfterGalary.txt")
    tmpout = codecs.open("Index.html", "w", "utf-8")
    tmpout.write(res)
main()


print("\n-----------------------\nHTML Build Success!!\n-----------------------\n")
