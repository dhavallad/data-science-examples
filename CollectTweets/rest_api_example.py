__author__ = "Dhava Lad"


import twitter, sys, json
from pattern.en import positive

reload(sys)
sys.setdefaultencoding("utf-8")

myApi=twitter.Api(consumer_key ='Enter consumer key',
                  consumer_secret='Enter consumer secret',
                  access_token_key='Enter access token key',
                  access_token_secret='Enter access token secret')

def randomsample():
    geo = ('32.7864', '-79.9408', '200mi')
    raw_tweets = myApi.GetSearch(None,geo,count = 100)
    output_text = open('Random_tweet.txt', 'w')
    # output_ID = open('Random_tweet_ID.txt', 'w')
    MAX_ID = None
    for it in range(8):
        tweets = [json.loads(str(raw_tweet)) for raw_tweet \
                  in myApi.GetSearch(None, geo, count = 100, max_id = MAX_ID)]
        for raw_t in tweets:
            output_text.write(str(raw_t['text'])+"\n")
            # output_ID.write(str(raw_t['id'])+"\n")
        # output_file.write(str(raw_tweet)+"\n")
        # print raw_tweet
        if tweets:
            MAX_ID = tweets[-1]['id']
         
def main():
    
    randomsample()
    
if __name__ == '__main__':
    main()
    
