from dash.dependencies import Input, Output
import pandas as pd
import plotly_express as px
from plotly_express import colors
import json
import emoji


from app import app
from data import bonanza_sellers
bs = bonanza_sellers()
df = bs.df

@app.callback([Output('l_category_name', 'children'), Output('r_category_name','children')],
            [Input('left_category','value'),Input('right_category','value')])
def get_category_names(left_name, right_name):
    return str(left_name), str(right_name)

@app.callback(Output('left_df', 'children'), [Input('left_category', 'value')])
def filter_left_df(left_category):
    dff = df[df.category== left_category]
    return dff.to_json(date_format='iso', orient='split')

@app.callback(Output('right_df', 'children'), [Input('right_category', 'value')])
def filter_right_df(right_category):
    dff = df[df.category == right_category]
    return dff.to_json(date_format='iso', orient='split')

#@app.callback(Output())

@app.callback([Output('l-minnow-count','children'),
                Output('l-sea-bass-count','children'),
                Output('l-dolphin-count','children'),
                Output('l-whale-count','children')],
                [Input('left_df', 'children')])
def left_count(value):
    dff = pd.read_json(value, orient='split')
    x = bs.value_em_count(dff)
    return (u'{} {}'.format(emoji.emojize(':fishing_pole_and_fish:', use_aliases=True), x[0]),
        u'{} {}'.format(emoji.emojize(':fish:', use_aliases=True), x[1]),
        u'{} {}'.format(emoji.emojize(':dolphin:', use_aliases=True), x[2]),
        u'{} {}'.format(emoji.emojize(':whale:', use_aliases=True), x[3]))


@app.callback([Output('l-minnow-winning','children'),
                Output('l-sea-bass-winning','children'),
                Output('l-dolphin-winning','children'),
                Output('l-whale-winning','children')],
                [Input('left_df', 'children')])
def left_winning(value):
    dff = pd.read_json(value, orient='split')
    x = bs.value_em_winning(dff)
    return (u'{} {}'.format(emoji.emojize(':fishing_pole_and_fish:', use_aliases=True), x[0]),
        u'{} {}'.format(emoji.emojize(':fish:', use_aliases=True), x[1]),
        u'{} {}'.format(emoji.emojize(':dolphin:', use_aliases=True), x[2]),
        u'{} {}'.format(emoji.emojize(':whale:', use_aliases=True), x[3]))

@app.callback([Output('l-minnow-dps','children'),
                Output('l-sea-bass-dps','children'),
                Output('l-dolphin-dps','children'),
                Output('l-whale-dps','children')],
                [Input('left_df', 'children')])
def left_dps(value):
    dff = pd.read_json(value, orient='split')
    x = bs.value_em_dps(dff)
    return (u'{} {}'.format(emoji.emojize(':fishing_pole_and_fish:', use_aliases=True), x[0]),
        u'{} {}'.format(emoji.emojize(':fish:', use_aliases=True), x[1]),
        u'{} {}'.format(emoji.emojize(':dolphin:', use_aliases=True), x[2]),
        u'{} {}'.format(emoji.emojize(':whale:', use_aliases=True), x[3]))     


@app.callback([Output('l-minnow-median-dps','children'),
                Output('l-sea-bass-median-dps','children'),
                Output('l-dolphin-median-dps','children'),
                Output('l-whale-median-dps','children')],
                [Input('left_df', 'children')])
def left_median_dps(value):
    dff = pd.read_json(value, orient='split')
    x = bs.value_em_median_dps(dff)
    return (u'{} {}'.format(emoji.emojize(':fishing_pole_and_fish:', use_aliases=True), x[0]),
        u'{} {}'.format(emoji.emojize(':fish:', use_aliases=True), x[1]),
        u'{} {}'.format(emoji.emojize(':dolphin:', use_aliases=True), x[2]),
        u'{} {}'.format(emoji.emojize(':whale:', use_aliases=True), x[3]))   

'''Right Seletion'''

@app.callback([Output('r-minnow-count','children'),
                Output('r-sea-bass-count','children'),
                Output('r-dolphin-count','children'),
                Output('r-whale-count','children')],
                [Input('right_df', 'children')])
def right_count(value):
    dff = pd.read_json(value, orient='split')
    x = bs.value_em_count(dff)
    return (u'{} {}'.format(emoji.emojize(':fishing_pole_and_fish:', use_aliases=True), x[0]),
        u'{} {}'.format(emoji.emojize(':fish:', use_aliases=True), x[1]),
        u'{} {}'.format(emoji.emojize(':dolphin:', use_aliases=True), x[2]),
        u'{} {}'.format(emoji.emojize(':whale:', use_aliases=True), x[3]))


@app.callback([Output('r-minnow-winning','children'),
                Output('r-sea-bass-winning','children'),
                Output('r-dolphin-winning','children'),
                Output('r-whale-winning','children')],
                [Input('right_df', 'children')])
def right_winning(value):
    dff = pd.read_json(value, orient='split')
    x = bs.value_em_winning(dff)
    return (u'{} {}'.format(emoji.emojize(':fishing_pole_and_fish:', use_aliases=True), x[0]),
        u'{} {}'.format(emoji.emojize(':fish:', use_aliases=True), x[1]),
        u'{} {}'.format(emoji.emojize(':dolphin:', use_aliases=True), x[2]),
        u'{} {}'.format(emoji.emojize(':whale:', use_aliases=True), x[3]))

@app.callback([Output('r-minnow-dps','children'),
                Output('r-sea-bass-dps','children'),
                Output('r-dolphin-dps','children'),
                Output('r-whale-dps','children')],
                [Input('right_df', 'children')])
def right_dps(value):
    dff = pd.read_json(value, orient='split')
    x = bs.value_em_dps(dff)
    return (u'{} {}'.format(emoji.emojize(':fishing_pole_and_fish:', use_aliases=True), x[0]),
        u'{} {}'.format(emoji.emojize(':fish:', use_aliases=True), x[1]),
        u'{} {}'.format(emoji.emojize(':dolphin:', use_aliases=True), x[2]),
        u'{} {}'.format(emoji.emojize(':whale:', use_aliases=True), x[3]))     


@app.callback([Output('r-minnow-median-dps','children'),
                Output('r-sea-bass-median-dps','children'),
                Output('r-dolphin-median-dps','children'),
                Output('r-whale-median-dps','children')],
                [Input('right_df', 'children')])
def right_median_dps(value):
    dff = pd.read_json(value, orient='split')
    x = bs.value_em_median_dps(dff)
    return (u'{} {}'.format(emoji.emojize(':fishing_pole_and_fish:', use_aliases=True), x[0]),
        u'{} {}'.format(emoji.emojize(':fish:', use_aliases=True), x[1]),
        u'{} {}'.format(emoji.emojize(':dolphin:', use_aliases=True), x[2]),
        u'{} {}'.format(emoji.emojize(':whale:', use_aliases=True), x[3]))  

@app.callback(Output("winning-booths2", "figure"), 
[Input("left_df", "children"),Input("right_df", "children")])
def make_figure2(left_df, right_df):
    left_dff = pd.read_json(left_df, orient='split')
    right_dff = pd.read_json(right_df, orient='split')
    return bs.value_em_profit(left_dff, right_dff)




if __name__ == '__main__':
    print(filter_right_df('fashion'))
    #app.run_server(debug=True)