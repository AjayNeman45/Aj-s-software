while True:
    print()
    p=input("Enter your requirement : ")
    p=p.lower()
    if(("exit" in p) or ("close" in p) or ("discard" in p) or ("egress" in p) or ("quite" in p) or ("out" in p) or ("escape" in p) 
    or ("shut down" in p) or ("back" in p) or ("finish" in p) or ("finished" in p)or("end" in p)or("return to" in p) or("conclue" in p) or("stop" in p)  or("home" in p)):
        print("You are out")
        break

    #program to run chrome
    elif(("run"in p) or ("execute" in p) or ("open" in p) or ("launch" in p) or ("start" in p) or ("go to" in p) or ("into" in p) or ("starts" in p) or ("want" in p) or ("enter" in p))and(("browser" in p)or("chrome" in p)or("google" in p)or("search engine" in p)):
        if("not" in p)or("don't" in p)or("never" in p)or("dont" in p):
            s=int(input("press 1 to continue or press 0 to exit : "))
            if(s==1):
                continue
            else:
                print("You are out")
                break
        print("opening chrome")

    #program to run notepad
    elif(("run"in p) or ("execute" in p) or ("open" in p) or ("launch" in p) or ("start" in p) or ("go to" in p) or ("into" in p) or ("starts" in p) or ("want" in p) or ("enter" in p))and(("editor" in p) or ("notepad" in p) or("type writer" in p)):
        if("not " in p)or("don't" in p)or("never" in p)or("dont" in p):
            s=int(input("press 1 to continue or press 0 to exit : "))
            if(s==1):
                continue
            else:
                print("You are out")
                break
        print("opening editor")

    #program to run wmplayer
    elif(("run"in p) or ("execute" in p) or ("open" in p) or ("launch" in p) or ("start" in p) or ("go to" in p) or ("into" in p) or ("starts" in p) or ("want" in p)or("play" in p) or ("enter" in p)) and(("wmplayer" in p)or("player" in p)or("media player" in p)or("windows media player" in p)or("play" in p)or("song" in p) or("songs" in p) or ("videos" in p) or("video" in p)):
        if("not" in p)or("don't" in p)or("never" in p)or("dont" in p):
            s=int(input("press 1 to continue or press 0 to exit : "))
            if(s==1):
                continue
            else:
                print("You are out")
                break
        print("opening windows media player")

        
    else:
        print("don't support")

