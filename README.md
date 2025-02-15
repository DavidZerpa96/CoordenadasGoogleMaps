# Geocoding y Reverse Geocoding para Alquileres en las Islas Canarias con Google Maps

## Contexto del Proyecto

Este proyecto nace de la necesidad de desarrollar un buscador eficiente para encontrar los mejores hoteles, Airbnb y otros alojamientos en las Islas Canarias en minutos, utilizando **Power BI** como herramienta principal de visualización.

Uno de los principales retos al trabajar con datos de alquileres es la falta de coordenadas precisas. En los mapas de Power BI, las ubicaciones sin coordenadas pueden ser ambiguas y menos precisas, afectando la calidad del análisis y la interpretación de los datos.

### **Problema**
- Los datos provienen de **una consulta en SQL Server**, extrayendo las columnas:
  - **Ubicación** (descripción del alquiler)
  - **Isla**
  - **Número de veces** que aparece en la base de datos.
- No se contaban con coordenadas (latitud y longitud) ni con el municipio asociado.
- La precisión geográfica en Power BI se ve afectada si no se agregan coordenadas exactas.

### **Solución Aplicada**

Para solucionar este problema, se implementó un script en **Python** que realiza los siguientes procesos:
1. **Geocoding:** Uso de la API de Google Maps para obtener latitud y longitud basadas en la ubicación y la isla.
2. **Reverse Geocoding:** Con las coordenadas obtenidas, se extrae el municipio correspondiente a cada ubicación.
3. **Generación de un archivo Excel** con los datos enriquecidos, listos para ser utilizados en **Power BI**.

El resultado final es un dataset completo con:
- **Isla**
- **Ubicación**
- **Número de veces**
- **Latitud**
- **Longitud**
- **Municipio**

Este proceso mejora significativamente la calidad de los mapas y visuales en Power BI, permitiendo un análisis más preciso y eficiente.

---

## Instalación y Configuración

### **1. Requisitos**
- Python 3.x
- Una API Key de Google Maps (instrucciones abajo)
- Dependencias necesarias:
  ```bash
  pip install googlemaps pandas openpyxl
  ```

### **2. Configurar la API Key de Google Maps**
1. Ve a la [consola de Google Cloud](https://console.cloud.google.com/).
2. Habilita la **API de Geocoding** y la **API de Reverse Geocoding**.
3. En **Credenciales**, crea una nueva **API Key**.
4. **Restríngela** para evitar un uso indebido (puedes limitarla por IP o dominios permitidos).
5. Configura la API Key como una variable de entorno:


#### **Linux/Mac**
```bash
export GOOGLE_MAPS_API_KEY="TU_API_KEY"
```

#### **Windows (CMD)**
```cmd
set GOOGLE_MAPS_API_KEY="TU_API_KEY"
```

#### **Windows (PowerShell)**
```powershell
$env:GOOGLE_MAPS_API_KEY="TU_API_KEY"
```

Esto permite que el script pueda leer la API Key sin exponerla en el código.

---

## Uso del Script

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/DavidZerpa96/CoordenadasGoogleMaps.git
   cd CoordenadasGoogleMaps
   ```

2. **Ejecuta el script:**
   ```bash
   python geocoding_script.py
   ```

3. **Revisa el archivo resultante:**
   El script generará un archivo Excel `resultado_google.xlsx` con las coordenadas y municipios agregados.

---

## Estructura del Repositorio

```
CoordenadasGoogleMaps/
│── geocoding_script.py        # Código en Python sin exponer la API Key
│── README.md                  # Documentación completa
│── resultado_google.xlsx       # Archivo Excel con los datos procesados
│── datosenbruto.csv           #Información de base usada en el script. 
```

---

## Contribuciones

Las contribuciones son bienvenidas. Si quieres mejorar el script o adaptarlo a otras necesidades, siéntete libre de hacer un **fork** o enviar un **pull request**.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.




