#!/usr/bin/python3
import cgi
print("content-type:text/html")
print()

import subprocess as sp
import cgi
form = cgi.FieldStorage()
i = form.getvalue("x")
if (("run" in i) or ("Run" in i) or ("RUN" in i) or ("Execute" in i) or ("execute" in i) or ("EXECUTE" in i) or ("show" in i) or ("SHOW" in i) or ("Show" in i)) and (("date" in i) or ("DATE" in i) or ("Date" in i) or ("Time" in i) or ("TIME" in i) or ("time" in i)):
    cmd="date"
    output=sp.getoutput(cmd)
    print(output)
    exit()
elif (("run" in i) or ("Run" in i) or ("RUN" in i) or ("Execute" in i) or ("execute" in i) or ("EXECUTE" in i) or ("show" in i) or ("SHOW" in i) or ("Show" in i)) and (("CALENDAR" in i) or ("Calendar" in i) or ("calendar" in i) or ("month" in i) or ("MONTH" in i) or ("Month" in i) or ("CAL" in i) or ("Cal" in i) or ("cal" in i)):
    cmd="cal"
    output=sp.getoutput(cmd)
    print(output)
    exit()
elif (("run" in i) or ("Run" in i) or ("RUN" in i) or ("Execute" in i) or ("execute" in i) or ("EXECUTE" in i) or ("show" in i) or ("SHOW" in i) or ("Show" in i)) and (("PRESENT" in i) or ("Present" in i) or ("present" in i) or ("CURRENT" in i) or ("Current" in i) or ("current" in i) or ("location" in i) or ("LOCATION" in i) or ("Location" in i) or ("pwd" in i) or ("PWD" in i) or ("Pwd" in i) ):
    cmd="pwd"
    output=sp.getoutput(cmd)
    print(output)
    exit()
elif (("run" in i) or ("Run" in i) or ("RUN" in i) or ("Execute" in i) or ("execute" in i) or ("EXECUTE" in i) or ("show" in i) or ("SHOW" in i) or ("Show" in i)) and (("Content" in i) or ("content" in i) or ("CONTENT" in i) or ("FILES" in i) or ("Files" in i) or ("files" in i) or ("list" in i) or ("List" in i) or ("LIST" in i) or ("ls" in i) or ("Ls" in i) or ("LS" in i)):
    cmd="ls"
    output=sp.getoutput(cmd)
    print(output)
    exit()
else:
    print("Sorry! Not supported here. Please, try again!")

















