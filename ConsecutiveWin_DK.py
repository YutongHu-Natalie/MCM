import pandas as pd
ND= pd.read_csv("Novak_Djokovic.csv")
ND['new_game'] = ND['game_no'].ne(ND['game_no'].shift())
# the index of the first point of a new game
new_game= list(ND[ND["new_game"]].index)
#where the result shows up(normally the one before the next game)
game_result=list(i-1 for i in new_game if i!=0)
game_result.append(len(ND)-1)
#the indexes of the point that NDn satisfy win twice consecutively at the beginning
Win_ft= list(i for i in new_game if (ND.loc[i, "point_victor"]==1) and (ND.loc[i+1, "point_victor"]==1))
# beNDuse the last group is not in that list, we don't need to consider about this situation
#intersection_index= list(Win_ft[i] for i in range(len(Win_ft)) if ND.loc[Win_ft[i+1]-1, 'game_victor']==1)
# I leave the simplified version in the comment so you NDn understand
'''
intersection_index=list()
for i in range(len(new_game)):
    if (ND.loc[game_result[i], 'game_victor']==1) and new_game[i] in Win_ft:
       intersection_index.append(new_game[i])'''

intersection_index= list(new_game[i] for i in range(len(new_game)) if (ND.loc[game_result[i], 'game_victor']==1) and new_game[i] in Win_ft)
cond_probability= len(intersection_index)/len(Win_ft)
print("conditional probability")
print(cond_probability)
#print(intersection_index)
#print(Win_ft)

#Calculate the average rounds for winning games
rounds_list= list((game_result[i]-new_game[i]+1) for i in range(len(new_game)) if ND.loc[game_result[i], 'game_victor']==1)
avg_victor_rounds= sum(rounds_list)/len(rounds_list)
print("average rounds for winning games")
print(avg_victor_rounds)
consecutive_rounds= list((game_result[i]-new_game[i]+ 1) for i in range(len(new_game)) if (ND.loc[game_result[i], 'game_victor']==1) and new_game[i] in Win_ft)
avg_consecutive_rounds= sum(consecutive_rounds)/len(consecutive_rounds)
print("average rounds for winning games starting with two consecutive points")
print(avg_consecutive_rounds)
# regardless of the game results, the average round
general_rounds_list= list((game_result[i]- new_game[i]) for i in range(len(game_result)))
avg_general_rounds_list= sum(general_rounds_list)/len(general_rounds_list)
print("average rounds regardless of the game results")
print(avg_general_rounds_list)
