import turtle
import random

# Helper functions
def draw_background():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    screen.title("Chemist Game")
    screen.setup(width=800, height=600)

def display_message(text, font_size=18, y_offset=0):
    message_pen = turtle.Turtle()
    message_pen.hideturtle()
    message_pen.penup()
    message_pen.color("black")
    message_pen.goto(0, y_offset)
    message_pen.clear()
    message_pen.write(text, align="center", font=("Arial", font_size, "bold"))
    return message_pen

def firework_from_center(center_x, center_y, color, size):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    pen.goto(center_x, center_y)
    pen.pendown()
    pen.color(color)

    for angle in range(0, 360, 12):
        pen.setheading(angle)
        pen.forward(size)
        pen.backward(size)

def fireworks_show():
    colors = ["red", "blue", "yellow", "green", "orange", "purple", "white", "cyan", "magenta"]
    positions = [(-200, 200), (200, 200), (-200, -200), (200, -200), (0, 0)]

    for pos in positions:
        color = random.choice(colors)
        size = random.randint(50, 100)
        firework_from_center(pos[0], pos[1], color, size)

    display_message("Congratulations, Chemist! You've made the perfect solution!", 18, -200)

# Main game function
def chemist_game():
    draw_background()

    target_altairium = 57
    target_achiride = 43

    display_message("Welcome to Lab Mix Master!", 24, 250)
    display_message("Your goal: Mix 57% Altairium and 43% Achiride.", 18, 225)

    while True:
        try:
            altairium = float(turtle.textinput("Altairium", "Enter the percentage of Altairium:"))
            achiride = float(turtle.textinput("Achiride", "Enter the percentage of Achiride:"))

            if altairium + achiride != 100:
                display_message("The total percentage must equal 100. Try again.", 16, -300)
                continue

            if altairium == target_altairium and achiride == target_achiride:
                fireworks_show()
                break
            else:
                message = ""
                if altairium > target_altairium:
                    message += "Altairium: Too much! "
                elif altairium < target_altairium:
                    message += "Altairium: Not enough! "

                if achiride > target_achiride:
                    message += "Achiride: Too much!"
                elif achiride < target_achiride:
                    message += "Achiride: Not enough!"

                display_message(message, 16, -300)
        except (ValueError, TypeError):
            display_message("Invalid input. Please enter numeric values.", 16, -300)

    restart = turtle.textinput("Play Again", "Do you want to play again? (y/n):")
    if restart and restart.lower() == 'y':
        turtle.clearscreen()
        chemist_game()
    else:
        turtle.bye()

if __name__ == "__main__":
    chemist_game()