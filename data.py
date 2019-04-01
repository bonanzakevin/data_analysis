import pandas as pd
import plotly_express as px

full_df = pd.read_csv("./csv/winning_booths_data.csv")

class bonanza_sellers:
    def __init__(self):
        self.df = pd.read_csv("./csv/winning_booths_data.csv")
        self.col_options = [dict(label=x, value=x) for x in self.df.columns]
        self.category_options = [dict(label=x, value=x) for x in self.df.category.unique()]
        self.value_em = ["MINNOW", "SEA_BASS", "DOLPHIN", "WHALE"]

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
            color="category",
            y="value_em",
            x="profit_estimate",
            template="plotly+xgridoff",
            points=False,
            log_x=True,
            orientation='h',
            notched=True,
            title='Profit by Seller Value' ,
        )


    def __str__(self):
        return '{} - Category Stats'

    def __repr__(self):
        return '{self.__class__.__name__}({self.df})'.format(self==self)



class CategoryTableData:
    def __init__(self, df, value_em):
        self.dff = df[df.value_em==value_em]
        self.value_em = value_em
        self.count = self.dff.id.count()
        self.winning = "{:.0%}".format(self.dff.is_winning.value_counts('True')[1])
        self.dps = '${:,.0f}'.format(self.dff.profit_estimate.sum()/self.dff.id.count())
        self.median_dps = '${:,.0f}'.format(self.dff.profit_estimate.median())
        self.days_as_user = round(self.dff.days_as_user.mean())
        self.first_sale = round(self.dff.days_to_sale.mean())
        self.membership = "{:.0%}".format(self.dff.membership.value_counts()[1]/self.dff.id.count())

    
    
    def __str__(self):
        return '{} - Category Stats'.format(' '.join(self.dff.columns[1].split("_")).title())

    def __repr__(self):
        return '{self.__class__.__name__}({self.category})'.format(self==self)


if __name__ == "__main__":
    cs = CategoryTableData(full_df, 'WHALE')
    print(cs.category)