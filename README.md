# Expressvpn GUI escritorio GNOME

![expressvpn-gui](https://github.com/sapoclay/expressvpn-gui/assets/6242827/e70b3476-b2a5-49be-9efc-666467836df6)

Una GUI para ExpressVPN ejecutable con python3.11 y en escritorio GNOME. Evidentemente debes de tener una cuenta con [EXPRESSVPN](https://www.expressvpn.com/es/refer-a-friend/30-days-free?locale=es&referrer_id=40141467&utm_campaign=referrals&utm_medium=copy_link&utm_source=referral_dashboard) comprada. Esto solo se ha creado por comodidad para mi ...

![desconexion-expressvpn](https://github.com/sapoclay/expressvpn-gui/assets/6242827/7747e455-0ade-4177-beae-cb9ffef34bbd)

## Crea un Script de Inicio:

Primero, necesitas asegurarte de que tu script tenga permisos de ejecución. Abre una terminal y navega al directorio donde se encuentra tu script. Luego, ejecuta el siguiente comando para darle permisos de ejecución:

bash

chmod +x tu_script.py

Crea un Archivo de Escritorio:

Abre un editor de texto y crea un nuevo archivo. Puedes usar el siguiente comando en la terminal para abrir el editor de texto Gedit:

bash

gedit ~/.local/share/applications/mi_script.desktop

Esto abrirá Gedit y te permitirá crear un nuevo archivo de escritorio. Si prefieres otro editor, puedes usarlo en su lugar.

Agrega el Contenido al Archivo:

En el archivo que acabas de abrir, agrega el siguiente contenido, pero asegúrate de actualizar la ruta del script:

plaintext

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

Guarda y Cierra:

Guarda el archivo y ciérralo.

Haz que el Archivo sea Ejecutable:

Debes asegurarte de que el archivo .desktop sea ejecutable. Para hacerlo, ejecuta el siguiente comando:

bash

chmod +x ~/.local/share/applications/mi_script.desktop

Encuentra el Acceso Directo en tu Menú:

Ahora deberías poder buscar y encontrar tu script en el menú de aplicaciones.

¡Eso es todo! De ahora en adelante, puedes ejecutar tu script haciendo clic en el acceso directo.
