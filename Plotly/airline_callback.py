import pandas as pd 
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

# read data 
data= pd.read_csv("airline_data.csv")
data= data.sample(n=500, random_state=42)

#create app 

app=dash.Dash(__name__)

app.layout=html.Div(children=[
    html.H1("Airline Performance Dashboard", 
    style={
        'text-align':'center',
        'font-size':40,
        'color': 'green'
    }),
    html.Div(
        ['Input Year:', 
        dcc.Input(id='input-year', value='2010', type='number',
        style={'height':'50px', 'font-size':20})],
        style={'font-size':30}
    ),
    html.Br(),
    html.Div(dcc.Graph(id='line_plot'))
])

# add callback decorator

@app.callback(Output(component_id='line_plot',component_property='figure'),Input(component_id='input-year', component_property='value'))

# add computation to callback function and return Graph
def get_graph(entered_year):

    df=data[data['Year']==int(entered_year)]

    line_data=df.groupby('Month')['ArrDelay'].mean().reset_index()

    fig= go.Figure(data=go.Scatter( x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='red') ))

    fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='Arrdelay')
    return fig 

# Run the app 

if __name__=='__main__':
    app.run_server()