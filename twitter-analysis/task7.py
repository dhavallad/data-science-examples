__author__ = "Dhaval Lad"

import json

def task7():
    """
    This function reads the CrimeReport file and prints out the id for each tweet.
    :return:
    """
    # Open the data file and read line by line
    with open('CrimeReport.txt', 'r') as file:
        # for each line
        for line in file:
            # Load it as a json object
            tweet = json.loads(line)
            
            # If the tweet has 'id' print it.
            if 'id' in tweet.keys():
                print(tweet['id'])
            else:
                print('Tweet id not found.')

if __name__ == '__main__':
    task7()