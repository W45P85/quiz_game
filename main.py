print ("Willkommen bei Daniels Quiz-Game. Mach' es dir gemütlich.")

playing = input("Möchtest du spielen? (Ja/Nein): ")

# Groß und Kleinschreibung ist durch die Methode .lower() egal
if playing.lower() != "ja" :
    print("Schade und goodbye")
    quit()
    
print("Okay, dann lass uns spielen :)")
score = 0

answer = input("Was bedeutet die englische Abkürzung 'GPU'? ")
if answer.lower() == "graphics processing unit":
    print("Klasse! Die Antwort ist richtig! :)")
    score += 1 # Score rechnet die Punktzahl zusammen
else: 
    print("Schade, die Antwort ist leider falsch. :(")
    
answer = input("Was bedeutet die englische Abkürzung 'RAM'? ")
if answer.lower() == "random access memory":
    print("Klasse! Die Antwort ist richtig! :)")
    score += 1
else: 
    print("Schade, die Antwort ist leider falsch. :(")
    
answer = input("Was bedeutet die englische Abkürzung 'PSU'? ")
if answer.lower() == "power supply unit":
    print("Klasse! Die Antwort ist richtig! :)")
    score += 1
else: 
    print("Schade, die Antwort ist leider falsch. :(")

answer = input("Was bedeutet die englische Abkürzung 'CPU'? ")
if answer.lower() == "central processing unit":
    print("Klasse! Die Antwort ist richtig! :)")
    score += 1
else: 
    print("Schade, die Antwort ist leider falsch. :(")
    
print(f"Das Quiz ist leider schon vorbei. Du hast {score} Punkte von möglichen 4 Punkten erreicht.")
print("Das sind" + str((score / 4) * 100) + "% richtige Angaben.")
