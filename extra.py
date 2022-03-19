directory = [
    {'name': "Megan Bailey", 'hair': "Black", 'eyes': "Brown", 'species': 'dog', 'nationality': "USA"},
    {'name': "Wallace", 'hair': None, 'eyes': "black", 'species': 'human', 'nationality': "UK"},
    {'name': "Gromit", 'hair': "brown", 'eyes': "black", 'species': 'dog', 'nationality': "UK"},
    {'name': "Wendoline Ramsbottom", 'hair': "brown", 'eyes': "Black", 'species': 'human', 'nationality': "UK"},
    {'name': "Mr. Blobby", 'hair': "pink", 'eyes': "green", 'species': 'blob', 'nationality': "UK"},
    {'name': "Bob McKenzie", 'hair': "brown", 'eyes': "green", 'species': 'human', 'nationality': "CA"},
    {'name': "Doug McKenzie", 'hair': "blond", 'eyes': "blue", 'species': 'human', 'nationality': "CA"},
    ]
# side note: d = {1: 'a', 2: 'b', 3: True, 4: False}
MESSAGE_TEXT = {True: "Welcome to Pottersville Bank!",
             False: "I'm sorry, we could not find your records.  Please call Pottersville Bank at 800-WE-NASTY"
             }

login_result = login(username)
print(MESSAGE_TEXT[login_result])
# Store some people in variables [] are index operator 
megan = directory[0]
wendoline = directory[3]
blobby = directory[4]
# Fill in the following strings:
print(f"Megan had {megan['eyes']} eyes and {megan['hair']} hair.")
print(f"Wendoline has {wendoline['eyes']} eyes and {wendoline['hair']} hair.")
print(f"Mr. Blobby has {blobby['eyes']} eyes and {blobby['hair']} hair.")
# make a function to return True or False if the person is British
def is_british(person):
    # your code here
    pass