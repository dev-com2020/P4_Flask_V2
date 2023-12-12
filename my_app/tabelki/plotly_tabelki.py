import random

import dash
from dash import html, Output, Input
from dash import dcc
import plotly.express as px
import pandas as pd

app5 = dash.Dash(__name__)

df = pd.DataFrame({
    "Owoce": ["Jabłka", "Pomarańcze", 'Banany', "Jabłka", "Pomarańcze", 'Banany'],
    "Ilość": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Poland", "Poland", "Poland"]
})
print(df)

fig = px.bar(df, x='Owoce', y="Ilość", color='City', barmode='group')


@app5.callback(
    Output('example', 'figure'),
    Input('button', 'n_clicks')
)
def update_graph(n_clicks):
    if n_clicks is None:
        return fig
    else:
        new_fig = px.bar(df, x='Owoce', y=[random.randint(1, 10) for _ in range(6)], color='City', barmode='group')
        return new_fig


app5.layout = html.Div(children=[
    html.H1(children='Hello Dash!'),
    html.Div(children='''
        Test aplikacji z Pythona...
    '''),
    html.Button("Kliknij mnie aby zaktualizować dane", id='button'),
    dcc.Graph(id='example', figure=fig)
])

if __name__ == '__main__':
    app5.run_server(debug=True)
