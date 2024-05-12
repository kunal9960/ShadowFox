# Initial list of Justice League members

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Calculate the number of members in the Justice League

num_members = len(justice_league)
print("Number of members in the Justice League:", num_members)

# 2. Batman recruits Batgirl and Nightwing as new members

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(justice_league)

# 3. Wonder Woman is now the leader, move her to the beginning of the list

justice_league.insert(0, justice_league.pop(justice_league.index("Wonder Woman")))
print(justice_league)

# 4. Separate Aquaman and Flash by moving Green Lantern in between

justice_league.insert(justice_league.index("Aquaman"), justice_league.pop(justice_league.index("Green Lantern")))
print(justice_league)

# 5. Superman assembles a new team, replacing the existing list

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(justice_league)

# 6. Sort the Justice League alphabetically

justice_league.sort()

print("Updated Justice League:", justice_league)
print("New leader of the Justice League:", justice_league[0])
