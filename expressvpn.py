import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import re  

# Variable global para el estado de la conexión
connected = False

# Variable global para el color del círculo
circle_color = "red"  # Inicialmente, el círculo está en rojo (desconectado)

def get_server_list():
    try:
        result = subprocess.run(["expressvpn", "list", "all"], capture_output=True, text=True)
        output = result.stdout.strip().splitlines()

        # Obtener el primer grupo de letras de cada fila, omitiendo los dos primeros resultados
        locations = [line.split(None, 1)[0] for line in output[2:] if line.strip()]

        return locations

    except subprocess.CalledProcessError as e:
        print(f"Error al obtener la lista de servidores: {e}")
        return []

# lista de servidores
server_list = get_server_list()

def get_connection_status():
    try:
        result = subprocess.run(["expressvpn", "status"], capture_output=True, text=True)
        output = result.stdout.strip()

        if "Not connected" in output:
            return "Desconectado", ""
        else:
            server_line = re.search(r"Connected to (.*?)\n", output)
            server = server_line.group(1) if server_line else ""
            return "Conectado", server
    except subprocess.CalledProcessError as e:
        print(f"Error al obtener el estado de la conexión: {e}")
        return "Desconectado", ""



def connect_vpn(selected_server):
    global connected
    if not selected_server:
        messagebox.showwarning("Advertencia", "Primero debes seleccionar un servidor al que conectarte.")
    else:
        if connected:
            # Si ya está conectado, no se permite reconectar.
            messagebox.showinfo("Conexión VPN", "Ya estás conectado a un servidor.")
        else:
            try:
                subprocess.run(["expressvpn", "connect", selected_server])
                connected = True  # Actualiza el estado de la conexión
                update_status_and_server(selected_server)
                messagebox.showinfo("Conexión VPN", f"Conectado a {selected_server}.")
            except subprocess.CalledProcessError:
                messagebox.showerror("Error", "No se pudo conectar a ExpressVPN.")

def disconnect_vpn():
    global connected
    try:
        subprocess.run(["expressvpn", "disconnect"])
        connected = False  # Actualiza el estado de la conexión
        messagebox.showinfo("Conexión VPN", "Desconectado de ExpressVPN.")
        update_status_and_server("")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "No se pudo desconectar de ExpressVPN.")


def update_status_and_server(server):
    global status_label
    global server_label
    global connect_button
    global disconnect_button
    global circle_color  # Agrega una referencia al color del círculo

    status, _ = get_connection_status()
    status_label.config(text=f"Estado: {status}")
    server_label.config(text=f"Servidor: {server}" if server else "Servidor: ")

    # Cambia el texto y el color de fondo del botón según el estado de la conexión
    if connected:
        connect_button.config(state=tk.DISABLED)  # Deshabilita el botón "Conectar"
        disconnect_button.config(state=tk.NORMAL)  # Habilita el botón "Desconectar"
        circle_color = "green"  # Cambia el color del círculo a verde cuando estás conectado
    else:
        connect_button.config(state=tk.NORMAL)  # Habilita el botón "Conectar"
        disconnect_button.config(state=tk.DISABLED)  # Deshabilita el botón "Desconectar"
        circle_color = "red"  # Cambia el color del círculo a rojo cuando estás desconectado

    # Actualiza el círculo de estado
    update_circle_status()

def update_circle_status():
    status, _ = get_connection_status()

    if status == "Conectado":
        circle.config(bg="green")
    else:
        circle.config(bg="red")

def create_vpn_window():
    global status_label
    global server_label
    global connect_button
    global disconnect_button
    global circle  # Agrega una referencia al widget del círculo
    global connected  # Añade esta línea para indicar que estás utilizando la variable global 'connected'
    global server_combobox

    connected = False  # Agrega esta línea para asegurarte de que 'connected' se inicialice correctamente

    window = tk.Tk()
    window.title("Conexión - ExpressVPN")

    window.resizable(False, False)  # Esta línea deshabilita el redimensionamiento

    label = tk.Label(window, text="Conexión a ExpressVPN", font=("Arial", 14))
    label.grid(columnspan=2, pady=10)

    # Cargar la imagen
    img = tk.PhotoImage(file="ExpressVPN-logo.png")

    # Asignar la imagen como ícono de la ventana
    window.tk.call('wm', 'iconphoto', window._w, img)

    # Mostrar la imagen en un widget Label
    img_label = tk.Label(window, image=img)
    img_label.grid(columnspan=2, pady=(10, 10))

    server_combobox = ttk.Combobox(window, values=server_list, state="readonly")
    server_combobox.grid(columnspan=2, pady=5)

    connect_button = tk.Button(window, text="Conectar", command=lambda: connect_vpn(server_combobox.get()))
    connect_button.grid(columnspan=2, pady=10)

    # Agrega una etiqueta para el círculo junto a la etiqueta "Estado"
    circle = tk.Label(window, text="●", bg=circle_color, font=("Arial", 12))
    circle.grid(row=5, column=0, padx=(5, 0), pady=10, sticky="e")  # Coloca el círculo junto a la etiqueta "Estado"

    status_label = tk.Label(window, text="Estado: ")
    status_label.grid(row=5, column=1, pady=10, sticky="w")  # Asegura que esté en la fila 5

    disconnect_button = tk.Button(window, text="Desconectar", command=disconnect_vpn, state=tk.DISABLED)
    disconnect_button.grid(columnspan=2, pady=(10, 10))  # Aumenta el espacio inferior a 10 píxeles

    server_label = tk.Label(window, text="Servidor: ")
    server_label.grid(columnspan=2, pady=10)

    # Intenta obtener el estado de la conexión al inicio
    initial_status, initial_server = get_connection_status()
    if initial_status == "Conectado":
        connected = True
        update_status_and_server(initial_server)
        server_combobox.set(initial_server)

    window.mainloop()

if __name__ == "__main__":
    create_vpn_window()
