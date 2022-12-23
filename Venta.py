import BD
#Venta: Cliente , Vendedor ,Total , Producto , Unidades
#Almacen: Producto, Unidades , Precio
#Usuario: Nombre , Clave
import Almacen
class Venta:
    def __init__(self):
        self.fuente = "ventas.txt"
        self.separador = ";"
        self.campos = ["Cliente" , "Vendedor" ,"Total" , "Producto" , "Unidades"]
        self.con = BD.bd(self.fuente,self.separador,self.campos)
    def total(self):
        def c(r):
            return True
        r=0
        R=self.con.READ(c)
        for x in R:
            r=r+float(x["Total"])
        return r
    def totalPorUsuario (self,usuario):
        def c(r):
            return r["Vendedor"]==usuario
        r=0
        R=self.con.READ(c)
        for x in R:
            r=r+float(x["Total"])
        return r
    def obtenerTodo(self):
        def c(r):
            return True
        return self.con.READ(c)
    def obtenerPorUsuario(self,usuario):
        def c(r):
            return r["Vendedor"]==usuario
        return self.con.READ(c)
    def ingresarVenta(self,registro):
        producto = registro["Producto"]
        cantidad = float(registro["Unidades"])
        precio=0
        def c(r):
            return r["Producto"]==producto
        a = Almacen.Almacen()
        r1=(a.salidaDeMercaderia(cantidad,producto))
        if(r1=="OK"):
            precio= float((a.obtener(c))[0]["Precio"])
            registro["Total"]=str(cantidad*precio)
            self.con.create(registro)
        return (r1,cantidad*precio)
