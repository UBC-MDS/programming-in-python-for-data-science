import pandas as pd

# The database 

hockey_players = pd.read_csv('data/canucks.csv', index_col = 0)

# Save`Thatcher Demko`'s salary in an object named`demko_paid`. 

demko_paid = hockey_players.loc["Thatcher Demko", "Salary"]
demko_paid

# How old is `Zack MacEwen`? Save it as object `macewen_age`.

macewen_age = hockey_players.loc["Zack MacEwen", "Age"]
macewen_age

# What position does `Jacob Markstrom` play? Save this as object `markstrom_position`.

markstrom_position = hockey_players.loc["Jacob Markstrom", "Position"]
markstrom_position

# When was `Justin Bailey` born? Save it as an object named `bailey_birth`. 

bailey_birth = hockey_players.loc["Justin Bailey", "Birth Date"]
bailey_birth
