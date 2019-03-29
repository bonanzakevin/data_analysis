from dash.dependencies import Input, Output
import pandas as pd
import plotly_express as px
from plotly_express import colors
import json

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

@app.callback(Output('left-winning','children'), [Input('left_df', 'children')])
def calculate_left_winning(value):
    dff = pd.read_json(value, orient='split')
    perc_winning = dff[dff.is_winning == True].is_winning.count()/dff.is_winning.count()
    return u'% winning booths: "{}"'.format(perc_winning)

@app.callback(Output('right-winning','children'), [Input('right_df', 'children')])
def calculate_right_winning(value):
    dff = pd.read_json(value, orient='split')
    perc_winning = dff[dff.is_winning == True].is_winning.count()/dff.is_winning.count()
    return u'% winning booths: "{}"'.format(perc_winning)

@app.callback(Output("winning-booths", "figure"), [Input("left_"+d, "value") for d in bs.scatter_dimensions])
def make_figure(x,y, color, left_df):
    dff = pd.read_json(left_df, orient='split')
    return px.scatter(
        dff,
        x=x,
        y=y,
        color=color,
        template="plotly_dark",
        height=700,
    )

@app.callback(Output("winning-booths2", "figure"), [Input("right_"+d, "value") for d in bs.scatter_dimensions])
def make_figure2(x,y, color, right_df):
    dff = pd.read_json(right_df, orient='split')
    return px.scatter(
        dff,
        x=x,
        y=y,
        color=color,
        template="plotly_dark",
        height=700, 
    )


# @app.callback(Output("dic", "figure"), [Input("left_"+d, "value") for d in bs.scatter_dimensions])
# def make_figure(x,y, color, facet_col, facet_row, left_df):
#     dff = pd.read_json(left_df, orient='split')
#     return px.scatter(
#         dff,
#         x=x,
#         y=y,
#         color=color,
#         facet_col=facet_col,
#         facet_row=facet_row,
#         height=700,
#     )

# @app.callback(Output("winning booths2", "figure"), [Input("right_"+d, "value") for d in bs.scatter_dimensions])
# def make_figure2(x,y, color, facet_col, facet_row, right_df):
#     dff = pd.read_json(right_df, orient='split')
#     return px.scatter(
#         dff,
#         x=x,
#         y=y,
#         color=color,
#         facet_col=facet_col,
#         facet_row=facet_row,
#         height=700,
#     )



if __name__ == '__main__':
    print(filter_right_df('fashion'))
    #app.run_server(debug=True)