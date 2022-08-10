# generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].


subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hckey", "Football"]

for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            print("%s %s %s." %(subjects[i], verbs[j], objects[k]))
