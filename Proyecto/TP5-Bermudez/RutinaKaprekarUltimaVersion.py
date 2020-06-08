#https://github.com/GabrielBermudez/GrupoA-TT/tree/master/Proyecto/TP5-Bermudez

class Kaprekar:

    def Inicio(self):
        self.auxPrimerWhile=0
        self.listaIteraciones=[]

        print("Cuantas pruebas desea realizar?") #Al inicio del programa, se le pide al usuario que ingrese la cantidad de pruebas a realizar
        self.cantidadPruebas=input()

        while(self.auxPrimerWhile!=int(self.cantidadPruebas)): #Mediante este while el programa se repetira en base a lo que el usuario escribo con anterioridad

            self.AscNum=0
            self.desNum=0
            self.contador=0
            self.aux=1
            self.constanteKaprekar=6174
            self.condicion=False

            self.numeroEnteros=input()

            #Si se ingresa un numero menor a 4 cifras, es autocompletado con la cantidad de 0 que haga falta para llegar a los 4 digitos
            
            if(len(str(self.numeroEnteros))==3): #Los siguientes if, son para agregar 0 en caso de que en la diferencia, algun numero quede en 3 digitos, agrega los 0 que falten para llegar a 4 digitos
                self.numeroEnteros="0"+str(self.numeroEnteros)

            elif(len(str(self.numeroEnteros))==2):
                self.numeroEnteros="00"+str(self.numeroEnteros)
                    
            elif(len(str(self.numeroEnteros))==1):
                self.numeroEnteros="000"+str(self.numeroEnteros)
               

            
            self.auxPrimerWhile+=1 

            self.numero=list(map(int, str(self.numeroEnteros))) #El numero ingresado, lo paso a lista mediante la funcion list y map

            while(True): 

                if(self.numeroEnteros[0] == self.numeroEnteros[1] and self.numeroEnteros[0] == self.numeroEnteros[2] and self.numeroEnteros[0] == self.numeroEnteros[3] ):
                    self.listaIteraciones.append(8)
                    self.condicion=True
                    break

                if(self.numeroEnteros == str(self.constanteKaprekar)):
                    self.listaIteraciones.append(0)
                    self.condicion=True
                    break

                self.Ascendente(self.numero) #Llamo al metodo Ascendente que va a ordenar la lista de menor a mayor
                self.Descendente(self.numero) #Llamo al metodo Descendente que va a ordenar la lista de mayor a menor

                self.resultado= self.desNum - self.AscNum #El resultado es el valor numero de las listas convertidas a int y su posterior diferencia
               
                if(self.resultado == self.constanteKaprekar): #Si resultado llega a ser igual a la constante de Kaprekar, entonces corta el while
                    
                    break

                if(len(str(self.resultado))==3): #Los siguientes if, son para agregar 0 en caso de que en la diferencia, algun numero quede en 3 digitos, agrega los 0 que falten para llegar a 4 digitos
                    self.resultado="0"+str(self.resultado)

                elif(len(str(self.resultado))==2):
                    self.resultado="00"+str(self.resultado)
                    
                elif(len(str(self.resultado))==1):
                    self.resultado="000"+str(self.resultado)
                    


                self.numero=list(map(int, str(self.resultado)))
                self.aux+=1
            if(self.condicion!=True):
                self.listaIteraciones.append(self.aux)

           
        for self.value in self.listaIteraciones:
                  
            print(self.value)
            pass   
            

    def ValidarNumero(self,numero): #Mediante este metodo, verifico que todos los numeros no sean iguales, y que haya almenos 2 o mas diferentes
        if((numero[0] != numero[1]) or (numero[0] != numero[2]) or (numero[0] != numero[3] )):
            self.contador+=1

        if((numero[1] != numero[0]) or (numero[1] != numero[2]) or (numero[1] != numero[3] )):
            self.contador+=1

        if((numero[2] != numero[0]) or (numero[2] != numero[1]) or (numero[2] != numero[3] )):
            self.contador+=1

        if((numero[3] != numero[0]) or (numero[3] != numero[1]) or (numero[3] != numero[2] )):
            self.contador+=1 
        

    def Ascendente(self,numero): #Ordena la lista de menor a mayor
        self.listaAsc=sorted(numero)
        self.AscNum=int(str(self.listaAsc[0]) + str(self.listaAsc[1]) + str(self.listaAsc[2]) + str(self.listaAsc[3]))
       

    def Descendente(self,numero): #Ordena la lista de mayor a menor
        self.listaDes=sorted(numero,reverse=True)
        self.desNum=int(str(self.listaDes[0]) + str(self.listaDes[1]) + str(self.listaDes[2]) + str(self.listaDes[3])) 
       


kaprekar = Kaprekar()
kaprekar.Inicio()


