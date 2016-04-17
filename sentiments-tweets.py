__auhtor__ = "Dhaval Lad"

import json
from pattern.en import positive

def task10():
    """
    This function sort all the tweets from CrimeReport according to posititve function of pattern.en who has polarity >= threshold will put in positive-sentiment-tweets.txt otherwise in negative-sentiment-tweets.txt. 
    :return:
    """
    # Initialize  tweets list
    tweets = []

    # Open the data file and read line by line
    with open('CrimeReport.txt', 'r') as data_file:
        for line in data_file:
            # Load it as a json object
            tweets.append(json.loads(line))
            
        # Open output files
        file1 = open('positive-sentiment-tweets.txt','w+')
        file2 = open('negative-sentiment-tweets.txt','w+')

        for tweet in tweets:
            # If positive function return TRUE then store to positive-tweets else negative-tweets.
            if positive(tweet['text'],threshold=0.1):
                file1.write(json.dumps(tweet) + '\n')
            else:
                file2.write(json.dumps(tweet) + '\n')
            
        # Close the output files.
        file1.close()
        file2.close()
    print "Please check the output files:\npositive-sentiment-tweets.txt  negative-sentiment-tweets"

if __name__ == '__main__':
    task10()
