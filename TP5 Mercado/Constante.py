class Constante:
    def __init__(self):
        self.menor = ""
        self.mayor = ""
        self.casos = 0
        self.contCasos = 0
        self.numeroIngresado = 0
        self.nuevoNro = 0
        self.numIguales = 0
        print("Ingrese la cantidad de pruebas que desea realizar: ")
        #Cantidad de veces que va a dar vueltas el bucle, pidiendo ingresar un numero
        #para realizar la prueba de la constante
        self.casos = int(input())
        
        while(self.contCasos != self.casos):
            print("Ingrese un número de 4 dígitos para el caso: ")
            #número de 4 dígitos ingresado por el usuario para el primer caso
            self.numeroIngresado = int(input())
            #si el número ingresado es la propia constante, se muestra 0
            if(self.numeroIngresado == 6174):
                print("0 => Constante de Kaprekar")
            self.contadorIteraciones = 0
            #contador de igualdades entre las cifras del mismo número
            self.numIguales = 0
            #cantidad de veces que se va a pedir al usuario que ingrese un nùmero
            self.contCasos +=1
            #Bucle que va a repetir el proceso hasta que el resultado de la resta sea 6174
            while(self.numeroIngresado != 6174):
                #se llama al primer método pasando como parámetro el número que ingreso el usuario
                self.validarLargoNumero(self.numeroIngresado)
                #se llama al segundo método 
                self.validarCifrasRepetidas(self.nuevoNro, self.numIguales)
                #Si la variable global luego de verificar las repeticiones es mayor o igual a 3
                #es porque no hay al menos dos cifras diferentes
                if(self.numIguales >= 3):
                    #por lo tanto imprime 8 por pantalla
                    print("8")
                    #y corta para pedir el pròximo número
                    break
                #Se llama al tercer método
                self.mayor_Menor(self.nuevoNro)
                #se llama al último método
                self.resta(self.mayor, self.menor, self.contadorIteraciones)

    def validarLargoNumero(self, numeroIngresado):
        #se hace un casteo para pasar de int a String
        nro = str(numeroIngresado)
        #nueva variable para ir almacenando los datos leídos del string anterior
        nuevoNro = ""
        #se recorrer cada una de las posiciones del primer String
        for i in nro:
            #if para validad que lo que contienen las posiciones son números
            if(i.isdigit):
                #si es un número se almacena en el nuevo string
                nuevoNro += i
        #Valida el largo del nuevo arreglo y en caso de que el largo sea diferente de 4 agrega "0" donde corresponda
        if(len(nuevoNro) == 1):
            nuevoNro = "000" + nuevoNro
        elif(len(nuevoNro) == 2):
            nuevoNro = "00" + nuevoNro
        elif(len(nuevoNro) == 3):
            nuevoNro = "0" + nuevoNro
        
        self.nuevoNro = nuevoNro
        #se asigna el nuevo valor a una variable global y se retorna ese valor
        return self.nuevoNro
    
    def validarCifrasRepetidas(self, nuevoNro, numIguales):
        #se inicializa un contador para recorrer el string que se recibe como parámetro
        cont = 0
        #se asigna a la variable PrimerValor el valor almacenado en la posición 0 del string
        primerValor = int(nuevoNro[0])
        #con el bucle se recorre el largo del String nuevoNro
        while(cont < len(nuevoNro) - 1):
            #el valor de contador se aumenta en 1
            cont += 1
            #y en la variable comparador se almacena el valor de la posición "contador" del string
            comparador = int(nuevoNro[cont])
            #if para comparar si el primer valor es igual a algun otro dento del string
            if(primerValor == comparador):
                #Si en algún momento los valores coinciden la variable globar que recibe por parámetro se aumenta en 1
                self.numIguales +=1
            

    def mayor_Menor(self, nuevoNro):
        #en la variable aux se almacena el valor de la variable que se recibe por parámetro ordenada de menor a mayor
        aux = ''.join(sorted(nuevoNro))
        #en la variable mayor se almacena el valor de auxiliar pero ordenado de forma inversa
        mayor = aux[::-1]
        #Se revisa el largo de la variable aux y si es diferente de 4 se agregan los "0" correspondientes
        if(len(aux) == 1):
            aux = aux + "000"
        elif(len(aux) == 2):
            aux = aux + "00"
        elif(len(aux) == 3):
            aux = aux + "0"
        #Se revisa el largo de la variable mayor y si es diferente de 4 se agregan los "0" correspondientes
        if(len(mayor) == 1):
            mayor = mayor + "000"
        elif(len(mayor) == 2):
            mayor = mayor + "00"
        elif(len(mayor) == 3):
            mayor = mayor + "0"
        print("Mayor: " + str(mayor))
        print("Menor: " + str(aux))
        #se almacenan los valores de aux y mayor en variables globales y esos valores son los que se retornan
        self.menor = aux
        self.mayor = mayor
        return self.menor, self.mayor
    
    def resta(self, mayor, menor, contadorIteraciones):
        #se castean los valores de los valores que se reciben por parámetros para poder operar con ellos
        minuendo = int(mayor)
        sustraendo = int(menor)
        #if para si alguno de los valores recibidos es la constante
        if(minuendo != 6174 or sustraendo != 6174):
            #si no lo es, se realiza la resta correspondiente
            resta = minuendo - sustraendo
            #y el valor del resultado se almacena en la variable global numeroIngresado para que ésta vuelva a hacer comenzar el bucle
            self.numeroIngresado = resta
            #se aumenta el contador de iteraciones en 1
            self.contadorIteraciones += 1
            #se muestra los resultados por pantalla
            print(str(minuendo) + " - " + str(sustraendo) + " = " + str(resta) + " => Cantidad iteraciones " + str(self.contadorIteraciones))
        #se devuelve el valor de resta dentro de la variable numeroIngresado
        return self.numeroIngresado
    
Constante = Constante()