import pandas as pd
#read csv file
euro12 = pd.read_csv(r'C:\Users\user\Documents\pandas\Euro_2012_stats_TEAM.csv')

#filter only on Goals column
#print(euro12['Goals'])

# filter of how many Teams participated in the Euro2012
#print(euro12.Team.count())

# see how many columns we have in our df
#print(euro12.info())

# #creating new  column named discipline who contains relevant columns
#discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
#print(discipline)

#Sorting  the teams by Red Cards, then to Yellow Cards
#sorting_teams = discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending = False)
#print(sorting_teams)

#Calculate the mean Yellow Cards given per Team
#mean_yellow_cards_per_team = (discipline['Yellow Cards'].mean())
#print(mean_yellow_cards_per_team)


#filter teams that scored more than 6 goals
#euro12[euro12.Goals > 6]

#Select the teams that start with G
#euro12[euro12.Team.str.startswith('G')]

#Select the first 7 columns
#print(euro12.head(7))

# Select all columns except the last 3
#euro12.iloc[: , :-3]

#filter only the Shooting Accuracy from England, Italy and Russia
#euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']]


