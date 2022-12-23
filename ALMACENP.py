import Almacen
import Venta
import Usuario
from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox
import ALMACENP

def Almacenp(USUARIO,CLAVE,root):
    window = Toplevel(root)
    window.geometry("970x490")
    window.title("Ricale")
    window.resizable(False,False)
    window.config(background="#216141")
    consola = scrolledtext.ScrolledText(window,width="112",height="20")
    consola.place(x=20,y=120)
    def imprimir( txt):
        limpiar()
        consola.insert("1.0", txt)
    def limpiar():
        consola.delete("1.0","end")
    def ventas():
        txt="Cliente\t\tVendedor\t\tTotal\t\tProducto\t\tUnidades\n"
        a=Venta.Venta()
        R=a.obtenerTodo()
        for r in R:
            txt=txt+r["Cliente"]+"\t\t"+r["Vendedor"]+"\t\t"+r["Total"]+"\t\t"+r["Producto"]+"\t\t"+r["Unidades"]+"\n"
        txt=txt+"Total: "+str(a.total())
        imprimir(txt)
    def stock():
        txt="Producto\t\tUnidades\t\tPrecio\n"
        a=Almacen.Almacen()
        R=a.obtenerTodo()
        for r in R:
            txt=txt+r["Producto"]+"\t\t"+r["Unidades"]+"\t\t"+r["Precio"]+"\n"
        imprimir(txt)
    def ventasUsuario():
        txt="Cliente\t\tVendedor\t\tTotal\t\tProducto\t\tUnidades\n"
        a=Venta.Venta()
        R=a.obtenerPorUsuario(USUARIO)
        for r in R:
            txt=txt+r["Cliente"]+"\t\t"+r["Vendedor"]+"\t\t"+r["Total"]+"\t\t"+r["Producto"]+"\t\t"+r["Unidades"]+"\n"
        txt=txt+"Total: "+str(a.totalPorUsuario(USUARIO))
        imprimir(txt)

    Label(window,text="Salida:  ",bg="#216141",fg="white").place(x=30,y=80)    
    Button(window,text="Ver Ventas",command=ventas, width="10",height="1").place(x=30,y=30)
    Button(window,text="Ver Stock",command=stock, width="10",height="1").place(x=170,y=30)
    Button(window,text="Ver Ventas del usuario",command=ventasUsuario, width="20",height="1").place(x=320,y=30)