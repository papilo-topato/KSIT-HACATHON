import pyinputplus
from tkinter import *
from translate import Translator

screen = Tk()
screen.title("Langauge Translator with GUI by- TechVidvan")

LanguageChoices = {'Hindi','English','French','German','Spanish','Kannada','Telugu'}
InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()

InputLanguageChoice.set('English')
TranslateLanguageChoice.set('Telugu')

def Translate():
    translator = Translator(from_lang= InputLanguageChoice.get(),to_lang=TranslateLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)

#choice for input language
InputLanguageChoiceMenu = OptionMenu(screen,InputLanguageChoice,*LanguageChoices)
Label(screen,text="Choose a Language").grid(row=0,column=1)
InputLanguageChoiceMenu.grid(row=1,column=1)
 
#choice in which the language is to be translated
NewLanguageChoiceMenu = OptionMenu(screen,TranslateLanguageChoice,*LanguageChoices)
Label(screen,text="Translated Language").grid(row=0,column=2)
NewLanguageChoiceMenu.grid(row=1,column=2)

Label(screen,text="Enter Text").grid(row=2,column =0)
TextVar = StringVar()
TextBox = Entry(screen,textvariable=TextVar).grid(row=2,column = 1)
 
Label(screen,text="Output Text").grid(row=2,column =2)
OutputVar = StringVar()
TextBox = Entry(screen,textvariable=OutputVar).grid(row=2,column = 3)
 
#Button for calling function
B = Button(screen,text="Translate",command=Translate, relief = GROOVE).grid(row=3,column=1,columnspan = 3)
 
mainloop()
