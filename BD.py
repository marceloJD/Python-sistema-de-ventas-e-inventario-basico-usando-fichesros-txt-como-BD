class bd:
    def __init__(self, fuente,separador,campos):
        self.fuente = fuente
        self.separador = separador
        self.campos = campos #["Nombre","Clave"]
    def WRITE(self,nuevo):#matriz de diccionarios [{"Nombre":"M","clave":"1232"}{..}{..}]
        archivo = open(self.fuente,'w')
        txt = ""
        for registro in nuevo:
            txtRegistro = ""
            for campo in self.campos:
                txtRegistro=txtRegistro+registro[campo]+";"  
            txtRegistro=txtRegistro.strip(";")    
            txt=txt+txtRegistro+"\n"
        txt=txt.strip("\n")          
        archivo.write(txt)
        archivo.close()

    def READ(self,condicion):##condicion es una funcion 
        r = []
        archivo = open(self.fuente)
        lineas = archivo.readlines()
        for i in range(len(lineas)):
            lineas[i]=lineas[i].strip('\n')
            objeto=lineas[i].split(self.separador) #["Marco","123"]
            diccionario = dict()
            j = 0
            for columna in self.campos:
                diccionario[columna]=objeto[j] # diccionario= {"Nombre":"M","clave":"1232"}
                j=j+1
            if( condicion(diccionario) ):
                r.append(diccionario)
        archivo.close()
        return r
    def create(self,registro):
        def f(r):
            return True
        r = self.READ(f) ## obtengo todos los elementos  del la tabla o del archivo [ {}{}{}{}]
        r.append(registro)
        self.WRITE(r)
    def upload(self,transformacion,condicion):
        def f(r):
            return True
        R = self.READ(f)
        i=0
        for r in R:
            if(condicion(r)):
                R[i]=transformacion(r)
            i=i+1
        self.WRITE(R)
    def delete(self,condicion):
        def f(r):
            return True
        R = self.READ(f)
        result = []
        for r in R:
            if(not condicion(r)):
                result.append(r)
        self.WRITE(result)
    


