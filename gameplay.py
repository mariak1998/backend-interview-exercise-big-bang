GAMEPLAY = {
    "Scissors": ["Paper", "Lizard"],
    "Paper": ["Rock", "Spock"],
    "Rock": ["Scissors", "Lizard"],
    "Lizard": ["Paper", "Spock"],
    "Spock": ["Scissors", "Rock"]
}

class SpockGame:
    def __init__(self, user1, user2):
        # store the initial values
        self.user1 = str(user1)
        self.user2 = str(user2)
        self.scoreboard = {user1:0, user2:0}

    def get_scoreboard(self):
      # return the scoreboard
      return self.scoreboard

    def player_entry(self, user1_choice, user2_choice):
      if user1_choice and user2_choice in GAMEPLAY.keys():
        if user1_choice == user2_choice:
          # denote a tie
          return 0 
        if user2_choice in GAMEPLAY[user1_choice]:
            # user1 wins 
            self.scoreboard[user1] += 1
            return 1
        else:
          self.scoreboard[user2] += 1
          # user2 wins
          return 2
      else:
        return "Not a valid choice"
        
    def clear_scoreboard(self):
        # set scoreboard back to original state
        self.scoreboard = {self.user1:0, self.user2:0}
