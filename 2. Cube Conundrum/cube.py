import re

class Game():
    '''
    Class object created for each line in game data
    '''
    def __init__(self, input_string:str):
        self.input_string:str = input_string
        self.game_number:int = self.get_game()
        self.game_sets:list[dict] = self.get_sets()

    def get_game(self):
        '''
        Returns the game number as an integer value
        '''
        pattern:str = r"\d+(?=:)"
        game_number = re.search(pattern, self.input_string)[0]
        return int(game_number)

    def get_sets(self):
        '''
        Returns a list of dictionaries where each color contains the corresponding number of cubes that were revealed
        '''
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
        '''
        Returns a boolean true or false value based on whether the game was valid
        '''
        for game_set in self.game_sets:
            for color in game_set.keys():
                if (game_set[color] > valid_set[color]) or (game_set[color] < 0):
                    return False

        return True

    def max_set(self):
        '''
        Returns a dictionary containing the maximum number of cubes for each color
        '''
        max_set:dict = {"red":1, "green":1, "blue":1}
        for game_set in self.game_sets:
            for color in game_set.keys():
                if game_set[color] > max_set[color]:
                    max_set[color] = game_set[color]
        return max_set

    def get_power(self):
        '''
        Returns the product of each color in the max set of the game
        '''
        power = 1
        for color in self.max_set().keys():
            power *= self.max_set()[color]

        return power

def _part_one():
    '''
    Solution for part one
    '''
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

def _part_two():
    '''
    Solution for part two
    '''
    directory = current_dir()
    with open(f"{directory}games", "r") as file_handle:
        lines:list[str] = file_handle.read().split("\n")
        sum_power = 0
        for line in lines:
            new_game = Game(line)
            sum_power += new_game.get_power()

    return sum_power

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
    print(_part_two())

if __name__ == "__main__":
    main()