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
    
# CREACION DE TRANSACCIÓN [webpay_plus_create]

Permite inicializar una transacción en Webpay. Como respuesta a la invocación se genera un token que representa en forma única una transacción.

Para crear una transacción basta llamar al método Transaction.create()

1.- Parametros buy_order - String

    Orden de compra de la tienda. Este número debe ser único para cada transacción. 
    Largo máximo: 26. La orden de compra puede tener: 
    Números, letras, mayúsculas y minúsculas, y los signos |_=&%.,~:/?[+!@()>-

2.- Parametros session_id - String

    Identificador de sesión, uso interno de comercio, este valor es devuelto al final de la transacción. 
    Largo máximo: 61

3.- Parametros amount - Int

    Monto de la transacción
    Largo máximo: 17
    
4.- Parametros return_url - String

    URL del comercio, a la cual Webpay redireccionará posterior al proceso de autorización. 
    Largo máximo: 256
  
# CONFIRMACION DE UNA TRANSACCIÓN [commitpay]
Permite confirmar y obtener el resultado de la transacción una vez que Webpay ha resuelto su autorización financiera.

Cuando el comercio retoma el control mediante return_url debes confirmar y obtener el resultado de una transacción usando el método Transaction.commit().
  
Parámetros Transaction.commit

1.- Parametros token - String

    Token de la transacción. Largo: 64. (Se envía en la URL, no en el body)
 
 
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
    
   

