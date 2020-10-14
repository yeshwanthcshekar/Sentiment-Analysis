# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import numpy as np
import pubYearPlot as pyp
import tagsTalksPlot as ttp
import ratingsPlot as rp
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import knn as k
import checktwitter as twty


#gui Window
 
window = Tk()
window.title("TedTalk Analyzer")
window.geometry('370x175') # Size 200, 200
window.configure(background="gray97")
def clicked():
    file = filedialog.askopenfilename()
                
menu = Menu(window)
new_item = Menu(menu,background='gray97', foreground='slate blue')
new_item.add_command(label='Browse',command=clicked)
menu.add_cascade(label='File', menu=new_item)
menu.add_cascade(label='Help')
window.config(menu=menu)

window.grid_rowconfigure(0, weight=1) # For row 0
window.grid_rowconfigure(1, weight=1) # For row 1
window.grid_rowconfigure(2, weight=1) # For row 2
window.grid_rowconfigure(3, weight=1) # For row 3
window.grid_rowconfigure(4, weight=1) # For row 4
window.grid_rowconfigure(5, weight=1) # For row 5
window.grid_rowconfigure(6, weight=1) # For row 6
window.grid_rowconfigure(7, weight=1) # For row 7
window.grid_rowconfigure(8, weight=1) # For row 8


window.grid_columnconfigure(0, weight=1) # For column 0
window.grid_columnconfigure(1, weight=1) # For column 1
window.grid_columnconfigure(2, weight=1) # For column 2
window.grid_columnconfigure(3, weight=1) # For column 2

titleLbl = Label(window, text="Ted Talk Analyzer",foreground="OrangeRed2")
titleLbl.grid(column=2, row=0, padx=5, pady=5,sticky=W)

durationLbl = Label(window, text="Duration",foreground="OrangeRed2")
durationLbl.grid(column=1,row=3,padx=1,pady=1,sticky=W)

durationEntry = Entry(window,width=20)
durationEntry.grid(column=2, row=3,padx=1, pady=1,sticky=W)

labguageLbl = Label(window, text="Language",foreground="OrangeRed2")
labguageLbl.grid(column=1,row=4,padx=1,pady=1,sticky=W)

languageEntry = Entry(window,width=20)
languageEntry.grid(column=2, row=4,padx=1, pady=1,sticky=W)

listTags = []

listOfTagsLbl = Label(window, text="",foreground="OrangeRed2")
listOfTagsLbl.grid(column=1,row=6,padx=1,pady=1,sticky=W)

tagsLbl = Label(window, text="Tags",foreground="OrangeRed2")
tagsLbl.grid(column=1,row=5,padx=1,pady=1,sticky=W)

def tagsSelected(event):
    listTags.append(tagsCombo.get().lower())
    listOfTagsLbl.configure(text=','.join(listTags))

tagsCombo = ttk.Combobox(window, 
                            values=[
                                    "Select",
                                    "Technology", 
                                    "Design",
                                    "Culture",
                                    "Science"])
tagsCombo.grid(column=2, row=5,padx=1, pady=1,sticky=W)
tagsCombo.current(0)
tagsCombo.bind("<<ComboboxSelected>>", tagsSelected)


def runCode():
    pd.set_option('display.max_columns',50)
    pd.set_option('display.expand_frame_repr', False)
    dataset=pd.read_csv('ted_main.csv') 
    
    #formatting date
    dataset['film_date'] = dataset['film_date'].apply(lambda x: datetime.datetime.fromtimestamp( int(x)).strftime('%d-%m-%Y'))
    dataset['published_date'] = dataset['published_date'].apply(lambda x: datetime.datetime.fromtimestamp( int(x)).strftime('%d-%m-%Y'))
    dataset["published_year"] = dataset["published_date"].apply(lambda x: x.split("-")[2])
    
    dataset = dataset.sort_values('views', ascending=False)
    
    pyp.pubYearPlot(dataset)
    
    #printing presenter's occupation and their counts.
    print(dataset["speaker_occupation"].value_counts().head(10),"\n")
    
    
    #printing the top 5 occupation's number of views.
    print("Occupation:  Views")
    print("Writer: ",int(dataset[dataset["speaker_occupation"]=="Writer"]["views"].sum() / len(dataset[dataset["speaker_occupation"]=="Writer"])))
    print("Designer: ", int(dataset[dataset["speaker_occupation"]=="Designer"]["views"].sum() / len(dataset[dataset["speaker_occupation"]=="Designer"])))
    print("Artist: ",int(dataset[dataset["speaker_occupation"]=="Artist"]["views"].sum() / len(dataset[dataset["speaker_occupation"]=="Artist"])))
    print("Jornalist: ",int(dataset[dataset["speaker_occupation"]=="Journalist"]["views"].sum() / len(dataset[dataset["speaker_occupation"]=="Journalist"])))
    print("Entrepreneur",int(dataset[dataset["speaker_occupation"]=="Entrepreneur"]["views"].sum() / len(dataset[dataset["speaker_occupation"]=="Entrepreneur"])))
    
        
    #plotting views for each tag.
    ttp.tagsTalksPlot(dataset)
    
    #tags count yearly (CAN USE GUI HERE)
    print("\nMost popular Tags for year 2015")
    print("===="*7)
    year="2015"
    ttp.tagsCountYearly(dataset,year,listTags)
    print("\nMost popular Tags for year 2016")
    print("===="*7)
    year="2016"
    ttp.tagsCountYearly(dataset,year,listTags)
    print("\nMost popular Tags for year 2017")
    print("===="*7)
    year="2017"
    ttp.tagsCountYearly(dataset,year,listTags)
    
#    #Ratings vs count plot
#    counter = {'Funny':0, 'Beautiful':0, 'Ingenious':0, 'Courageous':0, 'Longwinded':0, 'Confusing':0, 'Informative':0, 'Fascinating':0, 'Unconvincing':0, 'Persuasive':0, 'Jaw-dropping':0, 'OK':0, 'Obnoxious':0, 'Inspiring':0}
#    neg_descriptors = {"Confusing", "Unconvincing", "Longwinded", "Obnoxious", "OK"}
#    rp.ratingsPlot(dataset,counter,neg_descriptors)
#    
#    #Ratings vs count plot
#    counter = {'Funny':0, 'Beautiful':0, 'Ingenious':0, 'Courageous':0, 'Longwinded':0, 'Confusing':0, 'Informative':0, 'Fascinating':0, 'Unconvincing':0, 'Persuasive':0, 'Jaw-dropping':0, 'OK':0, 'Obnoxious':0, 'Inspiring':0}
#    neg_descriptors = {"Confusing", "Unconvincing", "Longwinded", "Obnoxious", "OK"}
#    rp.ratingsPlot(dataset,counter,neg_descriptors)
    
    k.knn(dataset,listTags,durationEntry,languageEntry)
    twty.searchTweets()
    
def checkInput():
    if(durationEntry.get() and languageEntry.get() and len(listTags)!=0):
        dur = durationEntry.get()
        lan = languageEntry.get()
        try:
            d = int(dur)
            l = int(lan)
            runCode()
        except ValueError:
            messagebox.showinfo("Error","Please Enter Valid Input")
    else:
        messagebox.showinfo("Error","Please Enter Valid Input")

runBtn = Button(window, text="Run", command=checkInput,background="gray92",foreground="OrangeRed2")
runBtn.grid(column=2, row=7)



def showTagGraph():
    newWindow = Toplevel()
    newWindow.title("Ted Talks per Tags")
            
    tagGraph = Image.open("tagTalk.png")
    tagPhoto = ImageTk.PhotoImage(tagGraph)
    tagImageLbl = Label(newWindow,image=tagPhoto)
    tagImageLbl.image = tagPhoto
    tagImageLbl.grid(column=2,row=1,padx=1,pady=1,sticky=W)
    newWindow.mainloop()

def showRatingGraph():
    newWindow = Toplevel()
    newWindow.title("Ted Talks per Ratings")
    
    ratingGraph = Image.open("rating.png")
    ratingPhoto = ImageTk.PhotoImage(ratingGraph)
    ratingImageLbl = Label(newWindow,image=ratingPhoto)
    ratingImageLbl.image = ratingPhoto
    ratingImageLbl.grid(column=2,row=1,padx=1,pady=1,sticky=W)
    newWindow.mainloop()


def showPublisherGraph():
    newWindow = Toplevel()
    newWindow.title("Ted Talks per Publishers")
    
    publisherGraph = Image.open("pyp.png")
    publisherPhoto = ImageTk.PhotoImage(publisherGraph)
    pubImageLbl = Label(newWindow,image=publisherPhoto)
    pubImageLbl.image = publisherPhoto
    pubImageLbl.grid(column=2,row=1,padx=1,pady=1,sticky=W)
    newWindow.mainloop()



new_itemTag = Menu(menu,background='gray97', foreground='slate blue')
new_itemTag.add_command(label='Tags Graph',command=showTagGraph)

new_itemTag.add_command(label='Ratings Graph',command=showRatingGraph)

new_itemTag.add_command(label='Publisher Graph',command=showPublisherGraph)


menu.add_cascade(label='Graphs Data',menu=new_itemTag)

window.mainloop()
#gui ends
#%%