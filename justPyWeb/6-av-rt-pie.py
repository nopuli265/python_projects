import justpy as jp 
import pandas 
from datetime import datetime
from pytz import utc
# we load the dataframe
data = pandas.read_csv('reviews.csv',parse_dates=['Timestamp'])
average_crs=data.groupby(['Course Name'])['Rating'].count()

# we have the HighCharts JavaScript code
chart_def="""
{
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Course Reviews'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""
# we have the function that renders the webpage
def app(): 
    wp=jp.QuasarPage()
    h1=jp.QDiv(a=wp, text='Analysis of Course Reviews' , classes='text-h3 text-center q-pa-md')
    p1=jp.QDiv(a=wp, text='these graphs represent course review analysis')
    hc=jp.HighCharts(a=wp, options=chart_def)
    #HighChart component
    hc_data=[{'name':v1, 'y': int(average_crs[v1] )} for v1 in average_crs.index] 
    # hc_data=[{'name':v1, 'y': v2} for v1,v2 in zip(average_crs.index,average_crs)]
    print(hc_data)
    hc.options.series[0].data=hc_data
    
    return wp
jp.justpy(app)