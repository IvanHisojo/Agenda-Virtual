# Usa una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requerimientos y el proyecto a la imagen
COPY requirements.txt /app/
COPY . /app/

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que corre la app Django
EXPOSE 8000

# Ejecutar el servidor de desarrollo de Django en el puerto 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Instalar pip más reciente
RUN python -m pip install --upgrade pip


