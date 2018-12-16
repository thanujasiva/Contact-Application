'''
Purpose of this program is to be able to add, edit, remove and search for contacts,
contact will remain (even when program is closed) unless deleted.
Contacts are saved in a text file called 'contact', with each contact taking up 5 lines
'''

''' setup '''
''' make a list out of the contacts file contents '''
c= open("contact.txt","r")
from graphics import *
from tkinter import *
myGui = Tk()
myGui.geometry ("500x300")
myGui.title("Contact Book")
bgcolor = "light blue" 
myGui.configure(background=bgcolor)

clist = (c.readlines())
c.close()


''' definitions '''

def add_list(entry1, entry2, entry3, entry4, list1):
    ''' add new or editted contact to list and file '''
    
    # open the files
    c = open("contact.txt","a")
    # add to the files
    c.write((entry1.get()) + "\n") # "\n" adds a space
    c.write((entry2.get()) + "\n")
    c.write((entry3.get()) + "\n")
    c.write((entry4.get()) + "\n")
    c.write("\n")
    # add to the lists
    list1.append (entry1.get() + "\n")
    list1.append (entry2.get() + "\n")
    list1.append (entry3.get() + "\n")
    list1.append (entry4.get() + "\n")
    # adding a blank line makes it easier when the programmer is reading the file
    list1.append ("\n") 
    # make entry boxes empty
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
    
    c.close()
    search.configure(state=NORMAL)
    delete.configure(state=DISABLED)
    cancel.configure(text= "Back", command= lambda: blank_entry(search, ent1, ent2, ent3, ent4, list1))
    display.configure(state=NORMAL)
    
def cancel_contact (search, ent1, ent2, ent3, ent4, list1, old1, old2, old3, old4):
    ''' change the contact details to the original form in entry boxes'''
    search.config(state=NORMAL)
    
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    
    ent1.insert(0,old1)
    ent2.insert(0,old2)
    ent3.insert(0,old3)
    ent4.insert(0,old4)
    
    add_list(ent1, ent2, ent3, ent4, list1)
    
def blank_entry(search, ent1, ent2, ent3, ent4, first):
    ''' resets entry boxes to blank '''
    search.config(state=NORMAL)
    ent1.config(state=NORMAL)
    ent2.config(state=NORMAL)
    ent3.config(state=NORMAL)
    ent4.config(state=NORMAL)
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    submit.configure(text= "Submit", command= lambda: add_list(ent1, ent2, ent3, ent4, first))
    display.configure(state=NORMAL)
    
def delete_contact(search, ent1, ent2, ent3, ent4, list1):
    ''' the contact is already removed from list and files '''
    search.config (state=NORMAL) 
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    delete.configure(state=DISABLED)
    
    submit.configure(text= "Submit", command= lambda: add_list(ent1, ent2, ent3, ent4, list1))
    cancel.configure(text= "Back", command= lambda: blank_entry(search, ent1, ent2, ent3, ent4, list1))
    display.configure(state=NORMAL)
    
    
def display_list (list1, t, ent1, ent2, ent3, ent4):
    ''' display the first name and last name of contacts in alphabetical order '''
    
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    
    t.config(state=NORMAL) # allows program to edit text box 
    t.delete(0.0,END)
    
    listsort = []
    for i in range (len(list1)):
        if i %5 == 0: # when the list item is a first name
            listsort.append (list1[i] + list1[i+1])
    listsort.sort(key=lambda s: s.lower()) # sorts list case insensitive
    
    for i in range (len(listsort)):
        for x in range (len(list1)):
            if listsort[i] == (list1[x] + list1[x+1]):
                firstDisplay = list1[x].replace("\n", "") # this removes the space
                lastDisplay = list1[x+1]
                t.insert(END,(firstDisplay + " " + lastDisplay ))
                break
    
    t.config(state=DISABLED) # disables text box so user cannot tamper with it
    
    
def edit_contact(e, first, t, entry1, entry2, entry3, entry4, i):
    submit.configure(text= "Submit", command= lambda: add_list(entry1, entry2, entry3, entry4, first))
    # cancel button does same thing as submit, except it goes to cancel_contact procedure first
    cancel.configure(text = "Cancel", command= lambda: cancel_contact(search, entry1, entry2, entry3, entry4, first, l1old, l2old, l3old, l4old))
    delete.configure(state=NORMAL)
    delete.configure (command= lambda: delete_contact(search, entry1, entry2, entry3, entry4, first))
    search.config (state=DISABLED)
    
    entry1.config(state=NORMAL)
    entry2.config(state=NORMAL)
    entry3.config(state=NORMAL)
    entry4.config(state=NORMAL)
    # saves original contact in case user wants to discard changes
    l1old = first[i].replace("\n", "")
    l2old = first[i+1].replace("\n", "") 
    l3old = first[i+2].replace("\n", "")
    l4old = first[i+3].replace("\n", "")

    # remove item in position i from the file and list    
    c= open("contact.txt","w")
    for m in range(len(first)):
        # only adds to file if it's not the contact that will be editted
        if not(m==i or m==i+1 or m==i+2 or m==i+3 or m==i+4): 
            c.write(first[m])
    c.close()
    
    c= open("contact.txt","r")
    del first[:]                # equivalent to   del list[0:len(list)]
    first.extend(c.readlines()) # extend adds multiple items at once
    c.close()


def search_contacts (entry, list1, t, ent1, ent2, ent3, ent4):
    ''' allows user to search specific contact '''
    
    t.config(state=NORMAL)
    t.delete(0.0,END)
    
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    exist = False
    
    for i in range (len(list1)):
        if (i % 5 == 0) and (list1[i] == (entry.get()+"\n")): 
            exist = True
            
            ent1.insert(0,list1[i].replace("\n", ""))
            ent2.insert(0,list1[i+1].replace("\n", ""))
            ent3.insert(0,list1[i+2].replace("\n", ""))
            ent4.insert(0,list1[i+3].replace("\n", ""))
            
            ent1.config(state=DISABLED)
            ent2.config(state=DISABLED)
            ent3.config(state=DISABLED)
            ent4.config(state=DISABLED)
            
            display.configure(state=DISABLED)
            search.configure(state=DISABLED)
            submit.configure(text= "Edit", command= lambda: edit_contact(entry, list1, t, ent1, ent2, ent3, ent4, i))
            cancel.configure(text= "Back", command= lambda: blank_entry(search, ent1, ent2, ent3, ent4, list1))
           
            break
        
    if not(exist):
        t.insert(END,("Could not find "  + entry.get()))
    t.config(state=DISABLED)
    
    entry.delete(0,END)
    entry.insert(0,"Enter first name")

    
''' main title '''
titleLabel = Label(myGui, bg=bgcolor, text = "Contacts", font=("Calibri", 17))
titleLabel.grid(row=0, column=0, columnspan=5)
LineLabel = Label (myGui, bg=bgcolor, text = "____________________________________________", font=("Calibri", 17), fg=color_rgb(0, 51, 102))
LineLabel.grid(row=1, column=0, columnspan=5)


''' labels and entry boxes for each contact item ''' 
firstLabel = Label(myGui, bg=bgcolor, text = "First Name        ")
firstLabel.grid(row=3, column=0)
firstEntry = Entry(myGui)
firstEntry.grid(row=3, column=1)

lastLabel = Label(myGui, bg=bgcolor, text = "Last Name        ")
lastLabel.grid(row=4, column=0)
lastEntry = Entry(myGui)
lastEntry.grid(row=4, column=1)

numLabel = Label(myGui, bg=bgcolor, text = "Phone Number")
numLabel.grid(row=5, column=0)
numEntry = Entry(myGui)
numEntry.grid(row=5, column=1)

emailLabel = Label(myGui, bg=bgcolor, text = "Email                 ")
emailLabel.grid(row=6, column=0)
emailEntry = Entry(myGui)
emailEntry.grid(row=6, column=1)


''' where all contacts are displayed'''
itemText = Text(myGui, height=10, width=20)
itemText.grid(row=4, rowspan=15, column=3, columnspan=2, sticky=E+W)
itemText.config(state=DISABLED) # makes sure user cannot change it, but needs to be NORMAL for code to change it


''' buttons '''
cancel = Button(myGui, text= "Back", width=8, command= lambda: blank_entry(search, firstEntry, lastEntry, numEntry, emailEntry, clist))
cancel.grid(row=8, column=0)

delete = Button(myGui, text= "Delete", width=8)
delete.configure(state=DISABLED)
delete.grid(row=9, column=0)

submit = Button(myGui, text= "Submit", width=8, command=lambda:add_list(firstEntry, lastEntry, numEntry, emailEntry, clist))
submit.grid(row=8, column=1)

display = Button(myGui, text= "View All", width=8, command=lambda: display_list(clist, itemText, firstEntry, lastEntry, numEntry, emailEntry))
display.grid(row=19, column=4, sticky=E+W)

searchEntry = Entry(myGui)
searchEntry.insert(0,"Enter first name")
searchEntry.grid(row=3, column=3, sticky=E+W)
search = Button(myGui, text= "Search Contacts", width=12, command=lambda: search_contacts(searchEntry, clist, itemText, firstEntry, lastEntry, numEntry, emailEntry))
search.grid(row=3, column=4, sticky=E+W)


''' links used '''
# https://www.youtube.com/watch?v=hst3AWjxF5o
# https://stackoverflow.com/questions/10927234/setting-the-position-on-a-button-in-python
# https://stackoverflow.com/questions/16373887/set-the-text-of-an-entry-using-a-button-tkinter
# https://stackoverflow.com/questions/3559559/how-to-delete-a-character-from-a-string-using-python
# https://www.python-course.eu/tkinter_canvas.php
# http://effbot.org/tkinterbook/grid.htm
# https://stackoverflow.com/questions/20196159/how-to-append-multiple-values-to-a-list-in-python
# https://stackoverflow.com/questions/3842155/is-there-a-way-to-make-the-tkinter-text-widget-read-only


myGui.mainloop()
