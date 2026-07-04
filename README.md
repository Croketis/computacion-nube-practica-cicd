# Practica CI/CD con GitHub Actions y Azure

Computacion en la Nube - II-26 SC-01
Universidad Tecnica Nacional

## Descripcion

App web sencilla hecha en Python con Flask. Tiene un endpoint /api/status
para probar que el despliegue automatico en Azure funciona.

## Como correr en local

1. Crear entorno virtual:
```
python -m venv venv
venv\Scripts\activate
```

2. Instalar librerias:
```
pip install -r requirements.txt
```

3. Correr la app:
```
python app.py
```

Abrir en el navegador: http://localhost:8000/api/status

## Despliegue

Cada vez que se hace push a la rama main, GitHub Actions ejecuta el workflow
que sube la app a Azure App Service.
