from util.read_file import read_file


# Part 1 = 2528
def part1(games, max_red=12, max_green=13, max_blue=14):
    valid_games = 0
    for index, game in enumerate(games):
        game_valid = True
        for game_round in game.replace(f"Game {index+1}: ", '').split(";"):
            for cube in game_round.split(","):
                cube = cube.strip()
                if cube.find("red") != -1 and int(cube.rstrip(" red")) > max_red:
                    game_valid = False
                if cube.find("green") != -1 and int(cube.rstrip(" green")) > max_green:
                    game_valid = False
                if cube.find("blue") != -1 and int(cube.rstrip(" blue")) > max_blue:
                    game_valid = False
        if game_valid:
            valid_games += index + 1
    return valid_games


# Part 2 = 67363
def part2(games):
    power_sum = 0
    for index, game in enumerate(games):
        minimum_red = 0
        minimum_green = 0
        minimum_blue = 0
        for game_round in game.replace(f"Game {index+1}: ", '').split(";"):
            for cube in game_round.split(","):
                cube = cube.strip()
                if cube.find("red") != -1 and int(cube.rstrip(" red")) > minimum_red:
                    minimum_red = int(cube.rstrip(" red"))
                if cube.find("green") != -1 and int(cube.rstrip(" green")) > minimum_green:
                    minimum_green = int(cube.rstrip(" green"))
                if cube.find("blue") != -1 and int(cube.rstrip(" blue")) > minimum_blue:
                    minimum_blue = int(cube.rstrip(" blue"))
        power_sum += minimum_red * minimum_green * minimum_blue
    return power_sum


def main(input_filepath):
    contents = read_file(input_filepath)
    contents = contents.split("\n")

    part1_result = part1(contents)
    part2_result = part2(contents)

    assert part1_result == 2528  # Verified solution
    assert part2_result == 67363  # Verified solution

    print(f"Day 2 Part 1: {part1_result}")
    print(f"Day 2 Part 2: {part2_result}")


if __name__ == '__main__':
    main("input.txt")


