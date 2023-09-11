# Expressvpn GUI escritorio GNOME

![expressvpn-gui](https://github.com/sapoclay/expressvpn-gui/assets/6242827/e70b3476-b2a5-49be-9efc-666467836df6)

Una GUI para ExpressVPN ejecutable con python3.11 y en escritorio GNOME. Evidentemente debes de tener una cuenta con [EXPRESSVPN](https://www.expressvpn.com/es/refer-a-friend/30-days-free?locale=es&referrer_id=40141467&utm_campaign=referrals&utm_medium=copy_link&utm_source=referral_dashboard) comprada. Esto solo se ha creado por comodidad para mi ...

![desconexion-expressvpn](https://github.com/sapoclay/expressvpn-gui/assets/6242827/7747e455-0ade-4177-beae-cb9ffef34bbd)

## Crea el script:

Primero, necesitas asegurarte de que tu script (el que te puedes descargar desde este repositorio) tenga permisos de ejecución. Abre una terminal y navega al directorio donde se encuentra tu script. Luego, ejecuta el siguiente comando para darle permisos de ejecución:

sudo chmod +x tu_script.py

## Crea un enlace directo

Abre un editor de texto y crea un nuevo archivo. Puedes usar el siguiente comando en la terminal para abrir el editor de texto Gedit:

gedit ~/.local/share/applications/tu_script.desktop

Esto abrirá Gedit y te permitirá crear un nuevo archivo de escritorio. Si prefieres otro editor, puedes usarlo en su lugar.

Llegados a este punto, adjunta el siguiente contenido al archivo (asegúrate de actualizar la ruta del script):

[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec=/ruta/del/script/tu_script.py
Name=Mi Script VPN
Comment=Inicia mi script VPN
Icon=/ruta/a/un/icono.png

    Exec: Debes reemplazar /ruta/del/script/tu_script.py con la ruta completa de tu script.
    Name: Es el nombre que aparecerá en el acceso directo.
    Comment: Es una descripción opcional.

Si tienes un icono personalizado, también puedes especificar la ruta en la línea Icon.

## Haz que el archivo sea ejecutable

Debes asegurarte de que el archivo .desktop sea ejecutable. Para hacerlo, ejecuta el siguiente comando:

sudo chmod +x ~/.local/share/applications/tu_script.desktop

## Encuentra el Acceso Directo en tu Menú

Ahora deberías poder buscar y encontrar tu script en el menú de aplicaciones.

¡Eso es todo! De ahora en adelante, puedes ejecutar tu script para utilizar tu EXPRESS VPN haciendo clic en el acceso directo.
