import dash_core_components as dcc
import dash_html_components as html

from data import bonanza_sellers
bs = bonanza_sellers()

bonanza_sellers = html.Div(
    children=[
        html.H1(children='Analysis of Bonanza Sellers'),
        html.Div(html.P(children="Look at 2 different categories side by side")),
        html.Div(
            className="selections",
            children=[
                html.Div(
                    className='top-selections',
                    children=[
                        html.P(["Choose Category:", dcc.Dropdown(id="left_category", options=bs.category_options, value='fashion')])
                    ],
                ),
                
                html.Div(
                    className='top-selections',
                    children=[
                        html.P(["Choose Category:", dcc.Dropdown(id="right_category", options=bs.category_options, value='parts_accessories')])
                    ],
                    
                ),
            ]
        ),
        html.Div(id='left_df', style={'display':'none'}),
        html.Div(id='right_df', style={'display':'none'}),
        html.Div(
            className='selections',
            children = [
                html.Div(
                    className='stats-container',
                    children=[
                        html.P(id='left-winning'),
                    ]
                ),
                html.Div(
                    className='stats-container',
                    children=[
                        html.P(id='right-winning'),
                    ]
                )
            ]
        ),
        html.Div(
            className='selections',
            children=[
                html.Div(
                    className='left-selection',
                    children=[
                        html.P([d + '1' + ":", dcc.Dropdown(id="left_"+d, options=bs.col_options)])
                        for d in bs.scatter_dimensions[:-1]
                    ],   
                ),
                dcc.Graph(
                    className='left-graph',
                    id = 'winning booths'),
                html.Div(
                    className='right-selection',
                    children=[
                        html.P([d + '2' + ":", dcc.Dropdown(id="right_"+d, options=bs.col_options)])
                        for d in bs.scatter_dimensions[:-1]
                    ],
                ),
                dcc.Graph(
                    className='right-graph',
                    id = 'winning booths2'),
                ]),
    ],
)