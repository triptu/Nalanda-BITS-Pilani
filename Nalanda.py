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
