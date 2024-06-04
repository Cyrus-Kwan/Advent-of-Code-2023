import re

class Number():
    def __init__(self, matrix:list[list], row:int, column:int):
        self.rows:int = row
        self.columns:set[int] = self.get_columns(matrix[self.rows], column)
        self.value:int = self.get_value(matrix, column)
        self.part:bool = self.is_part(matrix)

    def __eq__(self, other):
        if not isinstance(other, Number):
            return NotImplemented

        return self.__dict__ == other.__dict__

    def get_columns(self, line:list[str], column:int):
        columns:list[int] = [column]
        start = []
        end = []

        for i in range(len(line[column::-1])):
            if line[column-i].isdigit():
                start.append(column-i)
            else:
                break

        for j in range(len(line[column:])):
            if line[column+j].isdigit():
                end.append(column+j)
            else:
                break

        return set(start+end)

    def get_value(self, matrix:list[list], column:int):
        line = "".join(matrix[self.rows])

        pattern = r"\d*"
        start = re.match(pattern, line[column-1::-1])[0] or ""
        start = start[::-1]
        end = re.match(pattern, line[column:])[0] or ""
        return int(start+end)

    def is_part(self, matrix:list[list]):
        pattern = r"[^\s\d.]"
        for column in self.columns:
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    try:
                        if re.match(pattern, matrix[self.rows+i][column+j]):
                            return True
                    except IndexError:
                        continue
        return False

def matrix(matrix_input:str):
    matrix:list[list] = []
    lines:list[str] = matrix_input.splitlines()
    for line in lines:
        chars = [char for char in line]
        matrix.append(chars)

    return matrix

def part_one():
    directory = current_dir()
    with open(f"{directory}gears") as file_handle:
        gears = matrix(file_handle.read())
        nums = []
        for row in range(len(gears)):
            for column in range(len(gears[row])):
                try:
                    new_num = Number(gears, row, column)
                    if (new_num not in nums) and new_num.part:
                        nums.append(new_num)
                except ValueError:
                    continue

        values = [num.value for num in nums]
    return sum(values)

def current_dir():
    '''
    Returns the current directory of __main__
    '''
    pattern = r"^.*[/\\]"
    searches = re.search(pattern, __file__)
    groups = searches.group(0)
    return groups

def main():
    print(part_one())

if __name__ == "__main__":
    main()