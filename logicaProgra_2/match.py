
serie = "N-02"

match serie:
    case "N-01":
        print("Serie 1")
    case "N-02":
        print("Serie 2")
    case "N-03":
        print("Serie 3")
    case _:
        print("Serie no encontrada")

cliente = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Lima'}

pelicula = {'titulo': 'El padrino', 'año': 1972, 'director': 'Francis Ford Coppola'}

elementos = [cliente, pelicula, 'libro']

for elemento in elementos:
    match elemento:
        case {'nombre': nombre, 'edad': edad, 'ciudad': ciudad}:
            print("es un cliente")
            print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")