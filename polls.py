import pandas as pd 
import numpy as np
import plotly_express as px
from plotly.tools import mpl_to_plotly
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import dash_core_components as dcc
import plotly.tools as tls

dummy_data = "We are distributors in Portugal - we sell for shops Craigslist background burner Barnes & Noble and other outlets trying to grow Walmart Website shopify My website Just trying different site Websites Salehho Craig's List Sold shopping carts now I have clothing with large assortment have small store on bonanza decided to import amazon listings as well Ebay boot for no reason maxed out on ebay limits $6,000  No upfront fees Skip McGrath aliexpress eBid ebay sucks Alternative to Amazon My own Website website websites Amazon and Ebay cost too much and are too complicated Alibaba DSD Alternate to Ebay My website Website www.sharafiandco.com None yet,  just starting Shopify website First seeing Bonanzle around the Web, then seeing the change to Bonanza, and remembering the name. Can't answer this because I can't produce, list and market on any type of regular schedule at this time. I sell on Etsy and was looking for an additional venue and found Bonanza through the Etsy forum My own online store my own website Started as a hobby and beauty in the house. military bases craigslist Resellers on instagram Mercari I received an inquiry from Bonanza asking me to join Shopify website As much as possible my own site needed an alternative to declining eBay sales and high selling fees word of mouth in-person sales word of mouth and craft shows not sure Tradesy expanding Allegro instagram offer.up craigslist did not have any sale yet Due walmart Our website Will evaluate monthley email Found a competitor on Bonanaza I don't know how much traffic you get, I'm hoping $2001+ Paypal recommend Storenvy 10,000+ my own website I am a new seller Direct from my website walmart groupon online store YouTube Currently on E-bay, and their platform is not functioning properly for months.  Looking for another platform. DHgate Wish Traffic and Alexa A different venue Letgo Used to sell when you first began. Was a life member or Platinum but had to stop on line for a few years. PP sold on here before....Ebay is too expensive...they don't support sellers very well..Etsy is dead Not happy with Tophatter Tophatter don't know as much as I can make Unsure. I would like to sell $100 a week. I was looking for a specific item for myself and found it on for sale on bonanza Own Experience While searching google for a item, found one cheaper on bonanza. Read information about selling on bonanza and compare to e-bay. Decided to try selling on bonanza because of better final value cost. Pay-pale buttons Google searching alternatives to ebay a Houzz, Overstock slow eBay sales display in beauty shop local market 10,000 + word of mouth Pricing structure Half.com ebay's new policies and bots that make it hard to interact with people without violating something. Plus, their fees are constantly growing, while the site's systems and design are outdated. 6000 www.libex.ru lazada indonesia NEEDED A STORE/BOOTH TO SELL ITEMS ONLINE 24/7 AS EBAY ONLY GIVES YOU A FEW FREE PROMOTIONAL LISTINGS.  WE ALSO HAVE 2 OTHER ONLINE WEBSTORES, BUT DON'T SELL MUCH ON THOSE. Heard about it on Scavenger Life on Youtube ss.com i was a previous seller, Ebay sales have dropped dramatically offline just started selling More income Extremely unhappy with EBay and their policies and precedures. Looking for other medium and formats friends E Experimentation, seeking to not be reliant on the big A tradera facebook group recommendation DS Problems with other sites I've been watching Bonanza and it was time $5+ Ecommercebytes.com dissatisfied with Ebay Ebay would not let me list Enfamil brand Baby Formulas in cans eCrater Ebay isnt what it used to be. Info I found on AnthingSportsman.com, I think. P prefer not to say HI Looking for additional venues and fed up with eBay aiming to meet and exceed eBay sales of $10,000/mo friend found it, then I did online research Unhappy with the fees on eBay, especially store rate increases mid-year. Rakuten Ecommerce Bytes I have another Bonanza booth where I sell a  little bit of everything and Really like it. Wayfair PINTEREST I use bonannza for my IT business and sales of Anti-virus and related products and services SCAVENGER LIFE Yard Sale Expand to other platforms 100000 I SaleHoo YouTube video + Facebook friends Just started - new It was one of my options with Novatech Dropshipping. Unhappy with Etsy. the same, the better Trying out to see if its worth investing in Depends on sells Haven't sold anything yet. Ebay limits me to 10 listings. I'm a beginner and I tried Ebay but the suspend my account after 2hrs..without telling why. So I searched for ebay alternative and found you Comments from Etsy Forum Questions. Instagram Site looks better than Ebay No preconceived expectations Spotify I. Person I have  bought from Bonanza and liked  what I saw. None Poor search results & poor sales for my ebay listings (Collectibles) None was kicket out from eba No idea, possibly 10‚Äôs of thousands if this turns out to be a viable seller supportive service and not just a money grab. Amazon sales are down so we're trying to supplement them TopHatter.com $20,000+ Livingston country sell it Web search after being badly treated dissatisfied with Ebay afer 18 years with them Declampe for stamps and Ebid Yessy Disatisfaction with other platforms I like the platform Purchase here old five or more year a three hands bags and try selling then, gave up because I was working full time. Ebay alternatives Ebay's 2019 Sping Seller Update (read it and weap). dropship town Poshmark"

poll_info = pd.read_csv('./csv/polls.csv')
poll_data = pd.read_csv('./csv/active_seller_poll_data.csv')

class Polls:
    def __init__(self, id, user_ids):
        self.poll_info = poll_info[poll_info.poll_question_id==id].sort_values('sort_order')
        self.poll_data = poll_data[poll_data.user_id.isin(user_ids)].groupby('poll_question_answer_id').count()
        #self.poll_info['count'] = lambda x: df[df.poll_question_answer_id == x].id[1] for x in poll_info.poll_question_answer_id
        self.stopwords = set(STOPWORDS)


class CreateWordCloud:
    def __init__(self,df):
        self.words = df.freeform_response.dropna()
        self.mask = np.array(Image.open(r"./assets/bonz_b.png"))
        self.stopwords = set(STOPWORDS)
        self.stopwords.update(["website", "found", "site", "much", "looking", "trying"])

    def get_text(self):
        array = []
        for i in self.words.values:
            array += i.split(' ')
        return ' '.join(array)

    def create_plot(self, text):
        image_colors = ImageColorGenerator(self.mask)
        wordcloud = WordCloud(
            stopwords=self.stopwords, 
            background_color='rgba(0,0,0,0)',
            mode="RGBA", 
            max_words=200, 
            mask=self.mask).generate(text)
        plt.figure(figsize=(10,10))
        plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation='bilinear')
        plt.savefig("../assets/bonz_word_cloud.png", format="png")
        



if __name__ == '__main__':
    p = CreateWordCloud(poll_data)
    print(p.create_plot(dummy_data))