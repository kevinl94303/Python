"""
Name: Kevin Li
UNI: krl2134

create_FOF takes a dictionary of friends and returns a dictionary of all 
friends of friends for each entry
"""
def create_FOF(friends):
    #returns a list of friends of friends that are not friends

    friends_of_friends = {}
    for key in friends.keys():
        foflist = []
        for friend in friends[key]:
            if friend in friends.keys():
                for fof in friends[friend]:
                    if fof != key and fof not in friends[key]:
                            foflist.append(fof)
        friends_of_friends[key] = set(foflist)
    
    return friends_of_friends


if __name__ == '__main__':
    friends = {}
    friends["Caro"] = set(["Ben", "Yanlin", "Sahil"])
    friends["Sahil"] = set(["Caro", "James", "Shreyas"])
    friends["Vidya"] = set(["Caro", "Yanlin", "Sahil", "Shreyas"])
    friends["Ben"] = set(["Yanlin", "Caro", "Vidya"])

    fof = {}
    fof["Caro"] = set(["Vidya","James","Shreyas"])
    fof["Sahil"] = set(["Ben", "Yanlin"])
    fof["Vidya"] = set(["Ben", "James"])
    fof["Ben"] = set(["Sahil", "Shreyas"])

    print("Friends Input:", friends)
    print("Your output:", create_FOF(friends))
    print("Expected output:", fof)
