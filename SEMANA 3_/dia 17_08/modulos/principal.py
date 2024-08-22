#importamos el tkinter
import tkinter as tk #alias al tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

def abrirVentanaPrincipal():
    
    #Inicializamos la clase TK()
    ventana2 = tk.Tk() 
    #Tamaño de la ventana
    ventana2.geometry("350x450")
    
    boton1 = tk.Button(ventana2, text="ejercicio01", width=10,height=5,command="ejercicio01.py")
    boton1.grid(row=0,column=0,padx=50,pady=5)
    boton2 = tk.Button(ventana2, text="ejercicio02", width=10,height=5,command="") 
    boton2.grid(row=0,column=1,padx=50,pady=5)
    boton3 = tk.Button(ventana2, text="ejercicio03", width=10,height=5,command="")
    boton3.grid(row=1,column=0,padx=50,pady=5)
    boton4 = tk.Button(ventana2, text="ejercicio04", width=10,height=5,command="")
    boton4.grid(row=1,column=1,padx=50,pady=5)
    boton5 = tk.Button(ventana2, text="ejercicio05", width=10,height=5,command="")
    boton5.grid(row=2,column=0,padx=50,pady=5)
    boton6 = tk.Button(ventana2, text="ejercicio06", width=10,height=5,command="") 
    boton6.grid(row=2,column=1,padx=50,pady=5)
    boton7 = tk.Button(ventana2, text="ejercicio07", width=10,height=5,command="")
    boton7.grid(row=3,column=0,padx=50,pady=5)
    boton8 = tk.Button(ventana2, text="ejercicio08", width=10,height=5,command="")
    boton8.grid(row=3,column=1,padx=50,pady=5)
    
        
    #Mantener la ventana abierta
    ventana2.mainloop() 

#abrirVentanaPrincipal()