import turtle
import math


def draw_tree(branch_length, level):
    if level == 0:
        return

    turtle.forward(branch_length)

    angle = 45
    new_length = branch_length * math.sqrt(2) / 2

    turtle.right(angle)
    draw_tree(new_length, level - 1)

    turtle.left(2 * angle)
    draw_tree(new_length, level - 1)

    turtle.right(angle)
    turtle.backward(branch_length)


def setup_tree(level):
    turtle.speed("fastest")
    turtle.left(90)
    turtle.up()
    turtle.backward(200)
    turtle.down()

    draw_tree(100, level)
    turtle.done()


try:
    level = int(input("Enter recursion level for the Pythagorean tree: "))
    if level < 0:
        raise ValueError("The level should be a non-negative integer.")
    setup_tree(level)
except ValueError as e:
    print("Invalid input:", e)
