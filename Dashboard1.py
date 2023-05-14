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
df = pd.read_excel('Base_de_dados1.xlsx')

# Criando o gráfico
fig = px.bar(df, x="Defeito", y="Indice Falhas PPM", color="Linha Produção", barmode="group")
opcoes = list(df['Linha Produção'].unique())
opcoes.append('Todas as Linhas')

app.layout = html.Div(children=[
    html.H1(children='Índice de Defeitos da Fábrica 1'),
    html.H2(children='Gráfico do Índice de Defeitos por Linha de Produção'),

    html.Div(children='''
        Obs: Esse gráfico mostra o índice de falhas em Partes Por Milhão - PPM.
    '''),
    
 #Adicionando o Botão dropdown para a filtragem as linhas de produção   
    dcc.Dropdown(opcoes, value='Todas as Linhas', id='Linha Produção'),

    dcc.Graph(
        id='gráfico_índice_falhas',
        figure=fig
    )
])

# Adicionando callback e condicional para a filtragem das linhas de produção
@app.callback(
    Output('gráfico_índice_falhas', 'figure'),
    Input('Linha Produção', 'value')
)
def update_output(value):
    if value == "Todas as Linhas":
        fig = px.bar(df, x="Defeito", y="Indice Falhas PPM", color="Linha Produção", barmode="group")
    else:
        tabela_filtrada = df.loc[df['Linha Produção']==value, :]
        fig =  px.bar(tabela_filtrada, x="Defeito", y="Indice Falhas PPM", color="Linha Produção", barmode="group")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)