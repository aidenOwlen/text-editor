from tkinter import *

import re
from tkinter import filedialog
from tkinter import font

def Save2():
       texting = Le_texte.get(0.0,END)
       texx = re.sub("\([0-9]+\) ", "",texting)
       filename = filedialog.asksaveasfilename()
       All_texte = Le_texte.get(0.0,END)
       ff = open(filename+".txt","w")
       ff.write(texx)
       ff.close()


#helv36 = font.Font(family="Helvetica",size=36,weight="bold")

def helvetica():
        foN = font.Font(family="Helvetica")
        Le_texte.configure(font = foN)
def courrier():
        foN = font.Font(family="Courrier")
        Le_texte.configure(font = foN)
def times():
        foN = font.Font(family="Times")
        Le_texte.configure(font = foN)
        
def red():
        Le_texte.configure(fg ="red")
def blue():
        Le_texte.configure(fg = "blue")
def black():
        Le_texte.configure(fg = "black")
def yellow():
        Le_texte.configure(fg = "yellow")
def green():
        Le_texte.configure(fg = "green")
def grey():
        Le_texte.configure(fg = "grey")
def orange():
        Le_texte.configure(fg = "orange")
                

def start():
        
        
        
        x = Le_texte.get(0.0,END).splitlines()
        a = 1.0
        b= 1.999
        for i in x:
                if re.search("([0-9]+)",i) is not None:
                        
                        Le_texte.delete(a,b)
                        xxx = re.sub("([0-9]+)","",i)
                        xx = re.sub("([0-9]+)",str(len(xxx)-3),i)
                        
                        
                        Le_texte.insert(a, xx)
                else:
                        
                        Le_texte.insert(a,"("+str(len(i))+") ")
                
                        
                        
                        
                        
                
                        
                
               
                a +=1.0
                b += 1
        a = 1.0
        fenetre.after(300,start)

def clear():
        Le_texte.delete(0.0,END)
        

def save():
        filename = filedialog.asksaveasfilename()
        All_texte = Le_texte.get(0.0,END)
        ff = open(filename+".txt","w")
        ff.write(All_texte)
        ff.close()

def openx():
        fileName = filedialog.askopenfilename(title = "Choose a .txt file")
        
        fff = open(fileName,"r")
        fr = fff.read()
        Le_texte.delete(0.0,END)
        Le_texte.insert(0.0, fr)
        

def Lba(*args):
        Le_texte.yview(*args)
        Count.yview(*args)

fenetre = Tk()
fenetre.withdraw()




main = Toplevel(fenetre)
main.title("Texte Fiver Project")
main.grid_columnconfigure(0,weight=1)
main.grid_rowconfigure(0,weight=1)






Le_texte = Text(main)
Le_texte.grid(row=0,column = 0, sticky = N+S+W+E)
sc = Scrollbar(main,orient="vertical", command = Le_texte.yview)
sc.grid(row=0,column=1,sticky = NS)
#sc = Scrollbar(main,orient = "vertical", command = Le_texte.yview)
#sc.pack(RIGHT)
#Le_texte.configure(yscrollcommand = sc)
Le_texte.configure(yscrollcommand = sc.set)




#But = Button(main, text="start", command = start)
#But.grid(row=1,column=0)

#Count = Text(main,width=5,bg="dark grey")
#Count.grid(row=0,column=0, sticky=N+S)
#Count.configure(yscrollcommand = sc.set)
#helv36 = font.Font(family="Helvetica",size=36,weight="bold")


menu = Menu(main)

menu.add_command(label = "Save", command = save)

menu.add_command(label = "Save without counts", command = Save2)
menu.add_command(label = "Clear", command = clear)
menu.add_command(label = "Open file", command = openx)

Colormenu = Menu(menu,tearoff=0)
Colormenu.add_command(label="red", command=red)
Colormenu.add_command(label="blue",command=blue)
Colormenu.add_command(label="black", command = black)
Colormenu.add_command(label = "yellow", command = yellow)
Colormenu.add_command(label="green", command = green)
Colormenu.add_command(label="grey",command = grey)
Colormenu.add_command(label ="orange", command = orange)

Fontmenu = Menu(menu,tearoff= 0)
Fontmenu.add_command(label = "Courrier", command = courrier)
Fontmenu.add_command(label="Times", command = times)
Fontmenu.add_command(label = "Halvetica",command = helvetica)


menu.add_cascade(label = "Font", menu = Fontmenu)
menu.add_cascade(label = "Color", menu = Colormenu)


main.config(menu = menu)

fenetre.after(300,start)
fenetre.mainloop()
