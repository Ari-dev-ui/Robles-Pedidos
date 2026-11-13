# Robles Bernardo Aribert Hans

def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def calcular_envio(subtotal):
    if subtotal >= 300:
        return 0
    return 20

precio = 80
cantidad = 3
subtotal = calcular_subtotal(precio, cantidad)
envio = calcular_envio(subtotal)
total = subtotal + envio

print("Subtotal: S/", subtotal)
print("Envio: S/", envio)
print("Total: S/", total)
