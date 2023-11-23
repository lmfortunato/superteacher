
# Proyecto SuperTeacher

Una aplicación para ofrecer clases particulares


## Installation

Para ejecutar el proyecto

```bash
  pip install requirements.txt
  python manage.py runserver
```

### Superuser:
Usuario: user
Contraseña: user1234

### Users:
Usuario: lucilaf
Contraseña: user1234

Usuario: eugenior
Contraseña: user1234

Usuario: perezj
Contraseña: user1234

## Unit tests
super_teacher tests.py

## Como navegar

1. Al iniciar el proyecto, en la ruta inicial "/" se visualiza el home del proyecto. Desde allí se puede ver el listado de servicios disponibles y buscar un servicio. Al hacer click en algún servicio muestra los detalles completos del servicio. Un usuario no logueado va a poder ver el detalle del servicio pero no los datos de contacto del profesor. También puede acceder a la página "About me".
2. Al hacer clic en "Sign up" el usuario puede registrarse completando todos los campos requeridos o puede optar por loguearse con la opción "Already have an account? si ya tiene una cuenta"
3. Al finalizar el registro, el usuario debe loguearse para poder acceder a la plataforma.
4. Una vez iniciada la sesión, se visualiza en el título principal el nombre del usuario logueado, se puede acceder al perfil desde el menú o desloguearse.
5. Si el usuario ingresa al perfil, puede acceder a sus datos de perfil y editarlos, puede ver su avatar, en caso de que no haya cargado aún uno se va a poner un avatar por default, y le va a permitir cambiarlo las veces que quiera. También va a ver una sección de servicios creados, va a poder editarlos o eliminarlos y crear un nuevo servicio. Si aún no tiene servicios puede crear uno desde cero.
6. Para crear un servicio, debe ingresar la asignatura que va a brindar, junto con una breve descripción y el precio por hora de clase. Al crear el servicio la aplicación redirige al usuario al dashboard, donde puede ver todas las clases disponibles, incluyendo la última creada.
