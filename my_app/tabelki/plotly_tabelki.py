import dash
from dash import html
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

app5.layout = html.Div(children=[
    html.H1(children='Hello Dash!'),
    html.Div(children='''
        Test aplikacji z Pythona...
    '''),
    dcc.Graph(id='example', figure=fig)
])

if __name__ == '__main__':
    app5.run_server(debug=True)
