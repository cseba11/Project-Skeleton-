# CIIC 3015 Autumn 2021 Project 2 Skeleton
# Carlos Sebastian Hernandez Alvarado
# 802-20-2471

def Project2():
    CMD_BED = 'b'
    CMD_CLOSE = 'c'
    CMD_EAST = 'e'
    CMD_FEED = 'f'
    CMD_GET = 'g'
    CMD_LOCK = 'l'
    CMD_NORTH = 'n'
    CMD_OPEN = 'o'
    CMD_PUT = 'p'
    CMD_QUIT = 'q'
    CMD_SOUTH = 's'
    CMD_TV = 't'
    CMD_UNLOCK = 'u'
    CMD_WEST = 'w'
    

    ROOM_FRONT = 0
    ROOM_LIVING = 1
    ROOM_KITCHEN = 2
    ROOM_OFFICE = 3
    ROOM_BED = 4

    KEY = 0
    NUMSAFE = 0 
    PANTRY = 0
    OPEN = 0
    OPENPANTRY = 0 
    FOOD = 0
    FullyStella = 0
    tvOn = 0
    tvOff = 0
    PANTRYUNLOCK = 0
    PANTRYLOCK = 0
    NOKEY = 0
    SAFEOPEN = 0 
    SPAM = 0
    GRABEDSPAM = 0
    BEDTIME = 0
  




    ROOM_NAMES = ("Front Door", "Living Room", "Kitchen", "Office", "Bedroom")

    flag_me_awake = True
    flag_tv_on = False

    room = 0
    turn = 0

    print(
        "What an awful day! You are completely exhausted, all you want to do is climb into bed and collapse. Unfortunately, that is easier said than done…")
    print()
    print("CIIC 3015 Autumn 2021 Project 2: Time For Go-To-Bed")
    print()

    while flag_me_awake:
        print('                                                        Bedroom\n                                                           ^\n                                         Front Door < Living Room > Office  \n                                                           ↓\n                                                        Kitchen\n--------------------------------------------------------------------------\n-  b = bed, c = close, e = east, f = feed, g = get, l = lock, n = north  -\n-  o = open, p = put, q = quit, s = south, t = tv, u = unlock, w = west  -\n--------------------------------------------------------------------------\n')
        print("Location: ", ROOM_NAMES[room])
        
        cmd = input("> ")
        turn += 1

        if cmd == CMD_QUIT:
            return False
#'------------------------------------------------------------------------------------------'
        if room == ROOM_FRONT:
            if cmd == CMD_EAST:
                print("You enter your house.")
                room = ROOM_LIVING
                continue

#'------------------------------------------------------------------------------------------'

        if room == ROOM_LIVING:

            if cmd == CMD_SOUTH:
                print('You enter the Kitchen')
                room = ROOM_KITCHEN
                continue
           
                
            if cmd == CMD_EAST:
                print('You enter the Office')
                room = ROOM_OFFICE
                continue
                

            if cmd == CMD_WEST:
                  print("You are way too tired to face the world again just now. Best to remain indoors.")
                  continue

            if cmd == CMD_NORTH:
              if FullyStella == 1:
                print('You enter the Bedroom')
                room = ROOM_BED
                continue

              else:
                  print('Stella is Hungry and is blocking you.')
                  continue
          
            



            if cmd == CMD_TV:
              if flag_tv_on:
                  print("You turn off the tv.")
                  flag_tv_on = not flag_tv_on
                  tvOff = 1
                  tvOn = 0
                  continue
                    
              else:
                  print("You turn on the tv.")
                  flag_tv_on = not flag_tv_on
                  tvOn = 1
                  tvOff = 0
                  continue
              
            if cmd == CMD_FEED:
              if FOOD == 1:
                if FullyStella == 1:
                  print('You already give Stella food.')
                  continue

                if tvOn == 1:
                  print('Stella hungrily snatches the nice tasty bone out of you hand and starts to chew on it. She no longer seems to notice or care that you are here.')
                  FullyStella = 1
                  SPAM = 1
                  continue
                else:
                  print('Stella seems tense. She keeps glacing from the bone in your hand, to the silent tv, to you, and back to the silent tv again. Every now and then she makes a sad little noise.')
                  continue
              if FOOD == 0:
                print('First you need to look for food in the Kitchen.')
                continue

        


#'------------------------------------------------------------------------------------------'

        if room == ROOM_KITCHEN:

          if cmd == CMD_UNLOCK:
              if KEY ==  1: 
                if PANTRY == 0:
                  print('You unlock the pantry door.')             
                  PANTRY = 1 
                  PANTRYUNLOCK = 1

                  continue

                if PANTRY == 1:
                  print('The pantry door is already unlock.')
                  continue

              if KEY == 0:
                if PANTRY == 1:
                  print("You don't have the Key but the pantry door is already unlock.")
                  continue

                if PANTRYUNLOCK == 0 :
                  print('The pantry door is lock, you need a key to open it.')
                  continue

          if cmd == CMD_OPEN:          
            if PANTRY == 1:
              if FullyStella == 0:
                if OPEN == 0:              
                  print('The pantry door opens.')
                  print('Inside you see a nice tasty bone.')
                  OPEN = 1
                  PANTRYLOCK = 0
                  # OPENPANTRY = 1
                  continue

                if OPEN == 1:
                  print('The pantry door is already open')
                  continue
              if FullyStella == 1:
                if OPEN == 0:              
                  print('The pantry door opens.')
                  OPEN = 1
                  PANTRYLOCK = 0
                  continue

                if OPEN == 1:
                  print('The pantry door is already open')
                  continue



            
            
            if PANTRY == 0:
              print('The pantry door is close, you need a key to open it.')
              continue

          if cmd == CMD_CLOSE:
            # if OPENPANTRY == 1 :
            if OPEN == 1:
              #if PANTRYLOCK == 0:
                print('The pantry door closes.')
                PANTRYLOCK = 1
                PANTRYUNLOCK = 0
                OPEN = 0 
                OPENPANTRY = 0
                continue

              #if PANTRYLOCK == 1:
                #print('Pantry door is already close')
            if OPEN == 0:
              print('The pantry door is already close.')
          
          if cmd == CMD_LOCK:
            if PANTRYLOCK == 1:
              if KEY == 1:
                
                print('You lock the pantry door.')         
                PANTRYLOCK = 0
                PANTRYUNLOCK = 0
                continue
              if KEY == 0:
                print("you need the Key to lock it. ")
            if PANTRYLOCK == 0:
              print('First you need to close the pantry door')
                      
          if cmd == CMD_PUT:
            if OPEN == 1:
              if GRABEDSPAM == 1:
                print('You put the spam in the pantry door')
                #PANTRYLOCK = 1
                PANTRYUNLOCK =1
                BEDTIME = 1

                GRABEDSPAM = 0
                SPAM = 0
                continue

              else:
                print("You don't have nothing to put here")
                continue

            else:
              print('You need to unlock the pantry door first')
              continue
            


          # if cmd == CMD_GET:
          #   if OPEN ==  1: 
          #     print('You grab the bone for Stella from the pantry door. Stella watches you with great interest from the living room.')
          #     FOOD = 1 
          #     continue

          #   if OPEN == 0:             
          #     print('The pantry door is locked. You need a Key yo oppen it')
          #     continue

            
          if cmd == CMD_GET:
            if PANTRY == 1:
              if FullyStella == 1:
                print('You already gace Stella the food')
                #print
              if FOOD == 0:
                print('You take the nice tasty bone of the pantry. Stella watches you with great interest from the living room.')
                PANTRY = 0 
                FOOD = 1
                continue
              if FOOD == 1:
                print('You already grab the food.')
                continue

            if FullyStella == 1:
              print('You already gave Stella the food.')
              continue

            if PANTRY == 0:
              print('You already grab the food.')
              continue

          # if cmd == CMD_CLOSE:
          #   if OPEN == 1 :
          #     if PANTRYLOCK == 0:
          #       print('The pantry door closes.')
          #       PANTRYLOCK = 1
          #       PANTRYUNLOCK = 0
          #       OPEN = 0 
          #       continue
          #     if OPEN == 0:
          #       print('The pantry door is already close')
          
          # if cmd == CMD_LOCK:
          #   if PANTRYLOCK == 1:
          #     print('You lock the pantry door.')         
          #     PANTRYLOCK = 0
          #     continue
          #   else:
          #     print('First you need to close the pantry door')




              # else:
              #   print('The pantry door is open')
              # flag_pantry_lock = not flag_pantry_lock
              # continue


                # if cmd == CMD_TV:
                # if flag_tv_on:
                #     print("You turn off the tv.")
                    
                # else:
                #     print("You turn on the tv.")
                # flag_tv_on = not flag_tv_on
                # continue
            

          if cmd == CMD_SOUTH:
                print('You are not in the Living Room')
                continue

          if cmd == CMD_NORTH:
                print('You enter the Living Room')
                room = ROOM_LIVING
                continue
#'------------------------------------------------------------------------------------------'
        if room == ROOM_OFFICE:
          if cmd == CMD_OPEN:
            if SAFEOPEN == 0: 
                print('Please enter ther combination to the safe, one number at a time')
                print('You remember that it is the next three numbers in the Collatz        sequence after 42.')
                number1 = int(input('First number? '))
                number2 = int(input('Second number? '))
                number3 = int(input('Last number? '))
                if (number1 == 21) and (number2 == 64) and (number3 == 32):
                  if KEY == 0:
                    print('You hear a satisfying "Ka-CHUNK" as the handle turns and the safe door swings invitingly open. ')
                    print('Inside you see the pantry door key')
                    NUMSAFE = 1
                    SAFEOPEN = 1
                    continue
                  if KEY == 1:
                    print('You hear a satisfying "Ka-CHUNK" as the handle turns and the safe door swings invitingly open. ')
                    continue
                else:
                  print('Nope Thats not it. The locked safe silently mocks you')
                  continue
            if SAFEOPEN != 0:
              print('Safe is already open')
              continue      
          if cmd == CMD_GET :
            if (NUMSAFE == 1):
              if KEY == 0:
                print('You remove the pantry door key from the safe.')
                KEY = 1
                continue

              if KEY == 1:
                print('You already got the Key.')
                continue

            if (NUMSAFE == 0):
              print('You need to unlock the safe.')
              continue
            
          if cmd == CMD_CLOSE:
            if (NUMSAFE == 1):
              print('You close the safe and spin the dial a few times to reset it')
              NUMSAFE = 0
              NOKEY = 0
              SAFEOPEN = 0
              continue


          if cmd == CMD_PUT:
            if NUMSAFE == 1:
              if KEY == 1:
                print('you put key in safe')
                KEY = 0
                NOKEY = 1
                PANTRY = 0 
                #PANTRYUNLOCK = 0
                continue

              if KEY == 0:
                print('You already put the Key in safe.')
                continue

            if NUMSAFE == 0:
              print('You need to unlock the safe')
              continue

          if cmd == CMD_WEST:
            print('You enter the Living Room')
            room = ROOM_LIVING
            continue
          

#'------------------------------------------------------------------------------------------'

        if room == ROOM_BED:
          if cmd == CMD_SOUTH:
            print('You enter the Living Room')
            room = ROOM_LIVING
            continue
          
          # if SPAM == 1:
          #   print("You see a can of lovely spam. Wait, what's that doing in the bedroom?")
          #   continue

          if cmd == CMD_BED:
            if tvOn == 1:
              print('You can hear ramdom sounds coming from the television in the living room')
              #AnoyingNoiseON = 1
              continue
            if tvOff == 1:
              if PANTRYUNLOCK == 1:
                print('You keep thinking about that open pantry door and your OCD stresses you out too much')
                continue
              if PANTRYLOCK == 1:
                print('Wait...did ypu leave the pantry door unlocked? Better go check.')
                continue


              if KEY == 1:
                print('The pantry key in your pocket keeps digging into your leg. Best put it back.')
                continue
              
              if NOKEY == 1:
                print('You forget to lock the safe')
                continue
              
              if SPAM == 1:
                print('You should really put that can of lovely spam away in the pantry first.')
                #MAC = 1
                continue
              
              if BEDTIME == 1:
                print('Sleep! At last! You win!')
                break
              

          if cmd == CMD_GET:
            if SPAM == 1:
              print('You grab the can of lovely spam.')
              GRABEDSPAM = 1
              continue

        
                
                # if GRABEDSPAM == 1:
                #   print('You already have the spam.')
                #   continue
              
          
        
              #if 






              #if SAFEClOSE == 1:
                
              


              #continue 

            




      
        

        

            



              

          
        

          
          





        print("Illegal command.")

    print(turn, "turns played.")
    return True
print(Project2())