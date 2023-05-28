from bs4 import BeautifulSoup
import requests

aerodromo = 'SBMT'

url = f'https://aisweb.decea.mil.br/?i=aerodromos&codigo={aerodromo}'  # URL da página a ser raspada
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

tag_sunrise = soup.find('sunrise')
tag_sunset = soup.find('sunset')

tag_h5_metar = soup.find('h5', string='METAR')
tag_p_metar = tag_h5_metar.find_next_sibling('p')
tag_h5_taf = soup.find('h5', string='TAF')
tag_p_taf = tag_h5_taf.find_next_sibling('p')


h4_cartas = soup.select('h4.heading-primary')[4]
next_h4_cartas = h4_cartas.find_next_sibling('h4')

print("1. As cartas disponíveis são:")
print('--------------------------------------------------')
if h4_cartas:
    h4_cartas_text = h4_cartas.text
    qtdCartasDisponiveis = int(h4_cartas_text[8])
    cartaAtual = h4_cartas.find_next_sibling('h4')
    for i in range(qtdCartasDisponiveis):
        print(f"{i+1}- {cartaAtual.text}")
        cartaAtual = cartaAtual.find_next_sibling('h4')
else:
    print("Nenhuma carta encontrada.")
print('')

print("2. Os horários de nascer e pôr do sol de hoje:")
print('--------------------------------------------------')
if tag_sunrise:
    sunrise_text = tag_sunrise.text
    print(f"O nascer do sol será: {sunrise_text}")
else:
    print("Tag <sunrise> não encontrada.")

if tag_sunset:
    sunset_text = tag_sunset.text
    print(f"O por do sol será: {sunset_text}")
else:
    print("Tag <sunset> não encontrada.")
print('')

print("3. A informação de TAF e METAR disponíveis:")
print('--------------------------------------------------')
if tag_p_metar:
    p_text = tag_p_metar.text
    print(f"METAR: {p_text}")
else:
    print("METAR não encontrado.")

if tag_p_taf:
    p_text = tag_p_taf.text
    print(f"TAF: {p_text}")
else:
    print("TAF não encontrado.")
print('')