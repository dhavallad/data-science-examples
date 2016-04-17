__author__ = "Dhaval Lad"

import json
import datetime

def task8():
    """
    This function sorts all the tweets from CrimeReport file and puts 10 most recent tweets in output_task8.txt file
    :return:
    """
    # Initialize  tweets list
    tweets = []

    # Open the data file and read line by line
    with open('CrimeReport.txt', 'r') as data_file:

        for line in data_file:
            # Load it as a json object
            tweets.append(json.loads(line))
            
        # Fri Jan 31 05:51:59 +0000 2014
        sorted_tweets = sorted(tweets, key=lambda item: datetime.datetime.strptime(item['created_at'].split("+")[0] +
                                                                                   item['created_at'][-4:],
                                                                                   "%a %b %d %H:%M:%S %Y"))

        # Open the output file and write to it
        output_file = open('10_RecentTweets.txt', 'w')

        # Write the most recent 10 tweets
        for tweet in sorted_tweets[-10:]:
            output_file.write(json.dumps(tweet) + '\n')

        # Close the file after reading it
        output_file.close()
        print "Please check file: 10_RecentTweets.txt"

if __name__ == '__main__':
    task8()