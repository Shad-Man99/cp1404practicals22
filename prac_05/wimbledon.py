

infile = open("wimbledon.csv", "r", encoding="utf-8-sig")
CHAMPION_INDEX = 2
NATIONALITY_INDEX = 1
champions = []
nationalities = []
win_count = {}
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
print("Wimbledon Champions: ")
for key, value in win_count.items():
    print(f"{key} {value}")
print(f"These {len(nationalities)} countries have won Wimbledon: ")
nationalities.sort()
print(",".join(nationalities))
