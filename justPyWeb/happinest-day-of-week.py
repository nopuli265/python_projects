import justpy as jp 
import pandas 
from datetime import datetime
from pytz import utc 

data=pandas.read_csv('reviews.csv', parse_dates=['Timestamp'])
data['dayweek']=data['Timestamp'].dt.strftime('%A')
data['daynumber']=data['Timestamp'].dt.strftime('%w')
day_happy=data.groupby(['dayweek', 'daynumber']).mean()
day_happy=day_happy.sort_values('daynumber')
chart_def="""
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'The happinest day of the week'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix:"Rate"
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'Rating',
        data: [3, 4, 3, 5, 4, 10, 12]
    }]
}
"""
def app():
    wp=jp.QuasarPage()
    h1=jp.QDiv(a=wp, text='Analysis of course reviews', classes='text-h3 text-center')
    p1= jp.QDiv(a=wp, text='these graphs represent course review analysis')
    
    hc=jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories=list(day_happy.index.get_level_values(0))
    hc.options.series[0].data=list(day_happy['Rating'])
    return wp
jp.justpy(app)