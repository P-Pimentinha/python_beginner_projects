def player_Movement(arg):
    if arg == 18:
        return "you found home"
    elif arg < 9:
        return "you are in the forest"
    elif arg < 21:
        return "you are in the town"
    elif arg < 33:
        return "you are on the beach"
    else:
        return "you are in the ocean"