#this is my first experiment with webbrowser and time in form of a tiny project
#kumar atulya B.tech C.s.e 4th year
#psychozonestartshere@gmail.com
import time
import webbrowser
#total number of breaks as i have to take 5 breaks 
total_breaks = 6
break_count = 0 #initiated to zero

print("this psycho program started on " +time.ctime()) #printing the time stats on starting the program
while(break_count < total_breaks ) :
    if break_count == 0 :
        
        time.sleep(10) #first break
    
        webbrowser.open("https://www.youtube.com/watch?v=mxva6l4bCSI") #fikar not chichore movie
        break_count+=1

        if break_count ==1 :    # second break
            time.sleep(60)
            webbrowser.open("https://www.youtube.com/watch?v=kfuSG7uZArs")
            break_count+=1
            if break_count==2 :
                time.sleep(60)
                webbrowser.open("https://www.youtube.com/watch?v=eVTXPUF4Oz4")
                break_count+=1
                if break_count==3 :
                    time.sleep(60)
                    webbrowser.open("https://www.youtube.com/watch?v=-oCCnxBos10")
                    break_count+=1
                    if break_count==4 :
                        time.sleep(60)
                        webbrowser.open("https://www.youtube.com/watch?v=wp3kcWOda6k")
                        break_count+=1
                        if break_count==5 :
                            time.sleep(60)
                            webbrowser.open("https://www.youtube.com/watch?v=iSallxKpm8Y")
                            break_count+=1
            
            
