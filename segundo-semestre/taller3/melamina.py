def calcular_cantidad_melamina(ancho, alto, precio_melamina= 29900, perdida_corte= 0.4, medidas_melamina= [244, 215]): #retorno: placas_utilizadas, precio, perdida, sobrante
    ancho_melamina = medidas_melamina[0]
    alto_melamina = medidas_melamina[1]
    
    perdida = 0
    planchas_horizontales = 1
    planchas_verticales = 1
    
    if (ancho > ancho_melamina):
        planchas_horizontales += ancho // ancho_melamina
    if (alto > alto_melamina):
        planchas_verticales += alto // alto_melamina
    
    if (ancho % ancho_melamina) != 0:
        perdida += perdida_corte * ancho
    if (alto % alto_melamina) != 0:
        perdida += perdida_corte * alto
        
    planchas_totales = planchas_horizontales * planchas_verticales
    precio = planchas_totales * precio_melamina
    
    sobrante = ((ancho_melamina * planchas_horizontales) * (alto_melamina * planchas_verticales)) - (ancho * alto) - perdida

    return planchas_totales, precio, perdida, sobrante