#this is a simple program to open all the nalanda pages of my current sem
#courses. This saves the time to search for subjects and click on them manually.
#you need to be login initially.

import webbrowser

path="D:\somefolder\...\Nalanda"     #the path of the folder which contains all this.
courses=open(path+"\courses.txt")
for line in courses:
    id_=""
    for a in line:
        if a==" ":
            break
        id_+=a
    webbrowser.open_new_tab("http://nalanda.bits-pilani.ac.in/course/view.php?id="+id_)
