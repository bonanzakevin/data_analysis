import pandas as pd


class bonanza_sellers:
    def __init__(self):
        self.df = pd.read_csv("./csv/winning_booths_data.csv")
        self.col_options = [dict(label=x, value=x) for x in self.df.columns]
        self.category_options = [dict(label=x, value=x) for x in self.df.featured_category_id.unique()]
        self.scatter_dimensions = ["x", "y", "color", "df"]

if __name__ == "__main__":
    bs = bonanza_sellers()
    pass