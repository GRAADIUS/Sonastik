from random import *
def search():
    ru_file = open('rus.txt', 'r+', encoding="utf8")
    ee_file = open('est.txt', 'r+', encoding="utf8")
    languages = []
    ru_file_read = ru_file.readlines()
    ee_file_read = ee_file.readlines()
    languages.append(ru_file_read)
    languages.append(ee_file_read)
    search_word = input("sisestage sõna, vene või eesti keeles, et otsida sõnastikust: ")
    answer = " "
    for i in range(len(languages)):
        for j in range(len(languages[i])):
            clear_word = languages[i][j].rstrip()
            if clear_word == search_word:       
                if languages[i][j] == languages[0][j]:
                    answer = languages[1][j].rstrip()
                    print(answer)
                elif languages[i][j] == languages[1][j]:
                    answer = languages[0][j].rstrip()
                    print(answer)
    if answer == " ":
        add = input("Sõna, mida otsite, ei leitud sõnastikust. kas sa tahaksid lisada? (jah / ei): ")
        if add.upper() == "JAH":
            ru_translation = input("sisestage venekeelne tõlge: ")
            ee_translation = input("sisesta eestikeelne tõlge: ")
            ru_file.write(ru_translation + "\n") 
            ee_file.write(ee_translation + "\n")
            enter_data = ru_translation + " - " + ee_translation
            print(f"{enter_data} lisatud sõnastikku")
        elif add.upper() == "EI":
            pass
    ru_file.close()
    ee_file.close()    
def edit():
    while True:
        corrected_language = input("Millisest sõnastikust sa vea leidsid? (RUS/EST): ")
        if corrected_language.upper() == "RUS":
            ru_file = open('rus.txt', 'r+', encoding="utf8")
            ru_file_read = ru_file.readlines()
            fixable = input("Sisestage õige sõna: ")
            serviceable = input("Sisestage parandatud sõna: ")
            ind = ru_file_read.index(fixable + "\n")
            ru_file_read.remove(fixable + "\n")
            ru_file_read.insert(ind, serviceable + "\n")
            ru_file.close()
            ru_file = open('rus.txt', 'w', encoding="utf8")
            ru_file.writelines(ru_file_read)
            ru_file.close()
            print("Tehtud")
            break
        elif corrected_language.upper() == "EST":
            ee_file = open('est.txt', 'r+', encoding="utf8")
            ee_file_read = ee_file.readlines()
            fixable = input("Sisestage õige sõna: ")
            serviceable = input("Sisestage parandatud sõna: ")
            ind = ee_file_read.index(fixable + "\n")
            ee_file_read.remove(fixable + "\n")
            ee_file_read.insert(ind, serviceable + "\n")
            ee_file.close()
            ee_file = open('est.txt', 'w', encoding="utf8")
            ee_file.writelines(ee_file_read)
            ee_file.close()
            print("Tehtud")
            break      
        else:
            print("keelt pole valitud.")
            pass
def game():
    ru_file = open('rus.txt', 'r+', encoding="utf8")
    ee_file = open('est.txt', 'r+', encoding="utf8")
    ru_file_read = ru_file.readlines()
    ee_file_read = ee_file.readlines()
    languages = []
    languages.append(ru_file_read)
    languages.append(ee_file_read)
    wins = 0
    loses = 0    
    game_counts = checks_number = int(input("Mitu korda järjest tahad mängida?: "))
    while game_counts:   
        rand_lang = randint(0, 1)
        rand_word = randint(0, len(ru_file_read)-1)
        word_for_translate = languages[rand_lang][rand_word].rstrip()
        translate = input(f"sisestage sõna tõlge: {word_for_translate} - ")
        if languages[0 if rand_lang else 1][rand_word].rstrip() == translate:
            print("Õige")
            wins += 1
        else:
            print("Vale")
            loses += 1
        game_counts -= 1
    try:
        wins_procent = wins/checks_number*100
    except:
        wins_procent = 0
    print(f"Võidud: {wins}, kaotused: {loses}, võiduprotsent: {round(wins_procent)}%")
while True:
    print("sisestage '1' otsing\nparandamiseks sisestage '2'.\nteadmiste kontrollimiseks sisestage '3'.\nprogrammist väljuda '4'.")    
    try:
        read = int(input())
        if read == 1:
            print("Aktiveerige otsingufunktsioon")
            search()
        elif read == 2:
            print("Aktiveerige parandusfunktsioon")
            edit()
        elif read == 3:
            print("Aktiveerige mängusüsteem")
            game()
        elif read == 4:
            print("Initsialiseerin väljundi")
            break
    except:
        print("Vale väärtus.")