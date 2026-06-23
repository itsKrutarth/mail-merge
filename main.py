with open("input/names.txt") as namesFile:
    names = namesFile.readlines()
    print(names)

    
    
    # for names in namesFile:
with open ("input/letter.txt", "r") as letterFile:
    letterDraft = letterFile.read()
    print(letterDraft)

for name in names:
    name = name.strip()
    customLetter = letterDraft.replace("[name]", name)
    print(customLetter)
    #         for lines in letterFile:
    with open(f"output/{name}.txt", "w") as outputLetter:
        outputLetter.write(customLetter)