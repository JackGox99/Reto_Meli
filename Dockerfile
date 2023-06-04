# Utiliza una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requerimientos al contenedor
COPY requeriments.txt .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requeriments.txt

# Copia los archivos de la aplicación al contenedor
COPY . .

# Expone el puerto donde se ejecutará la aplicación
EXPOSE 8000

# Ejecuta el comando para iniciar la aplicación
CMD ["python", "manage.py", "runserver"]