from dash.dependencies import Input, Output
import pandas as pd
import plotly_express as px
from plotly_express import colors
import json
import emoji
from emojis import Emojis

from app import app
from data import bonanza_sellers, CategoryTableData
bs = bonanza_sellers()
df = bs.df
em = Emojis()

#Choose Categories

@app.callback([Output('l_category_name', 'children'), Output('r_category_name','children')],
            [Input('left_category','value'),Input('right_category','value')])
def get_category_names(left_name, right_name):
    return str(left_name), str(right_name)

#Create Dataframes

@app.callback(Output('left_df', 'children'), [Input('left_category', 'value')])
def filter_left_df(left_category):
    dff = df[df.category== left_category]
    return dff.to_json(date_format='iso', orient='split')

@app.callback(Output('right_df', 'children'), [Input('right_category', 'value')])
def filter_right_df(right_category):
    dff = df[df.category == right_category]
    return dff.to_json(date_format='iso', orient='split')

#Create Tables

@app.callback([Output('l-minnow-count','children'),
                Output('l-minnow-winning','children'),
                Output('l-minnow-dps','children'),
                Output('l-minnow-median-dps','children'),
                Output('l-minnow-days-as-user','children'),
                Output('l-minnow-first-sale','children'),
                Output('l-sea-bass-count','children'),
                Output('l-sea-bass-winning','children'),
                Output('l-sea-bass-dps','children'),
                Output('l-sea-bass-median-dps','children'),
                Output('l-sea-bass-days-as-user','children'),
                Output('l-sea-bass-first-sale','children'),
                Output('l-dolphin-count','children'),
                Output('l-dolphin-winning','children'),
                Output('l-dolphin-dps','children'),
                Output('l-dolphin-median-dps','children'),
                Output('l-dolphin-days-as-user','children'),
                Output('l-dolphin-first-sale','children'),
                Output('l-whale-count','children'),
                Output('l-whale-winning','children'),
                Output('l-whale-dps','children'),
                Output('l-whale-median-dps','children'),
                Output('l-whale-days-as-user','children'),
                Output('l-whale-first-sale','children')],
                [Input('left_df', 'children')])
def left_category_data(value):
    dff = pd.read_json(value, orient='split')
    m = CategoryTableData(dff, 'MINNOW')
    s = CategoryTableData(dff, 'SEA_BASS')
    d = CategoryTableData(dff, 'DOLPHIN')
    w = CategoryTableData(dff, 'WHALE')
    return (u'{} {}'.format(em.minnow, m.count),
        u'{} {}'.format(em.minnow, m.winning),
        u'{} {}'.format(em.minnow, m.dps),
        u'{} {}'.format(em.minnow, m.median_dps),
        u'{} {}'.format(em.minnow, m.days_as_user),
        u'{} {}'.format(em.minnow, m.first_sale),
        u'{} {}'.format(em.sea_bass, s.count),
        u'{} {}'.format(em.sea_bass, s.winning),
        u'{} {}'.format(em.sea_bass, s.dps),
        u'{} {}'.format(em.sea_bass, s.median_dps),
        u'{} {}'.format(em.sea_bass, s.days_as_user),
        u'{} {}'.format(em.sea_bass, s.first_sale),
        u'{} {}'.format(em.dolphin, d.count),
        u'{} {}'.format(em.dolphin, d.winning),
        u'{} {}'.format(em.dolphin, d.dps),
        u'{} {}'.format(em.dolphin, d.median_dps),
        u'{} {}'.format(em.dolphin, d.days_as_user),
        u'{} {}'.format(em.dolphin, d.first_sale),
        u'{} {}'.format(em.whale, w.count),
        u'{} {}'.format(em.whale, w.winning),
        u'{} {}'.format(em.whale, w.dps),
        u'{} {}'.format(em.whale, w.median_dps),
        u'{} {}'.format(em.whale, w.days_as_user),
        u'{} {}'.format(em.whale, w.first_sale))

@app.callback([Output('r-minnow-count','children'),
                Output('r-minnow-winning','children'),
                Output('r-minnow-dps','children'),
                Output('r-minnow-median-dps','children'),
                Output('r-minnow-days-as-user','children'),
                Output('r-minnow-first-sale','children'),
                Output('r-sea-bass-count','children'),
                Output('r-sea-bass-winning','children'),
                Output('r-sea-bass-dps','children'),
                Output('r-sea-bass-median-dps','children'),
                Output('r-sea-bass-days-as-user','children'),
                Output('r-sea-bass-first-sale','children'),
                Output('r-dolphin-count','children'),
                Output('r-dolphin-winning','children'),
                Output('r-dolphin-dps','children'),
                Output('r-dolphin-median-dps','children'),
                Output('r-dolphin-days-as-user','children'),
                Output('r-dolphin-first-sale','children'),
                Output('r-whale-count','children'),
                Output('r-whale-winning','children'),
                Output('r-whale-dps','children'),
                Output('r-whale-median-dps','children'),
                Output('r-whale-days-as-user','children'),
                Output('r-whale-first-sale','children')],
                [Input('right_df', 'children')])
def right_category_data(value):
    dff = pd.read_json(value, orient='split')
    m = CategoryTableData(dff, 'MINNOW')
    s = CategoryTableData(dff, 'SEA_BASS')
    d = CategoryTableData(dff, 'DOLPHIN')
    w = CategoryTableData(dff, 'WHALE')
    return (u'{} {}'.format(em.minnow, m.count),
        u'{} {} {}'.format(em.minnow, m.winning, 'hello'),
        u'{} {}'.format(em.minnow, m.dps),
        u'{} {}'.format(em.minnow, m.median_dps),
        u'{} {}'.format(em.minnow, m.days_as_user),
        u'{} {}'.format(em.minnow, m.first_sale),
        u'{} {}'.format(em.sea_bass, s.count),
        u'{} {}'.format(em.sea_bass, s.winning),
        u'{} {}'.format(em.sea_bass, s.dps),
        u'{} {}'.format(em.sea_bass, s.median_dps),
        u'{} {}'.format(em.sea_bass, s.days_as_user),
        u'{} {}'.format(em.sea_bass, s.first_sale),
        u'{} {}'.format(em.dolphin, d.count),
        u'{} {}'.format(em.dolphin, d.winning),
        u'{} {}'.format(em.dolphin, d.dps),
        u'{} {}'.format(em.dolphin, d.median_dps),
        u'{} {}'.format(em.dolphin, d.days_as_user),
        u'{} {}'.format(em.dolphin, d.first_sale),
        u'{} {}'.format(em.whale, w.count),
        u'{} {}'.format(em.whale, w.winning),
        u'{} {}'.format(em.whale, w.dps),
        u'{} {}'.format(em.whale, w.median_dps),
        u'{} {}'.format(em.whale, w.days_as_user),
        u'{} {}'.format(em.whale, w.first_sale))


#Create Graphs

@app.callback(Output("winning-booths2", "figure"), 
[Input("left_df", "children"),Input("right_df", "children")])
def make_figure2(left_df, right_df):
    left_dff = pd.read_json(left_df, orient='split')
    right_dff = pd.read_json(right_df, orient='split')
    return bs.value_em_profit(left_dff, right_dff)




if __name__ == '__main__':
    print(filter_right_df('fashion'))
    #app.run_server(debug=True)



