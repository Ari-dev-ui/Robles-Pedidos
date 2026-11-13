Robles Bernardo Aribert Hans

# Solicitudes de cambio de Comercial Robles
## INC-014 — Corrección del subtotal

- **Tipo de cambio:** Corrección de un error.
- **Descripción:** El programa muestra el precio de una unidad como subtotal.
- **Justificación:** El subtotal debe tomar en cuenta todas las unidades compradas.
- **Regla afectada:** RN-01.
- **Archivo afectado:** `codigo/pedidos.py`.
- **Riesgo:** Cobrar de menos cuando se compran varias unidades.
- **Criterio de aceptación:** Si se compran 3 unidades de S/ 80, el subtotal debe ser S/ 240.
- **Decisión:** Aprobada en la simulación.

## CR-015 — Cálculo del envío

- **Tipo de cambio:** Nueva funcionalidad.
- **Descripción:** Agregar el cálculo del envío y del total del pedido.
- **Justificación:** La gerencia necesita que el sistema calcule el importe final.
- **Reglas afectadas:** RN-02, RN-03 y RN-04.
- **Archivos afectados:** `codigo/pedidos.py` y `documentos/requisitos.md`.
- **Riesgo:** Cobrar envío cuando el subtotal es de S/ 300.
- **Criterio de aceptación:** Con S/ 240 de subtotal, el envío es S/ 20 y el total S/ 260. Con S/ 300 o S/ 450, el envío es gratuito y el total es igual al subtotal.
- **Decisión:** Aprobada en la simulación.