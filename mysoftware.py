import os

while True:
    print()
    p=input("Enter your requirement : ")
    p=p.lower()
    if(("exit" in p) or ("close" in p) or ("discard" in p) or ("egress" in p) or ("quite" in p) or ("out" in p) or ("escape" in p) or ("shut down" in p) or ("back" in p) or ("finish" in p) or ("finished" in p)or("end" in p)or("return to" in p) or("conclude" in p) or("stop" in p)  or("home" in p)):
        print("You are out")
        break
        
      # if user dont wants to open anything  
    elif(("don't" in p)or("never" in p)or("dont" in p)) and ( ("browser" in p)or("chrome" in p)or("google" in p)or("search engine" in p) or ("editor" in p) or ("notepad" in p) or("type writer" in p) or ("wmplayer" in p)or("player" in p)or("media player" in p)or("windows media player" in p)or("play" in p)or("song" in p) or("songs" in p) or ("videos" in p) or("video" in p)or ("window media player" in p)):

            
            while True:
                print()
                print("ok! Enter your choise")
                s=input("press 1 to continue or press 0 to exit : ")
                if(s=="1"):
                    break
                elif(s=="0"):
                    break
                else:
                    print("Invalid input: Try again")
                    continue
            if(s=="1"):
                continue
            else:
                print("You are out")
                break

    #program to run chrome
    elif(("run"in p) or ("execute" in p) or ("open" in p) or ("launch" in p) or ("start" in p) or ("go to" in p) or ("into" in p) or ("starts" in p) or ("want" in p) or ("enter" in p))and(("browser" in p)or("chrome" in p)or("google" in p)or("search engine" in p)):
            
            # opening chrome 
            print("opening chrome")
            os.system("chrome")

    #program to run notepad
    elif(("run"in p) or ("execute" in p) or ("open" in p) or ("launch" in p) or ("start" in p) or ("go to" in p) or ("into" in p) or ("starts" in p) or ("want" in p) or ("enter" in p))and(("editor" in p) or ("notepad" in p) or("type writer" in p)):
            
            # opening notepad
            print("opening editor")
            os.system("notepad")

    #program to run wmplayer
    elif(("run"in p) or ("execute" in p) or ("open" in p) or ("launch" in p) or ("start" in p) or ("go to" in p) or ("into" in p) or ("starts" in p) or ("want" in p)or("play" in p) or ("enter" in p)) and(("wmplayer" in p)or("player" in p)or("media player" in p)or("windows media player" in p)or("play" in p)or("song" in p) or("songs" in p) or ("videos" in p) or("video" in p)):
            
            #opening wmplayer    
            print("opening windows media player")
            os.system("wmplayer")
          
    
  # if user enter invalid input 
    else:
        print("Oops! You have Entered something wrong...please try again ")
