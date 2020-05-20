
class Kaprekar:

    def Inicio(self):
        self.auxPrimerWhile=0

        print("Cuantas pruebas desea realizar?") #Al inicio del programa, se le pide al usuario que ingrese la cantidad de pruebas a realizar
        self.cantidadPruebas=input()

        while(self.auxPrimerWhile!=int(self.cantidadPruebas)): #Mediante este while el programa se repetira en base a lo que el usuario escribo con anterioridad

            self.AscNum=0
            self.desNum=0
            self.contador=0
            self.aux=1
            self.constanteKaprekar=6174

            while(True): #Este bucle se repetira siempre que el usuario ingrese un numero donde su cantidad de digitos sean diferentes a 4, en caso contrario hara un break
                print("Por favor ingrese un valor de 4 digitos: ")
                self.numeroEnteros=input()

                if(len(self.numeroEnteros) == 4):
                    print("------------------------------------------------------------")
                    break

            self.numero=list(map(int, str(self.numeroEnteros))) #El numero ingresado, lo paso a lista mediante la funcion list y map
            self.ValidarNumero(self.numero) #Llamo al metodo ValidarNumero, con su respectivo parametro que es una lista

            if(self.contador==4): #Si en el metodo de ValidarNumero hubieron al menos dos diferentes, va entrar en la secuencia del if
                
                self.auxPrimerWhile+=1 
                print("Numero ingresado: "+str(self.numeroEnteros))
                print("Caso de Prueba: "+str(self.auxPrimerWhile))

                while(True): 
                    self.Ascendente(self.numero) #Llamo al metodo Ascendente que va a ordenar la lista de menor a mayor
                    self.Descendente(self.numero) #Llamo al metodo Descendente que va a ordenar la lista de mayor a menor

                    self.resultado= self.desNum - self.AscNum #El resultado es el valor numero de las listas convertidas a int y su posterior diferencia
                    
                    print(str(self.desNum) +" + "+ str(self.AscNum)+" = " + str(self.resultado) + "        Iteracion: "+str(self.aux)) #Muestro cada iteracion con las listas ordenadas en su respectivo orden y el resultado
                    
                    if(self.resultado == self.constanteKaprekar): #Si resultado llega a ser igual a la constante de Kaprekar, entonces corta el while
                        print("------------------------------------------------------------")
                        break

                    if(len(str(self.resultado))==3): #Los siguientes if, son para agregar 0 en caso de que en la diferencia, algun numero quede en 3 digitos, agrega los 0 que falten para llegar a 4 digitos
                        self.resultado="0"+str(self.resultado)

                    elif(len(str(self.resultado))==2):
                        self.resultado="00"+str(self.resultado)
                    
                    elif(len(str(self.resultado))==1):
                        self.resultado="000"+str(self.resultado)
                    


                    self.numero=list(map(int, str(self.resultado)))
                    self.aux+=1
            else: #En caso de que los numeros eran iguales, va imprimir que es incorrecto el valor
                print("El numero ingresado es incorrecto.")
           
            

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


