import random

import dash
from dash import html, Output, Input
from dash import dcc
import plotly.express as px
import pandas as pd
from sqlalchemy import create_engine, text as sql_text

app6 = dash.Dash(__name__)

engine = create_engine('mysql+pymysql://root:12345@localhost/exampledbflask')
query = "SELECT * FROM product"

df = pd.read_sql_query(con=engine.connect(), sql=sql_text(query))
# print(df)

fig = px.line(df, x="id", y="price", title='Wykres cen')


def update_sql():
    global df
    df = pd.read_sql_query(con=engine.connect(), sql=sql_text(query))
    return df


@app6.callback(
    Output('example', 'figure'),
    Input('button', 'n_clicks')
)
def update_graph(n_clicks):
    if n_clicks is None:
        return fig
    else:
        new_fig = fig
        update_sql()
        return new_fig


app6.layout = html.Div(children=[
    html.H1(children='Wykres #2'),
    html.Div(children='''
        Test wykresu nr 2...
    '''),
    html.Button("Kliknij mnie aby zaktualizować dane", id='button'),
    dcc.Graph(id='example', figure=fig)
])

if __name__ == '__main__':
    app6.run_server(debug=True)
