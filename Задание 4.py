import random

def simulate_game(num_doors, num_prizes):
    doors = ["пусто"] * num_doors
    prize_indices = random.sample(range(num_doors), num_prizes)
    for idx in prize_indices:
        doors[idx] = "приз"
    return doors

def calculate_win_probabilities(num_doors, num_prizes):
    num_simulations = 10000
    switch_wins = 0
    stay_wins = 0

    for _ in range(num_simulations):
        doors = simulate_game(num_doors, num_prizes)
        player_choice = random.randint(0, num_doors - 1)
        remaining_choices = [i for i in range(num_doors) if i != player_choice and doors[i] != "приз"]
        opened_door = random.choice(remaining_choices)
        final_choice = [i for i in range(num_doors) if i != player_choice and i != opened_door][0]

        if doors[player_choice] == "приз":
            stay_wins += 1
        elif doors[final_choice] == "приз":
            switch_wins += 1

    stay_win_prob = stay_wins / num_simulations
    switch_win_prob = switch_wins / num_simulations
    return stay_win_prob, switch_win_prob

num_doors = 3
num_prizes = 1

stay_prob, switch_prob = calculate_win_probabilities(num_doors, num_prizes)
print("Вероятность выигрыша для игрока, оставшегося при своем первоначальном выборе:", stay_prob)
print("Вероятность выигрыша для игрока, меняющего свой выбор:", switch_prob)


