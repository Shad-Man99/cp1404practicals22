CHAMPION_INDEX = 2
NATIONALITY_INDEX = 1


def main():
    info = read_file()
    display_info(info)


def read_file():
    champions = []
    nationalities = []
    win_count = {}
    infile = open("wimbledon.csv", "r", encoding="utf-8-sig")
    infile.readline()
    for line in infile:
        parts = line.split(",")
        champion = parts[CHAMPION_INDEX]
        if champion in champions:
            win_count[champion] += 1
        else:
            win_count[champion] = 1
            champions.append(champion)
        nationality = parts[NATIONALITY_INDEX]
        if nationality not in nationalities:
            nationalities.append(nationality)
    infile.close()
    info = [champions, nationalities, win_count]
    return info


def display_info(info):
    print("Wimbledon Champions: ")
    for key, value in info[2].items():
        print(f"{key} {value}")
    print(f"These {len(info[1])} countries have won Wimbledon: ")
    info[1].sort()
    print(",".join(info[1]))


main()
