# Criação de Dashboar de indicadores da Qualidade de uma indústria
# Necessário instalar o Dash, Panda, Openpyxl
# comando --> ex.: pip install pandas
# Criar uma base de dados (Farei em Excel)

# Copiado do Dash o código Template o qual será editado:

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

# Criando a tabela
df = pd.read_excel('Base_de_dados.xlsx')

# Criando o gráfico
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children='Gráfico com o Faturamento de Todos os Produtos separados por loja'),

    html.Div(children='''
        Obs: Esse gráfico mostra a quantidade de produtos vendidos, não o faturamento.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)