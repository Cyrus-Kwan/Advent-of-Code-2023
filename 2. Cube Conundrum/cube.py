import re

class Game():
    def __init__(self, input_string:str):
        self.input_string:str = input_string
        self.game_number:int = self.get_game()
        self.game_sets:list[dict] = self.get_sets()

    def get_game(self):
        pattern:str = r"\d+(?=:)"
        game_number = re.search(pattern, self.input_string)[0]
        return int(game_number)

    def get_sets(self):
        pattern:str = "[:;]"
        game_sets:list[str] = re.split(pattern, self.input_string)
        sets:list[dict] = []

        for game_set in game_sets[1:]:
            color_pattern = "[a-zA-Z]+"
            colors = list(re.findall(color_pattern, game_set))

            num_pattern = "[0-9]+"
            nums = re.findall(num_pattern, game_set)
            ints = [int(num) for num in nums]

            set_map = dict(zip(colors, ints))
            sets.append(set_map)

        return sets

    def game_possible(self, valid_set:list[dict]):
        for game_set in self.game_sets:
            for color in game_set.keys():
                if (game_set[color] > valid_set[color]) or (game_set[color] < 0):
                    return False

        return True

def _part_one():
    directory = current_dir()
    possible = {"red":12, "green":13, "blue":14}
    with open(f"{directory}games", "r") as file_handle:
        lines:list[str] = file_handle.read().split("\n")
        game_sum = 0
        for line in lines:
            new_game = Game(line)
            if new_game.game_possible(valid_set=possible):
                game_sum += new_game.game_number

    return game_sum

def current_dir():
    '''
    Returns the current directory of __main__
    '''
    pattern = r"^.*[/\\]"
    searches = re.search(pattern, __file__)
    groups = searches.group(0)
    return groups

def main():
    directory = current_dir()
    print(_part_one())

if __name__ == "__main__":
    main()