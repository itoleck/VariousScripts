import subprocess as sp
import os
from tkinter import filedialog
from tkinter import *

actions =["activityintervals","analyzepower","boot","bootprefetch","cpudisk","cswitch","diskidlehistogram","diskio","dpcisr","drips","drvdelay","dumper","energydiag","eventmetadata","filename","fileversion","focuschange","hardfault","heap","heapsnapshot","idlehistogram","marks","minifilterddelay","pagefault","perfctrs","pmc","pnp","pool","power","powerhistogram","prefetch","process","profile","readythread","regions","registry","residentset","screenshots","services","shutdown","spinlock","stack","suspend","symcache","sysconfig","systemsleep","timer","tracestats","uidelay","virtualalloc","winlogon","wpptrace"]
efile = Tk()

efile.filename =  filedialog.askopenfilename(initialdir = "f:\\Temp\\",title = "Select file",filetypes = (("etl files","*.etl"),("all files","*.*")))
etlpath=efile.filename.replace("/", "\\")

pwd = os.path.dirname(os.path.abspath(efile.filename))

print ('Processing file: ' + etlpath)

#print(os.path.dirname(os.path.abspath(efile.filename)) + '\\' + os.path.basename(efile.filename).split('.')[0])
#os.mkdir(os.path.dirname(os.path.abspath(efile.filename)) + '\\' + os.path.basename(efile.filename))

#for action in actions:
#    cmd = 'xperf.exe -i ' + etlpath + ' -o ' + etlpath + '-' + action + '.txt' + ' -a ' + action
#    print(cmd)
#    sp.Popen(cmd, shell=True)

print('Processed files saved in folder: ' + os.path.dirname(os.path.abspath(efile.filename)))

list = os.listdir(pwd)
for file in list:
    print(file + str(os.path.getsize(os.path.join(pwd, file))))
    if (os.path.getsize(os.path.join(pwd, file))) == 0:
        os.remove(pwd + '\\' + file)
sys.exit(0)
