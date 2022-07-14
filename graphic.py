print("Loading...")
import PySimpleGUI as sg
from word_app import word_app
import random


#a=sg.popup_get_text('Technical English')
#print(a)
layout=[
    [sg.Text('Choose your function')],
    [sg.OK('Generate a empty wordnote')],
    [sg.OK('Generate a english wordnote')],
    [sg.OK('Generate a chinese wordnote')],
    [sg.OK('Review mode')],
    [sg.Text('Note size'),sg.Input('20',size=(8,5))],
    [sg.Text('Note num'),sg.Input('1',size=(8,5))]
]

window=sg.Window('Technical English',layout)
app=word_app()

def review_mode():
    print("hey!")
    OPEN=True
    while OPEN:
        word=app.random_word()
        word=word[random.randint(0,len(word)-1)]
        #print(word)
        if word not in app.dict:
            continue
        #print('emm')
        layout2=[
        [sg.Text(app.dict.query(word)['translation'])],
        [sg.Input(key=1)],
        [sg.OK(),sg.Button('hint',key='Hint')]
        ]
        window2=sg.Window('Review',layout2,finalize=True)
        window2.bind('<Button-3>','Hint')
        window2.bind('<Control-z>','Hint')
        testing=True
        while testing and OPEN:
            event,values=window2.read()
            print(event,':',values)
            if event==None:
                OPEN=False
            elif event=='Hint':
                print(word)
            elif values[1]==word:
                testing=False
        window2.close()            
    

while True:
    event,values=window.read()
    print(event)
    #print(values)
    for x in values.keys():
        values[x]=int(values[x])
    
    if event==None:
        break
    elif event=='Generate a empty wordnote':
        app.generate_word_note(lang='',size=values[0],num=values[1])
        print('Finish!')
    elif event=='Generate a english wordnote':
        app.generate_word_note(lang='english',size=values[0],num=values[1])
        print('Finish!')
    elif event=='Generate a chinese wordnote':
        app.generate_word_note(lang='chinese',size=values[0],num=values[1])
        print('Finish!')
    elif event=='Review mode':
        review_mode()
window.close()
