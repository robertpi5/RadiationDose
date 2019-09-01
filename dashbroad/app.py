import dash
import dash_core_components as dcc
import dash_html_components as html
import pymssql
import datetime;
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
month=['1月','2月','3月']
year=['2018','2019','2020']

app.layout = html.Div(children=[
    html.H1(children='Hello Dash1'),

    html.Div(children='''
        Dash: A web application framework for Python1111.
    '''),
dcc.Dropdown(
    options=[
        {'label': '一月', 'value': 'NYC'},
        {'label': '二月', 'value': 'MTL'},
        {'label': '三月', 'value': 'SF'}
    ],
    value='MTL'
) , 
dcc.Dropdown(
    options=[
        {'label': '2018', 'value': 'NYC'},
        {'label': '2019', 'value': 'MTL'},
        {'label': '2020', 'value': 'SF'}
    ],
    value='MTL'
) , 
    dcc.Graph(
        id='example-graph',
        style={'height':300},
        figure={
            'data': [
                {'x': month, 'y': [4, 1, 2], 'type': 'bar', 'name': 'PET/CT'},
                {'x': month, 'y': [2, 4, 5], 'type': 'bar', 'name': 'ECT'},
            ],
            'layout': {
                'title': '检查统计'
            }
        }
    ),

    dcc.Graph(
        id='example-graph2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
   app.run_server(host='0.0.0.0', port=5080,debug=True)
