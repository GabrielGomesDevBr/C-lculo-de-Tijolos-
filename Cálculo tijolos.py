# Cálculo de tijolos para parede

# Objetivo: Calcular quantos tijolos serão utilizados em uma parede.

#1 O usuário deverá fornecer largura e altura dessa parede.

# São necessário 25 tijolos por metro quadrado



largura_da_parede = float(input ("Digite a largura da parede. "))
altura_da_parede = float(input ("Digite a altura da parede. "))

area_da_parede = largura_da_parede * altura_da_parede

qtd_de_tijolos = area_da_parede / 0.04

print ("Quantidade de tijos necessárias é: ", qtd_de_tijolos)

