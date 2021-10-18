#Ingresar desde el teclado una frase cualquiera e invertir aquellas palabras que tengan dos o mas consonantes
#consecutivas. Mostrar por pantalla la frase obtenida.

def invertir_palabra(palabra):
    consonante_anterior = False
    for letra in palabra:
        if consonante_anterior==False:
            if letra.lower() not in 'aeiouáéíóú':
                consonante_anterior=True
                continue
        else:
            if letra.lower() not in 'aeiouáéíóú':
                return palabra[::-1]
            else:
                consonante_anterior=False
       
    return palabra
    


frase = input('Ingrese una frase: ')
print('')
print('Frase ingresada:')
print(frase)

# primero hago la separacion de palabras por espacios
lista_palabras = frase.split()

# recorro las palabras evaluando sus condiciones
for i in range(len(lista_palabras)):
    # chequeo por simbolo al principio
    if not lista_palabras[i][0].isalpha():
        lista_palabras[i] = lista_palabras[i][0] + invertir_palabra(lista_palabras[i][1:])
    elif not lista_palabras[i][-1].isalpha():     # chequeo simbolo al final
        lista_palabras[i] = invertir_palabra(lista_palabras[i][:-1]) + lista_palabras[i][-1]
    else:
        lista_palabras[i] = invertir_palabra(lista_palabras[i])
        
# reordeno la frase
frase_convertida = ' '.join(lista_palabras)
print('')
print('Frase converida:')
print(frase_convertida)