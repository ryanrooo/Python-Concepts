


def main():

    ctemp = [0, 12, 34, 100]

    tempdict = {t: (t*9/5) +32 for t in ctemp if t < 100}
    print (tempdict)
    print (tempdict[12])

    team1 = {"jones": 24, "Jameson": 18, "smith": 58, "burns": 7}
    team2 = {"white": 12, "macke": 88, "perce":4}

    newteam = {k:v for team in (team1, team2) for k,v in team.items()}
    print (newteam)




if __name__ == "__main__":
    main()