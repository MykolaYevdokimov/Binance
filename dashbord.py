import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output
from tokens import normalize_data_standard, normalize_data_minMax
from main import ohlcv, tokens_pair_list
from tokens import to_ohlc_type, get_historical_data

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
        scaled_data = normalize_data_standard(ohlcv)
        return create_scatter_chart(scaled_data)

    elif button_id == 'btn-scale':
        scaled_data = normalize_data_minMax(ohlcv)
        return create_scatter_chart(scaled_data)

    elif button_id == 'btn-mean':   
        return create_scatter_chart(ohlcv)  


tokens_name_dropdown_options = [{'label': token, 'value': token} for token in tokens_pair_list]

dropdown = dcc.Dropdown(
    id='token-dropdown',
    options=tokens_name_dropdown_options,
    value=tokens_pair_list[0]
)

app.layout = html.Div([
    html.Div(dropdown,id='tokens-name'),
    html.Div(id='output-graph'),
    html.Button('Mean Value', id='btn-mean', className='button'),
    html.Button('Standardization', id='btn-std', className='button'),
    html.Button('Scaling', id='btn-scale', className='button'),
    
])


if __name__ == '__main__':
    app.run_server(debug=True)