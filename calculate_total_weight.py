# Calculate the total weight of rugby players
weights = [122, 122,  145, 208, 202, 156,  177, 234, 145, 168, 197, 234, 142,  211, 201, 211, 144, 189, 188, 210, 203, 231, 311, 178, 210, 190, 210, 231, 180, 195, 195, 177, 234, 201, 210, 201, 234, 234, 145, 178, 122, 195, 210, 122, 195, 178, 210, 145, 122]
total_weight = 0
number_of_players = len(weights)

for weight in weights:
    total_weight += weight
    average_weight = total_weight / number_of_players
print(f'The total weight of your rugby players is {total_weight} kg')
print(f'The average weight for each player in your team is {average_weight} kg')