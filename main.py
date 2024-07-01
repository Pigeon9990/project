import tkinter
import tkinter.font as tkFont
window = tkinter.Tk()
window.title('한국여행지추천')
window.geometry('600x400+100+100')
title_font = tkinter.font.Font(family='맑은고딕',size=40)
title = tkinter.Label(window,text='한국여행지추천',font=title_font)
title1_font = tkinter.font.Font(family='맑은고딕',size=20)

image1 = tkinter.PhotoImage(file='팔공산.png')
image2 = tkinter.PhotoImage(file='이월드.png')
image3 = tkinter.PhotoImage(file='이이.png')
image4 = tkinter.PhotoImage(file='막창.png')
image5 = tkinter.PhotoImage(file='청송.png')

label1 = tkinter.Label(window,image=image1)


def start_next_screen(): #정의
    print('TEST')
    
    for widget in window.winfo_children(): 
        widget.destroy()
    
    
    next_screen_title_font = tkFont.Font(family='맑은고딕', size=30)
    next_screen_title = tkinter.Label(window, text='여행지 고르기', font=next_screen_title_font)
    next_screen_title.pack(pady=20)
    
    next_screen_label = tkinter.Label(window, text='대구'   )
    next_screen_label.pack(pady=10)
    label1 = tkinter.Label(window,)
    label1.place(x=50, y=100)
    next_screen_label.place(x=80,y=200)
    button = tkinter.Button(window,image=image2,command=start_next_screen2)
    button.place(x=50, y=100, width=100, height=100)
    button2 = tkinter.Button(window,image=image5,command=start_next_screen6)
    button2.place(x=200, y=100, width=100, height=100)
    next_screen_label2 = tkinter.Label(window, text='청송'   )
    next_screen_label2.pack(pady=10)
    next_screen_label2.place(x=230,y=200)
    
def start_next_screen2():
    print('TEST')

    for widget in window.winfo_children():
        widget.destroy()
    next_screen_label2 = tkinter.Label(window,image=image3 )
    # next_screen_label2.place(x=80,y=150)
    next_screen_label2.place(x=0,y=0)
    next_screen2_title_font = tkFont.Font(family='맑은고딕', size=50)
    next_screen2_title = tkinter.Label(window,text='이월드', font=next_screen2_title_font)
    
    next_screen2_title.pack(pady=20)

    next_screen_label = tkinter.Label(window, text='대구에서 가장 큰 놀이공원 이월드! 이월드는 국내에서 가장 높은 스카이드롭과\n 다양한 놀이기구들이 갖추어져 있습니다. 가서 즐거운 시간을 보내보아요')
    next_screen_label.pack(pady=10)
    label1 = tkinter.Label(window,)
    label1.place(x=50, y=100)
    next_screen_label.place(x=80,y=350)
    button2 = tkinter.Button(window,text='다음으로',command=start_next_screen3)
    button2.place(x=500, y=250, width=100, height=100)


def start_next_screen3():
    print('TEST')
    
    for widget in window.winfo_children():
        widget.destroy()
    for widget in window.winfo_children():
        widget.destroy()
    next_screen_label2 = tkinter.Label(window,image=image1 )
    # next_screen_label2.place(x=80,y=150)
    next_screen_label2.place(x=0,y=0)
    next_screen2_title_font = tkFont.Font(family='맑은고딕', size=50)
    next_screen2_title = tkinter.Label(window,text='팔공산', font=next_screen2_title_font)
    
    next_screen2_title.pack(pady=20)

    next_screen_label = tkinter.Label(window, text='사계절 각각 새로운 모습을 지닌 팔공산! 대구에서 가장 유명한 산 중 하나입니다.\n 팔공산에서 멋진 풍경과 건강을 함께 채워 보아요!')
    next_screen_label.pack(pady=10)
    label1 = tkinter.Label(window,)
    label1.place(x=50, y=100)
    next_screen_label.place(x=80,y=350)
    button2 = tkinter.Button(window,text='다음으로',command=start_next_screen4)
    button2.place(x=500, y=250, width=100, height=100)


def start_next_screen4():
    print('TEST')

    for widget in window.winfo_children():
        widget.destroy()
    next_screen_label2 = tkinter.Label(window,image=image4 )
    # next_screen_label2.place(x=80,y=150)
    next_screen_label2.place(x=0,y=0)
    next_screen2_title_font = tkFont.Font(family='맑은고딕', size=50)
    next_screen2_title = tkinter.Label(window,text='음식', font=next_screen2_title_font)
    
    next_screen2_title.pack(pady=20)

    next_screen_label = tkinter.Label(window, text='대구에서 가장 유명한 음식은 막창입니다. 막창은 \n 소와 돼지의 내장(창자) 끄트머리 부위, 혹은 이것으로 만든 음식을 뜻 합니다.')
    next_screen_label.pack(pady=10)
    label1 = tkinter.Label(window,)
    label1.place(x=50, y=100)
    next_screen_label.place(x=80,y=350)
    button2 = tkinter.Button(window,text='다음으로',command=start_next_screen5)
    button2.place(x=500, y=250, width=100, height=100)

def start_next_screen5():
    print('TEST')

    for widget in window.winfo_children():
        widget.destroy()
    next_screen_label2 = tkinter.Label(window, )
    # next_screen_label2.place(x=80,y=150)
    next_screen_label2.place(x=0,y=0)
    next_screen2_title_font = tkFont.Font(family='맑은고딕', size=50)
    next_screen2_title = tkinter.Label(window,text='추천 끝', font=next_screen2_title_font)
    
    next_screen2_title.pack(pady=20)

    next_screen_label = tkinter.Label(window, text='')
    next_screen_label.pack(pady=10)
    label1 = tkinter.Label(window,)
    label1.place(x=50, y=100)
    next_screen_label.place(x=80,y=350)
    button2 = tkinter.Button(window,text='처음으로',command=start_next_screen)
    button2.place(x=500, y=250, width=100, height=100)

    
def start_next_screen6():
    print('TEST')
  
    for widget in window.winfo_children():
        widget.destroy()
    
    
    next_screen_title_font = tkFont.Font(family='맑은고딕', size=30)
    next_screen_title = tkinter.Label(window, text='여행지 고르기', font=next_screen_title_font)
    next_screen_title.pack(pady=20)
    
    next_screen_label = tkinter.Label(window, text='준비중'   )
    next_screen_label.pack(pady=10)
    label1 = tkinter.Label(window,)
    label1.place(x=50, y=100)
    button2 = tkinter.Button(window,text='처음으로',command=start_next_screen)
    button2.place(x=500, y=250, width=100, height=100)
    

   
title.pack()
label1.place(x=0, y=0)
label1.lower()
button = tkinter.Button(window, text='시작하기!!',command=start_next_screen)
# button.place(side='right')
# button.place(fill=10, ipady=10)
button.place(x=400, y=300, width=200, height=50)






window.mainloop()