# Webpay_Django2.2
 Repositorio con el fin de tener un entorno el cual se pueda pagar con webpay con templates simples.

# TARJETAS DE PRUEBA PARA WEBPAY
Estas son las tarjetas para poder probar en la aplicacion del webpay en modo de prueba

    Tarjeta Numero 1

    Tipo de tarjeta:VISA
    Detalle: 4051 8856 0044 6623
    CVV: 123
    Fecha de Expiracion: Cualquier fecha
    Resultado: Genera transacciones aprobadas.

    Tarjeta Numero 2

    Tipo de tarjeta:AMEX
    Detalle: 3700 0000 0002 032
    CVV: 1234
    Fecha de Expiracion: Cualquier fecha
    Resultado: Genera transacciones aprobadas.

    Tarjeta Numero 3

    Tipo de tarjeta:AMEX
    Detalle: 5186 0595 5959 0568
    CVV: 123
    Fecha de Expiracion: Cualquier fecha
    Resultado: Genera transacciones rechazadas.

    [!]IMPORTANTE:Cuando aparece un formulario de autenticación con RUT y clave,
    se debe usar el RUT *11.111.111-1* y la clave *123*.

# CREAR ENTORNO VIRTUAL [VENV]

1.- Dirigirse a la Carpeta "Project_webpay" por la consola [CMD o VScode]
    
    -> C:\Users\XXXXX\Desktop\Project_webpay
    
2.- Escribir en la consola
    
    Entiendase por el segundo 'venv' es el nombre del entorno virtual el cual se esta creando.
    - python -m venv venv
    
3.- Activar entorno virtual
    
    1- Entrar a la carpeta "Scripts" del entorno virtual "venv".
    - cd venv\Scripts
    2- Escribir lo siguiente en la consola para activarlo.
    - activate

    Listo, ahora en un incio deberia mostrar (venv) como el nombre del entorno virtual
    
    *Para desactivar el entorno virtual*
    1- Entrar a la carpeta "Scripts" del entorno virtual "venv".
    - cd venv\Scripts
    2- Escribir lo siguiente en la consola para desactivarlo.
    - deactivate
    
    [!]IMPORTANTE: Si les tira algun error por consola, hacerlo desde CMD y no de PS. 
    (Para entrar a la CMD deben escribir cmd en consola y listo)
 
# INSTALACION DE LOS REQUIREMENTS [REQUIREMENTS.TXT]

1.- Instalacion de los requirements en el entorno virtual
    
    Volver al directorio principal.
    - cd ..\.. ó cd C:\Users\XXXXX\Desktop\Project_webpay
    Escribir en consola.
    - pip install -r requirements.txt
    Listo! 
    
 # HABILITACION DEL ENTORNO DJANGO

1.- Habilitacion del Entorno Django
    
    Descripcion de comandos globales:
    -> python manage.py runserver [Encender el servidor]
    
   

