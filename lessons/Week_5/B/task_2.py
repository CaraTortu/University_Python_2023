def sync(l: list) -> list:
    s = set()

    for team in l:
        s.update(team)

    return s

team_sheet_1 = {"Mary", "Nuala", "Paddy", "Colm"}
team_sheet_2 = {"Maeve", "Paddy", "Brendan", "Colm"}
team_sheet_3 = {"Cliona", "Colm", "Brendan", "Nuala"}
team_sheets = [team_sheet_1, team_sheet_2, team_sheet_3]

print(sync(team_sheets))
