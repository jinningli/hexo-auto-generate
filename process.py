import codecs
import os
import sys
import datetime
import tinify
tinify.key = "07kVTh8oGbNFNHn4Fb0XU-t_ncAlJkMq"
# tinify.proxy = "http://user:pass@192.168.0.1:8080"
reload(sys)
sys.setdefaultencoding('utf8')

rootdir = os.getcwd()

def hexoCalling():
    print ("\n\n--------------- Calling Hexo Contributor ---------------\n")
    os.chdir(rootdir)
    os.system('hexo clean')
    os.system('hexo generate')

def insertRealIndex():
    print ("\n\n--------------- Insert Homepage ---------------\n")
    publicdir = rootdir + '/' + 'public'
    os.system('mv ' + publicdir + '/' + 'index.html ' + publicdir + '/' + 'blog.html')
    for root, dirs, files in os.walk(rootdir + '/' + 'HomePage'):
        for file in files:
            if file == '.DS_Store':
                continue
            print ('Extracting ' + root + '/' + file)
            os.system('cp ' + root + '/' + file + ' ' + publicdir + '/' + file)
        for dir in dirs:
            if dir == '.git':
                continue
            print ('Extracting Directory ' + root + '/' + dir)
            os.system('cp -r ' + root + '/' + dir + ' ' + publicdir + '/' + dir)
        break

def compressMoveImg():
    print ("\n\n--------------- Compressing Images ---------------\n")
    assetsdir = rootdir + '/' + 'source' + '/' + '_posts' + '/' + 'assets'

    compressedimgdir_bak = rootdir + '/' + 'source' + '/' + '_posts' + '/' + 'assets_bak'
    if not os.path.exists(compressedimgdir_bak):
        os.system('mkdir ' + compressedimgdir_bak)

    thumbnaildir_bak = rootdir + '/' + 'source' + '/' + '_posts' + '/' + 'thumbnails_bak'
    if not os.path.exists(thumbnaildir_bak):
        os.system('mkdir ' + thumbnaildir_bak)

    compressedimgdir = rootdir + '/' + 'public' + '/' + 'assets'
    # os.system('rm -r ' + compressedimgdir)
    print ("Create Directory " + compressedimgdir)
    os.system('mkdir ' + compressedimgdir)

    thumbnaildir = rootdir + '/' + 'public' + '/' + 'thumbnails'
    # os.system('rm -r ' + thumbnaildir)
    print ("Create Directory " + thumbnaildir)
    os.system('mkdir ' + thumbnaildir)

    for root, dirs, files in os.walk(assetsdir):
        for file in files:
            if file == '.DS_Store':
                continue
            print ('> Compressing ' + root + '/' + file + ' ...')
            if os.path.exists(thumbnaildir_bak + '/' + file):
                print ('Already Exist, Copy File: ' + file)
                os.system('cp ' + thumbnaildir_bak + '/' + file + ' ' + thumbnaildir + '/' + file)
                os.system('cp ' + compressedimgdir_bak + '/' + file + ' ' + compressedimgdir + '/' + file)
                continue

            size = os.path.getsize(root + '/' + file)/float(1024)
            if  size < 100:
                print ('Skip Compressing with size: ' + str(size) + "  >> " + root + '/' + file + ' to assets...')
                os.system('cp ' + assetsdir + '/' + file + ' ' + compressedimgdir + '/' + file)
                os.system('cp ' + assetsdir + '/' + file + ' ' + compressedimgdir_bak + '/' + file)
                os.system('cp ' + assetsdir + '/' + file + ' ' + thumbnaildir + '/' + file)
                os.system('cp ' + assetsdir + '/' + file + ' ' + thumbnaildir_bak + '/' + file)
                continue

            source = tinify.from_file(root + '/' + file)
            print ('Resizing ' + root + '/' + file + ' to assets...')
            resized = source.resize(method = "scale", width = 800)
            resized.to_file(compressedimgdir + '/' + file)
            os.system('cp ' + compressedimgdir + '/' + file + ' ' + compressedimgdir_bak + '/' + file)
            print ('Resizing ' + root + '/' + file + ' to thumbnails...')
            reresize = source.resize(method = "scale", width = 256)
            reresize.to_file(thumbnaildir + '/' + file)
            os.system('cp ' + thumbnaildir + '/' + file + ' ' + thumbnaildir_bak + '/' + file)
            print ('Baking File: ' + file)
        break


def MoveToGithubDir():
    print ("\n\n--------------- Moving To Github Directory ---------------\n")
    githubdir = rootdir + '/' + 'jinningli.github.io'

    for root, dirs, files in os.walk(githubdir):
        for file in files:
            if file == '.DS_Store':
                continue
            print ('Delete ' + root + '/' + file)
            os.system('rm ' + root + '/' + file)
        for dir in dirs:
            if dir == '.git':
                continue
            print ('Delete Directory ' + root + '/' + dir)
            os.system('rm -r ' + root + '/' + dir)
        break

    for root, dirs, files in os.walk(rootdir + '/' + 'public'):
        for file in files:
            if file == '.DS_Store':
                continue
            print ('Extracting ' + root + '/' + file)
            os.system('cp ' + root + '/' + file + ' ' + githubdir + '/' + file)
        for dir in dirs:
            if dir == '.git':
                continue
            print ('Extracting Directory ' + root + '/' + dir)
            os.system('cp -r ' + root + '/' + dir + ' ' + githubdir + '/' + dir)
        break


def pushToGithub():
    print ("\n\n--------------- Pushing To Github Directory ---------------\n")
    s = raw_input("Pushing to jinningli.github.io? (y/n)\n")
    if not (s == "y" or s == "Y"):
        return
    githubdir = rootdir + '/' + 'jinningli.github.io'
    os.chdir(githubdir)
    print('> git add .')
    os.system('git add .')
    print('> git commit -m \"Updated, AutoCommit at ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\"')
    os.system('git commit -m \"Updated, AutoCommit at ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\"')
    print('> git push')
    os.system('git push')



hexoCalling()
insertRealIndex()
compressMoveImg()
MoveToGithubDir()
pushToGithub()
