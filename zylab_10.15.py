# Alexandra Excell  PSID: 1595971

class Team:
    def __init__(self, teamname='none', teamwins=0.0, team_losses=0.0):
        self.teamname = teamname
        self.team_wins = teamwins
        self.team_losses = team_losses

    def get_win_percentage(self):
        win_percentage = float(self.team_wins / (self.team_wins + self.team_losses))
        if win_percentage > .5:
            print('Congratulations, Team', self.teamname, 'has a winning average!')
        else:
            print('Team', self.teamname, 'has a losing average.')
        return(win_percentage)


if __name__ == "__main__":
    input_name = input()
    input_wins = float(input())
    input_loss = float(input())

    student_team = Team(input_name, input_wins, input_loss)
    student_team.get_win_percentage()





