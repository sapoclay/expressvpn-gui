# Expressvpn GUI escritorio GNOME

![conexion-expressvpn](https://github.com/sapoclay/expressvpn-gui/assets/6242827/4877cec7-412c-4a81-a2d2-de8ad3af9c31)

Una GUI para ExpressVPN ejecutable con Python 3.11 y en escritorio GNOME. Evidentemente debes de tener una cuenta con [EXPRESSVPN](https://www.expressvpn.com/es/refer-a-friend/30-days-free?locale=es&referrer_id=40141467&utm_campaign=referrals&utm_medium=copy_link&utm_source=referral_dashboard) comprada. Esto solo se ha creado por comodidad para mi ...

![desconexion-expressvpn](https://github.com/sapoclay/expressvpn-gui/assets/6242827/8f3dab8e-ed20-40ab-9401-61f1500df16c)

# Dependencias

Para ejecutar este script, necesitarás tener instalado Python 3.11 y las bibliotecas tkinter y ttk en tu sistema. Estas bibliotecas están incluidas en la instalación estándar de Python, así que normalmente no debería ser necesario instalar nada adicional.

Nota: Después de probar esta GUI en Mint, he tenido que instalar tkinter con el siguiente comando:

```
sudo apt install python3-tk
```

Sin embargo, este script también depende de la herramienta expressvpn. Por eso, es necesario asegurarse de tener esta herramienta instalada y configurada correctamente en tu sistema. Si no la tienes, deberás [instalarla](https://www.expressrefer.com/refer-a-friend/30-days-free?locale=es&referrer_id=40141467&utm_campaign=referrals&utm_medium=copy_link&utm_source=referral_dashboard)  antes de ejecutar el script.

## Crea el script:

Primero, necesitas asegurarte de que tu script (el que te puedes descargar desde este repositorio) tenga permisos de ejecución. Abre una terminal y navega al directorio donde se encuentra tu script. Luego, ejecuta el siguiente comando para darle permisos de ejecución:
```
sudo chmod +x expressvpn.py
```
## Crea un enlace directo

Abre un editor de texto y crea un nuevo archivo. Puedes usar el siguiente comando en la terminal para abrir el editor de texto Gedit:
```
gedit ~/.local/share/applications/tu_script.desktop
```
Esto abrirá Gedit y te permitirá crear un nuevo archivo de escritorio. Si prefieres otro editor, puedes usarlo en su lugar.

Llegados a este punto, adjunta el siguiente contenido al archivo (asegúrate de actualizar la ruta del script):
```
[Desktop Entry]
Type=Application
Name=Express-VPN
Icon=/ruta/hasta/la/carpeta/de/la/imagen/ExpressVPN-logo.png
Exec=python3 /ruta/hasta/el/script/expressvpn.py
Version=1.0
Comment=Inicia la conexión VPN
Terminal=false
Path=/ruta/a/la/carpeta/donde/guardamos/el/script/expressvpn
```
    Exec: Debes reemplazar /ruta/hasta/el/script/expressvpn.py con la ruta completa de tu script.
    Name: Es el nombre que aparecerá en el acceso directo.
    Comment: Es una descripción opcional.
    Path: Indica solo la ruta. No es necesario añadir al final el nombre del archivo.

Si tienes un icono personalizado, también puedes especificar la ruta en la línea Icon.

## Haz que el archivo sea ejecutable

Debes asegurarte de que el archivo .desktop sea ejecutable. Para hacerlo, ejecuta el siguiente comando:
```
sudo chmod +x ~/.local/share/applications/tu_script.desktop
```
## Encuentra el Acceso Directo en tu Menú

Ahora deberías poder buscar y encontrar tu script en el menú de aplicaciones.

![lanzador-expressvpn](https://github.com/sapoclay/expressvpn-gui/assets/6242827/ca44463d-69e3-4b50-b838-beddbcaa7b6b)

¡Eso es todo! De ahora en adelante, puedes ejecutar tu script para utilizar tu EXPRESS VPN haciendo clic en el acceso directo.

## A tener en cuenta

El tooltip que debería leerse al pasar el ratón por encima del icono que aparece en la barra de herramientas, no se muestra correctamente en todos los sistemas operativos.
