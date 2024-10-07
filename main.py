# main.py
from game_tools import solve_riddle, end_game, sleep, get_random_event, display_inventory, slow_print

def greeting():
    slow_print("Willkommen bei 'Das Geheimnis des verfluchten Hauses'!")
    sleep(2)
    slow_print("Es ist Halloween, und du bist in einem alten, verfluchten Haus gefangen.")
    sleep(2)
    slow_print("Dunkle Schatten und unheimliche Geräusche umgeben dich.")
    sleep(2)
    slow_print("Um zu entkommen, musst du schreckliche Rätsel lösen und die Geheimnisse des Hauses lüften.")
    sleep(2)

def enter_room(room, inventory):
    if room == "hannibals_diner":
        slow_print("Du betrittst 'Hannibal's Diner'. Die Wände sind mit blutigen Handabdrücken bedeckt, und der Geruch von verwestem Fleisch liegt in der Luft.")
        sleep(2)
        reward = solve_riddle(
            "Was ist kalt wie Eis, doch bricht nicht, und hat die Form einer Klinge?", 
            "Es wird oft in der Küche verwendet.", 
            ["messer"], 
            "Blutiges Messer"
        )
        inventory.append(reward)
        return "annabelles_playroom"
    
    elif room == "annabelles_playroom":
        slow_print("Willkommen im 'Annabelle's Playroom'. Überall stehen gruselige Puppen, deren Augen dir folgen.")
        sleep(2)
        reward = solve_riddle(
            "Was kann lebendig scheinen, doch ist es nie?", 
            "Es hat Kleidung und oft ein Lächeln.", 
            ["puppe"], 
            "Verfluchte Puppe"
        )
        inventory.append(reward)
        return "freddys_basement"
    
    elif room == "freddys_basement":
        slow_print("Du bist in 'Freddy's Basement'. Die Wände sind mit gruseligen Bildern von schlafenden Kindern bedeckt.")
        sleep(2)
        reward = solve_riddle(
            "Was kommt nachts, um dich zu holen, wenn du schläfst?", 
            "Es ist der Grund, warum viele Menschen Angst vor dem Dunkeln haben.", 
            ["albtraum"], 
            "Albtraum-Amulett"
        )
        inventory.append(reward)
        return "michaels_attic"
    
    elif room == "michaels_attic":
        slow_print("Du betrittst 'Michael's Attic'. Überall liegen alte, verstaubte Gegenstände und das Licht flackert.")
        sleep(2)
        reward = solve_riddle(
            "Wer kommt mit einem Messer, wenn die Nacht hereinbricht?", 
            "Ein bekannter Horrorfilmcharakter, der oft in der Dunkelheit lauert.", 
            ["michael myers"], 
            "Michaels Messer"
        )
        inventory.append(reward)
        return "exit"  # Gehe zum Ausgang

def navigate():
    slow_print("Wie möchtest du dich bewegen? (Hoch, Runter, Vor, Zurück)")
    move = input("Dein Befehl: ").strip().lower()
    return move

def main():
    greeting()
    current_room = "hannibals_diner"  # Starte direkt im ersten Raum
    inventory = []  # Inventar initialisieren

    while current_room != "exit":
        slow_print(get_random_event())  # Zufallsereignis
        slow_print(f"Du bist im Raum: {current_room}.")
        move = navigate()  # Navigation abfragen
        
        if move == "vor":
            current_room = enter_room(current_room, inventory)
        elif move == "zurück":
            # Hier könntest du eine Logik für das Zurückgehen einfügen, wenn nötig
            slow_print("Du kannst nicht zurückgehen, die Türen sind verschlossen.")
        elif move == "hoch":
            slow_print("Du hast keinen Platz, um nach oben zu gehen.")
        elif move == "runter":
            slow_print("Du hast keinen Platz, um nach unten zu gehen.")
        else:
            slow_print("Unbekannter Befehl. Versuche 'Hoch', 'Runter', 'Vor' oder 'Zurück'.")

        display_inventory(inventory)  # Inventar anzeigen

    slow_print("Du hast alle Rätsel gelöst und stehst nun vor dem Ausgang des Hauses.")
    slow_print("Du öffnest die Tür und trittst ins Freie. Du bist endlich entkommen!")
    end_game(success=True)

if __name__ == "__main__":
    main()