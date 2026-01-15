def deep():
    thought = input("What is the Great Question of Life, the Universe and Everything? \n")
    clear_thought = thought.lower().strip()
    match clear_thought:
        case "42" | "forty-two" | "forty two" :
            print("Yes")
        case _:
            print("No")

deep()
