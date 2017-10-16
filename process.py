import codecs
import os
import sys
import datetime
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


def MoveToGithubDir():
    print ("\n\n--------------- Moving To Github Directory ---------------\n")
    githubdir = rootdir + '/' + 'jinningli.github.io'

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
    if s == "n" or s == "N":
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
MoveToGithubDir()
pushToGithub()
