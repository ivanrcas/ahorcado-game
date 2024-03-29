# AHORCADO GAME
## Descripción
Juego desarrollado en pygame basado en el juego del ahorcado con tres niveles dificultad ubicados en botones del menú principal.
- Nivel Bajo: El juegador cuenta con 18 intentos.
- Nivel Medio: El jugador cuenta con 12 intentos.
- Nivel Alto: El jugador cuenta con 6 intentos.

## Instalación del juego
1. Descargar el repositorio [click aquí] (https://codeload.github.com/ivanrcas/ahorcado-game/zip/refs/heads/main) o clonar repositorio desde computadora local desde tu cuenta github.
2. Instalar pygame
```
pip install pygame
```
4. Ejecutar main.py
5. El código se encuentra debidamente comentado con la lógica usada para los archivos: main.py y button.py. Además, el programa requiero arhivos multimedia para la experiencia del juego (imágenes y audios).

## Funcionalidades del Juego del Ahorcado
1. Selección de Palabra Secreta: El juego elige una palabra secreta al azar que el jugador debe adivinar.
2. Representación Gráfica: Se muestra un dibujo del ahorcado en progreso para indicar los errores del jugador.
3. Espacios Vacíos: Se presentan espacios vacíos para cada letra de la palabra secreta.
4. Intentos Restantes: Se muestra el número de intentos restantes antes de que el jugador sea “ahorcado”.
5. Entrada de Letras: El jugador ingresa letras para adivinar la palabra.
6. Validación de Letras: Se verifica si la letra ingresada está en la palabra secreta.
7. Fin del Juego: El juego termina cuando el jugador adivina la palabra o se completa el dibujo del ahorcado.

## Pseudocódigo:
1. Inicializar el juego:
   - Definir una lista de palabras secretas.
   - Elegir una palabra al azar como la palabra secreta.
   - Inicializar variables (intentos, letras adivinadas, etc.).

2. Bucle principal: mientras existan intentos restantes:
    - Mostrar la representación visual del ahorcado.
    - Mostrar la palabra parcialmente adivinada (con espacios en blanco para letras no adivinadas).
    - Solicitar al jugador que ingrese una letra.
    - Validar la entrada del jugador:
          - Verificar si la letra está en la palabra secreta.
          - Actualizar las letras adivinadas y los intentos restantes.
    - Verificar si el jugador adivinó la palabra completa:
          - Si todas las letras están adivinadas, mostrar un mensaje de victoria.
          - Si no, continuar con el siguiente intento.
    - Repetir el bucle.

3. Fin del juego:
   - Si se agotan los intentos, mostrar un mensaje de derrota y revelar la palabra secreta.
   - Permitir al jugador reiniciar el juego si lo desea.

## Configuración de palabras
Para agregar más palabras en el juego, se puede editar la línea de código 41:
```
WORDS = ['KODLAND', 'PYTHON', 'IDE', 'PYGAME', 'BUCLE', 'CONDICION']
```

Según el fragmento anterior, el juego está configurado por defecto con las seis palabras:
* KODLAND 
* PYTHON
* IDE
* PYGAME
* BUCLE
* CONDICION

