# lat = 34.5
# lon = 45.6
# posicion = [lat, lon]

historial = [
    [34.5, 45.6, "2022/02/02 17:20:24"],
    [34.5, 46.3, "2022/02/02 17:20:34"],
    [35.5, 47.3, "2022/02/02 17:20:44"],
    [34.5, 46.3, "2022/02/02 17:20:54"],
    [34.5, 48.3, "2022/02/02 17:21:04"],
    [33.5, 49.3, "2022/02/02 17:21:14"],
]

indiceLongitud = 0
indiceLatitud = 1
indiceFecha = 2

# print(historial[0])
# print(historial[0][1])
# print(historial[0][indiceFecha])

for coordenada in historial:
    print(coordenada[indiceLongitud])
