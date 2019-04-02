import pandas as pd
import plotly_express as px
import plotly.io as pio
import plotly.graph_objs as go


full_df = pd.read_csv("./csv/active_sellers_apr_19.csv")

def set_plotly_template():
    layout = go.Layout(
        title='Figure Title',
        font = dict(size= 14, family='Roboto', color='white'),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        xaxis=dict(
            autorange=True,
            showgrid=False,
        ),
        yaxis=dict(
            autorange=True,
            showgrid=False,
        )
    )
    fig = go.Figure(layout=layout)
    templated_fig = pio.to_templated(fig)
    pio.templates['no_background'] = templated_fig.layout.template
    return 'no_background'

class BonanzaSellers:
    def __init__(self):
        self.df = pd.read_csv("./csv/active_sellers_apr_19.csv")
        self.col_options = [dict(label=x, value=x) for x in self.df.columns]
        self.category_options = [dict(label=x, value=x) for x in self.df.featured_category_id.unique()]
        self.value_em = ["minnow", "sea_bass", "dolphin", "whale"]
        self.template = set_plotly_template()
        self.color_dict = { 'Computers/Tablets & Networking' : '#A6CEE3',
               'Parts & Accessories' : '#1E78B4',
               'Fashion' : '#B2DF8A',
               'Jewelry & Watches' : '#329F2C',
               'a' : '#FB9A99',
               'Home & Garden' : '#E3191B',
               'Sports Mem, Cards & Fan Shop' : '#FDBF6F',
               'Sporting Goods' : '#FF7F00',
               'Health & Beauty' : '#C9B2D6',
               'b' : '#6B3D9A',
               'Other' : '#FFFF99',}


    def min_max_norm(self, values):
        normalized = []
        minimum = min(values)
        maximum = max(values)
        for value in values:
            normalized.append((value-minimum)/(maximum-minimum))
        return normalized

    def sample_sized(self, df):
        size = min(df.groupby(['value_em']).value_em.count())
        dff = []
        for value in self.value_em:
            dff.append(df[df.value_em == value].sample(size))
        return pd.concat(dff)
        

    def value_em_profit(self, df1, df2):
        dff = pd.concat([df1, df2])
        return px.box(
            dff,
            color="featured_category_id",
            y="value_em",
            x="profit_estimate",
            template="no_background",
            points=False,
            log_x=True,
            orientation='h',
            notched=True,
            title='Profit by Seller Value' ,
        )

    def orders_items(self, df1, df2):
        dff = pd.concat([df1, df2])
        dff.amount = dff.amount.fillna(0)
        return px.scatter(
            dff,
            color="featured_category_id",
            y="offers",
            x="days_as_user",
            size='amount',
            template="no_background",
            color_discrete_map = self.color_dict,
            title='Orders for # of Items',
        )


    def __str__(self):
        return '{} - Category Stats'

    def __repr__(self):
        return '{self.__class__.__name__}({self.df})'.format(self==self)



class CategoryTableData:
    def __init__(self, df, value_em):
        self.dff = df[df.value_em==value_em]
        self.value_em = value_em
        self.count = self.dff.seller_id.count()
        self.winning = "{:.1%}".format(sum(self.dff.is_winning)/self.dff.seller_id.count())
        self.dps = '${:,.0f}'.format(self.dff.profit_estimate.sum()/self.dff.seller_id.count())
        self.median_dps = '${:,.0f}'.format(self.dff.profit_estimate.median())
        self.days_as_user = round(self.dff.days_as_user.mean())
        self.first_sale = round(self.dff.days_to_sale.dropna().mean())
        self.orders = round(self.dff.offers.mean())
        self.items = round(self.dff.item_count.mean())
        #self.membership = "{:.0%}".format(self.dff.membership.value_counts()[1]/self.dff.seller_id.count())

    def __str__(self):
        return '{} - Category Stats'.format(' '.join(self.dff.columns[1].split("_")).title())

    def __repr__(self):
        return '{self.__class__.__name__}({self.category})'.format(self==self)


class Facts:
    def __init__(self, df1, df2):
        self.df1 = df1
        self.df2 = df2
        self.num_sellers1 = self.df1.seller_id.count()
        self.num_sellers_width1 = 100
        self.num_sellers2 = self.df2.seller_id.count()
        self.order_value1 = '${:,.0f}'.format(self.df1.order_value.mean())
        self.order_value2 = '${:,.0f}'.format(self.df2.order_value.mean())
        self.num_orders1 = round(self.df1.offers.mean())
        self.num_orders2 = round(self.df2.offers.mean())
        self.fvf_per_seller1 = '${:,.0f}'.format(self.df1.sum_fvf.mean())
        self.fvf_per_seller2 = '${:,.0f}'.format(self.df2.sum_fvf.mean())
        self.gmv_per_seller1 = '${:,.0f}'.format(self.df1.amount.mean())
        self.gmv_per_seller2 = '${:,.0f}'.format(self.df2.amount.mean())





if __name__ == "__main__":
    print(set_plotly_template())
    print(list(pio.templates))
    # cs = CategoryTableData(full_df, 'sea_bass')
    # print(cs.winning)