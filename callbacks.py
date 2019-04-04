from dash.dependencies import Input, Output
import pandas as pd
import plotly_express as px
from plotly_express import colors
import json
import emoji
from emojis import Emojis

from app import app
from data import BonanzaSellers, CategoryTableData, Facts

bs = BonanzaSellers()
df = bs.df
em = Emojis()

#Choose Categories

@app.callback([Output('l_category_name', 'children'), Output('r_category_name','children'),
            Output('l_category_name', 'style'), Output('r_category_name','style')],
            [Input('left_category','value'),Input('right_category','value')])
def get_category_names(left_name, right_name):
    l_color, r_color = None, None
    for key, value in bs.color_dict.items():
        if left_name == key:
            l_color = value
        elif right_name == key:
            r_color = value
    return str(left_name), str(right_name), {'color': l_color}, {'color': r_color}

#Create Dataframes

@app.callback(Output('left_df', 'children'), [Input('left_category', 'value')])
def filter_left_df(left_category):
    dff = df[df.featured_category_id == left_category]
    return dff.to_json(date_format='iso', orient='split')

@app.callback(Output('right_df', 'children'), [Input('right_category', 'value')])
def filter_right_df(right_category):
    dff = df[df.featured_category_id == right_category]
    return dff.to_json(date_format='iso', orient='split')

@app.callback([Output('left-num-sellers', 'children'),
            Output('right-num-sellers', 'children'),
            Output('left-order-value', 'children'),
            Output('right-order-value', 'children'),
            Output('left-num-orders', 'children'),
            Output('right-num-orders', 'children'),
            Output('left-fvf-per-seller', 'children'),
            Output('right-fvf-per-seller', 'children'),
            Output('left-gmv-per-seller', 'children'),
            Output('right-gmv-per-seller', 'children')], 
            [Input('left_df','children'),
            Input('right_df','children')])
def fact_one(left_df, right_df):
    left_dff = pd.read_json(left_df, orient='split')
    right_dff = pd.read_json(right_df, orient='split')
    f = Facts(left_dff, right_dff)
    return (u'{}'.format(f.num_sellers1),
            u'{}'.format(f.num_sellers2),
            u'{}'.format(f.order_value1),
            u'{}'.format(f.order_value2),
            u'{}'.format(f.num_orders1),
            u'{}'.format(f.num_orders2),
            u'{}'.format(f.fvf_per_seller1),
            u'{}'.format(f.fvf_per_seller2),
            u'{}'.format(f.gmv_per_seller1),
            u'{}'.format(f.gmv_per_seller2))
    

#Create Tables

@app.callback([Output('l-minnow-count','children'),
                Output('l-minnow-winning','children'),
                Output('l-minnow-dps','children'),
                Output('l-minnow-median-dps','children'),
                Output('l-minnow-days-as-user','children'),
                Output('l-minnow-first-sale','children'),
                Output('l-minnow-orders','children'),
                Output('l-minnow-items','children'),
                Output('l-sea-bass-count','children'),
                Output('l-sea-bass-winning','children'),
                Output('l-sea-bass-dps','children'),
                Output('l-sea-bass-median-dps','children'),
                Output('l-sea-bass-days-as-user','children'),
                Output('l-sea-bass-first-sale','children'),
                Output('l-sea-bass-orders','children'),
                Output('l-sea-bass-items','children'),
                Output('l-dolphin-count','children'),
                Output('l-dolphin-winning','children'),
                Output('l-dolphin-dps','children'),
                Output('l-dolphin-median-dps','children'),
                Output('l-dolphin-days-as-user','children'),
                Output('l-dolphin-first-sale','children'),
                Output('l-dolphin-orders','children'),
                Output('l-dolphin-items','children'),
                Output('l-whale-count','children'),
                Output('l-whale-winning','children'),
                Output('l-whale-dps','children'),
                Output('l-whale-median-dps','children'),
                Output('l-whale-days-as-user','children'),
                Output('l-whale-first-sale','children'),
                Output('l-whale-orders','children'),
                Output('l-whale-items','children')],
                [Input('left_df', 'children')])
def left_category_data(value):
    dff = pd.read_json(value, orient='split')
    m = CategoryTableData(dff, 'minnow')
    s = CategoryTableData(dff, 'sea_bass')
    d = CategoryTableData(dff, 'dolphin')
    w = CategoryTableData(dff, 'whale')
    return (
            u'{} {}'.format(em.minnow, m.count),
            u'{} {}'.format(em.minnow, m.winning),
            u'{} {}'.format(em.minnow, m.dps),
            u'{} {}'.format(em.minnow, m.median_dps),
            u'{} {}'.format(em.minnow, m.days_as_user),
            u'{} {}'.format(em.minnow, m.first_sale),
            u'{} {}'.format(em.minnow, m.orders),
            u'{} {}'.format(em.minnow, m.items),
            u'{} {}'.format(em.sea_bass, s.count),
            u'{} {}'.format(em.sea_bass, s.winning),
            u'{} {}'.format(em.sea_bass, s.dps),
            u'{} {}'.format(em.sea_bass, s.median_dps),
            u'{} {}'.format(em.sea_bass, s.days_as_user),
            u'{} {}'.format(em.sea_bass, s.first_sale),
            u'{} {}'.format(em.sea_bass, s.orders),
            u'{} {}'.format(em.sea_bass, s.items),
            u'{} {}'.format(em.dolphin, d.count),
            u'{} {}'.format(em.dolphin, d.winning),
            u'{} {}'.format(em.dolphin, d.dps),
            u'{} {}'.format(em.dolphin, d.median_dps),
            u'{} {}'.format(em.dolphin, d.days_as_user),
            u'{} {}'.format(em.dolphin, d.first_sale),
            u'{} {}'.format(em.dolphin, d.orders),
            u'{} {}'.format(em.dolphin, d.items),
            u'{} {}'.format(em.whale, w.count),
            u'{} {}'.format(em.whale, w.winning),
            u'{} {}'.format(em.whale, w.dps),
            u'{} {}'.format(em.whale, w.median_dps),
            u'{} {}'.format(em.whale, w.days_as_user),
            u'{} {}'.format(em.whale, w.first_sale),
            u'{} {}'.format(em.whale, w.orders),
            u'{} {}'.format(em.whale, w.items))

@app.callback([Output('r-minnow-count','children'),
                Output('r-minnow-winning','children'),
                Output('r-minnow-dps','children'),
                Output('r-minnow-median-dps','children'),
                Output('r-minnow-days-as-user','children'),
                Output('r-minnow-first-sale','children'),
                Output('r-minnow-orders','children'),
                Output('r-minnow-items','children'),
                Output('r-sea-bass-count','children'),
                Output('r-sea-bass-winning','children'),
                Output('r-sea-bass-dps','children'),
                Output('r-sea-bass-median-dps','children'),
                Output('r-sea-bass-days-as-user','children'),
                Output('r-sea-bass-first-sale','children'),
                Output('r-sea-bass-orders','children'),
                Output('r-sea-bass-items','children'),
                Output('r-dolphin-count','children'),
                Output('r-dolphin-winning','children'),
                Output('r-dolphin-dps','children'),
                Output('r-dolphin-median-dps','children'),
                Output('r-dolphin-days-as-user','children'),
                Output('r-dolphin-first-sale','children'),
                Output('r-dolphin-orders','children'),
                Output('r-dolphin-items','children'),
                Output('r-whale-count','children'),
                Output('r-whale-winning','children'),
                Output('r-whale-dps','children'),
                Output('r-whale-median-dps','children'),
                Output('r-whale-days-as-user','children'),
                Output('r-whale-first-sale','children'),
                Output('r-whale-orders','children'),
                Output('r-whale-items','children')],
                [Input('right_df', 'children')])
def right_category_data(value):
    dff = pd.read_json(value, orient='split')
    m = CategoryTableData(dff, 'minnow')
    s = CategoryTableData(dff, 'sea_bass')
    d = CategoryTableData(dff, 'dolphin')
    w = CategoryTableData(dff, 'whale')
    return (u'{} {}'.format(em.minnow, m.count),
        u'{} {}'.format(em.minnow, m.winning),
        u'{} {}'.format(em.minnow, m.dps),
        u'{} {}'.format(em.minnow, m.median_dps),
        u'{} {}'.format(em.minnow, m.days_as_user),
        u'{} {}'.format(em.minnow, m.first_sale),
        u'{} {}'.format(em.minnow, m.orders),
        u'{} {}'.format(em.minnow, m.items),
        u'{} {}'.format(em.sea_bass, s.count),
        u'{} {}'.format(em.sea_bass, s.winning),
        u'{} {}'.format(em.sea_bass, s.dps),
        u'{} {}'.format(em.sea_bass, s.median_dps),
        u'{} {}'.format(em.sea_bass, s.days_as_user),
        u'{} {}'.format(em.sea_bass, s.first_sale),
        u'{} {}'.format(em.sea_bass, s.orders),
        u'{} {}'.format(em.sea_bass, s.items),
        u'{} {}'.format(em.dolphin, d.count),
        u'{} {}'.format(em.dolphin, d.winning),
        u'{} {}'.format(em.dolphin, d.dps),
        u'{} {}'.format(em.dolphin, d.median_dps),
        u'{} {}'.format(em.dolphin, d.days_as_user),
        u'{} {}'.format(em.dolphin, d.first_sale),
        u'{} {}'.format(em.dolphin, d.orders),
        u'{} {}'.format(em.dolphin, d.items),
        u'{} {}'.format(em.whale, w.count),
        u'{} {}'.format(em.whale, w.winning),
        u'{} {}'.format(em.whale, w.dps),
        u'{} {}'.format(em.whale, w.median_dps),
        u'{} {}'.format(em.whale, w.days_as_user),
        u'{} {}'.format(em.whale, w.first_sale),
        u'{} {}'.format(em.whale, w.orders),
        u'{} {}'.format(em.whale, w.items))


#Create Graphs

@app.callback(Output("orders-items", "figure"), 
[Input("left_df", "children"),Input("right_df", "children")])
def make_orders_items(left_df, right_df):
    left_dff = pd.read_json(left_df, orient='split')
    right_dff = pd.read_json(right_df, orient='split')
    return bs.orders_items(left_dff, right_dff)

@app.callback(Output("winning-booths2", "figure"), 
[Input("left_df", "children"),Input("right_df", "children")])
def make_value_em_profit(left_df, right_df):
    left_dff = pd.read_json(left_df, orient='split')
    right_dff = pd.read_json(right_df, orient='split')
    return bs.value_em_profit(left_dff, right_dff)




if __name__ == '__main__':
    print(filter_right_df('fashion'))
    #app.run_server(debug=True)



