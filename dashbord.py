import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from main import ohlcv  

external_stylesheets = ['assets/stylesheets.css']

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

def create_scatter_chart(ohlcv):
    scatter_chart = dcc.Graph(
        id='scatter_chart',
        figure={
            'data':[
                go.Scatter(
                    x=pd.to_datetime(ohlcv.index),
                    y=ohlcv['Open'].values,
                    name='Open',
                ),
                go.Scatter(
                    x=pd.to_datetime(ohlcv.index),
                    y=ohlcv['Close'].values,
                    name='Close',
                ),
                go.Scatter(
                    x=pd.to_datetime(ohlcv.index),
                    y=ohlcv['High'].values,
                    name='High',
                ),
                go.Scatter(
                    x=pd.to_datetime(ohlcv.index),
                    y=ohlcv['Low'].values,
                    name='Low',
                )
            ],
            'layout': go.Layout(
                title='Coin Prices',
                xaxis={'title': 'Date'},
                yaxis={'title': 'Value'},
            )
        }
    )
    return scatter_chart

@app.callback(
    Output('output-graph', 'children'),
    [Input('btn-std', 'n_clicks'),
     Input('btn-scale', 'n_clicks'),
     Input('btn-mean', 'n_clicks')]  
)
def update_graph(n_clicks_std, n_clicks_scale, n_clicks_mean):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = 'No clicks yet'
        return create_scatter_chart(ohlcv)  # Возврат исходной диаграммы 
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'btn-std':
        scaler = StandardScaler()
        scaled_data = ohlcv.copy()
        scaled_data[['Open', 'Close', 'High', 'Low']] = scaler.fit_transform(scaled_data[['Open', 'Close', 'High', 'Low']])
        return create_scatter_chart(scaled_data)

    elif button_id == 'btn-scale':
        scaler = MinMaxScaler()
        scaled_data = ohlcv.copy()
        scaled_data[['Open', 'Close', 'High', 'Low']] = scaler.fit_transform(scaled_data[['Open', 'Close', 'High', 'Low']])
        return create_scatter_chart(scaled_data)

    elif button_id == 'btn-mean':   
        return create_scatter_chart(ohlcv)  
app.layout = html.Div([
    html.Div(id='output-graph'),
    html.Button('Mean Value', id='btn-mean', className='button'),
    html.Button('Standardization', id='btn-std', className='button'),
    html.Button('Scaling', id='btn-scale', className='button'),
    
])

if __name__ == '__main__':
    app.run_server(debug=True)