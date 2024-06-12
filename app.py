import streamlit as st
import requests
import pandas as pd

# Função para obter as cotações de moedas
def get_exchange_rates():
    url = 'https://api.exchangerate-api.com/v4/latest/BRL'
    response = requests.get(url)
    data = response.json()
    return data['rates']

# Função para converter valores para BRL
def convert_to_brl(amount, rate, money_to_brl):
    return amount * (money_to_brl / rate)

# Dados de gastos médios (exemplo simplificado)
expenses = {
    'Estado': ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins'],
    'Categoria': ['Beleza Natural', 'Urbano', 'Fazenda', 'Praia', 'Montanha', 'Cultural', 'Aventura', 'Luxo', 'Beleza Natural', 'Urbano', 'Fazenda', 'Praia', 'Montanha', 'Cultural', 'Aventura', 'Luxo', 'Beleza Natural', 'Urbano', 'Fazenda', 'Praia', 'Montanha', 'Cultural', 'Aventura', 'Luxo', 'Beleza Natural', 'Urbano', 'Fazenda'],
    'Custo Médio': [300, 1500, 500, 400, 2000, 700, 600, 900, 300, 1500, 500, 400, 2000, 700, 600, 900, 300, 1500, 500, 400, 2000, 700, 600, 900, 300, 1500, 500]
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
selected_state = st.selectbox('Selecione um estado', df_expenses['Estado'].unique())
interests = st.multiselect('Selecione seus interesses', df_expenses['Categoria'].unique())

# Filtrando os dados conforme estado selecionado e categorias de interesse
filtered_interests_df = df_expenses[(df_expenses['Estado'] == selected_state) & (df_expenses['Categoria'].isin(interests))]

if not filtered_interests_df.empty:
    st.write(f"Você selecionou {selected_state} com interesses em {', '.join(interests)}.")
    st.write('Aqui estão os custos médios para suas preferências:')
    st.write(filtered_interests_df)
else:
    st.write('Não há dados disponíveis para os critérios selecionados.')
