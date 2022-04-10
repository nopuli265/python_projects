import justpy as jp 
import pandas 
from datetime import datetime
from pytz import utc
# we load the dataframe
data = pandas.read_csv('reviews.csv',parse_dates=['Timestamp'])
data['Week']=data['Timestamp'].dt.strftime('%Y-%U') 
average_week=data.groupby('Week').mean()

# we have the HighCharts JavaScript code
chart_def="""
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Week'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""
# we have the function that renders the webpage
def app(): 
    wp=jp.QuasarPage()
    h1=jp.QDiv(a=wp, text='Analysis of Course Reviews' , classes='text-h3 text-center q-pa-md')
    p1=jp.QDiv(a=wp, text='these graphs represent course review analysis')
    hc=jp.HighCharts(a=wp, options=chart_def)#HighChart component
    hc.options.title.text = 'Average Rating By Day'
    hc.options.xAxis.categories=list(average_week.index)
    hc.options.series[0].data =list(average_week['Rating'])
    hc.options.xAxis.title.text = 'Week'
    hc.options.yAxis.title.text ='Rating'

    return wp
jp.justpy(app)