FROM python:3.11-slim

# Crear carpeta de trabajo
WORKDIR /app

# Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la app y el HTML
COPY . .

# Exponer el puerto 80
EXPOSE 80

# Comando para correr la app
CMD ["python", "app.py"]