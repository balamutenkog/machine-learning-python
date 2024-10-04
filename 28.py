songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"] 
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key: value for key, value in zip(songs, playcounts)}
print(plays)
plays.update({"Purple Haze": 1, "Respect": 5})
empty_library = {}
library = {"The Best songs:": plays, "Sunday Feelings": empty_library}
print(library)