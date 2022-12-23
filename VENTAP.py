import Almacen
import Venta
import Usuario
from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox
import ALMACENP

def VENTAS(USUARIO,CLAVE,root):
    window = Toplevel(root)
    window.geometry("550x270")
    window.title("Ricale")
    window.resizable(False,False)
    window.config(background="#813141")
    Label(window,text="Producto  ",bg="#813141",fg="white").place(x=20,y=60)
    Label(window,text="Cantidad  ",bg="#813141",fg="white").place(x=20,y=90)
    Label(window,text="Cliente  ",bg="#813141",fg="white").place(x=20,y=120)
    Label(window,text="Ventas:  ",bg="#813141",fg="white",font=40).place(x=20,y=16)
    producto=StringVar()
    cantidad=StringVar()
    cliente=StringVar()
    Entry(window,textvariable=producto,width="20").place(x=100,y=60)
    Entry(window,textvariable=cantidad,width="20").place(x=100,y=90)
    Entry(window,textvariable=cliente,width="20").place(x=100,y=120)
    Label(window,text="Salida  ",bg="#813141",fg="white").place(x=250,y=60)
    consola = scrolledtext.ScrolledText(window,width="30",height="6")
    consola.place(x=250,y=90)
    def imprimir(total, txt):
        limpiar()
        T="Total a pagar: "+str(total)+"\n "+txt
        consola.insert("1.0", T)
    def limpiar():
        consola.delete("1.0","end")
    def ingresarVenta():
        v=Venta.Venta()
        r,t=v.ingresarVenta({"Cliente":cliente.get() , "Vendedor" :USUARIO,"Total":"230" , "Producto":producto.get() , "Unidades":cantidad.get()})
        imprimir(t,r)
        pass
    def Alma():
        ALMACENP.Almacenp(USUARIO,CLAVE,window)
    Button(window,text="Ingresar",command=ingresarVenta, width="26",height="1").place(x=30,y=160)
    img=PhotoImage(file="img.png")
    img=img.subsample(8)
    Button(window,text="Almacen",command=Alma, width="100",height="20",image = img,  compound = LEFT).place(x=190,y=210)
    window.mainloop()