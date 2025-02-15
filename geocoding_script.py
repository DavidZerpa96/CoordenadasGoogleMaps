import os
import pandas as pd
import googlemaps
from time import sleep

# Leer la API Key desde una variable de entorno (configúrala antes de ejecutar el script)
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

if not API_KEY:
    raise ValueError("No se encontró la API Key. Configúrala como variable de entorno 'GOOGLE_MAPS_API_KEY'.")

# Inicializar cliente de Google Maps
gmaps = googlemaps.Client(key=API_KEY)

# Leer el CSV de entrada
df = pd.read_csv("datos.csv")

# Listas para almacenar resultados
latitudes, longitudes, municipios = [], [], []

def obtener_coordenadas(ubicacion, isla):
    query = f"{ubicacion}, {isla}, Islas Canarias, España"
    try:
        geocode_result = gmaps.geocode(query)
        if geocode_result:
            loc = geocode_result[0]["geometry"]["location"]
            return loc["lat"], loc["lng"]
    except Exception as e:
        print(f"Error en geocoding para '{query}': {e}")
    return None, None

def obtener_municipio(lat, lon):
    if lat is None or lon is None:
        return ""
    try:
        reverse_result = gmaps.reverse_geocode((lat, lon))
        if reverse_result:
            for comp in reverse_result[0]["address_components"]:
                if "locality" in comp["types"]:
                    return comp["long_name"]
                if "administrative_area_level_2" in comp["types"]:
                    return comp["long_name"]
    except Exception as e:
        print(f"Error en reverse geocoding ({lat}, {lon}): {e}")
    return ""

# Procesar cada fila
for idx, row in df.iterrows():
    ubicacion, isla = row["ubicacion"], row["isla"]
    lat, lon = obtener_coordenadas(ubicacion, isla)
    municipio = obtener_municipio(lat, lon)
    
    latitudes.append(lat)
    longitudes.append(lon)
    municipios.append(municipio)
    
    print(f"[{idx+1}/{len(df)}] '{ubicacion}' en {isla} -> Lat: {lat}, Lon: {lon}, Municipio: {municipio}")
    sleep(0.1)

# Guardar resultados
df["latitud"], df["longitud"], df["municipio"] = latitudes, longitudes, municipios
df.to_excel("resultado_google.xlsx", index=False)

print("Proceso completado. Archivo 'resultado_google.xlsx' generado.")
