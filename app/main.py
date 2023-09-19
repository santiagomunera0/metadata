import tkinter as tk
from tkinter import filedialog
import pandas as pd
from src.extract.extract_metadata import extract_metadata

# Lista para almacenar los nombres de los archivos seleccionados
archivos_seleccionados = []

def cargar_varios_archivos():
    archivos = filedialog.askopenfilenames(
        title="Selecciona archivos",
        filetypes=[("Todos los archivos", "*.*")]
    )
    
    if archivos:
        archivos_seleccionados.extend(archivos)
        # Agrega los nombres de los archivos a la lista archivos_seleccionados
        #print("Archivos seleccionados:", archivos_seleccionados)
        for archivo_cargado in archivos_seleccionados:
          extract_metadata(archivo_cargado)
          



# Crear una ventana de tkinter
ventana = tk.Tk()
ventana.title("Cargar Varios Archivos")

# Crear un botón para cargar archivos
boton_cargar = tk.Button(ventana, text="Cargar Archivos", command=cargar_varios_archivos)
boton_cargar.pack(pady=20)

# Iniciar el bucle principal de tkinter
ventana.mainloop()