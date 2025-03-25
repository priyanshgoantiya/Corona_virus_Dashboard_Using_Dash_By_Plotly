import pandas as pd
import numpy as np
import plotly.graph_objects as go
import dash
from dash import html, dcc
from dash.dependencies import Input,Output



external_stylesheets = [
    {
        "href": "https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css",
        "rel": "stylesheet",
        "integrity": "sha384-MCw98/SFnGE8fJT3GXwEOngsV7Z127NXFoaoApmYm81iuXoPkFOJwJBERdknLPMO",
        "crossorigin": "anonymous",
    }
]

df=pd.read_csv('Corona/IndividualDetails.csv')
Total = df.shape[0]
Recovered = df[df['current_status'] == 'Recovered'].shape[0]
Deaths = df[df['current_status'] == 'Deceased'].shape[0]
Active = df[df['current_status'] == 'Hospitalized'].shape[0]


options=[{'label':'All','value':'All'},
         {'label':'Hospitalized','value':'Hospitalized'},
         {'label':'Recovered','value':'Recovered'},
         {'label':'Deceased','value':'Deceased'}]



app = dash.Dash(__name__, external_stylesheets=[external_stylesheets[0]["href"]])

app.layout=html.Div([
    html.H1("Corona Virus Pandemic",style={'color':'#fff','text-align':'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Cases",className='text-light'),
                    html.H4(Total ,className='text-light')
                ],className='card-body')
            ],className='card bg-danger')
        ],className='col-md-3'),
        html.Div([html.Div([
                html.Div([
                    html.H3("Active Cases",className='text-light'),
                    html.H4(Active,className='text-light')
                ],className='card-body')
            ],className='card bg-info')],className='col-md-3'),
        html.Div([html.Div([
                html.Div([
                    html.H3("Recovered",className='text-light'),
                    html.H4(Recovered,className='text-light')
                ],className='card-body')
            ],className='card bg-warning')],className='col-md-3'),
        html.Div([html.Div([
                html.Div([
                    html.H3("Total Deaths",className='text-light'),
                    html.H4(Deaths ,className='text-light')
                ],className='card-body')
            ],className='card bg-success')],className='col-md-3')
    ],className='row'),
    html.Div([],className='row'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='picker',options=options,value='All'),
                    dcc.Graph(id='bar')
                ],className='card-body')
            ],className='card')
        ],className='col-md-12')
    ],className='row')
],className='container')

@app.callback(Output('bar','figure'),[Input('picker','value')])
def update_graph(type):
    if type=='All':
        State_data = df['detected_state'].value_counts().reset_index()
        return {'data':[go.Bar(x=State_data['detected_state'],y=State_data['count'])],'layout':go.Layout(title='State Total Count')}
    else:
        Recovered = df[df['current_status'] == type]
        State_data = Recovered['detected_state'].value_counts().reset_index()
        return {'data': [go.Bar(x=State_data['detected_state'], y=State_data['count'])],
                'layout': go.Layout(title='State Total Count')}
if __name__=='__main__':
    app.run(debug=True)
