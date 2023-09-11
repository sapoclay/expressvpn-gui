import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import re  

# Variable global para el estado de la conexión
connected = False



# Variable global para el color del círculo
circle_color = "red"  # Inicialmente, el círculo está en rojo (desconectado)


# Listado de servidores personalizados
server_list = [
    "Spain - Barcelona",
    "India (via UK)",
    "India (via Singapore)",
    "Spain - Madrid",
    "Spain - Barcelona - 2",
    "Singapore - Jurong",
    "Singapore - CBD",
    "Singapore - Marina Bay",
    "UK - Docklands",
    "UK - London",
    "UK - East London",
    "UK - Midlands",
    "UK - Wembley",
    "Hong Kong - 2",
    "Hong Kong - 1",
    "Japan - Tokyo",
    "Japan - Shibuya",
    "Japan - Yokohama",
    "Japan - Tokyo - 2",
    "USA - New Jersey - 1",
    "USA - New Jersey - 3",
    "USA - New York",
    "USA - Atlanta",
    "USA - Miami",
    "USA - Miami - 2",
    "USA - Washington DC",
    "USA - Dallas",
    "USA - Chicago",
    "USA - Lincoln Park",
    "USA - Albuquerque",
    "USA - San Francisco",
    "USA - Los Angeles - 3",
    "USA - Los Angeles - 2",
    "USA - Seattle",
    "USA - Denver",
    "USA - Salt Lake City",
    "USA - Tampa - 1",
    "USA - Phoenix",
    "USA - New Jersey - 2",
    "USA - Dallas - 2",
    "USA - Los Angeles - 1",
    "USA - Los Angeles - 5",
    "USA - Santa Monica",
    "Australia - Melbourne",
    "Australia - Woolloomooloo",
    "Australia - Sydney",
    "Australia - Perth",
    "Australia - Brisbane",
    "Australia - Adelaide",
    "Australia - Sydney - 2",
    "Germany - Frankfurt - 3",
    "Germany - Nuremberg",
    "Germany - Frankfurt - 1",
    "South Korea - 2",
    "Philippines",
    "Malaysia",
    "Netherlands - Rotterdam",
    "Netherlands - Amsterdam",
    "Netherlands - The Hague",
    "Sri Lanka",
    "Pakistan",
    "Kazakhstan",
    "France - Marseille",
    "France - Paris - 2",
    "France - Paris - 1",
    "France - Strasbourg",
    "France - Alsace",
    "Thailand",
    "Indonesia",
    "Mexico",
    "New Zealand",
    "Belgium",
    "Taiwan - 3",
    "Switzerland",
    "Switzerland - 2",
    "Vietnam",
    "Italy - Cosenza",
    "Italy - Naples",
    "Italy - Milan",
    "Macau",
    "Cambodia",
    "Mongolia",
    "Laos",
    "Myanmar",
    "Nepal",
    "Uzbekistan",
    "Bangladesh",
    "Bhutan",
    "Brunei",
    "Pick for Me",
    "Canada - Toronto",
    "Canada - Vancouver",
    "Canada - Toronto - 2",
    "Canada - Montreal",
    "Brazil - 2",
    "Brazil",
    "Panama",
    "Chile",
    "Argentina",
    "Bolivia",
    "Costa Rica",
    "Colombia",
    "Venezuela",
    "Ecuador",
    "Guatemala",
    "Peru",
    "Uruguay",
    "Bahamas",
    "Sweden",
    "Sweden - 2",
    "Romania",
    "Isle of Man",
    "Turkey",
    "Ireland",
    "Iceland",
    "Norway",
    "Denmark",
    "Finland",
    "Greece",
    "Portugal",
    "Austria",
    "Armenia",
    "Poland",
    "Lithuania",
    "Latvia",
    "Estonia",
    "Czech Republic",
    "Andorra",
    "Montenegro",
    "Bosnia and Herzegovina",
    "Luxembourg",
    "Hungary",
    "Bulgaria",
    "Belarus",
    "Ukraine",
    "Malta",
    "Liechtenstein",
    "Cyprus",
    "Albania",
    "Croatia",
    "Slovenia",
    "Slovakia",
    "Monaco",
    "Jersey",
    "North Macedonia",
    "Moldova",
    "Serbia",
    "Georgia",
    "South Africa",
    "Israel",
    "Egypt",
    "Kenya",
    "Algeria",
]

def get_connection_status():
    try:
        result = subprocess.run(["expressvpn", "status"], capture_output=True, text=True)
        output = result.stdout.strip()

        if "Not connected" in output:
            return "Desconectado", ""
        else:
            server_line = re.search(r"Connected to (.*?)\s*(\(|$)", output)
            server = server_line.group(1) if server_line else ""
            return "Conectado", server
    except subprocess.CalledProcessError:
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
    global circle_color  # Agrega una referencia al color del círculo

    status, _ = get_connection_status()
    status_label.config(text=f"Estado: {status}")
    server_label.config(text=f"Servidor: {server}" if server else "Servidor: ")

    # Cambia el texto y el color de fondo del botón según el estado de la conexión
    if connected:
        connect_button.config(text="Conectado", bg="green", state=tk.DISABLED)
        circle_color = "green"  # Cambia el color del círculo a verde cuando estás conectado
    else:
        connect_button.config(text="Conectar", bg="silver", state=tk.NORMAL)
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
    global circle  # Agrega una referencia al widget del círculo

    window = tk.Tk()
    window.title("Aplicación ExpressVPN")

    label = tk.Label(window, text="Conexión a ExpressVPN", font=("Arial", 14))
    label.grid(columnspan=2, pady=10)

    server_combobox = ttk.Combobox(window, values=server_list, state="readonly")
    server_combobox.grid(columnspan=2, pady=5)

    connect_button = tk.Button(window, text="Conectar", command=lambda: connect_vpn(server_combobox.get()))
    connect_button.grid(columnspan=2, pady=5)

    disconnect_button = tk.Button(window, text="Desconectar", command=disconnect_vpn)
    disconnect_button.grid(columnspan=2, pady=5)

    # Agrega una etiqueta para el círculo
    circle = tk.Label(window, text="●", bg=circle_color, font=("Arial", 12))
    circle.grid(row=4, column=0, padx=5, pady=5, sticky="e")  # Coloca el círculo junto a la etiqueta "Estado"

    status_label = tk.Label(window, text="Estado: ")
    status_label.grid(row=4, column=1, pady=5, sticky="w")  # Coloca la etiqueta "Estado" al lado del círculo

    server_label = tk.Label(window, text="Servidor: ")
    server_label.grid(columnspan=2, pady=5)

    update_status_and_server("")  # Pasa una cadena vacía como valor inicial

    # Añade este código para verificar el estado de la conexión al inicio
    initial_status, initial_server = get_connection_status()
    if initial_status == "Conectado":
        connected = True
        update_status_and_server(initial_server)

    server_combobox.set(initial_server)  # Establece el servidor conectado como seleccionado

    window.mainloop()

if __name__ == "__main__":
    create_vpn_window()
