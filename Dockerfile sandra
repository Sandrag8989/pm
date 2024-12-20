# Usar una imagen base oficial de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /examen

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt /examen/

# Instalar las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de la aplicación al contenedor
COPY . /examen/

# Exponer el puerto 5000 (el puerto en el que Flask corre por defecto)
EXPOSE 5000

# Definir el comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
