
# Proyecto SuperTeacher

Una aplicación para ofrecer clases particulares


## Installation

Para ejecutar el proyecto

```bash
  python manage.py runserver
```
### Superuser:
Usuario: user
Contraseña: user1234
## Como navegar

1. Al iniciar el proyecto, en la ruta inicial "/" se visualiza una presentación de la aplicación, desde donde se puede acceder a la plataforma.
2. Al hacer clic en "Access here" te lleva a un formulario de registro, donde el usuario debe cargar usuario y contraseña. Si ya tiene un usuario, puede optar por loguearse con la opción "Already have an account?"
3. Al finalizar el registro, el usuario debe loguearse para poder acceder a la plataforma.
4. Una vez dentro del dashboard, se visualiza un buscador, donde puede filtrar por la asignatura o clase que está buscando, y otra sección donde se visualizan las clases disponibles creadas por un profesor.
5. Desde el menú de navegación se puede acceder al perfil del usuario, donde una vez dentro, le pedirá registrarse como profesor. Al finalizar el registro se muestra otra pantalla con los datos ingresados y la posibilidad de brindar un servicio.
6. Si el profesor quiere brindar un servicio, debe hacer clic en la opción "Promote your classes", que solo se mostrará si creó un perfil de profesor.
7. Para crear un servicio, debe ingresar la asignatura que va a brindar, junto de una breve descripción y el precio por hora de clase. Al crear el servicio la aplicación redirige al usuario al dashboard, donde puede ver todas las clases disponibles, incluyendo la última creada.
