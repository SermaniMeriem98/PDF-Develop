# coding: utf-8
from distutils.dir_util import copy_tree
from PyPDF2 import PdfFileMerger
import os, string as st
import glob
import shutil
import os
import codecs
import sqlite3
from tkinter import *
#-----------------------------------------------Interface1--------------------------------------------------------------
window = Tk()
#personnaliser cette fenitre
window.title("PDF Develop ")
window.geometry("1080x720")
window.minsize()
window.iconbitmap("logo.ico")
window.config(background='#800000')
#--------------------------------------------fusion_pdf-----------------------------------------------------------------
def fusion_pdf():
    pdfs = [a for a in os.listdir() if a.endswith(".pdf")]
    # Fusionner les pdf du répertoire courant
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(open(pdf, 'rb'))
    # Créer un répertoire "fusion_pdf" s'il n'existe pas déjà
    try:
        os.mkdir(r'.\fusion_pdf')
    except:
        pass
    # './fusion_pdf/result.pdf' : fichier contenant les pdf fusionnés
    with open('./fusion_pdf/result.pdf', 'wb') as fout:
        merger.write(fout)
    # ----------------------------------------autre page---------------------------------------------------------------
    Manager = Tk()
    Manager.title("PDF Develop ")
    Manager.geometry("420x120")
    #Manager.minsize()
    Manager.iconbitmap("logo.ico")
    Manager.config(background='#800000')
    presentation = Label(Manager, font=("Helvetica",10),bg='#800000',fg='white',text='The listed files are concatenated in /fusion_pdf/result.pdf')
    presentation.pack()
    Bouton = Button(Manager, text='Leave', command=Manager.quit, bg='#999999',font=("Helvetica",10), fg='white')
    Bouton.pack()
    Manager.mainloop()
#---------------------------------------------Fonction copy-------------------------------------------------------------
def copy():
    # copier pdf
    Manager = Tk()
    Manager.title("PDF Develop ")
    Manager.geometry("220x120")
    # Manager.minsize()
    Manager.iconbitmap("logo.ico")
    Manager.config(background='#800000')
    chemin = data_path = os.path.expanduser('~')+nomfich.get()
    chemin2 = data_path = os.path.expanduser('~') + '\Desktop\PDF-Develop'
    try:
        shutil.move(chemin, chemin2)
        # Presentation du programme
        """chemin = data_path = os.path.expanduser('~') + '\Desktop'
        chemin2 = data_path = os.path.expanduser('~') + '\Desktop\PDF-Develop'
        nom_fich = input("donnez le nom de fichier : ")
        liste1 = os.listdir(chemin)
        liste2 = []
        for fich in liste1:
            if fich.endswith(".pdf"):
                liste2.append(fich)
        f = codecs.open("liste3.tex", "wb", encoding='utf8')
        for fichier in liste2:
            if nom_fich == fichier:
                with open('fichier', 'rb') as fout:
                    a = shutil.copy2(fichier, chemin2)
        f.close()"""
        presentation = Label(Manager, font=("Helvetica", 10), bg='#800000', fg='white', text='The file  has been copied')
        presentation.pack()
        # Creation du bouton
        Bouton2 = Button(Manager, text=' Leave', command=Manager.quit, bg='#999999', font=("Helvetica", 10), fg='white')
        Bouton2.pack()
        print("work")
    except:
        presentation1 = Label(Manager, font=("Helvetica", 10), bg='#800000', fg='white',text='PDF file does not exist!')
        presentation1.pack()
        Bouton2 = Button(Manager, text=' Leave', command=Manager.quit, bg='#999999', font=("Helvetica", 10), fg='white')
        Bouton2.pack()
        print("PDF file does not exist!")
    Manager.mainloop()

#------------------------------------------------------supprimer-------------------------------------------------------
def supprimer():
    Manager = Tk()
    Manager.title("PDF Develop ")
    Manager.geometry("220x120")
    # Manager.minsize()
    Manager.iconbitmap("logo.ico")
    Manager.config(background='#800000')
    chemin = data_path = os.path.expanduser('~') + '\Desktop\PDF-Develop'+nomfich.get()
    try:
        os.remove(chemin)
        print("work")
        # Presentation du programme
        presentation = Label(Manager, font=("Helvetica", 10), bg='#800000', fg='white',
                             text='File' + nomfich.get() + ' has been deleted')
        presentation.pack()
        # Creation du bouton
        Bouton2 = Button(Manager, text=' Leave', command=Manager.quit, bg='#999999', font=("Helvetica", 10), fg='white')
        Bouton2.pack()
    except:
        presentation1 = Label(Manager, font=("Helvetica", 10), bg='#800000', fg='white',text='PDF file does not exist!')
        presentation1.pack()
        Bouton2 = Button(Manager, text=' Leave', command=Manager.quit, bg='#999999', font=("Helvetica", 10), fg='white')
        Bouton2.pack()
        print("PDF file does not exist!")
    Manager.mainloop()
#---------------------------------------------main----------------------------------------------------------------------
frame=Frame(window,bg='#800000')
#---------------------------------------------image---------------------------------------------------------------------
width=300
height=300
image=PhotoImage(file="images.png").zoom(35).subsample(32)
canvas=Canvas(frame,width=width,height=height,bg='#800000',bd=0,highlightthickness=0)
canvas.create_image(width/2,height/2,image=image)
canvas.grid(row=0,column=0,sticky=W)
#--------------------------------------------Interface------------------------------------------------------------------
right_frame=Frame(frame,bg='#800000')
l_chemin2_label = Label(right_frame, text="File : ",font=("Helvetica",14), bg='#800000', fg='white')
l_chemin2_label.pack()
nomfich = Entry(right_frame, width=30, bg='#999999', fg='black',font=("Helvetica",14))
nomfich.pack()
l = Label(right_frame, text="", bg='#800000', fg='white')
l.pack()
#copy
copy_but = Button(right_frame, text="Copy", font=("Helvetica",11),bg='#999999',fg='black', command=copy)
copy_but.pack(fill=X)
#supprimer
copy_but = Button(right_frame, text="Remove", font=("Helvetica",11),bg='#999999',fg='black', command=supprimer)
copy_but.pack(fill=X)
# Fusion
save_button=Button(right_frame, text="Fusion",font=("Helvetica",11),bg='#999999',fg='black',command=fusion_pdf)
save_button.pack(fill=X)
#fermer frame
right_frame.grid(row=0,column=1,padx=30, ipadx=30)
#ajouter
frame.pack(expand=YES)
#afficher la fenetre
window.mainloop()