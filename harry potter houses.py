print('I am the sorting hat 🎩')

name = input("What's your name? ")

match name: 
    case "Harry" | "Hermione" | "Ron" | "Ginny" | "Fred" | "George" | "Neville" | "Dumbledore" | "Hagrid" | "James" | "Lily" | "Remus" | "Sirius Black" | 'Peter' | 'Fiona':
        print("Gryffindor")
    case "Draco" | "Snape" | 'Voldemort' | 'Lucius' | 'Bellatrix' :
        print("Slytherin")
    case "Luna" | "Cho" | 'Jake':
        print('Ravenclaw')
    case "Cedric" | 'Lisa' | 'David':
        print('Hufflepuff')        
    case _:
        print("Who?")