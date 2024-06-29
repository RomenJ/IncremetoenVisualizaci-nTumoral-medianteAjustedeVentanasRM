import imageio.v2 as imageio
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import tkinter.font as tkFont

# Número total de imágenes y subplots por plot
num_images = 80
images_per_plot = 10

# Valores iniciales para vmin y vmax
vmin = -200
vmax = 200

# Leer todas las imágenes
images = [imageio.imread(f'{i+1}.dcm') for i in range(num_images)]

# Crear la ventana principal de tkinter
root = tk.Tk()
root.title("Visualización Tumoral mediante Ajuste de Ventanas RM")

# Configurar fondo verde muy suave
root.configure(bg='#f0f8f0')

# Variables para mantener el estado actual
current_plot_idx = 0

# Crear figura y ejes
fig, axes = plt.subplots(2, 5, figsize=(15, 6))
axes = axes.flatten()

def update_plot(plot_idx):
    for subplot_idx in range(images_per_plot):
        image_idx = plot_idx * images_per_plot + subplot_idx
        if image_idx < num_images:
            axes[subplot_idx].imshow(images[image_idx], cmap='gray', vmin=vmin, vmax=vmax)
            axes[subplot_idx].set_title(f'Image {image_idx + 1}')
            axes[subplot_idx].axis('off')
        else:
            axes[subplot_idx].axis('off')
    fig.tight_layout()
    canvas.draw()

def next_plot():
    global current_plot_idx
    if current_plot_idx < (num_images // images_per_plot):
        current_plot_idx += 1
        update_plot(current_plot_idx)

def previous_plot():
    global current_plot_idx
    if current_plot_idx > 0:
        current_plot_idx -= 1
        update_plot(current_plot_idx)

def increase_vmin():
    global vmin
    vmin += 50
    update_plot(current_plot_idx)
    vmin_text.set(f"vmin: {vmin}")

def decrease_vmin():
    global vmin
    vmin -= 50
    update_plot(current_plot_idx)
    vmin_text.set(f"vmin: {vmin}")

def increase_vmax():
    global vmax
    vmax += 50
    update_plot(current_plot_idx)
    vmax_text.set(f"vmax: {vmax}")

def decrease_vmax():
    global vmax
    vmax -= 50
    update_plot(current_plot_idx)
    vmax_text.set(f"vmax: {vmax}")

def modo_estudiante():
    global vmin, vmax
    vmin = 0
    vmax = 50
    update_plot(current_plot_idx)
    vmin_text.set(f"vmin: {vmin}")
    vmax_text.set(f"vmax: {vmax}")

# Crear un canvas de tkinter para la figura de matplotlib
canvas = FigureCanvasTkAgg(fig, master=root)

# Añadir el título centrado en Arial negrita de 50px al inicio
title_font = tkFont.Font(family='Arial', size=30, weight='bold')
title_label = tk.Label(root, text="Visualización Tumoral mediante Ajuste de Ventanas RM", font=title_font, bg='#f0f8f0')
title_label.pack()

# Agregar carácter unicode médico debajo del título
unicode_label = tk.Label(root, text="⚕️", font=("Arial", 40), bg='#f0f8f0')
unicode_label.pack()

canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Inicializar el primer plot después de definir el canvas
update_plot(current_plot_idx)

# Crear botones de navegación
btn_prev = tk.Button(root, text="⬅", command=previous_plot, font=("Arial", 20, "bold"), bg='#f0f8f0')
btn_prev.pack(side=tk.LEFT, padx=40, pady=10)

btn_next = tk.Button(root, text="➡", command=next_plot, font=("Arial", 20, "bold"), bg='#f0f8f0')
btn_next.pack(side=tk.RIGHT, padx=40, pady=10)

# Variables de texto para mostrar los valores de vmin y vmax
vmin_text = tk.StringVar(value=f"vmin: {vmin}")
vmax_text = tk.StringVar(value=f"vmax: {vmax}")

# Crear botones y áreas de texto para ajustar vmin y vmax
frame_vmin = tk.Frame(root, bg='#f0f8f0')
frame_vmin.pack(side=tk.LEFT, padx=20, pady=20)

btn_increase_vmin = tk.Button(frame_vmin, text="Increase vmin", command=increase_vmin, font=("Arial", 30, "bold"))
btn_increase_vmin.pack(side=tk.TOP)

btn_decrease_vmin = tk.Button(frame_vmin, text="Decrease vmin", command=decrease_vmin, font=("Arial", 30, "bold"))
btn_decrease_vmin.pack(side=tk.TOP)

vmin_label = tk.Label(frame_vmin, textvariable=vmin_text, font=("Arial", 30))
vmin_label.pack(side=tk.TOP)

frame_vmax = tk.Frame(root, bg='#f0f8f0')
frame_vmax.pack(side=tk.RIGHT, padx=20, pady=20)

btn_increase_vmax = tk.Button(frame_vmax, text="Increase vmax", command=increase_vmax, font=("Arial", 30, "bold"))
btn_increase_vmax.pack(side=tk.TOP)

btn_decrease_vmax = tk.Button(frame_vmax, text="Decrease vmax", command=decrease_vmax, font=("Arial", 30, "bold"))
btn_decrease_vmax.pack(side=tk.TOP)

vmax_label = tk.Label(frame_vmax, textvariable=vmax_text, font=("Arial", 30))
vmax_label.pack(side=tk.TOP)

# Crear botón "Modo Estudiante"
btn_mod_estudiante = tk.Button(root, text="Modo Estudiante", command=modo_estudiante, font=("Arial", 20, "bold"), bg='#f0f8f0')
btn_mod_estudiante.pack(side=tk.RIGHT, padx=20, pady=20)

# Crear botón de salir
btn_exit = tk.Button(root, text="Salir", command=root.quit, font=("Arial", 30, "bold"))
btn_exit.pack(side=tk.BOTTOM, pady=20)

# Ejecutar el bucle principal de tkinter
root.mainloop()
