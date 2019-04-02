import pandas as pd 
import plotly_express as px
poll_info = pd.read_csv('./csv/polls.csv')
poll_data = pd.read_csv('./csv/active_seller_poll_data.csv')

class Polls:
    def __init__(self, id, user_ids):
        self.poll_info = poll_info[poll_info.poll_question_id==id].sort_values('sort_order')
        self.poll_data = poll_data[poll_data.user_id.isin(user_ids)].groupby('poll_question_answer_id').count()
        #self.poll_info['count'] = lambda x: df[df.poll_question_answer_id == x].id[1] for x in poll_info.poll_question_answer_id

    def poll_chart(self, df):
        px.bar(
            df=poll_data
        )

if __name__ == '__main__':
    p = Polls(272,[19422475, 9433507])
    print(p.poll_info)