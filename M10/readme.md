1. ¿Que hace el bloque try/except ValueError? ¿Que pasaria si el usuario escribe "veinte" y quitamos ese bloque?

Este bloque sirve para evitar que el programa se cierre si escribimos algo que no sea un numero. Si escribimos "veinte" y quitamos ese bloque, el programa daria un error y se detendria.

Diccionarios y funciones (los refranes)

4. ¿Por que guardamos los refranes en un diccionario y no en una lista? ¿Que ventaja tiene que el refran sea la clave y el significado el valor?

Porque asi podemos encontrar mas facilmente el significado de cada refran. Solo buscamos la frase y el programa nos muestra lo que significa.

5. ¿Para que sirven las funciones decir_refran() y decir_refran_especifico()? ¿En que se diferencian?

La primera muestra un refran al azar y la segunda muestra el refran que nosotros elegimos.

6. Si quisieras agregar un refran de tu propia abuela, ¿que linea tendrias que modificar? ¿Hay que cambiar algo mas?

Agregaria el nuevo refran dentro del diccionario REFRANES, siguiendo el mismo formato de los otros. No necesitaria cambiar nada mas.

Decisiones (if / elif / else)

7. En el programa, ¿que refran recibe una persona de 18 años? ¿Y una de 17? Explica por que.

Una persona de 18 años recibe "Uno pone y Dios dispone", porque ya tiene 18 años. Una persona de 17 recibe "Haz el bien y no mires a quien", porque todavia no tiene 18.

8. ¿Que pasaria si cambiaramos el orden y pusieramos primero if edad >= 18 y despues elif edad >= 60? ¿Alguien recibiria alguna vez el refran de "Agua que no has de beber"?

No, porque las personas de 60 años o mas tambien cumplen la primera condicion. Por eso el programa nunca llegaria a la segunda.

API y JSON (Parte 2)

9. ¿Que convierte json.loads() y en que se transforma? ¿Y json.dumps(), que hace en direccion contraria?

json.loads() convierte el texto JSON en un diccionario de Python. En cambio, json.dumps() convierte los datos de Python en texto JSON.

10. Para obtener la ciudad del usuario, escribimos datos['address']['city']. ¿Por que necesitamos dos pares de corchetes?

Porque la informacion esta dentro de dos diccionarios. Primero buscamos address y despues city para encontrar la ciudad.

11. Hay tres tipos de error en esa parte (HTTPError, URLError y JSONDecodeError). ¿Cual ocurriria si no tienes internet? ¿Y si el servidor responde con una pagina rota?

Si no tenemos internet, puede aparecer URLError porque el programa no logra conectarse. Si el servidor envia informacion que no tiene un formato JSON correcto, aparece JSONDecodeError.

12. ¿Por que es buena idea usar timeout=10 al hacer la peticion?

Porque asi el programa no se queda esperando demasiado tiempo si el servidor no responde. Despues de 10 segundos puede mostrar un error.

Juego y reflexion general (Parte 3)

13. En el juego "Completa el refran", ¿como divide el programa el refran en dos mitades? ¿Que hacen split(), join() y //?

Primero split() separa el refran en palabras. Despues join() sirve para unirlas y // divide la cantidad de palabras en dos partes.

14. ¿Para que sirve el bloque if name == "main": al final del archivo?

Sirve para que el programa ejecute main() cuando abrimos el archivo directamente. Asi no se ejecuta automaticamente cuando se usa desde otro archivo.

15. Si tuvieras que agregar una cuarta parte al programa, ¿que agregarias y que conceptos nuevos necesitarias usar?

Yo agregaria una parte para guardar nuestros refranes favoritos y poder verlos despues. Usaria listas, diccionarios y archivos para guardar esa informacion.