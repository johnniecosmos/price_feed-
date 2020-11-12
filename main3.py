#!/usr/bin/env python
import PySimpleGUI as sg
import time
from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()



# ----------------  Create Form  ----------------
sg.theme('Black')

layout = [[sg.Text('')],
          [sg.Text('', size=(30, 10), font=('Helvetica',18),
                justification='center', key='text')],]


window = sg.Window('Running Timer', layout,
                   no_titlebar=False,
                   auto_size_buttons=True,
                   keep_on_top=True,
                   grab_anywhere=True,
                   element_padding=(0, 0))


while True:
    # --------- Read and update window --------
        event, values = window.read(timeout=1)

        window['text'].update(cg.get_price(ids='secret', vs_currencies='usd'))
        time.sleep(5)
    
window.close()