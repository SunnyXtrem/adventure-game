import random
import time

def sleep(seconds):
    time.sleep(seconds)

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()

def solve_riddle(riddle, hint, valid_answers, reward):
    slow_print(riddle)
    slow_print(f"Hinweis: {hint}")
    answer = input("Deine Antwort: ").strip().lower()
    if answer in valid_answers:
        slow_print("Rätsel gelöst!")
        return reward
    else:
        slow_print("Falsche Antwort. Du bist verloren...")
        end_game(success=False)

def end_game(success):
    if success:
        slow_print("Du hast das Geheimnis des verfluchten Hauses gelüftet und bist entkommen! Herzlichen Glückwunsch!")
    else:
        slow_print("Der Schatten hat dich eingeholt... Das Spiel ist zu Ende.")
    sleep(2)
    exit()

def get_random_event():
    events = [
        "Ein leises Kichern ist in der Ferne zu hören.",
        "Du spürst einen kalten Luftzug hinter dir.",
        "Ein Schatten huscht über die Wand.",
        "Eine Puppe dreht sich langsam zu dir um.",
    ]
    return random.choice(events)

def display_inventory(inventory):
    if inventory:
        slow_print("Dein Inventar enthält:")
        for item in inventory:
            slow_print(f"- {item}")
    else:
        slow_print("Dein Inventar ist leer.")