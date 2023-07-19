from copy import copy
from struct import pack
from tokenize import String
import pyperclip
import pyshorteners
from tkinter import *
#madebyHemangVyas
#GUI
root = Tk()
root.geometry("700x350")
root.title("URL Shortner Application")
root.configure(bg="#7F7FFF")

#Define Variable for url
urlmain = StringVar()
urlshortmain = StringVar()

#Define Function
def urlShortner():
    urladdress = urlmain.get()
    urlshort = pyshorteners.Shortener().tinyurl.short(urladdress)
    urlshortmain.set(urlshort)

def copyurl():
    urlshort = urlshortmain.get()
    pyperclip.copy(urlshort)


Label(root,text="URL Shortner App",font=('Arial', 12)).pack(pady=10)
Entry(root,textvariable=urlmain,width=50,font=('Arial 14')).pack(padx=10, pady=10)
Button(root,text="Generate Short Url",command=urlShortner).pack(pady=7)
Entry(root,textvariable=urlshortmain,width=50,font=('Arial 14')).pack(padx=10, pady=10)
Button(root,text="Copy Short Url",command=copyurl).pack(pady=5)

root.mainloop()
#author: hemang vyas