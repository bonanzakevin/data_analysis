import pandas as pd


class bonanza_sellers:
    def __init__(self):
        self.df = pd.read_csv("./csv/winning_booths_data.csv")
        self.dff = None
        self.col_options = [dict(label=x, value=x) for x in self.df.columns]
        self.category_options = [dict(label=x, value=x) for x in self.df.featured_category_id.unique()]
        self.scatter_dimensions = ["x", "y" , "color" , "df"]
        self.value_em = ["MINNOW", "SEA_BASS", "DOLPHIN", "WHALE"]
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

if __name__ == "__main__":
    bs = bonanza_sellers()
    pass