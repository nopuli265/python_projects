import pandas as pd 
import plotly.express as px
import dash 
from dash import html 
from dash import dcc
from dash.dependencies import Input, Output

data = pd.read_csv('airline_data.csv', encoding='ISO-8859-1')
data=data.sample(n=500,random_state=42)


fig =px.pie(data, values='Flights', names='DistanceGroup', title='Distance group proportion by flights')

#create a dash application 

app=dash.Dash(__name__)

# build  dash app layout 

app.layout=html.Div(children=[
    html.H1('Airline Dashboard',
    style={
        'text-align': 'center',
        'color':'#503D36',
        'font-size':40,
    }),
    html.P('Proportion of distance group (250 mile distance interval group) by flights.',
    style={
        'text-align': 'center',
        'color':'#F57241'
    }),
    dcc.Graph(figure=fig)
])

# run the application 
if __name__ =='__main__':
    app.run_server()
    