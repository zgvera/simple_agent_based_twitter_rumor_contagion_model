class Tweet:
    """
    This class provides methods for setting and getting information about
    tweets. An extension would include likes, number of views and retweets
    """
    def __init__(self, is_rumor):
        """
        Initialize value of a tweet.

        :param is_rumor: whether the tweet is a rumor
        """
        self.is_rumor = is_rumor


class Hashtag:
    """
    This class provides methods for managing tweets in hashtag.
    """
    def __init__(self):
        """Initialize value of a hashtag"""
        self.num_rumors = 0
        self.tweets = []

    def add_tweet(self, tweet):
        """
        Add tweet to hashtag.

        :param tweet: a tweet object
        """
        self.tweets.append(tweet)
        if tweet.is_rumor:
            self.num_rumors += 1

    def get_most_recent_tweet(self):
        """
        Get the most recent tweet in list. Return none if there is no tweet
        in the hashtag.

        :return a tweet object or none
        """
        return self.tweets[-1] if self.tweets else None


if __name__ == '__main__':
    # Testing the classes
    h = Hashtag()
    print(h.get_most_recent_tweet())
    h.add_tweet(Tweet(True))
    t = h.get_most_recent_tweet()
    print(t.is_rumor)
    h.add_tweet(Tweet(False))
    t = h.get_most_recent_tweet()
    print(t.is_rumor)

