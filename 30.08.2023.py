# Испытание: Статистика матчей по командам 
def wins_by_team(matches):
    winners = {team_1 for team_1, team_2 in matches}
    return {
        team_1: {loser for winner, loser in matches if winner == team_1}
        for team_1 in winners
    }
