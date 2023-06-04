# API REST Django

## Requisitos previos

- Python 3.x instalado
- Bibliotecas adicionales mencionadas en el archivo `requirements.txt`
- Configuración de una base de datos MySQL

## Arquitectura

El proyecto sigue una arquitectura típica de una API REST en Django. Los componentes principales son:

- `models.py`: Contiene los modelos de datos utilizados en la API.
- `serializers.py`: Se encarga de la serialización y deserialización de los objetos en formato JSON.
- `views.py`: Define las vistas y maneja las solicitudes HTTP.
- `urls.py`: Mapea las URLs a las vistas correspondientes.

## Configuración Motor de Base de Datos MySQL

Se realizó la creación de un SCHEMA con el nombre de la base de datos USERS

![image](https://github.com/JackGox99/Reto_Meli/assets/93834468/a274f4dd-417e-4ce4-9b0f-670fdc0aec3a)

Conexión que fue agragada en el archivo `settings.py`:

![image](https://github.com/JackGox99/Reto_Meli/assets/93834468/9487be6e-10bc-4f12-9e87-6cee8b5ed874)

Finalmente la tabla fue creada desde la hoja `models.py`, para que fuera actualizada directamente desde la API:

![image](https://github.com/JackGox99/Reto_Meli/assets/93834468/064eab27-f0d5-43a4-8339-b157536c7ff5)

## Modelos de datos

### BBDD USERS

Descripción del Modelo 1.

| Campo    | Tipo    | Descripción             |
| -------- | ------- | ----------------------- |
| `id` | `bigint` | Descripción del campo1. |
| `username` | `chard` | Descripción del campo2. |
| `useremail` | `chard` | Descripción del campo3. |
| `credit_card_number` | `int` | Descripción del campo3. |
| `created_timestamp` | `date` | Descripción del campo3. |

## Endpoints de la API

### `GET /api/v1/database/scan/`

Descripción del endpoint. Devuelve una lista de recursos.

![image](https://github.com/JackGox99/Reto_Meli/assets/93834468/bbcb260b-8af0-4cde-93fd-6c67c8969af8)

#### Parámetros de consulta

### `GET /api/v1/database/scan/{column_id}/`

Descripción del endpoint. Devuelve una lista de recursos.

| Parámetro | Tipo    | Descripción                  |
| --------- | ------- | ---------------------------- |
| `column_id`  | `int` | N/A. |


![image](https://github.com/JackGox99/Reto_Meli/assets/93834468/c7117033-881d-43c4-bc38-9eb797d30a88)



#### Respuesta

```json
{
  "data": [
    {
      "campo1": "valor1",
      "campo2": "valor2",
      "campo3": "valor3"
    },
    {
      "campo1": "valor4",
      "campo2": "valor5",
      "campo3": "valor6"
    }
  ]
}

 
```
