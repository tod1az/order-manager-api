# Usa una imagen base con Python
FROM python:3.12-slim

# Crea y entra al directorio de la app
WORKDIR /app

# Copia los archivos
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Expone el puerto que usa Flask
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]
