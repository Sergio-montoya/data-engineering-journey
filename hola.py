producto = 39.90
cantidad = 5
descuento = 15

subtotal = producto * cantidad
imp_descuento = subtotal * (descuento / 100)
total = subtotal - imp_descuento

print ("Subtotal:", subtotal)
print ("Descuento:", imp_descuento)
print ("Total:", total)
