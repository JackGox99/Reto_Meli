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
| `id` | `bigint` | N/A |
| `username` | `chard` | USERNAME |
| `useremail` | `chard` | EMAIL_ADDRESS |
| `credit_card_number` | `int` | CREDIT_CARD_NUMBER |
| `created_timestamp` | `date` | N/A |

## Scan y Categorización de la BBDD

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
    {
      "column_id": "3",
      "field_type": "useremail"
    }
}

 
```

## CRUD DDBB USERS

Se realizó adicionalmente un modulo en la API que permite realizar acciones directas sobre la Base de datos ya sea Crear, Leer, Actualizar y Borrar.

## Escaneo BBDD USERS

#### Parámetros de consulta

### `GET /api/v1/users/`

Para realizar la consulta unicamente es necesario realizar la petición GET directo sobre la base datos y esta responde con toda la información que se encuentre en ella.

![image](https://github.com/JackGox99/Reto_Meli/assets/93834468/408ca396-c37d-4e14-a571-ab1a55cf15fc)

#### Respuesta

```json
[
  {
    "id": 1,
    "username": "jackjax",
    "useremail": "Juliango@email.com",
    "credit_card_number": 2345654,
    "created_timestamp": "2023-06-21"
  },
  {
    "id": 3,
    "username": "JackGox",
    "useremail": "Juliango@email.com",
    "credit_card_number": 123123123,
    "created_timestamp": "2023-06-07"
  },
  {
    "id": 4,
    "username": "JackGox9",
    "useremail": "Juliango@email.com",
    "credit_card_number": 123123,
    "created_timestamp": "2023-06-02"
  }
]
```
 
 ## Crear USERS

#### Parámetros de consulta

### `POST /api/v1/users/params = {
    "username": ...,
    "useremail": ...,
    "credit_card_number": ...,
    "created_timestamp": ...,
}`

| Campo    | Tipo    | Descripción             |
| -------- | ------- | ----------------------- |
| `username` | `chard` | USERNAME |
| `useremail` | `chard` | EMAIL_ADDRESS |
| `credit_card_number` | `int` | CREDIT_CARD_NUMBER |
| `created_timestamp` | `date` | N/A |

Para realizar la consulta unicamente es necesario realizar la petición POST directo sobre la base datos con los parametros relacionados anteriormente, tendiendo en cuenta que todos son requeridos para que se realice de manera satisfactoria esta acción.

![image](https://github.com/JackGox99/Reto_Meli/assets/93834468/457bdc40-438e-494a-b104-3daa8cb7d78e)

#### Respuesta

```json
{
  "id": 6,
  "username": "test-username",
  "useremail": "Useremail@test.com",
  "credit_card_number": 1231241,
  "created_timestamp": "2023-05-29"
}
```
 
 ## Consulta Por ID - USERS

#### Parámetros de consulta

### `GET /api/v1/users/{id}/`

| Campo    | Tipo    | Descripción             |
| -------- | ------- | ----------------------- |
| `id` | `bigint` | N/A |


Para realizar la consulta unicamente es necesario realizar la petición GET directo sobre la base datos con el ID como parametro, tendiendo en cuenta que este campo es requerido para que se realice de manera satisfactoria esta acción.

![image](https://github.com/JackGox99/Reto_Meli/assets/93834468/e66c5382-f7f4-4707-bd12-f8622ccec845)

#### Respuesta

```json
{
    "id": 4,
    "username": "JackGox9",
    "useremail": "Juliango@email.com",
    "credit_card_number": 123123,
    "created_timestamp": "2023-06-02"
}
```
 
 
## Actualización Completa por ID - USERS

#### Parámetros de consulta

### `PUT /api/v1/users/{id}/params = {
    "username": ...,
    "useremail": ...,
    "credit_card_number": ...,
    "created_timestamp": ...,
}`

| Campo    | Tipo    | Descripción             |
| -------- | ------- | ----------------------- |
| `id` | `bigint` | N/A |

#### Parametros Adicionales

| Campo    | Tipo    | Descripción             |
| -------- | ------- | ----------------------- |
| `username` | `chard` | USERNAME |
| `useremail` | `chard` | EMAIL_ADDRESS |
| `credit_card_number` | `int` | CREDIT_CARD_NUMBER |
| `created_timestamp` | `date` | N/A |

Para realizar la consulta unicamente es necesario realizar la petición PUT directo sobre la base datos con el ID como parametro inicial paa confirmar que este exista en la base y adicional enviando los parametros a actualizar, tendiendo en cuenta que este campo es requerido para que se realice de manera satisfactoria esta acción.

#### Antes de la actualización

![image](https://github.com/JackGox99/Reto_Meli/assets/93834468/59e3e6b3-e7b6-4e3a-b885-4d570009b534)

#### Actualización

![image](https://github.com/JackGox99/Reto_Meli/assets/93834468/4faac095-9234-4a39-a667-9f1d19dceef0)

#### Despues de la actualización

![image](https://github.com/JackGox99/Reto_Meli/assets/93834468/782b1d64-b2de-4a4d-851b-781976d436d7)

 
## Actualización Parcial por ID - USERS

#### Parámetros de consulta

### `PATCH /api/v1/users/{id}/params = {
    "username": ...,
    "useremail": ...,
    "credit_card_number": ...,
    "created_timestamp": ...,
}`

| Campo    | Tipo    | Descripción             |
| -------- | ------- | ----------------------- |
| `id` | `bigint` | N/A |

#### Parametros Adicionales

| Campo    | Tipo    | Descripción             |
| -------- | ------- | ----------------------- |
| `username` | `chard` | USERNAME |
| `useremail` | `chard` | EMAIL_ADDRESS |
| `credit_card_number` | `int` | CREDIT_CARD_NUMBER |
| `created_timestamp` | `date` | N/A |

Para realizar la consulta unicamente es necesario realizar la petición PATCH directo sobre la base datos con el ID como parametro inicial paa confirmar que este exista en la base y adicional enviando los parametros a actualizar, tendiendo en cuenta que en este caso cualquier parametro es opcional ya que solo se desea actualziar un parametro y el resto dejarlos iguales

#### Antes de la actualización

![image](https://github.com/JackGox99/Reto_Meli/assets/93834468/d519de96-41b5-4b8a-9fd9-9e46693e03f0)

#### Actualización

![image](https://github.com/JackGox99/Reto_Meli/assets/93834468/acb70a0c-5f6a-40ab-a50a-c5569d4bc7b8)

#### Despues de la actualización

![image](https://github.com/JackGox99/Reto_Meli/assets/93834468/8566d7fd-014a-4485-99af-641188f1d243)

## Eliminación por ID - USERS

#### Parámetros de consulta

### `DELETE /api/v1/users/{id}/`

| Campo    | Tipo    | Descripción             |
| -------- | ------- | ----------------------- |
| `id` | `bigint` | N/A |


Para realizar la consulta unicamente es necesario realizar la petición DELETE directo sobre la base datos con el ID como parametro inicial para confirmar que este exista en la base y realizar la eliminación correspondiente 

#### Respuesta

![image](https://github.com/JackGox99/Reto_Meli/assets/93834468/8f52382f-7907-4876-80ad-1cee579ba31a)

![image](https://github.com/JackGox99/Reto_Meli/assets/93834468/8b905daa-4958-4edc-8f4c-ef97cf4fe8fe)
