"""
The aim is to understand how the bots' rumor spreading behavior influence
the rumor spreading of human.

Next steps: human choose to use hashtag or not. If not using hashtag,
then the spreading happen within friend network.
"""

from random import seed, randint

from Agent import Bot, Human
from Tweet_Hashtag import Tweet, Hashtag


class TwitterNetwork:
    """
    This class provides methods for managing all agents and hashtags in the
    model.
    """

    def __init__(self, num_agents=10, num_hashtags=3, num_bots=1,
                 rate_become_spreader=10):
        """
        Initialize a twitter network, including hashtags and agents.
        Assign agents to view random hashtags.

        :param tweet: a tweet object
        :param num_agents: number of agents = num_bots + number of humans
        :param num_hashtags: number of hashtags
        :param num_bots: number of bots
        :param rate_become_spreader: the average
        """
        self.num_agents = num_agents
        self.num_hashtags = num_hashtags
        self.num_bots = num_bots
        self.rate_become_spreader = rate_become_spreader

        # a variable to keep track of timesteps and spreaders
        self.timesteps = 0
        self.num_human_spreaders = 0

        # indicating if any agents became a spreader in the last timestep
        self.agents_updated = False

        # create hashtags, agents and add them to list
        self.hashtags = [Hashtag() for i in range(num_hashtags)]

        # create human and bot agents
        # in this simplified model, all human has same rate become spreader
        self.agents = [Bot() if index < num_bots else Human(
            rate_become_spreader) for index in range(num_agents)]

    def run(self, num_timesteps):
        """
        Run the network for a given number of timesteps.
        """
        for t in range(num_timesteps):
            self.action()
            print(self.get_num_rumors(), self.get_num_human_spreaders())

    def action(self):
        """
        All agents are assigned to a random hashtag and take actions
        """
        for agent in self.agents:
            index = randint(0, self.num_hashtags - 1)
            agent.action(self.hashtags[index])
            if agent.status_updated:
                self.agents_updated = True

    def get_num_rumors(self):
        """
        Get number of rumors in the model.

        :return : the number of rumors in the network
        """
        return sum(h.num_rumors for h in self.hashtags)

    def get_num_human_spreaders(self):
        """
        Get number of human rumors spreaders in the model.

        :return : If no agents' status got updated since last timestep,
        return the stored number of spreaders. If updated, calculate the
        new number.
        """
        if self.agents_updated:
            self.num_human_spreaders = sum(1 for a in self.agents if
                                           a.is_human_spreader())
        return self.num_human_spreaders


if __name__ == '__main__':
    # seed random number generator
    seed()
    model = TwitterNetwork()
    model.run(100)
