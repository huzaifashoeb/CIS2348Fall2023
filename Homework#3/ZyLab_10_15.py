# Name: Huzaifa Shoeb, ID: 1925670

class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    def get_win_percentage(self):
        return self.wins / (self.wins + self.losses)


if __name__ == "__main__":

    team = Team()

    user_name = input()
    user_wins = int(input())
    user_losses = int(input())

    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses

    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.name, 'has a winning average!')
    else:
        print('Team', team.name, 'has a losing average.')
