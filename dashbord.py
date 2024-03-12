import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

from dash.dependencies import Input, Output
from tokens import normalize_data_standard, normalize_data_minMax
from main import tokens_pair_list
from tokens import to_ohlc_type, get_historical_data

external_stylesheets = ['assets/stylesheets.css']

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

def create_df_chart(token_name, start_date):
    ohlcv = to_ohlc_type((get_historical_data(token_name, start_date)),value=True)
    return ohlcv

def create_scatter_chart(ohlcv):
    scatter_chart = dcc.Graph(
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
    [
        Output('token-dropdown', 'options'),
        Output('scatter_chart', 'children'),
        Output('token-open-max', 'children'),
        Output('token-high-max', 'children'),
        Output('token-low-max', 'children'),
        Output('token-close-max', 'children'),
        Output('token-volume-max', 'children'),
    ],
    [
        Input('token-dropdown', 'value'),
        Input('btn-std', 'n_clicks'),
        Input('btn-scale', 'n_clicks'),
        Input('btn-mean', 'n_clicks'),
    ]
)
def update_graph(token_name, n_clicks_std, n_clicks_scale, n_clicks_mean):
    ohlcv = create_df_chart(token_name, '1 Jan 2022')
    ctx = dash.callback_context
    if not ctx.triggered:
        return [{'label': token, 'value': token} for token in tokens_pair_list], create_scatter_chart(ohlcv), ohlcv['Open'].max(), ohlcv['High'].max(), ohlcv['Low'].max(), ohlcv['Close'].max(),ohlcv['Volume'].max()
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'token-dropdown':
        ohlcv = create_df_chart(token_name, '1 Jan 2022')
        return dash.no_update, create_scatter_chart(ohlcv), ohlcv['Open'].max(), ohlcv['High'].max(), ohlcv['Low'].max(), ohlcv['Close'].max(),ohlcv['Volume'].max()
    elif button_id == 'btn-std':
        scaled_data = normalize_data_standard(ohlcv)
        return dash.no_update, create_scatter_chart(scaled_data), ohlcv['Open'].max(), ohlcv['High'].max(), ohlcv['Low'].max(), ohlcv['Close'].max(),ohlcv['Volume'].max()
    elif button_id == 'btn-scale':
        scaled_data = normalize_data_minMax(ohlcv)
        return dash.no_update, create_scatter_chart(scaled_data), ohlcv['Open'].max(), ohlcv['High'].max(), ohlcv['Low'].max(), ohlcv['Close'].max(),ohlcv['Volume'].max()
    elif button_id == 'btn-mean':
        return dash.no_update, create_scatter_chart(ohlcv), ohlcv['Open'].max(), ohlcv['High'].max(), ohlcv['Low'].max(), ohlcv['Close'].max(),ohlcv['Volume'].max()
    return dash.no_update, dash.no_update

@app.callback(
    Output("download-csv", "data"),
    [Input("btn-download", "n_clicks"),
     Input('token-dropdown', 'value')]
)
def download_csv(n_clicks, token_name):
    if n_clicks:
        ohlcv = create_df_chart(token_name, '1 Jan 2022')
        csv_string = ohlcv.to_csv(index=False, encoding="utf-8")
        return dict(content=csv_string, filename="ohlcv_data.csv")

app.layout = html.Div([
    dcc.Dropdown(
        id='token-dropdown',
        options=[{'label': token, 'value': token} for token in tokens_pair_list],
        value=tokens_pair_list[0]
    ),
    html.Div(id='scatter_chart'),
    html.Button('Mean Value', id='btn-mean', className='button'),
    html.Button('Standardization', id='btn-std', className='button'),
    html.Button('Scaling', id='btn-scale', className='button'),
    html.Div([
        'Token Open Max: ',
        html.Div(id = 'token-open-max', className='div'),
        'Token High Max: ',
        html.Div( id = 'token-high-max', className='div'),
        'Token Low Max :',
        html.Div( id = 'token-low-max', className='div'),
        'Token Close Max :',
        html.Div( id = 'token-close-max', className='div'),
        'Token Volume Max :',
        html.Div( id = 'token-volume-max', className='div'),
        dcc.Download(id="download-csv"),
        html.Button("Скачать CSV", id="btn-download"),
    ], id = 'token-statistics',
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)