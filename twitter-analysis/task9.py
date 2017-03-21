__author__ = "Dhaval Lad"

import json
import os
import datetime

def task9():
    """
    This function reads all the tweets from CrimeReport file and puts it in output_folder with Mon-Day-Year-Hour.txt as
    file name.
    :return:
    """
    # Initialize  tweets list
    tweets = []

    # Open the data file and read line by line
    with open('CrimeReport.txt', 'r') as data_file:
        # For each line
        for line in data_file:
            tweets.append(json.loads(line))

        # Check if the output_folder has already been created, if not create it
        if not os.path.exists(os.getcwd() + "/output-folder"):
            os.makedirs('output-folder')

        # Write tweets to output file.
        for tweet in tweets:
            # Re-create time string
            new_date_time = tweet['created_at'].split("+")[0] + tweet['created_at'][-4:]

            # Get the date and hour of the tweet
            tweet_date_time = datetime.datetime.strptime(new_date_time, "%a %b %d %H:%M:%S %Y")

            # Create the file name for tweet (Mon-Day-Year-Hour.txt)
            file_name = tweet_date_time.strftime("%m-%d-%Y-%H") + '.txt'

            # Open the output file and append mode and write to it
            output_file = open('output-folder/' + file_name, 'a')
            output_file.write(json.dumps(tweet) + '\n')
            output_file.close()
    
    print "Please check the folder:output-folder."
    
if __name__ == '__main__':
    task9()