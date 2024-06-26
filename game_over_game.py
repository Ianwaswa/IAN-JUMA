import random

game_over = False
score = 0

while not game_over:
    score += random.randint(1, 10)
    print(score)
        
    if score > 100:
        game_over = True
        break
    print("Game is still on!!!")