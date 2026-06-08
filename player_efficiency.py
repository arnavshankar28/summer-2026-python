def calculate_efficiency(points, rebounds, assists):
    efficiency = points + rebounds + assists
    return efficiency
points = int(input("Enter points: "))
rebounds = int(input("Enter rebounds: "))
assists = int(input("Enter assists: "))
player_efficiency = calculate_efficiency(points, rebounds, assists)
print("efficiency score", player_efficiency)    