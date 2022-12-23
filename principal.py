import Almacen
import Venta
import Usuario
from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox
from tkinter import simpledialog
import VENTAP

#####################
window = Tk()
window.geometry("250x350")
window.title("Ricale")
window.resizable(False,False)
window.config(background="#213141")

Label(text="Ricale  ",bg="#213141",fg="white",font=25  ).place(x=95,y=15)
Label(text="Usuario  ",bg="#213141",fg="white").place(x=20,y=60)
Label(text="Clave  ",bg="#213141",fg="white").place(x=20,y=90)
img=PhotoImage(file="imagen.png")
img=img.subsample(2)
Label(window,image=img).place(x=65,y=210)

clave=StringVar()
usuario=StringVar()
Entry(textvariable=usuario,width="20").place(x=100,y=60)
Entry(textvariable=clave,width="20").place(x=100,y=90)
def ingresar():
    c=clave.get()
    u=usuario.get()
    clave.set("")
    usuario.set("")
    U = Usuario.Usuario()
    if U.autenticar(u,c):
        VENTAP.VENTAS(u,c,window) 
    else:
        messagebox.showinfo(message="Usuario o contraseña incorrectos , puede registrarse primero", title="ERROR")

    pass
def registrar():
    c=clave.get()
    u=usuario.get()
    U = Usuario.Usuario()
    m = simpledialog.askstring(title="MSG", prompt="Super Usuario:")
    mk = simpledialog.askstring(title="MSG", prompt="Super Clave:")
    messagebox.showinfo(message=U.ingresar(u,c,m,mk), title="RESULTADO")   
    pass

Button(window,text="Ingresar",command=ingresar, width="26",height="1").place(x=30,y=130)
Button(window,text="Nuevo usuario",command=registrar, width="26",height="1").place(x=30,y=170)


window.mainloop()
















#v =Venta.Venta()
#v.ingresarVenta({"Cliente":"Marce" , "Vendedor" :"Xime","Total":"230" , "Producto":"Pollo" , "Unidades":"12"})
#Venta: Cliente , Vendedor ,Total , Producto , Unidades
#Almacen: Producto, Unidades , Precio
#Usuario: Nombre , Clave
#a = Almacen.Almacen()
##print(a.eliminarProductoPorNombre("Pizza"))
#print(a.editarProductoPorNombre({"Producto":"Pizza","Unidades":"4665","Precio":"1000"}))
#c = BD.bd("archivo.txt",";",["nombre","edad","hermana"])
#def condicion(registro):
#    return True
#def trans(registro):
#    return {"nombre":"GAAA","edad":"2","hermana":"X"}
#print(c.READ(condicion))
#c.upload(trans,condicion)
#print(c.READ(condicion))
##print(c.READ(condicion))

