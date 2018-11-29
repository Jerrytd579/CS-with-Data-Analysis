# Improved example.  Uses training and test set.
__author__ = 'bixlermike'
# Based on tutorial at http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/
# This version uses different data set, incorporates optional neutral tweet category,
# removes hashtags from tweet, and stems words
import csv
import matplotlib.pyplot as plt
import nltk
import time

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

# Stemming a word means grabbing just the root of the word, so "stopping" becomes "stop", etc.
# This object will help us stem the tweets.
s = nltk.stem.SnowballStemmer('english')

pos_tweets = []
neg_tweets = []
neutral_tweets = []

# If we define this here, we can avoid having to manually change this number in each place that it's used in the code
TRAINING_LINES = 1000

start_time = time.clock()
print ('Reading in tweets!')
with open('airline_tweets.csv','r', encoding='utf-8',errors='ignore') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    # Skip first line of file (headers)
    next(plots)
    for i, row in enumerate(plots):
        # i contains the line number of the file, row contains the actual data
        # Kick us out of the loop if we get to this line of the input file.
        # We might want to leave the loop early, as the program runtime gets large very quickly!
        if i == TRAINING_LINES:
            break
        # Break the tweet down into the individual stemmed words
        # Append the stemmed tweet as well as the sentiment to the list
        if row[1] == 'positive':
            temp = s.stem(row[10]), 'positive'
            pos_tweets.append(temp)
        elif row[1] == 'negative':
            temp = s.stem(row[10]), 'negative'
            neg_tweets.append(temp)
        # elif row[1] == 'neutral':
        #     temp = s.stem(row[10]), 'neutral'
        #     neutral_tweets.append(temp)

print ('Finished reading tweets!')

tweets = []
# Take all of the strings stored in both the positive and negative tweet lists, along with the sentiment labels
for (words, sentiment) in pos_tweets + neg_tweets:
#for (words, sentiment) in pos_tweets + neg_tweets + neutral_tweets:
    # Filter the set of words to include only those that have at least 4 characters and don't start with a hashtag
    words_filtered = [e.lower() for e in words.split() if len(e) >= 4 and not e.startswith('@')]
    tweets.append((words_filtered, sentiment))
print ('Wrote all training data into a giant list!')

# Calculate how often we see each word in a positive or negative tweet
word_features = get_word_features(get_words_in_tweets(tweets))
# Tell the machine learning algorithm that this is our training set of data
training_set = nltk.classify.apply_features(extract_features, tweets)

print ('Starting to train data using Naive Bayes classifier!')
# This is the time consuming step.  The machine learning algorithm tries to learn from the training data given to it.
classifier = nltk.NaiveBayesClassifier.train(training_set)
print ('Done training the data!')

# Lists the words that are the most informative as to whether we are looking at a positive or negative tweet
classifier.show_most_informative_features(50)
#tweet = ["You guys are terrible","Thank you for the great bday experience", "My plane was delayed 3 hours.  You suck!"]
# Cycle through list of tweets that we want to test.  Classify them one by one and print result
#for i in tweet:
#    print("The sentiment of '" + str(i) + "' is " + classifier.classify(extract_features(i.split())))

# Create a list to store all of the tweets that we're trying to predict
test_set_tweets = []
correct_guesses = 0
incorrect_guesses = 0
attempts = 0
print ('Reading in tweets again!')
with open('airline_tweets.csv','r', encoding='utf-8',errors='ignore') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    # Skip first line of file (headers)
    next(plots)
    for i, row in enumerate(plots):
        # Start guessing at the sentiment after we get past the data used to train the model
        # It's not fair to test the same tweets that we used to train the model
        # Let's skip the neutral tweets, as we didn't train the model to understand what neutral means
        if i > TRAINING_LINES and str(row[1]) != 'neutral':
            actual_sentiment = str(row[1])
            # Don't forget to stem the tweet, since the model was trained with stemmed words!
            current_tweet = s.stem(row[10])
            test_set_tweets.append(current_tweet)
            # Predict the sentiment of this tweet
            predicted_sentiment = classifier.classify(extract_features(current_tweet.split()))
            # Print line statements to make sure code is working correctly
            #print("The predicted sentiment of '" + str(row[10]) + "' is " + predicted_sentiment + ".")
            #print("The actual sentiment was " + actual_sentiment + ".")
            #print()
            if (predicted_sentiment == actual_sentiment):
                correct_guesses+=1
                attempts+=1
            else:
                incorrect_guesses+=1
                attempts+=1

        # Since code like this can take a long time to run, it's sometimes difficult to know if it's stuck in a loop,
        # barely running, almost done, etc.
        # Put in statements like the one below to give you occasional status updates
        if (i % 1000 == 0):
            print ("We're " + str(i) + " lines into the file!")

accuracy = correct_guesses / (correct_guesses + incorrect_guesses)
end_time = time.clock()
print ("For a training set of " + str(TRAINING_LINES) + " samples, the accuracy across " + str(attempts) + " predictions was " + str(round(accuracy*100,2)) + "%")
print ("The code took " + str(round(end_time-start_time,2)) + " seconds to run.")
accuracy *= 100

accuracy = [accuracy]
with open('C:/Users/jerry/Desktop/School Stuff/MachineLearning.csv', 'w') as csvfile:
    fieldnames = ['accuracy']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'accuracy':accuracy})
