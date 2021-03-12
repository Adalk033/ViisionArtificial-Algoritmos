import tkinter
from tkinter import *
from tkinter import filedialog  # Para cargar archivos desde explorador
from tkinter import ttk  # Para poder usar combobox
from tkinter import messagebox #Para mostrar mensajes simples al usuario
import time #Para la ejecución paso a paso
from threading import Thread #Para la ejecución paso a paso


window = tkinter.Tk()
imagen = NONE

def readfile():
    filename = filedialog.askopenfile(title="Select file",
                                      filetypes=(("text files", "*.txt"), ("all files", "*.*")))

def cargar_imagen(event):
    global imagen
    ttk.Label(window, text="Cargue su imagen que desea :", font=("Cambria", 15)).grid(column=0, row=6, padx=10, pady=10)
    imagen.grid(column=1, row=6)
    imagen.current()


def Creacion_Interfaz():
    global window
    global imagen

    window.title("Menu de programas de vision artificial")
    window.geometry('700x400')    

    #Seleccionar algoritmo
    ttk.Label(window, text="Eliga el tipo de algoritmo :", font=("Cambria", 15)).grid(column=0, row=5, padx=10, pady=10)
    algoritmos = ttk.Combobox(window, width=35, height=30, textvariable=tkinter.StringVar(), state="readonly")
    algoritmos.bind("<<ComboboxSelected>>", cargar_imagen)
    algoritmos['values'] = (' 1', ' 2', ' 3', ' 4', ' 5')
    algoritmos.grid(column=1, row=5)
    algoritmos.current()

    #Cargar imagen
    imagen = Button(window, text='LOAD MAP', relief='flat', font='Verdana 20 bold', bg='plum2', fg='black',
                    activebackground='darkorange4', activeforeground='black', command=readfile)
    imagen.place(x=186, y=420, width=280, height=118)
    
    imagen.bind("<<Button>>")


    # No permite redimiensionar la ventana por cuestiones de formato
    window.resizable(width=False, height=False)


    



Creacion_Interfaz()
window.mainloop()
