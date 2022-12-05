boss_HP = 104
player_HP = 100
boss_damage = 8
boss_armor = 1

weapons = [[4, 0, 8], [5, 0, 10], [6, 0, 25], [7, 0, 40], [8, 0, 74]]
armors = [[0,0,0], [0, 1, 13], [0, 2, 31], [0, 3, 53], [0, 4, 75], [0, 5, 102]]
rings = [[0, 0, 0], [1, 0, 25], [2, 0, 50], [3, 0, 100], [0, 1, 20], [0, 2, 40], [0, 3, 80]]


def fight(pl_damage, pl_armor):
    pl_dpt = pl_damage - boss_armor
    if pl_dpt < 1:
        pl_dpt = 1
    boss_dpt = boss_damage - pl_armor
    if boss_dpt < 1:
        boss_dpt = 1
    if boss_HP % pl_dpt == 0:
        N_boss_dead = boss_HP // pl_dpt
    else: 
        N_boss_dead = boss_HP // pl_dpt + 1
    if player_HP % boss_dpt == 0:
        N_pl_dead = player_HP // boss_dpt
    else:
        N_pl_dead = player_HP // boss_dpt + 1
    if N_boss_dead <= N_pl_dead:
        return True
    else:
        return False
        
        

min_cost = 1000

max_cost = 0

for i in range(len(weapons)):
    for j in range(len(armors)):
        for k in range(len(rings)):
            for r in range(len(rings)):
                if r == k and not k == 0:
                    continue
                cost = weapons[i][2] + armors[j][2] + rings[k][2] + rings[r][2]
                damage = weapons[i][0] + rings[k][0] + rings[r][0]
                armor = armors[j][1] + rings[k][1] + rings[r][1]
                #print ('Damage, armor, cost is', damage, armor, cost, 'for', i,j,k,r, 'set')
                #input()
                player_won = fight(damage, armor)
                #print('Player won?', player_won)
                if player_won and cost < min_cost:
                    min_cost = cost
                    a, b, c, d = i, j, k, r
                if not player_won and cost > max_cost:
                    max_cost = cost
                    e, f, g, h = i, j, k, r
                    
print('Min win cost:', min_cost, 'with', a,b,c,d, 'set' )
print('Max still-lose cost:', max_cost, 'with', e,f,g,h, 'set' )
input()
                    
                
               
        
    
        

   
    
