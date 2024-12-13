#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *
from PIL import ImageTk, Image
import tkinter as ttk
from tkinter import font

# A should get what is in the search bar
root = Tk()
root.title('JCI Search')
root.iconbitmap('JCI Logo.ico')
root.geometry("500x500")

# Create a label
my_label = Label(root, text = "Search Acronyms", font = "Arial 20")
my_label.pack(pady=20)

# Create an entrybox
my_entry = Entry(root, font=("Helvetica", 20))

my_entry.grid_size()
my_entry.pack()

my_entry.bbox



# Create function to check entry vs list
def check(e):
    
    a = my_entry.get()
    definitions = {
    "fcu": ["Fan Coil Unit (FCU)",  "Fan Coil Unit             (FCU): Small terminal unit that uses a heat exchanger and a fan to generate heating or cooling for a space."],
    "ef": ["Exhaust Fan (EF)", "Exhaust Fan               (EF): Removes unpleasant odors like steam or smoke from rooms and reduces mold."],
    "uh": ["Unit Heater (UH)",  "Unit Heater               (UH):  A unit heater has a heating element, a blower fan, and a heat exchanger that is designed to warm a space."],
    "dhw": ["Domestic Hot Water System (DHW)", "Domestic Hot Water System (DHW): Delivers hot water to people at sinks, tubs, and other areas that humans interact."],
    "sump": ["Unknown (SUMP)", "Unknown                  (SUMP): DEF"],
    "misc": ["Unknwon (MISC)", "Unknwon                  (MISC): DEF"]
    }
    isprint_all = a.lower() == "all"
    # Sample sentence
    a = a.replace(".", "")
    
    # Split the sentence into words
    words = a.split()
    
    # Replace words with their translations from the definitions
    new_sentence = ' '.join([definitions[word][0] if word in definitions else word for word in words])
    my_list.delete(0,END)
    my_list.insert(END, "TRANSLATIONS")
    my_list.insert(END, new_sentence)
    my_list.insert(END, "")
    my_list.insert(END, "SUMMARIES")

    my_set = []
    # feed all entries to a string that stores the entries and insert that strsing into the
    for i in words:
        for j in definitions:
            if((i.lower() == j and j not in my_set) or isprint_all):
                my_list.insert(END, definitions[j][1])
                my_set.append(j)
    #new_summary = ' '.join([summaries.get(s.lower(), s) for s in words])



# Create a Translator
my_list = Listbox(root, font=("Helvetica", 10, "bold"), width=160, height=50)
my_list.pack(pady=40)

# Insert
#my_list.insert(END, a)

# Create binding on the entry box call a function if release the key
my_entry.bind("<Key-Return>", check)

# Magnifying glass behavior
searchIcon = PhotoImage(file = 'Magnifying Glass.png')
label = ttk.Label(root, image =  searchIcon)
PhotoImage(file = 'Magnifying Glass.png')

d=my_entry.get()

isActive = False
def leave(e):
    isActive = True
    label.place(x = 32232, y=12323)
    
#my_entry.bind("<Leave>", stay)
my_entry.bind("<Enter>", leave)
    

label.place(x=102, y=82.75)


#myLabel.pack(side="bottom")
root.mainloop()


# In[ ]:





# In[4]:


from tkinter import *
from PIL import ImageTk, Image
import tkinter as ttk
from tkinter import font
from tkinter import messagebox

# A should get what is in the search bar
root = Tk()
root.title('JCI Search')
root.iconbitmap('JCI Logo.ico')
root.geometry("500x500")

# Create a label
my_label = Label(root, text = "Search Acronyms", font = "Arial 20")
my_label.pack(pady=20)

# Create an entrybox
my_entry = Entry(root, font=("Helvetica", 20))

my_entry.grid_size()
my_entry.pack()

my_entry.bbox

definitions = {}

# Create function to check entry vs list
def check(e):
    
    a = my_entry.get()
    
    isprint_all = a.lower() == "all"
    # Sample sentence
    a = a.replace(".", "")
    
    # Split the sentence into words
    words = a.split()
    
    # Replace words with their translations from the definitions
    new_sentence = ' '.join([definitions[word][0] if word in definitions else word for word in words])
    my_list.delete(0,END)
    my_list.insert(END, "TRANSLATIONS")
    my_list.insert(END, new_sentence)
    my_list.insert(END, "")
    my_list.insert(END, "SUMMARIES")

    my_set = []
    # feed all entries to a string that stores the entries and insert that strsing into the
    for i in words:
        for j in definitions:
            if((i.lower() == j and j not in my_set) or isprint_all):
                my_list.insert(END, definitions[j][1])
                my_set.append(j)
    #new_summary = ' '.join([summaries.get(s.lower(), s) for s in words])



# Create a Translator
my_list = Listbox(root, font=("Helvetica", 10, "bold"), width=160, height=50)
my_list.pack(pady=40)

# Insert
#my_list.insert(END, a)

# Create binding on the entry box call a function if release the key
my_entry.bind("<Key-Return>", check)

# Magnifying glass behavior
searchIcon = PhotoImage(file = 'Magnifying Glass.png')
label = ttk.Label(root, image =  searchIcon)
PhotoImage(file = 'Magnifying Glass.png')

d=my_entry.get()

isActive = False
def leave(e):
    isActive = True
    label.place(x = 32232, y=12323)
    
#my_entry.bind("<Leave>", stay)
my_entry.bind("<Enter>", leave)
    

label.place(x=102, y=82.75)

# Function to save the dictionary to a file
def save_dict():
    with open("data.txt", "w") as file:
        for key, value in definitions.items():
            file.write(f"{key}:{','.join(value)}\n")
    messagebox.showinfo("Info", "Dictionary saved successfully!")

# Function to load the dictionary from a file
def load_dict():
    try:
        with open("data.txt", "r") as file:
            for line in file:
                key, values = line.strip().split(":")
                
                definitions[key] = values.split(",")
                
    except FileNotFoundError:
        pass

def add_item():
    edit_root = Tk()
    edit_root.title('JCI Search')
    edit_root.iconbitmap('JCI Logo.ico')
    edit_root.geometry("500x500")
    my_label = Label(edit_root, text = "Add Acronyms", font = "Arial 20")
    my_label.pack(pady=20)
    
    # Create an entrybox
    acronym_label = Label(edit_root, text = "Acronym", font = "Arial 10")
    acronym_label.pack(pady=20)
    
    my_acronym = Entry(edit_root, font=("Helvetica", 20))
    my_acronym.grid_size()
    my_acronym.pack()
    
    translation_label = Label(edit_root, text = "Translation", font = "Arial 10")
    translation_label.pack(pady=20)
    
    # Summary Title
    my_translation = Entry(edit_root, font=("Helvetica", 20))
    my_translation.grid_size()
    my_translation.pack()
    
    # Summary Entry
    summary_label = Label(edit_root, text = "Summary", font = "Arial 10")
    summary_label.pack(pady=20)
    
    my_summary = Entry(edit_root, font=("Helvetica", 20))
    my_summary.grid_size()
    my_summary.pack()

    #aedd a command to delete the add acronym screen, add acronym type to definitions, save, and prompt user with success screen
    #print out or listen for definitions to check if ti added properly for debugging purposes
    add_button = ttk.Button(edit_root, text="Add", command= lambda: save_item(my_acronym.get().lower(), my_translation.get(), my_summary.get()))
    
    saved_acronym = my_acronym.get().lower()
    saved_translation = my_translation.get()
    saved_summary = my_summary.get()
        
    add_button.place(relx = .5, y=425, anchor='center')



def save_item(acronym, translation, summary):
    definitions[acronym] = [translation+" ("+acronym.upper()+")",translation+"  " +"("+acronym.upper()+");"+" "+summary]
    messagebox.showinfo("Info", "New acronym added!")
    save_dict()
    for key in definitions:
        print(key)
    

add_button = ttk.Button(root, text="Edit", command=add_item)
add_button.place(relx = .75, y=20)

load_dict()



#myLabel.pack(side="bottom")
root.mainloop()


# In[7]:


from tkinter import *
from PIL import ImageTk, Image
import tkinter as ttk
from tkinter import font
from tkinter import messagebox

# A should get what is in the search bar
root = Tk()
root.title('JCI Search')
root.iconbitmap('JCI Logo.ico')
root.geometry("500x500")

# Create a label
my_label = Label(root, text = "Search Acronyms", font = "Arial 20")
my_label.pack(pady=20)

# Create an entrybox
my_entry = Entry(root, font=("Helvetica", 20))

my_entry.grid_size()
my_entry.pack()

my_entry.bbox

definitions = {}

# Create function to check entry vs list
def check(e):
    
    a = my_entry.get()
    
    isprint_all = a.lower() == "all"
    # Sample sentence
    a = a.replace(".", "")
    
    # Split the sentence into words
    words = a.split()
    
    # Replace words with their translations from the definitions
    new_sentence = ' '.join([definitions[word][0] if word in definitions else word for word in words])
    my_list.delete(0,END)
    my_list.insert(END, "TRANSLATIONS")
    my_list.insert(END, new_sentence)
    my_list.insert(END, "")
    my_list.insert(END, "SUMMARIES")

    my_set = []
    # feed all entries to a string that stores the entries and insert that strsing into the
    for i in words:
        for j in definitions:
            if((i.lower() == j and j not in my_set) or isprint_all):
                my_list.insert(END, definitions[j][1])
                my_set.append(j)
    #new_summary = ' '.join([summaries.get(s.lower(), s) for s in words])



# Create a Translator
my_list = Listbox(root, font=("Helvetica", 10, "bold"), width=160, height=50)
my_list.pack(pady=40)

# Insert
#my_list.insert(END, a)

# Create binding on the entry box call a function if release the key
my_entry.bind("<Key-Return>", check)

# Magnifying glass behavior
searchIcon = PhotoImage(file = 'Magnifying Glass.png')
label = ttk.Label(root, image =  searchIcon)
PhotoImage(file = 'Magnifying Glass.png')

d=my_entry.get()

isActive = False
def leave(e):
    isActive = True
    label.place(x = 32232, y=12323)
    
#my_entry.bind("<Leave>", stay)
my_entry.bind("<Enter>", leave)
    

label.place(x=102, y=82.75)

# Function to save the dictionary to a file
def save_dict():
    with open("data.txt", "w") as file:
        for key, value in definitions.items():
            file.write(f"{key}:{','.join(value)}\n")
    messagebox.showinfo("Info", "Dictionary saved successfully!")

# Function to load the dictionary from a file
def load_dict():
    try:
        with open("data.txt", "r") as file:
            for line in file:
                key, values = line.strip().split(":")
                
                definitions[key] = values.split(",")
                
    except FileNotFoundError:
        pass

def add_item():
    edit_root = Tk()
    edit_root.title('JCI Search')
    edit_root.iconbitmap('JCI Logo.ico')
    edit_root.geometry("500x500")
    my_label = Label(edit_root, text = "Add Acronyms", font = "Arial 20")
    my_label.pack(pady=20)
    
    # Create an entrybox
    acronym_label = Label(edit_root, text = "Acronym", font = "Arial 10")
    acronym_label.pack(pady=20)
    
    my_acronym = Entry(edit_root, font=("Helvetica", 20))
    my_acronym.grid_size()
    my_acronym.pack()
    
    translation_label = Label(edit_root, text = "Translation", font = "Arial 10")
    translation_label.pack(pady=20)
    
    # Summary Title
    my_translation = Entry(edit_root, font=("Helvetica", 20))
    my_translation.grid_size()
    my_translation.pack()
    
    # Summary Entry
    summary_label = Label(edit_root, text = "Summary", font = "Arial 10")
    summary_label.pack(pady=20)
    
    my_summary = Entry(edit_root, font=("Helvetica", 20))
    my_summary.grid_size()
    my_summary.pack()

    #aedd a command to delete the add acronym screen, add acronym type to definitions, save, and prompt user with success screen
    #print out or listen for definitions to check if ti added properly for debugging purposes
    add_button = ttk.Button(edit_root, text="Add", command= lambda: save_item(my_acronym.get().lower(), my_translation.get(), my_summary.get()))

    delete_button = ttk.Button(edit_root, text="Delete", command=delete_item)
    delete_button.place(relx = .75, y=20)
        
    add_button.place(relx = .5, y=425, anchor='center')


def delete_item():
    edit_root = Tk()
    edit_root.title('JCI Search')
    edit_root.iconbitmap('JCI Logo.ico')
    edit_root.geometry("500x500")
    deletionList = Listbox(root, width=80, height=15)
    my_label = Label(edit_root, text = "delete Acronyms", font = "Arial 20")
    my_label.pack(pady=20)

    selected = deletionList.curselection()
    if selected:
        item = deletionList.get(selected[0])
        key = item.split(":")[0]
        del definitions[key]
        deletionList.delete(selected[0])
        messagebox.showinfo("Info", "Acronym deleted!")
    else:
        messagebox.showwarning("Warning", "No item selected!")
    
    deletionList.pack(pady=10)

    #aedd a command to delete the add acronym screen, add acronym type to definitions, save, and prompt user with success screen
    #print out or listen for definitions to check if ti added properly for debugging purposes
    add_button = ttk.Button(edit_root, text="Add", command= lambda: save_item(my_acronym.get().lower(), my_translation.get(), my_summary.get()))
    
    
    add_button.place(relx = .5, y=425, anchor='center')



def save_item(acronym, translation, summary):
    if(acronym and translation and summary):
        definitions[acronym] = [translation+" ("+acronym.upper()+")",translation+"  " +"("+acronym.upper()+");"+" "+summary]
        messagebox.showinfo("Info", "New acronym added!")
        save_dict()
    else:
        messagebox.showwarning("Warning", "All fields must be filled!")
    

add_button = ttk.Button(root, text="Edit", command=add_item)
add_button.place(relx = .75, y=20)

load_dict()



#myLabel.pack(side="bottom")
root.mainloop()


# In[62]:


from tkinter import *
from PIL import ImageTk, Image
import tkinter as ttk
from tkinter import font, messagebox

# A should get what is in the search bar
root = Tk()
root.title('JCI Search')
root.iconbitmap('JCI Logo.ico')
root.geometry("500x500")

# Create a label
my_label = Label(root, text="Search Acronyms", font="Arial 20")
my_label.pack(pady=20)

# Create an entry box
my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()

definitions = {}

# Create function to check entry vs list
def check(e):
    a = my_entry.get()
    isprint_all = a.lower() == "all"
    a = a.replace(".", "")
    words = a.split()
    
    new_sentence = ' '.join([definitions[word][0] if word in definitions else word for word in words])
    my_list.delete(0, END)
    my_list.insert(END, "TRANSLATIONS")
    my_list.insert(END, new_sentence)
    my_list.insert(END, "")
    my_list.insert(END, "SUMMARIES")

    my_set = []
    for i in words:
        for j in definitions:
            if((i.lower() == j and j not in my_set) or isprint_all):
                my_list.insert(END, definitions[j][1])
                my_set.append(j)

# Create a Translator
my_list = Listbox(root, font=("Helvetica", 10, "bold"), width=160, height=50)
my_list.pack(pady=40)

# Create binding on the entry box to call a function on key release
my_entry.bind("<Key-Return>", check)

# Magnifying glass behavior
searchIcon = PhotoImage(file='Magnifying Glass.png')
label = ttk.Label(root, image=searchIcon)
label.place(x=102, y=82.75)

isActive = False
def leave(e):
    isActive = True
    label.place(x=32232, y=12323)

my_entry.bind("<Enter>", leave)

# Function to save the dictionary to a file
def save_dict():
    with open("data.txt", "w") as file:
        for key, value in definitions.items():
            file.write(f"{key}:{','.join(value)}\n")
    messagebox.showinfo("Info", "Dictionary saved successfully!")

# Function to load the dictionary from a file
def load_dict():
    try:
        with open("data.txt", "r") as file:
            for line in file:
                key, values = line.strip().split(":")
                definitions[key] = values.split(",")
    except FileNotFoundError:
        pass

def clear():
    for widget in root.winfo_children():
        widget.destroy()

def add_item():
    clear()
    my_label = Label(root, text="Add Acronyms", font="Arial 20")
    my_label.pack(pady=20)
    
    acronym_label = Label(root, text="Acronym", font="Arial 10")
    acronym_label.pack(pady=20)
    
    my_acronym = Entry(root, font=("Helvetica", 20))
    my_acronym.pack()
    
    translation_label = Label(root, text="Translation", font="Arial 10")
    translation_label.pack(pady=20)
    
    my_translation = Entry(root, font=("Helvetica", 20))
    my_translation.pack()
    
    summary_label = Label(root, text="Summary", font="Arial 10")
    summary_label.pack(pady=20)
    
    my_summary = Entry(root, font=("Helvetica", 20))
    my_summary.pack()

    add_button = ttk.Button(root, text="Add", command=lambda: save_item(my_acronym.get().lower(), my_translation.get(), my_summary.get()))
    add_button.place(relx=0.45, y=425, anchor='center')
    add_button = ttk.Button(root, text="Delete", command=delete_page)
    add_button.place(relx=0.55, y=425, anchor='center')
    
    return_button = ttk.Button(root, text="Return", command=home_item)
    return_button.place(relx=0.75, y=20)

def home_item():
    clear()
    global my_entry, my_list
    my_label = Label(root, text="Search Acronyms", font="Arial 20")
    my_label.pack(pady=20)
    
    my_entry = Entry(root, font=("Helvetica", 20))
    my_entry.pack()
    
    my_list = Listbox(root, font=("Helvetica", 10, "bold"), width=160, height=50)
    my_list.pack(pady=40)
    
    my_entry.bind("<Key-Return>", check)
    
    add_button = ttk.Button(root, text="Edit", command=add_item)
    add_button.place(relx=0.75, y=20)

def delete_page():
    clear()
    
    my_label = Label(root, text="Delete Acronyms", font="Arial 20")
    my_label.pack(pady=20)
    
    deletionList = Listbox(root, width=80, height=15, selectmode=MULTIPLE)
    deletionList.pack(pady=40)

    for words in definitions:
        deletionList.insert(END, definitions[words][1])

    
    selected = deletionList.curselection()
    delete_button = ttk.Button(root, text="Delete", command=lambda: delete_item(deletionList, selected))
    delete_button.place(relx=0.5, y=425, anchor='center')
    
    
    if selected:
        
        item = deletionList.get(selected[0])
        key = item.split(":")[0]
        del definitions[key]
        deletionList.delete(selected[0])
        messagebox.showinfo("Info", "Acronym deleted!")
    
    deletionList.pack(pady=10)

def delete_item(deletionList, selected):

    toDelete = []
    
    for selection in deletionList.curselection():
            toDelete.append(deletionList.get(selection).split(";")[0])

    
    for i in toDelete:
        print(i)
        for j in definitions:
            print(definitions[j][0])
            if(definitions[j][0] == i):
                del definitions[j]
                deletionList.delete(i)
    
    #save_dict()
    messagebox.showinfo("Info", "Acronym deleted!")

def save_item(acronym, translation, summary):
    if acronym and translation and summary:
        definitions[acronym] = [translation + " (" + acronym.upper() + ")", translation + " (" + acronym.upper() + "); " + summary]
        messagebox.showinfo("Info", "New acronym added!")
        save_dict()
    else:
        messagebox.showwarning("Warning", "All fields must be filled!")

add_button = ttk.Button(root, text="Edit", command=add_item)
add_button.place(relx=0.75, y=20)

load_dict()

root.mainloop()


# In[10]:


from tkinter import *
from PIL import ImageTk, Image
import tkinter as ttk
from tkinter import font, messagebox

# A should get what is in the search bar
root = Tk()
root.title('JCI Search')
root.iconbitmap('JCI Logo.ico')
root.geometry("500x500")

# Create a label
my_label = Label(root, text="Search Acronyms", font="Arial 20")
my_label.pack(pady=20)

# Create an entry box
my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()

definitions = {"Help":["This is where you search all acronyms!",""]}

# Create function to check entry vs list
def check(e):
    a = my_entry.get()
    isprint_all = a.lower() == "all"
    a = a.replace(".", "")
    words = a.split()
    
    new_sentence = ' '.join([definitions[word][0] if word in definitions else word for word in words])
    my_list.delete(0, END)
    my_list.insert(END, "TRANSLATIONS")
    my_list.insert(END, new_sentence)
    my_list.insert(END, "")
    my_list.insert(END, "SUMMARIES")

    my_set = []
    for i in words:
        for j in definitions:
            if((i.lower() == j and j not in my_set) or isprint_all):
                my_list.insert(END, definitions[j][1])
                my_set.append(j)
                my_list.insert(END, "")

# Create a Translator
my_list = Listbox(root, font=("Helvetica", 10, "bold"), width=160, height=50)
my_list.pack(pady=40)

# Create binding on the entry box to call a function on key release
my_entry.bind("<Key-Return>", check)

# Magnifying glass behavior
searchIcon = PhotoImage(file='Magnifying Glass.png')
label = ttk.Label(root, image=searchIcon)
label.place(x=102, y=82.75)

isActive = False
def leave(e):
    isActive = True
    label.place(x=32232, y=12323)

my_entry.bind("<Enter>", leave)

# Function to save the dictionary to a file
def save_dict():
    with open("data.txt", "w") as file:
        for key, value in definitions.items():
            file.write(f"{key}:{','.join(value)}\n")
    messagebox.showinfo("Info", "Dictionary saved successfully!")

# Function to load the dictionary from a file
def load_dict():
    try:
        with open("data.txt", "r") as file:
            for line in file:
                key, values = line.strip().split(":")
                definitions[key] = values.split(",")
    except FileNotFoundError:
        pass

def clear():
    for widget in root.winfo_children():
        widget.destroy()

def add_item():
    clear()
    my_label = Label(root, text="Add Acronyms", font="Arial 20")
    my_label.pack(pady=20)
    
    acronym_label = Label(root, text="Acronym", font="Arial 10")
    acronym_label.pack(pady=20)
    
    my_acronym = Entry(root, font=("Helvetica", 20))
    my_acronym.pack()
    
    translation_label = Label(root, text="Translation", font="Arial 10")
    translation_label.pack(pady=20)
    
    my_translation = Entry(root, font=("Helvetica", 20))
    my_translation.pack()
    
    summary_label = Label(root, text="Summary", font="Arial 10")
    summary_label.pack(pady=20)
    
    my_summary = Entry(root, font=("Helvetica", 20))
    my_summary.pack()

    add_button = ttk.Button(root, text="Add", command=lambda: save_item(my_acronym.get().lower(), my_translation.get(), my_summary.get(), viewList))
    add_button.place(relx=0.45, y=425, anchor='center')
    add_button = ttk.Button(root, text="Delete", command=delete_page)
    add_button.place(relx=0.55, y=425, anchor='center')

    viewList = Listbox(root, width=80, height=15)
    viewList.place(relx = .5, y = 600, anchor='center')

    for words in definitions:
        viewList.insert(END, definitions[words][1])
    
    return_button = ttk.Button(root, text="Return", command=home_item)
    return_button.place(relx=0.75, y=20)

def home_item():
    clear()
    global my_entry, my_list
    my_label = Label(root, text="Search Acronyms", font="Arial 20")
    my_label.pack(pady=20)
    
    my_entry = Entry(root, font=("Helvetica", 20))
    my_entry.pack()
    
    my_list = Listbox(root, font=("Helvetica", 10, "bold"), width=160, height=50)
    my_list.pack(pady=40)
    
    my_entry.bind("<Key-Return>", check)
    
    add_button = ttk.Button(root, text="Edit", command=add_item)
    add_button.place(relx=0.75, y=20)

def delete_page():
    clear()
    
    my_label = Label(root, text="Delete Acronyms", font="Arial 20")
    my_label.pack(pady=20)

    return_button = ttk.Button(root, text="Return", command=add_item)
    return_button.place(relx=0.75, y=20)
    
    deletionList = Listbox(root, width=80, height=15, selectmode=MULTIPLE)
    deletionList.pack(pady=40)

    for words in definitions:
        deletionList.insert(END, definitions[words][1])

    delete_button = ttk.Button(root, text="Delete", command=lambda: delete_item(deletionList))
    delete_button.place(relx=0.5, y=425, anchor='center')
    
    deletionList.pack(pady=10)

def delete_item(deletionList):
    selected_indices = deletionList.curselection()
    to_delete = [deletionList.get(i).split(";")[0] for i in selected_indices]
    
    for key in list(definitions.keys()):
        if definitions[key][0] in to_delete:
            del definitions[key]
    
    for i in reversed(selected_indices):
        deletionList.delete(i)

    save_dict()
    messagebox.showinfo("Info", "Acronym(s) deleted!")

def save_item(acronym, translation, summary, viewList):
    
    if acronym and translation and summary:
        definitions[acronym] = [translation + " (" + acronym.upper() + ")", translation + " (" + acronym.upper() + ")= " + summary]
        messagebox.showinfo("Info", "New acronym added!")
        save_dict()
    else:
        messagebox.showwarning("Warning", "All fields must be filled!")
    viewList.delete(0, ttk.END)
    for words in definitions:
        viewList.insert(END, definitions[words][1])

add_button = ttk.Button(root, text="Edit", command=add_item)
add_button.place(relx=0.85, y=80)

load_dict()

root.mainloop()


# In[2]:


import nbconvert
get_ipython().system('jupyter nbconvert --to script config_template.ipynb')


# In[ ]:




