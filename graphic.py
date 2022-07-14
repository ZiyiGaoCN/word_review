print("Loading...")
import PySimpleGUI as sg
from word_app import word_app

#a=sg.popup_get_text('Technical English')
#print(a)
layout=[
    [sg.Text('Choose your function')],
    [sg.OK('Generate a empty wordnote')],
    [sg.OK('Generate a english wordnote')],
    [sg.OK('Generate a chinese wordnote')],
    [sg.Text('Note size'),sg.Input('20',size=(8,5))],
    [sg.Text('Note num'),sg.Input('1',size=(8,5))]
]

window=sg.Window('Technical English',layout)
app=word_app()

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
window.close()
