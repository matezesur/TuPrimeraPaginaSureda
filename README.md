# TuPrimeraPaginaSureda

Proyecto web desarrollado en Django para la tercera entrega de Python en Coderhouse.

## Nombre del proyecto

SuredaFinanzas - Tu primera página

## Descripción

La web simula una página simple de educación financiera. Permite cargar artículos financieros, servicios ofrecidos y consultas de clientes. También tiene un buscador de artículos guardados en la base de datos.

El proyecto usa el patrón MVT de Django y herencia de plantillas HTML.

## Modelos creados

En la app `finanzas` hay 3 modelos:

1. `ArticuloFinanciero`
2. `ServicioFinanciero`
3. `ConsultaCliente`

## Formularios

El proyecto incluye un formulario para cargar datos en cada modelo:

- Formulario para crear artículos financieros.
- Formulario para crear servicios financieros.
- Formulario para crear consultas de clientes.

También incluye un formulario de búsqueda de artículos por título.

## Herencia de HTML

El archivo principal es:

`templates/finanzas/base.html`

Las demás plantillas heredan de ese archivo usando `{% extends 'finanzas/base.html' %}`.

## Cómo probar el proyecto

Primero clonar el repositorio:

```bash
git clone https://github.com/matezesur/TuPrimeraPaginaSureda.git
```

Entrar a la carpeta del proyecto:

```bash
cd TuPrimeraPaginaSureda
```

Crear el entorno virtual:

```bash
python -m venv venv
```

Activar el entorno virtual en Windows:

```bash
venv\Scripts\activate
```

Instalar Django:

```bash
pip install -r requirements.txt
```

Aplicar migraciones:

```bash
python manage.py migrate
```

Levantar el servidor:

```bash
python manage.py runserver
```

Entrar desde el navegador a:

```text
http://127.0.0.1:8000/
```

## Orden sugerido para revisar las funcionalidades

1. Ir al inicio: `http://127.0.0.1:8000/`
2. Cargar un artículo desde: `/articulos/crear/`
3. Ver los artículos cargados desde: `/articulos/`
4. Cargar un servicio desde: `/servicios/crear/`
5. Ver los servicios desde: `/servicios/`
6. Cargar una consulta desde: `/consultas/crear/`
7. Ver las consultas desde: `/consultas/`
8. Buscar un artículo desde: `/buscar/`

## Autor

Matías Sureda
