# Criação de Dashboar de indicadores da Qualidade de uma indústria
# Necessário instalar o Dash, Panda, Openpyxl
# comando --> ex.: pip install pandas
# Criar uma base de dados (Farei em Excel)

# Copiado do Dash o código Template o qual será editado:

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

# Criando a tabela
df = pd.read_excel('Base_de_dados.xlsx')

# Criando o gráfico
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
opcoes = list(df['ID Loja'].unique())
opcoes.append('Todas as Lojas')

app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children='Gráfico com o Faturamento de Todos os Produtos separados por loja'),

    html.Div(children='''
        Obs: Esse gráfico mostra a quantidade de produtos vendidos, não o faturamento.
    '''),
    
    dcc.Dropdown(opcoes, value='Todas as Lojas', id='Lista_Lojas'),

    dcc.Graph(
        id='Gráfico_quantidade_vendas',
        figure=fig
    )
])

@app.callback(
    Output('Gráfico_quantidade_vendas', 'figure'),
    Input('Lista_Lojas', 'value')
)
def update_output(value):
    if value == 'Todas as Lojas':
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df["ID loja"]==value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)