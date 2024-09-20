# OFAC Sanctions Search Automation

## Descripción

Este proyecto es una solución automatizada que busca entidades en la base de datos de sanciones OFAC (Office of Foreign Assets Control) utilizando Selenium para automatizar la navegación web. Se conecta a una base de datos PostgreSQL, recupera una lista de registros, realiza la búsqueda en el sitio de OFAC y guarda los resultados en la base de datos. Adicionalmente, toma capturas de pantalla de los resultados de la búsqueda si se encuentran coincidencias.

## Dependencias

- Selenium: 4.25.0
- psycopg2: 2.9.9

## Crear ambiente virtual

Para crear un ambiente virtual, ejecuta el siguiente comando:

```bash
  python -m venv venv
```

Asegúrate de estar en el directorio correcto. Abre tu terminal y ejecuta el siguiente comando: `ls`. Si todo está bien, deberías ver una carpeta llamada venv entre los resultados.

## Activar ambiente virtual

Para activar el ambiente virtual, ejecuta el siguiente comando:

Windows


```bash
   source venv/Scripts/activate
```

MacOS / Linux

```bash
   source venv/bin/activate
```

## Instalación de dependencias

Para instalar las dependencias necesarias, ejecuta el siguiente comando:

```bash
  pip install selenium psycopg2
```

## Configuración de la base de datos


```python
  connection_params = {
   "host": "",
   "database": "",
   "user": "",
   "password": "",
   "port": 5432     
}
```
## Uso 

- Asegúrate de que la base de datos PostgreSQL esté en funcionamiento

- Ejecuta el comando `python src/bot.py` para iniciar el proceso.

