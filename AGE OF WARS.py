import random as rnd
def start():
    Level = int(1)
    HP = float(0)
    MP = float(0)
    Damage = float(0)
    Def = float(0)
    Crit_Rate = float(0)
    abilities_character = list()
    abilities_list = list()
    while True:
        try:
            abilities_character.clear()
            print("###########################################")
            print("#         Ласкаво просимо в гру           #")
            print("#             -Age of Wars-               #")
            print("###########################################")
            print("._________________________________________.")
            print("|            Виберіть воїна:              |")
            print("|_________________________________________|")
            print("|         ***Печерна людина***            |")
            print("|_________________________________________|")
            print("|            ***Мушкетер***               |")
            print("|_________________________________________|")
            print("|             ***Солдат***                |")
            print("|_________________________________________|")
            print("|            ***Кібервоїн***              |")
            print("|_________________________________________|")
            class_character = str(input('|Зробіть ваш вибір-> '))
            if class_character.lower() == 'печерна людина':
                HP = 10
                MP = 3
                Damage = 2
                Def = 2
                Crit_Rate = 5
                abilities_list.append('падіння метеоритів')
                x = 'падіння метеоритів'
                for i in range(0, 2):
                    ability = abilities_list[rnd.randint(0, len(abilities_list)-1)]
                    if ability in abilities_character:
                        i -= 1
                    else:
                        abilities_character.append(ability)
                print(abilities_character)
                break
            elif class_character.lower() == 'мушкетер':
                HP = 9
                MP = 4
                Damage = 5
                Def = 4
                Crit_Rate = 7
                abilities_list.append('Відновлення здоровя')
                for i in range(0, 2):
                    ability = abilities_list[rnd.randint(0, len(abilities_list) - 1)]
                    if ability in abilities_character:
                        i -= 1
                    else:
                        abilities_character.append(ability)
                print(abilities_character)
                break
            elif class_character.lower() == 'солдат':
                HP = 11
                MP = 2
                Damage = 5
                Def = 5
                Crit_Rate = 8
                abilities_list.append('Бомбардування винищувачем')
                for i in range(0, 2):
                    ability = abilities_list[rnd.randint(0, len(abilities_list) - 1)]
                    if ability in abilities_character:
                        i -= 1
                    else:
                        abilities_character.append(ability)
                print(abilities_character)
                break
            elif class_character.lower() == 'кібервоїн':
                HP = 12
                MP = 1
                Damage = 7
                Def = 8
                Crit_Rate = 10
                abilities_list.append('Смертельний лазер')
                for i in range(0, 2):
                    ability = abilities_list[rnd.randint(0, len(abilities_list) - 1)]
                    if ability in abilities_character:
                        i -= 1
                    else:
                        abilities_character.append(ability)
                print(abilities_character)
                break
            else:
                raise Exception('Воїна з таким іменем не існує! Повторіть спробу!')
        except Exception as e:print(e)

    game_process(HP, MP, Damage, Def, Crit_Rate, abilities_character, class_character)
def game_process(HP, MP, Damage, Def, Crit_Rate, abilities_character, class_character):
    start = False
    e_Level = 1
    e_HP = 0
    e_MP = 0
    e_Damage = 0
    e_Def = 0
    e_Crit_Rate = 0
    list_enemy = ['абориген', 'відьмак', 'термінатор']
    for i in range(0, 3):
        enemy_name = str(list_enemy[rnd.randint(0, len(list_enemy)-1)])
        if enemy_name.lower() == 'абориген':
            e_HP = 8
            e_MP = 2
            e_Damage = 2
            e_Def = 4
            e_Crit_Rate = 2
        elif enemy_name.lower() == 'відьмак':
            e_HP = 5
            e_MP = 4
            e_Damage = 3
            e_Def = 6
            e_Crit_Rate = 3
        elif enemy_name.lower() == 'термінатор':
            e_HP = 7
            e_MP = 1
            e_Damage = 4
            e_Def = 10
            e_Crit_Rate = 4
        start = bool(rnd.randint(0, 2))
        print(f"Хвиля №{i+1}")
        while True:
            print(' ##########################')
            print(" # Інформація про ворога  # ")
            print(' ##########################')
            print('========================')
            print(f"|Назва: {enemy_name}")
            print(f"[HP: {e_HP}           ")
            print(f"<Damage: {e_Damage}    ")
            print(f"(Def: {e_Def}          ")
            print("========================")
            print('____________________________________')
            print("#Статус персонажа:                  ")
            print(f"0 персонаж: {class_character}      ")
            print(f"# HP: {HP}                         ")
            print(f"0 MP: {MP}                         ")
            print(f"# Damage: {Damage}                 ")
            print(f"0 Def: {Def}                       ")
            print(f"# Crit Rate: {Crit_Rate}           ")
            print(f"0 Здібності: {abilities_character} ")
            print('____________________________________')
            Crit_Rate_Bonus = 0
            if start == True: #user
                print('Ваш хід:')
                x = input('супер здібності ->')
                if x == 'падіння метеоритів':
                    Crit_Rate_Bonus = 30
                    print(f'Crit_Rate + {Crit_Rate_Bonus} = {Crit_Rate} + {Crit_Rate_Bonus}')
                if x == 'відновлення здоровя':
                    Crit_Rate_Bonus = 40
                    print(f'Crit_Rate + {Crit_Rate_Bonus} = {Crit_Rate} + {Crit_Rate_Bonus}')
                if x == 'бомбардування винищувачем':
                    Crit_Rate_Bonus = 20
                    print(f'Crit_Rate + {Crit_Rate_Bonus} = {Crit_Rate} + {Crit_Rate_Bonus}')
                if x == 'смертельний лазер':
                    Crit_Rate_Bonus = 60
                    print(f'Crit_Rate + {Crit_Rate_Bonus} = {Crit_Rate} + {Crit_Rate_Bonus}')
                input()
                start = False
                Crit = (Damage *(Crit_Rate + Crit_Rate_Bonus)/100)
                result_damege_by_user = Damage + Crit
                print('#>------------------------------------<#')
                print(f'Bonus Crit: {Crit}                     ')
                print(f'Summary Damage: {result_damege_by_user}')
                print('#>------------------------------------<#')
                if result_damege_by_user > e_Def:
                    current_damage = result_damege_by_user - e_Def
                    e_Def = 0
                    e_HP -= current_damage
                    if e_HP < 0:
                        e_HP = 0
                        print('<#########################>')
                        print(f"|ви вбили {enemy_name}!  ")
                        print(' |  COOL GAME! GOOD LUCK  ')
                        print('<#########################>')
                        break
                else:
                    e_Def -= result_damege_by_user

            else: #enemy
                start = True
                result_damege_by_enemy = e_Damage + (e_Damage*e_Crit_Rate/100)
                if result_damege_by_enemy > Def:
                    current_damage = result_damege_by_enemy - Def
                    Def = 0
                    HP -= current_damage
                    if HP < 0:
                        HP = 0
                        print('<#########################>')
                        print(f"|      Вас вбили!        ")
                        print(' |      GAME OVER!        ')
                        print('<#########################>')
                        break
                        end()
                else:
                    Def -= result_damege_by_enemy
        input()
def end():
    print('Exit')
if __name__ == "__main__":
    try:
        start()
    except Exception as e:
        print(e)
