from crypto_news_api import CryptoControlAPI
from pandas.io.json import json_normalize

api = CryptoControlAPI("4472c2e079ab562dd00f6ebb5dc6d64f")

# get top news in Chinese
top_news = json_normalize(api.getTopNews("cn"))
print(top_news)
print(top_news['title'])

# get latest news
lat_news = json_normalize(api.getLatestNews())
print(lat_news)
print(lat_news['title'])

# get top news by category
top_news_cat = json_normalize(api.getTopNewsByCategory())
top_news_analysis = json_normalize(top_news_cat['analysis'][0])
print(top_news_analysis['title'])
top_news_ico = json_normalize(top_news_cat['ico'][0])
print(top_news_ico['title'])

# get top news by coin
top_news_btc = json_normalize(api.getTopNewsByCoin("bitcoin"))
print(top_news_btc)
print(top_news_btc['title'])

# get latest news by coin
lat_news_btc = json_normalize(api.getLatestNewsByCoin("bitcoin", language = 'cn'))
print(lat_news_btc)
print(lat_news_btc['title'])

# get top news by coin category
top_news_coincat = json_normalize(api.getTopNewsByCoinCategory('bitcoin'))
print(top_news_coincat)
print(top_news_coincat['title'])

# get top reddit post by coin
top_red_coin = json_normalize(api.getTopRedditPostsByCoin('bitcoin'))
print(top_red_coin)
print(top_red_coin['title'])

# get latest reddit post by coin
lat_red_coin = json_normalize(api.getLatestRedditPostsByCoin('bitcoin'))
print(lat_red_coin)
print(lat_red_coin['title'])

# get top tweets by coin
top_tw_coin = json_normalize(api.getTopTweetsByCoin("eos"))
print(top_tw_coin)
print(top_tw_coin['text'])

# get latest tweets by coin
lat_tw_coin = json_normalize(api.getLatestTweetsByCoin("eos"))
print(lat_tw_coin)
print(lat_tw_coin['text'])

# get top feed by coin
top_feed_coin = json_normalize(api.getTopFeedByCoin("neo"))
print(top_feed_coin)

# get latest feed by coin
lat_feed_coin = json_normalize(api.getLatestFeedByCoin("neo"))
print(lat_feed_coin)

# get top items by coin
top_item_coin = json_normalize(api.getTopItemsByCoin("litecoin"))
print(top_item_coin)

# get latest items by coin
lat_item_coin = json_normalize(api.getLatestItemsByCoin("litecoin"))
print(lat_item_coin)

# get coin details
coin_detail = json_normalize(api.getCoinDetails("ethereum"))
print(coin_detail)
print(coin_detail['description'][0])