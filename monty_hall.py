import random

class Door:
    def __init__(self, has_prize=False):
        self.has_prize = has_prize

class MontyHallGame:
    def __init__(self, num_doors=3):
        self.num_doors = num_doors
        self.doors = [Door() for _ in range(num_doors)]
        self._place_prize()

    def _place_prize(self):
        prize_index = random.randint(0, self.num_doors - 1)
        self.doors[prize_index].has_prize = True

    def simulate(self, switch: bool) -> bool:
        player_choice = random.randint(0, self.num_doors - 1)

        revealed_door = self._reveal_goat_door(player_choice)

        # Player switches if the strategy says so
        if switch:
            player_choice = self._switch_choice(player_choice, revealed_door)

        return self.doors[player_choice].has_prize

    def _reveal_goat_door(self, player_choice):
        options = [
            i for i in range(self.num_doors)
            if i != player_choice and not self.doors[i].has_prize
        ]
        return random.choice(options)

    def _switch_choice(self, player_choice, revealed_door):
        # Switch to the one remaining unopened door
        for i in range(self.num_doors):
            if i != player_choice and i != revealed_door:
                return i
        return player_choice

class MontyHallSimulator:
    def __init__(self, trials: int = 10000):
        self.trials = trials

    def run(self, switch: bool):
        wins = 0
        for _ in range(self.trials):
            game = MontyHallGame()
            if game.simulate(switch):
                wins += 1

        self._report(wins)

    def _report(self, wins):
        losses = self.trials - wins
        win_percentage = (wins / self.trials) * 100
        loss_percentage = (losses / self.trials) * 100
        print(f"Wins: {wins} ({win_percentage:.2f}%)")
        print(f"Losses: {losses} ({loss_percentage:.2f}%)")

if __name__ == "__main__":
    simulator = MontyHallSimulator(trials=10000)
    simulator.run(switch=True)  # there is always a higher chance by switching (+33%), famous monty hall problem.