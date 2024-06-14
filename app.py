import streamlit as st
import requests
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Função para obter as cotações de moedas
def get_exchange_rates():
    url = 'https://api.exchangerate-api.com/v4/latest/BRL'
    response = requests.get(url)
    data = response.json()
    return data['rates']

# Função para converter valores para BRL
def convert_to_brl(amount, rate, money_to_brl):
    return amount * (money_to_brl / rate)

#   Estados
expenses = {
    'Estado': ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins'],
}
df_expenses = pd.DataFrame(expenses)

# Interface com Streamlit
st.title('Ache sua viagem perfeita!')

# Seção de cotações
st.header('Cotações de Moedas') 
rates = get_exchange_rates()
if 'BRL' not in rates:
    st.error('Erro ao carregar a cotação do BRL.')
else:
    money_to_brl = rates['BRL']
    currencies = ['USD', 'EUR', 'GBP', 'JPY']
    selected_currency = st.selectbox('Selecione uma moeda', currencies)
    amount = st.number_input('Insira o valor em ' + selected_currency, min_value=0.0, format="%.2f")
    
    if selected_currency in rates:
        rate = rates[selected_currency]
        converted_amount = convert_to_brl(amount, rate, money_to_brl)
        st.write(f'O valor em reais (BRL) é: R${converted_amount:.2f}')
    else:
        st.error('Erro ao carregar a cotação da moeda selecionada.')

# Seção de sugestão de viagem
st.header('Sugestão de Viagem')

# Fazer a solicitação para a página web
r = requests.get("https://buzzfeed.com.br/post/todo-estado-brasileiro-tem-um-lugar-que-voce-precisa-visitar-antes-de-morrer")

# Analisar o conteúdo HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Extrair dados do conteúdo analisado
entries = soup.find_all('div', class_='entry-image-heading')

# Criar um dicionário para armazenar os estados e pontos turísticos
state_tourist_spots = {}

for entry in entries:
    state_and_place = entry.find('h3').text if entry.find('h3') else "Título não encontrado"
    state, place = state_and_place.split(': ')
    state_tourist_spots[state] = place

# Seção de sugestão de viagem
selected_state = st.selectbox('Selecione um estado', df_expenses['Estado'].unique())

# Exibir o ponto turístico correspondente ao estado selecionado
def ponto_turistico(selected_state):
 if selected_state == "Acre":
        return st.header(state_tourist_spots[selected_state]), st.image('https://img.buzzfeed.com/buzzfeed-static/static/2019-05/24/13/asset/buzzfeed-prod-web-02/sub-buzz-23323-1558717922-1.jpg'), st.text('''Se você só sabe o nome da capital do Acre (dica: é Rio Branco!) já pode atualizar a
informação: o estado mais ao oeste do Brasil tem altas florestas, cachoeiras e vida
animal preservada, como no Parque Nacional da Serra do Divisor.''')

 elif selected_state == "Alagoas":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712263121250-187.jpg')
    st.text('''Areia branca, mar azul, coqueiros, o vento que sopra do oceano... imagina a cara dos primeiros colonizadores europeus quando chegaram nesse lugar? Fica perto de outro paraíso alagoano: Maragogi.''')

 elif selected_state == "Amapá":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712259371563-222.jpg')
    st.text('''Tem o maior parque de floresta tropical do mundo, na divisa com a Guiana Francesa e o Suriname, que só pode ser visitado com autorização.''')

 elif selected_state == "Amazonas":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712231523539-469.jpg')
    st.text('''Anavilhanas é um arquipélago do Rio Negro, um dos maiores do mundo, formado por ilhas de água doce que na temporada de seca se transformam em praias estupendas assim.''')

 elif selected_state == "Bahia":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712243042369-239.jpg')
    st.text('''A Praia da Camboinha, na foto, é uma das mais bonitas do espetacular litoral baiano.''')

 elif selected_state == "Ceará":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712205418495-834.jpg')
    st.text('''Jericoacoara é uma vila tranquila, com praias de águas calmas e dunas espetaculares. Um dos destinos mais famosos e belos do Brasil.''')

 elif selected_state == "Distrito Federal":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712285937695-499.jpg')
    st.text('''Santuário ecológico pertinho de Brasília que pode ser visitado pelo público e tem trilhas e dezenas de cachoeiras.''')

 elif selected_state == "Espírito Santo":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712245270533-803.jpg')
    st.text('''Essa serra fica na divisa com Minas Gerais e é famosa pelo clima frio, as plantações de café e por guardar o terceiro pico mais alto do Brasil, o Pico da Bandeira.''')

 elif selected_state == "Goiás":
    st.header(state_tourist_spots[selected_state])
    st.image('https://img.buzzfeed.com/buzzfeed-static/static/2019-05/20/14/asset/buzzfeed-prod-web-03/sub-buzz-23189-1558377114-11.jpg')
    st.text('''A Chapada dos Veadeiros é um parque nacional repleto de cachoeiras, cânions e formações rochosas incríveis, ideal para os amantes de natureza e aventura.''')

 elif selected_state == "Maranhão":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712180514949-421.jpg')
    st.text('''Os Lençóis Maranhenses são um deserto único com dunas e lagoas de água doce, criando uma paisagem surreal e impressionante.''')

 elif selected_state == "Mato Grosso":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712282176577-471.jpg')
    st.text('''Você gosta de andar? Então a Chapada dos Guimarães é pra você! As trilhas podem durar horas e todas levam até cachoeiras e paisagens incríveis. Curiosidade: o centro geográfico do Brasil é aqui.''')

 elif selected_state == "Mato Grosso do Sul":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712240000699-390.jpg')
    st.text('''Bonito é famoso por suas águas cristalinas, cavernas, grutas e cachoeiras, sendo um dos principais destinos de ecoturismo do Brasil.''')

 elif selected_state == "Minas Gerais":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712245672975-474.jpg')
    st.text('''Capaz de você já ter visto as águas azuis-turquesa dos cânions da Represa de Furnas: Capitólio rende, é bem famosa no Instagram e é um dos muitos lugares maravilhosos para visitar em Minas Gerais.''')

 elif selected_state == "Pará":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712265117459-17.jpg')
    st.text('''Alter do Chão, com suas praias de areia branca e águas cristalinas, é um verdadeiro paraíso amazônico.''')

 elif selected_state == "Paraíba":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712199163281-145.jpg')
    st.text('''Dá pra recomendar altas praias paradisíacas em todo o litoral brasileiro. Só que paisagens malucas cheia de incríveis formações rochosas em pleno sertão, como as de Cabaceiras, aí só tem nesse interior da Paraíba mesmo.''')

 elif selected_state == "Paraná":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712234710779-559.jpg')
    st.text('''Foz do Iguaçu é mundialmente famosa pelas Cataratas do Iguaçu, um dos maiores conjuntos de quedas d'água do mundo.''')

 elif selected_state == "Pernambuco":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712245270533-844.jpg')
    st.text('''O Vale do Catimbau é uma das últimas áreas da caatinga brasileira e é um paraíso para quem pira em arqueologia, com pinturas rupestres em aproximadamente DUAS MIL cavernas (!) e além de 28 cavernas-cemitério.''')

 elif selected_state == "Piauí":
    st.header(state_tourist_spots[selected_state])
    st.image('https://img.buzzfeed.com/buzzfeed-static/static/2019-05/24/16/asset/buzzfeed-prod-web-04/sub-buzz-26268-1558730736-1.jpg')
    st.text('''A Serra da Capivara é um parque nacional com pinturas rupestres pré-históricas, uma verdadeira viagem no tempo.''')

 elif selected_state == "Rio de Janeiro":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712263121250-295.jpg')
    st.text('''Sabe o que nasceu aqui? A cachaça! Além de ser uma graça, essa cidade colonial no pé da Serra do Mar, também é sede de festivais culturais.''')

 elif selected_state == "Rio Grande do Norte":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712241849868-927.jpg')
    st.text('''Imagina morar perto desse cenário? As dunas ficam bem do lado de Natal, capital do Rio Grande do Norte.''')

 elif selected_state == "Rio Grande do Sul":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712191072991-248.jpg')
    st.text('''Florestas de araucárias, cascatas de água gelada e paredões de granito: esse Parque Nacional no sul do Brasil é pouco conhecido entre o pessoal de outras regiões, mas vale muito a visita.''')

 elif selected_state == "Rondônia":
    st.header(state_tourist_spots[selected_state])
    st.image('https://img.buzzfeed.com/buzzfeed-static/static/2019-05/21/18/asset/buzzfeed-prod-web-05/sub-buzz-10194-1558479014-2.jpg')
    st.text('''O Parque Estadual Corumbiara, na fronteira com a Bolívia, é o único lugar do mundo com biomas de áreas de Cerrado, Pantanal e Floresta Amazônica.''')

 elif selected_state == "Roraima":
    st.header(state_tourist_spots[selected_state])
    st.image('https://img.buzzfeed.com/buzzfeed-static/static/2019-05/24/17/asset/buzzfeed-prod-web-01/sub-buzz-26708-1558731803-1.jpg')
    st.text('''O Monte Roraima é um dos tepuis mais famosos do mundo, com paisagens surreais e únicas.''')

 elif selected_state == "Santa Catarina":
    st.header(state_tourist_spots[selected_state])
    st.image('https://img.buzzfeed.com/buzzfeed-static/static/2019-05/21/18/asset/buzzfeed-prod-web-03/sub-buzz-25818-1558478338-1.jpg')
    st.text('''Vila de pescadores em um dos trechos mais lindos do espetacular litoral catarinense com ruas de areia, casinhas coloridas, mirantes e piscinas naturais. E esse mar, né? Olha esse mar!''')

 elif selected_state == "São Paulo":
    st.header(state_tourist_spots[selected_state])
    st.image('https://img.buzzfeed.com/buzzfeed-static/static/2019-05/20/17/asset/buzzfeed-prod-web-04/sub-buzz-24915-1558386241-14.jpg')
    st.text('''A sigla PETAR significa Parque Estadual Turístico do Alto Ribeira, e o parque, que fica no sul do estado, tem mais de 350 cavernas mapeadas..''')

 elif selected_state == "Sergipe":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712201005361-469.jpg')
    st.text('''O Cânion do Xingó é um espetáculo natural, com suas formações rochosas e águas verde-esmeralda.''')

 elif selected_state == "Tocantins":
    st.header(state_tourist_spots[selected_state])
    st.image('https://s3.amazonaws.com/images.buzzfeed.com.br/legacy/entries/1712277524016-439.jpg')
    st.text('''Jalapão é um destino de ecoturismo com fervedouros, cachoeiras e paisagens incríveis.''')

print(ponto_turistico(selected_state))
