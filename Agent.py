from abc import ABC, abstractmethod
from random import randint, choice, seed

from Tweet_Hashtag import Tweet, Hashtag


class Agent(ABC):
    """
    This is a supper class for bot and human agents in the model.
    """

    def __init__(self):
        """ Initialize value of a agent """
        self.is_bot = False
        self.is_rumor_spreader = False
        # updating status in this timestep
        self.status_updated = False

    def is_human_spreader(self):
        """
        Determine whether an agent is a human rumor spreader.

        :return false by default
        """
        return False

    def post(self, is_rumor, hashtag):
        """
        The agent composes a tweet, given a Boolean value as content

        :param is_rumor: whether the tweet is a rumor
        """
        tweet = Tweet(is_rumor)
        hashtag.add_tweet(tweet)

    @abstractmethod
    def action(self, hashtag):
        """
        This method must be overridden.

        :param hashtag: the place where the agent takes action
        """
        pass


class Human(Agent):
    """
    This class provides methods for setting and changing information about
    human agents.
    """
    def __init__(self, rate_become_spreader=10):
        """
        Initialize value of a human agent.

        :param rate_become_spreader: scale 0-100
        """
        super().__init__()
        self.rate_become_spreader = rate_become_spreader

    def is_human_spreader(self):
        """
        :return True if this human is a rumor spreader; otherwise, False.
        """
        return self.is_rumor_spreader

    def read_tweet(self, tweet):
        """
        This function simulate a reading action of human agents. If a non-
        spreader read a rumor, this person becomes a spreader spreader at
        a preset rate.

        :param tweet: tweet to read
        """
        if not tweet:
            return
        if self.is_rumor_spreader or not tweet.is_rumor:
            return

        # calculate a random chance to become spreader
        random_chance = randint(0, 99)
        if random_chance < self.rate_become_spreader:
            self.is_rumor_spreader = True
            self.status_updated = True
        print('random chance:', random_chance)

    def action(self, hashtag):
        """
        The agent randomly choose an action to take.
        """
        # set the update status back to false
        self.status_updated = False

        actions = [self.read_tweet(hashtag.get_most_recent_tweet()),
                   self.post(self.is_rumor_spreader, hashtag)]

        # In a refined model, we need to know how often does a person write a
        # post. But for now, the person has an equal chance to choose from
        # reading or writing a tweet.
        choice(actions)


class Bot(Agent):
    """
    This class provides methods for setting and changing information about
    bot agents.
    """
    def __init__(self):
        """
        Initialize value of a bot agent. For the simplified model,
        all bots are rumor spreader.
        """
        super().__init__()
        self.is_bot = True
        self.is_rumor_spreader = True

    def action(self, hashtag):
        """
        In the simplified model, all bots are rumor spreaders. So, they always
        post rumors.
        """
        return self.post(True, hashtag)


if __name__ == '__main__':
    # for testing only
    seed()

    # seed random number generator
    bot = Bot()
    print(bot.is_human_spreader())

    h = Hashtag()
    h.add_tweet(Tweet(False))

    t = h.get_most_recent_tweet()
    print('tweet:', t.is_rumor)

    bot.action(h)
    t = h.get_most_recent_tweet()
    print('tweet:', t.is_rumor)

    hu = Human(5)

    for i in range(100):
        print(i)
        bot.action(h)
        hu.action(h)
        print('huamn:', hu.is_human_spreader())
        t = h.get_most_recent_tweet()
        print('tweet:', t.is_rumor)






