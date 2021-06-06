#import pandas and name file as df
import pandas as pd
df = pd.read_excel('NFLteams.xlsx')
#make lists for each column
nfl_teams = df['Team'].tolist()
nfl_conferences = df['Conference'].tolist()
nfl_divisions = df['Division'].tolist()
nfl_records = df['Record'].tolist()

#Establish blank list then build master list of all elements
test_list2 = []
i = 0
while i < 32:
    test_list2.append(nfl_teams[i])
    test_list2.append(nfl_conferences[i])
    test_list2.append(nfl_divisions[i])
    test_list2.append(nfl_records[i])
    i += 1

#Find out which teams don't end in the letter s
print("The NFL teams without s at the end of their name are...")
i_2 = 0
while i_2 < 32:
    if nfl_teams[i_2][-1].find("s",0,len(str(nfl_teams[i_2]))) == -1:
        #print(nfl_teams[i_2][-1].find("s",0,len(str(nfl_teams[i_2]))))
        print(nfl_teams[i_2])
    i_2 += 1