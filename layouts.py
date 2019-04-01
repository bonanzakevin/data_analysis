import dash_core_components as dcc
import dash_html_components as html
import emoji

from data import bonanza_sellers
bs = bonanza_sellers()
dff = bs.df

#Header

bonanza_sellers = html.Div(
    children=[
        html.Div(
            className="header",
            children=[
                html.Img(className='logo', src='https://assets.bonanzastatic.com/images/header/bonanza_logo_no_tag@2x.png?1550523204'),
                html.Div(
                    className="selections",
                    children=[
                        html.Div(
                            className='top-selections',
                            children=[
                                html.P([dcc.Dropdown(id="left_category", options=bs.category_options, value='fashion')])
                            ],
                        ),
                        
                        html.Div(
                            className='top-selections',
                            children=[
                                html.P([dcc.Dropdown(id="right_category", options=bs.category_options, value='parts_accessories')])
                            ],
                            
                        ),
                    ]
                ),
                html.P('Updated: Apr 1'),
                
                dcc.Slider(
                    id='year-created-at',
                    min=2008,
                    max=2019,
                    value=2008,
                    marks={date: date for date in dff.created_at.unique()}
                ),
            ]),
        
        html.Div(
            className='name-bar',
            children=[
                html.Div(
                    className='category-name',
                    children=[
                        html.P(id='l_category_name')
                    ]
                ),
                html.Div(
                    className='category-name',
                    children=[
                        html.P(id='r_category_name')
                    ]
                ),
            ]
        ),
        
        
#Left Table
        html.Div(
            className='tables',
            children = [
                html.Div(
                    className='table',
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

#Right Table
                html.Div(
                    className='table',
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
                                    html.Td(id='r-minnow-count'),
                                    html.Td(id='r-sea-bass-count'),
                                    html.Td(id='r-dolphin-count'),
                                    html.Td(id='r-whale-count'),
                                    
                                ]),
                                html.Tr([
                                    html.Td([emoji.emojize(':tada: % winning booths', use_aliases=True)]),
                                    html.Td(id='r-minnow-winning'),
                                    html.Td(id='r-sea-bass-winning'),
                                    html.Td(id='r-dolphin-winning'),
                                    html.Td(id='r-whale-winning'),
                                    
                                ]),
                                html.Tr([
                                    html.Td([emoji.emojize(':money_bag: avg profit per seller', use_aliases=True)]),
                                    html.Td(id='r-minnow-dps'),
                                    html.Td(id='r-sea-bass-dps'),
                                    html.Td(id='r-dolphin-dps'),
                                    html.Td(id='r-whale-dps'),
                                    
                                ]),
                                html.Tr([
                                    html.Td([emoji.emojize(':money_bag: median profit per seller', use_aliases=True)]),
                                    html.Td(id='r-minnow-median-dps'),
                                    html.Td(id='r-sea-bass-median-dps'),
                                    html.Td(id='r-dolphin-median-dps'),
                                    html.Td(id='r-whale-median-dps'),
                                    
                                ]),
                            ]),
                        html.P(id='right-winning'),
                        html.P(id='right-value-em'),
                    ]
                ),
            ]),



#Box Chart
        html.Div(
            className='box-chart',
            children=[
                dcc.Graph(
                    id = 'winning-booths2'),
                ]),
        html.Div(id='left_df', style={'display':'none'}),
        html.Div(id='right_df', style={'display':'none'}),


#Left Table
        html.Div(
            className='tables',
            children = [
                html.Div(
                    className='table',
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
                                    html.Td([emoji.emojize(':smile: # of days as user', use_aliases=True)]),
                                    html.Td(id='l-minnow-days-as-user'),
                                    html.Td(id='l-sea-bass-days-as-user'),
                                    html.Td(id='l-dolphin-days-as-user'),
                                    html.Td(id='l-whale-days-as-user'),
                                    
                                ]),
                                html.Tr([
                                    html.Td([emoji.emojize(':tada: # of days to first sale', use_aliases=True)]),
                                    html.Td(id='l-minnow-first-sale'),
                                    html.Td(id='l-sea-bass-first-sale'),
                                    html.Td(id='l-dolphin-first-sale'),
                                    html.Td(id='l-whale-first-sale'),
                                    
                                ]),
                                html.Tr([
                                    html.Td([emoji.emojize(':money_bag: # of orders', use_aliases=True)]),
                                    html.Td(id='l-minnow-orders'),
                                    html.Td(id='l-sea-bass-orders'),
                                    html.Td(id='l-dolphin-orders'),
                                    html.Td(id='l-whale-orders'),
                                    
                                ]),
                                html.Tr([
                                    html.Td([emoji.emojize(':money_bag: # of items', use_aliases=True)]),
                                    html.Td(id='l-minnow-items'),
                                    html.Td(id='l-sea-bass-items'),
                                    html.Td(id='l-dolphin-items'),
                                    html.Td(id='l-whale-items'),
                                    
                                ]),
                            ]),
                        html.P(id='left-winning'),
                        html.P(id='left-value-em'),
                    ]
                ),
            ]),

#Right Table
        html.Div(
            className='tables',
            children = [
                html.Div(
                    className='table',
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
                                    html.Td([emoji.emojize(':smile: # of days as user', use_aliases=True)]),
                                    html.Td(id='r-minnow-days-as-user'),
                                    html.Td(id='r-sea-bass-days-as-user'),
                                    html.Td(id='r-dolphin-days-as-user'),
                                    html.Td(id='r-whale-days-as-user'),
                                    
                                ]),
                                html.Tr([
                                    html.Td([emoji.emojize(':tada: # of days to first sale', use_aliases=True)]),
                                    html.Td(id='r-minnow-first_sale'),
                                    html.Td(id='r-sea-bass-first-sale'),
                                    html.Td(id='r-dolphin-first-sale'),
                                    html.Td(id='r-whale-first-sale'),
                                    
                                ]),
                                html.Tr([
                                    html.Td([emoji.emojize(':money_bag: # of orders', use_aliases=True)]),
                                    html.Td(id='r-minnow-orders'),
                                    html.Td(id='r-sea-bass-orders'),
                                    html.Td(id='r-dolphin-orders'),
                                    html.Td(id='r-whale-orders'),
                                    
                                ]),
                                html.Tr([
                                    html.Td([emoji.emojize(':money_bag: # of items', use_aliases=True)]),
                                    html.Td(id='r-minnow-items'),
                                    html.Td(id='r-sea-bass-items'),
                                    html.Td(id='r-dolphin-items'),
                                    html.Td(id='r-whale-items'),
                                    
                                ]),
                            ]),
                        html.P(id='right-winning'),
                        html.P(id='right-value-em'),
                    ]
                ),
        

        ])
    ])
