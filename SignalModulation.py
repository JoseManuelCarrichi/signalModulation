import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Función para generar una señal senoidal
def generate_signal(amplitude, frequency, time):
    return amplitude * np.sin(2 * np.pi * frequency * time)

# Función para realizar la modulación AM
def am_modulation(signal, carrier_amplitude, carrier_frequency, modulation_index):
    carrier = generate_signal(carrier_amplitude, carrier_frequency, time)
    return (1 + modulation_index * signal) * carrier

# Función para realizar la modulación FM
def fm_modulation(signal, carrier_amplitude, carrier_frequency, modulation_index):
    deviation = modulation_index * signal
    return carrier_amplitude * np.sin(2 * np.pi * (carrier_frequency + deviation) * time)

# Parámetros iniciales
amplitude = 1.0
frequency = 1.0
carrier_amplitude = 1.0
carrier_frequency = 10.0
modulation_index = 1.0

# Crear figura y ejes
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.15, bottom=0.35)

# Generar tiempo
time = np.linspace(0, 1, 500)

# Generar señal senoidal inicial
signal = generate_signal(amplitude, frequency, time)

# Graficar señal senoidal
line, = ax.plot(time, signal, lw=2)

# Configurar ejes
ax.set_xlabel('Tiempo')
ax.set_ylabel('Amplitud')

# Configurar límites de los ejes
ax.set_xlim([0, 1])
ax.set_ylim([-2, 2])

# Crear ejes deslizables para modificar amplitud y frecuencia
amplitude_slider_ax = plt.axes([0.15, 0.2, 0.7, 0.03])
amplitude_slider = Slider(amplitude_slider_ax, 'AM', 0.1, 5.0, valinit=amplitude)

frequency_slider_ax = plt.axes([0.15, 0.15, 0.7, 0.03])
frequency_slider = Slider(frequency_slider_ax, 'FM', 0.1, 10.0, valinit=frequency)

# Función para actualizar la señal cuando se modifican los parámetros
def update(val):
    global amplitude, frequency

    # Actualizar los parámetros de amplitud y frecuencia
    amplitude = amplitude_slider.val
    frequency = frequency_slider.val

    # Generar la nueva señal
    signal = generate_signal(amplitude, frequency, time)

    # Actualizar la línea de la señal en el gráfico
    line.set_ydata(signal)

    # Redibujar el gráfico
    fig.canvas.draw_idle()

# Actualizar la señal cuando se modifican los parámetros
amplitude_slider.on_changed(update)
frequency_slider.on_changed(update)

# Mostrar el gráfico
plt.show()
