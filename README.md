# Ejercicios de Programación

## 📘 Ejercicio 1 - Módulo 2

### Contexto
Trabajas en la secretaría de una institución educativa y recibes periódicamente las notas finales de los cursos en formato de lista.  
Necesitas automatizar un pequeño reporte.

### Consigna
Desarrolla un script que, dada una lista de notas, filtre automáticamente el listado para aislar únicamente las notas aprobatorias (mayores o iguales a 7).  
Finalmente, el script debe imprimir en pantalla las notas aprobadas junto con la fecha actual del sistema en la que se generó el reporte:


### Restricciones técnicas
- Debes utilizar obligatoriamente la función **`filter()`** combinada con una función anónima (**lambda**) para realizar el filtrado.  
- Debes utilizar la librería estándar correspondiente para obtener la fecha actual.

---

## 🚲 Ejercicio 2 - Módulo 3 

### Contexto
Estás armando un script para registrar el inventario de una tienda de bicicletas.  
Necesitas modelar los artículos utilizando programación orientada a objetos.

### Consigna
Desarrolla un script que implemente la siguiente estructura:

- **Clase Base:**  
  - Crea una clase genérica llamada `Bicicleta` que reciba un modelo y un precio.  
  - El precio debe ser un dato **privado (encapsulado)** para protegerlo de modificaciones externas.  
  - Incluye un método específico que permita leer este valor.  
  - La clase debe tener un método genérico llamado `describir()` que imprima en pantalla el modelo de la bicicleta.

- **Clase Hija:**  
  - Crea una segunda clase llamada `BicicletaElectrica` que herede las características de la base.  
  - Incorpora un nuevo atributo llamado `bateria`.  
  - Para validar tu código, instancia un objeto de la clase `BicicletaElectrica`, muestra su precio por pantalla llamando al método correspondiente y ejecuta su método `describir()`.

### Restricciones técnicas
- Debes aplicar **encapsulamiento explícito** en el atributo del precio.  
- Debes utilizar **herencia** y la función **`super()`** para inicializar la clase hija.

