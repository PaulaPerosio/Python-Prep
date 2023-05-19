class Herramientas:
    def __init__(self, lista_numeros):

    # A proposito creamos una exepcion para cuando el valor ingresado no es lo que espero,
    # ya que en este caso es grave que lo ingresado no sea loq eu espero
        
    # Opcion 1: me aseguro que sea una lista. si no es, genera error
        #assert type (lista_numeros) == list, f'{lista_numeros} no es una lista'

    # Opcion 2: si no ingresa lo que quiero, lo capturo y despues puedo evaluarlo. Ademas creo una lista
        if type(lista_numeros) != list:
            self.lista = []
            raise ValueError ("valor ingresado incorrecto. se creo una lista vacia")
        else:
            self.lista = lista_numeros


    def verifica_primo(self):
        lista_primos =[]
        for i in self.lista:
            if (self.__verifica_primo(i)):
                lista_primos.append("True")
            else:
                lista_primos.append("False")
        return lista_primos

    def conversion_grados(self, origen, destino):

        lista_convertidos = []

        # Opcion 1: Me genera un error y me explica porque 
        #assert (origen=='celsius' or origen=='farenheit' or origen=='kelvin'), f'Los valores esperados son: 'celsius','farenheit','kelvin''

        # Opcion 2: No me geenra error, solo me imprime como debe ser
        valores_esperados = ['celsius','farenheit','kelvin']
        if str(origen) not in valores_esperados:
            print("Los valores esperados son:", valores_esperados)
            return lista_convertidos
        if str(destino) not in valores_esperados:
            print("Los valores esperados son:", valores_esperados)
            return lista_convertidos
        
        for i in self.lista:
            lista_convertidos.append(self.__conversion_grados(i, origen, destino))
        return lista_convertidos
    
    def factorial(self):
        lista_factoriados = []
        for i in self.lista:
            lista_factoriados.append (self.__factorial(i))
        return lista_factoriados

    def __verifica_primo(self, nro):
        es_primo = True
        for i in range(2, nro):
            if nro % i == 0:
                es_primo = False
                break
        return es_primo

    def valor_modal(self, menor):
        lista_unicos = []
        lista_repeticiones = []
        if len(self.lista) == 0:
            return None
        if (menor):
            self.lista.sort()
        else:
            self.lista.sort(reverse=True)
        for elemento in self.lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo

    def __conversion_grados(self, valor, origen, destino):
        valor_destino = None
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheit'):
                valor_destino = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                valor_destino = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                valor_destino = valor
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino

    def __factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.__factorial(numero - 1)
        return numero