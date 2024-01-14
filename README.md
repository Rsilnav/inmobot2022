# InmoApp

InmoApp es una aplicación desarrollada durante el Máster de Ingeniería Informática de la Universidad de Valladolid en el curso académico 2022/2023.
Esta aplicación permite la interacción con los servicios de Google Assistant para ofrecer diversas funcionalidades relacionadas con la gestión de una inmobiliaria.

## Contenido

En la carpeta _data_ se encuentran los datos de muestra que se pueden utilizar para probar la aplicación. Estos se generan
gracias a __Faker__ y al script _database_populate.py_.

El script app.py es el servicio web que se encarga de recibir las peticiones de Google Assistant y procesarlas. Para ello
utiliza las funciones definidas en _misc_functions.py_, _search_functions.py_ y _view_functions.py_.