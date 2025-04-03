# funciones del ejercicio 2:
# Función para encontrar el título con más palabras
def encontrar_titulo_con_mas_palabras(titles):
    max_palabras = 0
    titulo_con_mas_palabras = ""
    
    # Iterar sobre la lista de títulos
    for titulo in titles:
        # Contar las palabras en el título
        cantidad_palabras = len(titulo.split())
        
        # Actualizar el título con más palabras si es necesario
        if cantidad_palabras > max_palabras:
            max_palabras = cantidad_palabras
            titulo_con_mas_palabras = titulo
    
    return titulo_con_mas_palabras
#----------------------------------------------------------------------------------------------------------------------------

# funciones del ejercicio 4:
def validar_usuario(usuario):
    # Verifica si el nombre de usuario tiene al menos 5 caracteres
    if len(usuario) < 5:
        return False

    tiene_numero = False
    tiene_mayuscula = False
    solo_letras_y_numeros = True

    # Recorre cada caracter del usuario
    for char in usuario:
        if char.isdigit():
            tiene_numero = True
        elif char.isupper():
            tiene_mayuscula = True
        elif not char.isalnum():  # Si no es alfanumérico
            solo_letras_y_numeros = False

    # Verifica que todas las condiciones se cumplan
    if tiene_numero and tiene_mayuscula and solo_letras_y_numeros:
        return True
    else:
        return False
#----------------------------------------------------------------------------------------------------------------------------

# funciones del ejercicio 5:
def clasificar_velocidad(tiempo_ms):
    if tiempo_ms < 200:
        return "Rápido"
    elif 200 <= tiempo_ms <= 500:
        return "Normal"
    else:
        return "Lento"
#----------------------------------------------------------------------------------------------------------------------------

# funciones del ejercicio 6:
def contar_menciones(descriptions):

    #creo una lista con las palabras a buscar en la lista de descripciones
    palabras = ["entretenimiento", "música", "charla"]
    
    #creo un diccionario para ir contando cuantas veces se mencionan las palabras
    contador = {"entretenimiento": 0, "música": 0, "charla": 0}
    
    # Recorre cada descripción
    for descripcion in descriptions:
        # Convierte a minúsculas para hacer una búsqueda mas facil
        descripcion_lower = descripcion.lower()
        
        # Cuenta las menciones de cada palabra en la descripción
        for palabra in palabras:
            contador[palabra] += descripcion_lower.count(palabra)
    
    return contador
#----------------------------------------------------------------------------------------------------------------------------

# funciones del ejercicio 7:
import random
import string
import datetime
def generar_codigo_descuento(usuario):
    # Verificar que el nombre de usuario no exceda los 15 caracteres
    if len(usuario) > 15:
        return "El nombre de usuario no puede exceder los 15 caracteres."

    # Obtener la fecha actual en formato YYYYMMDD
    fecha_hora_actual = datetime.datetime.now().strftime("%Y%m%d")

    # Generar una cadena aleatoria de caracteres (letras y números) para completar hasta 30 caracteres
    caracteres_restantes = 30 - len(usuario) - len(fecha_hora_actual) - 1  # Resta 1 para el guion
    aleatorios = ''.join(random.choices(string.ascii_uppercase + string.digits, k=caracteres_restantes))

    # Crear el código de descuento con el formato requerido
    codigo_descuento = f"{usuario.upper()}-{fecha_hora_actual}-{aleatorios}"
    return codigo_descuento
#----------------------------------------------------------------------------------------------------------------------------

# funciones del ejercicio 8:
def son_anagramas(palabra1, palabra2):
    # Convierte las palabras a minúsculas y ordenar las letras
    palabra1 = sorted(palabra1.lower())
    palabra2 = sorted(palabra2.lower())

    # Compara las palabras ordenadas
    if palabra1 == palabra2:
        return True
    else:
        return False
#----------------------------------------------------------------------------------------------------------------------------

# funciones del ejercicio 9:
def limpiar_datos(clients):
    clientes_limpios = []
    
    for cliente in clients:
        if cliente:  # si hay valores vacíos o nulos
            cliente = cliente.strip()  # Elimina espacios extras(al principio y al final)
            if cliente:  # Si no queda vacío después de los espacios
                cliente = cliente.title()  # Convertierte a formato de título (primera letra en mayúscula y el resto en minúscula).
                clientes_limpios.append(cliente)
    
    # Eliminar registros duplicados
    clientes_limpios = list(set(clientes_limpios))
    
    # Ordenar los clientes por nombre
    clientes_limpios.sort()
    
    return clientes_limpios
#----------------------------------------------------------------------------------------------------------------------------


# funciones del ejercicio 10:
# Función para calcular el puntaje de un jugador
def calcular_puntaje_jugador(estadisticas):
    puntaje = estadisticas['kills'] * 3 + estadisticas['asistencias'] * 1
    if estadisticas['muertes']:
        puntaje -= 1  # Restar 1 si el jugador tiene muertes
    return puntaje

# Función para calcular el puntaje de todos los jugadores en una ronda
def calcular_puntajes_ronda(datos_ronda, estadisticas_jugadores):
    puntajes_ronda = []
    for jugador, estadisticas in datos_ronda.items():
        puntaje = calcular_puntaje_jugador(estadisticas)
        puntajes_ronda.append((jugador, puntaje))
        
        # Actualizar las estadísticas del jugador en estadisticas_jugadores
        estadisticas_jugadores[jugador]['kills'] += estadisticas['kills']
        estadisticas_jugadores[jugador]['asistencias'] += estadisticas['asistencias']
        estadisticas_jugadores[jugador]['muertes'] += 1 if estadisticas['muertes'] else 0
        estadisticas_jugadores[jugador]['puntos'] += puntaje
    
    return puntajes_ronda

# Función para determinar el MVP de una ronda
def determinar_mvp(puntajes_ronda):
    max_puntaje = -float('inf')
    mvp = None
    for jugador, puntaje in puntajes_ronda:
        if puntaje > max_puntaje:
            max_puntaje = puntaje
            mvp = jugador
    return mvp

# Función para obtener los puntos de un jugador 
def obtener_puntos_jugador(jugador_puntajes):
    return jugador_puntajes[1]['puntos']

# Función para imprimir el ranking de los jugadores
def imprimir_ranking(estadisticas_jugadores):
    jugadores_ordenados = sorted(estadisticas_jugadores.items(), key=obtener_puntos_jugador, reverse=True)
    print(f"{'Jugador':<8} {'Kills':<6} {'Asistencias':<12} {'Muertes':<7} {'MVPs':<5} {'Puntos':<7}")
    print("-" * 50)
    for jugador, estadisticas in jugadores_ordenados:
        print(f"{jugador:<8} {estadisticas['kills']:<6} {estadisticas['asistencias']:<12} {estadisticas['muertes']:<7} {estadisticas['mvp']:<5} {estadisticas['puntos']:<7}")
    print("\n")


