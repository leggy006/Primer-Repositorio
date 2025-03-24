def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a un monto total de compra.

    :param monto_total: Total de la compra
    :param porcentaje_descuento: Porcentaje de descuento (10% por defecto)
    :return: Monto del descuento
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Llamadas a la función
monto1 = 100  # Ejemplo de monto total de compra
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

monto2 = 200  # Otro ejemplo de monto total
descuento2 = calcular_descuento(monto2, 15)  # Aplicando un 15% de descuento
monto_final2 = monto2 - descuento2

# Mostrar resultados
print(f"Compra de ${monto1}: Descuento de ${descuento1:.2f}, Total a pagar: ${monto_final1:.2f}")
print(f"Compra de ${monto2}: Descuento de ${descuento2:.2f}, Total a pagar: ${monto_final2:.2f}")


