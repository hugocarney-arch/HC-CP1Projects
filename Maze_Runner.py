# HC Maze Runner 1st
import turtle as t
import random

column_nums = []
row_nums = []
solvable_path = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]

screen = t.Screen()
screen.title("Maze Runner")
screen.bgcolor("lightgray")
screen.setup(width=1200, height=1200)

maze_turtle = t.Turtle()
maze_turtle.teleport(-500, 500)
maze_turtle.speed(0)
maze_turtle.forward(1000)

def get_maze_nums(column_nums, row_nums):
    for x in range(6):
        row_nums.append(random.randint(0,1))
        column_nums.append(random.randint(0,1))
    return column_nums, row_nums

get_maze_nums(column_nums, row_nums)
print(*column_nums)
print(*row_nums)