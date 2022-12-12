# author: JHR 12/9/22

# Defining the nested lists
rows = [["Darick", "Eugene", "Kyle", "Azaan"], ["Ryan",
"Phil", "Eman", "Alex", "Nicholas"],
["Christian", "Josh", "Matt", "Francesco"],
["Patrick", "Nico", "Trevayne"]]

# Defining the nested loops
for row in rows:
    for names in row:
        if names[-1] == "s":
            names+="'"
        else:
            names+="'s"
        print(names)