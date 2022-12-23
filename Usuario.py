import BD
#Venta: Cliente , Vendedor ,Total , Producto , Unidades
#Almacen: Producto, Unidades , Precio
#Usuario: Nombre , Clave
class Usuario:
    def __init__(self):
        self.fuente = "usuarios.txt"
        self.separador = ";"
        self.campos = ["Nombre" , "Clave" ]
        self.con = BD.bd(self.fuente,self.separador,self.campos)
    def autenticar(self,usuario,clave):
        def c(r):
            return r["Nombre"]==usuario and r["Clave"]==clave
        r=self.con.READ(c)
        return 0<len(r) 
    def ingresar(self ,usuario,clave,master,masterKey):
        registro={"Nombre" :usuario, "Clave":clave}
        CON = BD.bd("masters.txt",";",["Nombre" , "Clave" ])
        def C(r):
            return r["Nombre"]==master and r["Clave"]==masterKey
        R=CON.READ(C)
        if len(R)<1:
            return "Acceso no permitido ... clave master incorrecta"
        def c(r):
            return r["Nombre"]==registro["Nombre"]
        r=self.con.READ(c)
        if(len(r)>0):
            return "Ya existe el usuario..."
        self.con.create(registro)
        return "OK"










