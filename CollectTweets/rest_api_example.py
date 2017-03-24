__author__ = "Dhava Lad"


import twitter, sys, json
from pattern.en import positive

reload(sys)
sys.setdefaultencoding("utf-8")

myApi=twitter.Api(consumer_key ='ENTER YOUR COSUMER KEY',
                  consumer_secret='ENTER YOUR COSUMER SECRET',
                  access_token_key='ENTER YOUR ACCESS TOKEN KEY',
                  access_token_secret='ENTER YOUR ACCESS TOKEN SECRET')

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
         
def mainquery():
    query = '(Trump OR Cruz OR President OR news OR donald OR victory OR atlanta OR wins OR wons OR supporter OR america OR winner)'  
    geo = ('40.7127', '-74.0059', '600mi') # New York City
    MAX_ID = None
    output_text = open('MainData.txt', 'w')
    # output_ID = open('MainData_ID.txt', 'w')
    for it in range(5): # Retrieve up to 200 tweets
        tweets = [json.loads(str(raw_tweet)) for raw_tweet \
                  in myApi.GetSearch(query, geo, count = 100, max_id = MAX_ID, result_type='recent')]
        for raw_t in tweets:
            output_text.write(str(raw_t['id'])+"-"+str(raw_t['text'])+"\n")
            # output_ID.write(str(raw_t['text'])+"\n")
        if tweets:
            MAX_ID = tweets[-1]['id']
            # print MAX_ID, len(tweets)

def main():
   
    # randomsample()
    # mainquery()
   
if __name__ == '__main__':
    main()
    
