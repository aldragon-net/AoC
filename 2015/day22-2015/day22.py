boss_HP = 51
boss_damage = 9
player_HP = 50
mana = 500



pl_strategies = [[]]
losing = []

def generate_strategies(pl_strategies):
    next_strategies = []
    for i in range(len(pl_strategies)):
        if i in losing:
            continue
        for spell in ['M', 'D', 'S', 'P', 'R']:
            pl_turns = pl_strategies[i].copy()
            if spell == 'M':
                pl_turns.append(spell)
                next_strategies.append(pl_turns)
            elif spell == 'D':
                pl_turns.append(spell)
                next_strategies.append(pl_turns)
            elif spell == 'S':
                if not 'S' in pl_turns[-2:]:
                    pl_turns.append(spell)
                    next_strategies.append(pl_turns)
            elif spell == 'P':
                if not spell in pl_turns[-2:]:
                    pl_turns.append(spell)
                    next_strategies.append(pl_turns)
            elif spell == 'R':
                if not spell in pl_turns[-2:]:
                    pl_turns.append(spell)
                    next_strategies.append(pl_turns)
    pl_strategies = next_strategies 
    return pl_strategies

undetermined = [[]]    
min_mana = 10000 
depth = 0 
while True:
    depth = depth + 1
    pl_strategies = generate_strategies(undetermined)
    print(len(pl_strategies), 'strategies of depth', depth, 'generated')
    print(pl_strategies[0])
    losing = []
    undetermined.clear()
    for i in range(len(pl_strategies)):
        shield, poison, recharge = 0, 0, 0
        boss_HP = 51  
        player_HP = 50
        mana = 500
        pl_turns = pl_strategies[i]
        t = 0
        while True:
            #player_turn
            player_HP = player_HP - 1
            if player_HP<=0:
                player_won = False
                break
            too_short = False
            if t>=len(pl_turns):
                too_short = True
                break
            #effects
            if shield>0:
                shield = shield - 1
            if poison>0:
                poison = poison - 1
                boss_HP = boss_HP - 3
            if recharge>0:
                recharge = recharge - 1
                mana = mana + 101
            if boss_HP<=0:
                player_won = True
                break
            #
            spell = pl_turns[t]
            if spell == 'M':
                if mana<53:
                    player_won = False
                    break
                else:
                    mana = mana - 53
                    boss_HP = boss_HP - 4
            if spell == 'D':
                if mana<73:
                    player_won = False
                    break
                else:
                    mana = mana - 73
                    boss_HP = boss_HP - 2
                    player_HP = player_HP + 2
            if spell == 'S':
                if mana<113:
                    player_won = False
                    break
                else:
                    mana = mana - 113
                    shield = 6
            if spell == 'P':
                if mana < 173:
                    player_won = False
                    break                   
                else:
                    mana = mana - 173
                    poison = 6                    
            if spell == 'R':
                if mana < 229:
                    player_won = False
                    break
                else:
                    mana = mana - 229
                    recharge = 5
            #boss_turn 
            #player_HP = player_HP - 1
            if shield>0:
                shield = shield - 1
                pl_armor = 7
            else:
                pl_armor = 0
            if poison>0:
                poison = poison - 1
                boss_HP = boss_HP - 3
            if recharge>0:
                recharge = recharge - 1
                mana = mana + 101
            player_HP = player_HP - (boss_damage - pl_armor)
            if boss_HP<=0:
                player_won = True
                break
            if player_HP<=0:
                player_won = False
                break
            t = t + 1
        if too_short:
            undetermined.append(pl_turns)
            continue
        if player_won:
            print('Winning sequence found:', pl_turns)
            input()
            spent_mana = 0
            for j in range(len(pl_turns)):
                if pl_turns[j] == 'M':
                    spent_mana = spent_mana + 53
                if pl_turns[j] == 'D':
                    spent_mana = spent_mana + 73
                if pl_turns[j] == 'S':
                    spent_mana = spent_mana + 113
                if pl_turns[j] == 'P':
                    spent_mana = spent_mana + 173
                if pl_turns[j] == 'R':
                    spent_mana = spent_mana + 229 
            print('It costed', spent_mana, 'mana')
            if min_mana>=spent_mana:
                min_mana = spent_mana
            print('Min mana spent is:', min_mana )

    
        

   
    
