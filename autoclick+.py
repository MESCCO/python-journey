import pyautogui
import time
import keyboard

print("=== AUTO-CLICK EN POSICIÓN DEL MOUSE ===")
print("\nInstrucciones:")
print("1. Coloca el mouse en la posición donde quieres hacer click")
print("2. Presiona 's' para iniciar el auto-click")
print("3. Presiona 'q' para detener el auto-click")
print("4. Presiona ESC para salir del programa")

# Configuración
intervalo = 0.00000001  # segundos entre clicks
activo = False

print(f"\nIntervalo entre clicks: {intervalo} segundos")
print("\nEsperando comando...")

while True:
    # Iniciar auto-click
    if keyboard.is_pressed('s') and not activo:
        activo = True
        # Capturar posición actual del mouse
        x, y = pyautogui.position()
        print(f"\n✓ Auto-click ACTIVADO en posición: ({x}, {y})")
        time.sleep(0.3)  # Evitar múltiples detecciones
    
    # Detener auto-click
    if keyboard.is_pressed('q') and activo:
        activo = False
        print("\n✗ Auto-click DETENIDO")
        time.sleep(0.3)
    
    # Salir del programa
    if keyboard.is_pressed('esc'):
        print("\n¡Programa finalizado!")
        break
    
    # Ejecutar click si está activo
    if activo:
        pyautogui.click(x, y)
        print(f"Click en ({x}, {y})", end='\r')
        time.sleep(intervalo)
    
    time.sleep(0.01)  # Pequeña pausa para no sobrecargar la CPU