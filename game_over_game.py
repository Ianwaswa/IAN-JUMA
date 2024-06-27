import random

game_over = False
score = 0

while not game_over:
    score += random.randint(20, 40)
    print(score)
    
    if score < 50:
        continue
        
    if score > 100:
        game_over = True
        break
    print("Game is still on!!!")
print("You Win!!!")