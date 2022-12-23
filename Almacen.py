import BD
#Venta: Cliente , Vendedor ,Total , Producto , Unidades
#Almacen: Producto, Unidades , Precio
#Usuario: Nombre , Clave
class Almacen:
    def __init__(self):
        self.fuente = "stock.txt"
        self.separador = ";"
        self.campos = ["Producto" , "Unidades" ,"Precio" ]
        self.con = BD.bd(self.fuente,self.separador,self.campos)
    def nuevoProducto(self,registro):
        def c(r):
            return r["Producto"] == registro["Producto"]
        r=self.con.READ(c)
        if(len(r)>0):
            return "Ya existe el producto..."
        self.con.create(registro)
        return "OK"
    def editarProductoPorNombre(self,registro):
        def c(r):
            return r["Producto"] == registro["Producto"]
        def t(r):
            return registro
        r=self.con.READ(c)
        if(len(r)<1):
            return "No existe el producto..."
        self.con.upload(t,c)
        return "OK"
    def eliminarProductoPorNombre(self,nombre):
        def c(r):
            return r["Producto"] == nombre
        r=self.con.READ(c)
        if(len(r)<1):
            return "No existe el producto..."
        self.con.delete(c)
        return "OK"

    def entradaDeMercaderia(self,cantidad,producto):
        def c(r):
            return r["Producto"] == producto
        def t(r):
            r["Unidades"]=str(float(r["Unidades"])+cantidad)
            return r
        r=self.con.READ(c)
        
        if(len(r)<1):
            return "No existe el producto..."
        r=r[0]
        self.con.upload(t,c)
        return "OK"

    def salidaDeMercaderia(self,cantidad,producto):
        def c(r):
            return r["Producto"] == producto
        def t(r):
            r["Unidades"]=str(float(r["Unidades"])-cantidad)
            return r
        r=self.con.READ(c)
        
        if(len(r)<1):
            return "No existe el producto..."
        r=r[0]
        if( float(r["Unidades"])<cantidad ):
            return "No existe stock suficiente..."
        self.con.upload(t,c)
        return "OK"
    def obtenerTodo(self):
        def c(r):
            return True
        return self.con.READ(c)
    def obtener(self,c):
        return self.con.READ(c)

        
        
