sum=0
while (sum<100 ):
    if(sum<=100):
        put=int(input("player 1 play "))
    
        while (put>10) or (put<1) :
            print ("THIS IS NOT LEGAL")
        
            put=(int(input("play 1 more time")))
        if sum<=100:
            sum =sum+put
            print ("SUM=" ,sum)
        if sum>=100 :
            print ("congratulations for one")
            break    

         #player two
    if(sum<=100):
        put2=int(input("player 2 play ") )
        while (put2>10) or (put2<1):
            print ("THIS IS NOT LEGAL")
            put2=(int(input("play 1 more time")))
        if sum<=100:
            sum =sum+put2
            print ("SUM=" ,sum)
        if sum>=100 :
            print ("congratulations for two")
            break    
