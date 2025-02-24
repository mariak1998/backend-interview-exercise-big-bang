from gameplay import SpockGame
import unittest


class TestGamePlay(unittest.TestCase):
    def __init__(self):
        self.user1 = "Samantha"
        self.user2 = "Jenny"
        self.testGame = SpockGame(user1, user2)
    
    def test_game_play(self):
        # check initial scoreboard
        testScore = self.testGame.get_scoreboard()
        self.assertEqual(testScore, {'Samantha': 0, 'Jenny': 0})

        # check the case of a tie
        self.testGame.player_entry("Spock", "Spock")
        testScore2 = self.testGame.get_scoreboard()
        self.assertEqual(testScore2, {'Samantha': 0, 'Jenny': 0})

        # check user1 wins
        self.testGame.player_entry("Spock", "Rock")
        testScore3 = self.testGame.get_scoreboard()
        self.assertEqual(testScore3, {'Samantha': 1, 'Jenny': 0})

        # check user2 wins
        self.testGame.player_entry("Spock", "Paper")
        testScore4 = self.testGame.get_scoreboard()
        self.assertEqual(testScore4, {'Samantha': 1, 'Jenny': 1})

        # clear the scoreboard
        self.testGame.clear_scoreboard()
        testScore5 = self.testGame.get_scoreboard()
        self.assertEqual(testScore5, {'Samantha': 0, 'Jenny': 0})


