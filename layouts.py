import dash_core_components as dcc
import dash_html_components as html
import emoji

from data import bonanza_sellers
bs = bonanza_sellers()
dff = bs.df


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
        
        dcc.Slider(
            id='year-created-at',
            min=2008,
            max=2019,
            value=2008,
            marks={date: date for date in dff.created_at.unique()}
        ),
        
        
        html.Div(
            className='selections',
            children = [
                html.Div(
                    className='stats-container',
                    children=[
                        html.Table([
                                html.Tr(
                                    className='table-header',
                                    children=[
                                    html.Td(['']),
                                    html.Td([emoji.emojize(':fishing_pole_and_fish: Minnow', use_aliases=True)]),
                                    html.Td([emoji.emojize(':fish: Sea Bass', use_aliases=True)]),
                                    html.Td([emoji.emojize(':dolphin: Dolphin', use_aliases=True)]),
                                    html.Td([emoji.emojize(':whale: Whale', use_aliases=True)]),
                                ]),
                                html.Tr([
                                    html.Td([emoji.emojize(':smile: # of booths', use_aliases=True)]),
                                    html.Td(id='l-minnow-count'),
                                    html.Td(id='l-sea-bass-count'),
                                    html.Td(id='l-dolphin-count'),
                                    html.Td(id='l-whale-count'),
                                    
                                ]),
                                html.Tr([
                                    html.Td([emoji.emojize(':tada: % winning booths', use_aliases=True)]),
                                    html.Td(id='l-minnow-winning'),
                                    html.Td(id='l-sea-bass-winning'),
                                    html.Td(id='l-dolphin-winning'),
                                    html.Td(id='l-whale-winning'),
                                    
                                ]),
                                html.Tr([
                                    html.Td([emoji.emojize(':money_bag: avg profit per seller', use_aliases=True)]),
                                    html.Td(id='l-minnow-dps'),
                                    html.Td(id='l-sea-bass-dps'),
                                    html.Td(id='l-dolphin-dps'),
                                    html.Td(id='l-whale-dps'),
                                    
                                ]),
                                html.Tr([
                                    html.Td([emoji.emojize(':money_bag: median profit per seller', use_aliases=True)]),
                                    html.Td(id='l-minnow-median-dps'),
                                    html.Td(id='l-sea-bass-median-dps'),
                                    html.Td(id='l-dolphin-median-dps'),
                                    html.Td(id='l-whale-median-dps'),
                                    
                                ]),
                            ]),
                        html.P(id='left-winning'),
                        html.P(id='left-value-em'),
                    ]
                ),
                html.Div(
                    className='stats-container',
                    children=[
                        html.Table([
                                html.Tr(
                                    className='table-header',
                                    children=[
                                    html.Td(['']),
                                        html.Td([emoji.emojize(':fishing_pole_and_fish: Minnow', use_aliases=True)]),
                                        html.Td([emoji.emojize(':fish: Sea Bass', use_aliases=True)]),
                                        html.Td([emoji.emojize(':dolphin: Dolphin', use_aliases=True)]),
                                        html.Td([emoji.emojize(':whale: Whale', use_aliases=True)]),
                                    ]),
                                    html.Tr([
                                        html.Td(['%winning booths']),
                                        html.Td([emoji.emojize(':fishing_pole_and_fish: 10%', use_aliases=True)]),
                                        html.Td([emoji.emojize(':fish: 15%', use_aliases=True)]),
                                        html.Td([emoji.emojize(':dolphin: 20%', use_aliases=True)]),
                                        html.Td([emoji.emojize(':whale: 30%', use_aliases=True)]),
                                    ]),
                                ]),
                        html.P(id='right-winning'),
                        html.P(id='right-value-em'),
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
                        html.P(["x:", dcc.Dropdown(id="left_x", options=bs.col_options, value="days_as_user")]),
                        html.P(["y:", dcc.Dropdown(id="left_y", options=bs.col_options, value = "profit_estimate")]),
                        html.P(["color:", dcc.Dropdown(id="left_color", options=bs.col_options, value = "value_em")]),
                    ],   
                ),
                dcc.Graph(
                    className='left-graph',
                    id = 'winning-booths'),
                html.Div(
                    className='right-selection',
                    children=[
                        html.P(["x:", dcc.Dropdown(id="right_x", options=bs.col_options, value = "days_as_user")]),
                        html.P(["y:", dcc.Dropdown(id="right_y", options=bs.col_options, value = "profit_estimate")]),
                        html.P(["color:", dcc.Dropdown(id="right_color", options=bs.col_options, value = "value_em")]),
                    ],
                ),
                dcc.Graph(
                    className='right-graph',
                    id = 'winning-booths2'),
                ]),
        html.Div(id='left_df', style={'display':'none'}),
        html.Div(id='right_df', style={'display':'none'}),
    ],
)