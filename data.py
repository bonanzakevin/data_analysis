import pandas as pd
import plotly_express as px

full_df = pd.read_csv("./csv/winning_booths_data.csv")

class bonanza_sellers:
    def __init__(self):
        self.df = pd.read_csv("./csv/winning_booths_data.csv")
        self.col_options = [dict(label=x, value=x) for x in self.df.columns]
        self.category_options = [dict(label=x, value=x) for x in self.df.category.unique()]
        self.scatter_dimensions = ["x", "y" , "color" , "df"]
        self.value_em = ["MINNOW", "SEA_BASS", "DOLPHIN", "WHALE"]
        self.value_em_small = ["minnow", "sea_bass", "dolphin", "whale"]
        self.value_emojis = {"MINNOW":":fishing_pole_and_fish:",
                            "SEA_BASS":":fish:",
                            "DOLPHIN":":dolphin:",
                            "WHALE":":whale:"}

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
        

    def value_em_count(self, df):
        count_winning = []
        for value in self.value_em:
            count_winning.append(df[df.value_em==value].id.count())
        return count_winning

    def value_em_winning(self, df):
        percent_winning = []
        for value in self.value_em:
            percent_winning.append(format(df[df.value_em==value].is_winning.value_counts('True')[1], ".0%"))
        return percent_winning

    def value_em_dps(self, df):
        dollars_per_seller = []
        for value in self.value_em:
            dff = df[df.value_em==value]
            dollars_per_seller.append('${:,.0f}'.format(dff.profit_estimate.sum()/dff.id.count()))
        return dollars_per_seller
    
    def value_em_median_dps(self, df):
        median_dollars_per_seller = []
        for value in self.value_em:
            dff = df[df.value_em==value]
            median_dollars_per_seller.append('${:,.0f}'.format(dff.profit_estimate.median()))
        return median_dollars_per_seller

    def value_em_with_membership(self,df):
        with_membership = []
        for value in self.value_em:
            dff = df[df.value_em==value]
            with_membership.append(dff.membership.value_counts()[1]/dff.id.count())
        return with_membership
        

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



#It would be better to create a class and set the data so that I can just call left = CategoryStats(left_category)
# this should give an array of values? I'm not sure that is the best thing to return. 

#I want this class to hold all of the data, but where is it going to hold it? 
# As soon as the function runs again everything is lost.
#In the long term I want to store the calculations in a db so that I don't need to recalculate each time. 
# I would only calculate when uploading a new csv.

#For now I should have each callback load the full side, so that the first side loads then the second. 
# This function should reload all of the stats each time a new category is selected

class CategoryStats:
    def __init__(self, category):
        self.category = category
        self.df = full_df[full_df.category == category]
        self.value_em = ["MINNOW", "SEA_BASS", "DOLPHIN", "WHALE"]
        self.value_em_count = None


    def value_em_count(self, df):
        count_winning = []
        for value in self.value_em:
            count_winning.append(df[df.value_em==value].id.count())
        return count_winning


    def __str__(self):
        return '{} - Category Stats'.format(' '.join(self.category.split("_")).title())

    def __repr__(self):
        return '{self.__class__.__name__}({self.category})'.format(self==self)


if __name__ == "__main__":
    cs = CategoryStats('parts_accessories')
    print(cs)