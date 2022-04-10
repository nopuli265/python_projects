import pandas as pd 
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output 
import plotly.express as px
data = pd.read_csv('airline_data.csv')

app=dash.Dash(__name__) 

app.layout= html.Div(children=[
    html.H1('Flight Delay Time Statistics',
    style={
        'text-align':'center',
        'color':'Blue',
        'font-size': 40
    }),
    html.Br(),
    html.Div([
        'Input Year: ',
        dcc.Input(id='input-year', value='2010',type='number',style={'height':'20px', 'color':'green', 'font-size':20}),
    ],
    style={'font-size':20}),
    html.Br(),

    # segment 1
    html.Div([ 
        html.Div(dcc.Graph(id='carrier-plot')),
        html.Div(dcc.Graph(id='weather-plot'))
    ],
    style={'display':'flex'}),
# segment 2
    html.Div([ 
        html.Div(dcc.Graph(id='nas-plot')),
        html.Div(dcc.Graph(id='security-plot'))
    ],
    style={'display':'flex'}),
# segment 3
    
    html.Div(dcc.Graph(id='late-plot'))
])

def compute_info(data, entered_year):
    df=data[data['Year']==int(entered_year)]

    avg_car=df.groupby(['Month','Reporting_Airline'])['CarrierDelay'].mean().reset_index()
    avg_weather= df.groupby(['Month','Reporting_Airline'])['WeatherDelay'].mean().reset_index()
    avg_NAS= df.groupby(['Month','Reporting_Airline'])['NASDelay'].mean().reset_index()
    avg_sec= df.groupby(['Month','Reporting_Airline'])['SecurityDelay'].mean().reset_index()
    avg_late= df.groupby(['Month','Reporting_Airline'])['LateAircraftDelay'].mean().reset_index()
    return  avg_car, avg_weather, avg_NAS, avg_sec,avg_late

@app.callback([ 
    Output(component_id='carrier-plot', component_property='figure'),
    Output(component_id='weather-plot', component_property='figure'),
    Output(component_id='nas-plot', component_property='figure'),
    Output(component_id='security-plot', component_property='figure'),
    Output(component_id='late-plot', component_property='figure'),
],
    Input(component_id='input-year', component_property='value'))

def get_graph(entered_year):
    avg_car, avg_weather, avg_NAS, avg_sec, avg_late= compute_info(data,entered_year)

    carrier_fig=px.line(avg_car, x='Month', y='CarrierDelay',color='Reporting_Airline', title=' Average carrier delay time(minutes) by airline')

    weather_fig=px.line(avg_weather, x='Month', y='WeatherDelay', color='Reporting_Airline', title=' Average weather delay time(minutes) by airline')

    nas_fig=px.line(avg_NAS, x='Month',y='NASDelay', color='Reporting_Airline', title=' Average NAS delay time(minutes) by airline')

    sec_fig=px.line(avg_sec, x='Month',y='SecurityDelay', color='Reporting_Airline', title=' Average security delay time(minutes) by airline')

    late_fig=px.line(avg_late, x='Month',y='LateAircraftDelay', color='Reporting_Airline', title=' Average late aircraft delay time(minutes) by airline')

    return [carrier_fig, weather_fig,nas_fig, sec_fig, late_fig]


if __name__ == '__main__':
    app.run_server()
