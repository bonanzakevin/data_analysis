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

@app.callback(Output('left_df', 'children'), [Input('left_category', 'value')])
def filter_left_df(left_category):
    dff = df[df.featured_category_id == left_category]
    return dff.to_json(date_format='iso', orient='split')

@app.callback(Output('right_df', 'children'), [Input('right_category', 'value')])
def filter_right_df(right_category):
    dff = df[df.featured_category_id == right_category]
    return dff.to_json(date_format='iso', orient='split')

#@app.callback(Output())
@app.callback([Output('l-minnow-count','children'),
                Output('l-sea-bass-count','children'),
                Output('l-dolphin-count','children'),
                Output('l-whale-count','children')],
                [Input('left_df', 'children')])
def calculate_left_count(value):
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
def calculate_left_winning(value):
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
def calculate_left_dps(value):
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
def calculate_left_meadian_dps(value):
    dff = pd.read_json(value, orient='split')
    x = bs.value_em_median_dps(dff)
    return (u'{} {}'.format(emoji.emojize(':fishing_pole_and_fish:', use_aliases=True), x[0]),
        u'{} {}'.format(emoji.emojize(':fish:', use_aliases=True), x[1]),
        u'{} {}'.format(emoji.emojize(':dolphin:', use_aliases=True), x[2]),
        u'{} {}'.format(emoji.emojize(':whale:', use_aliases=True), x[3]))   



@app.callback(Output('right-winning','children'), [Input('right_df', 'children')])
def calculate_right_winning(value):
    dff = pd.read_json(value, orient='split')
    perc_winning = dff.is_winning.sum()/dff.is_winning.count()
    return u'% winning booths: "{}"'.format(perc_winning)

@app.callback(Output("winning-booths", "figure"), 
[Input("left_df", "children")])
def make_figure(value):
    dff = pd.read_json(value, orient='split')
    return px.violin(
        dff,
        x="featured_category_id",
        y="profit_estimate",
        color='value_em',
        template="plotly",
        height=700,
        points="all",
        log_y=True,
    )

@app.callback(Output("winning-booths2", "figure"), 
[Input("right_x", "children"), Input("right_y", "children"), Input("right_color", "children"), Input("right_df", "children")])
def make_figure2(x,y, color, value):
    dff = pd.read_json(value, orient='split')
    return px.scatter(
        dff,
        x=x,
        y=y,
        color=color,
        template="plotly",
        height=700, 
    )




if __name__ == '__main__':
    print(filter_right_df('fashion'))
    #app.run_server(debug=True)