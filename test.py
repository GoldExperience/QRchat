import qrcode
from pyzbar.pyzbar import decode
import pyautogui
import PySimpleGUI as sg
import win32clipboard as clip
import win32con
from io import BytesIO

sg.theme('DarkAmber')

layout = [
    [sg.Text("文本输入/展示")],
    [sg.Multiline(size=(50, 5), key="_textBox_")],
    [sg.Button('生成二维码'), sg.Button('获取二维码信息')],
    [sg.Text("Info", size=(50, 1), key="_Info_")]
]

# Create the window
window = sg.Window("QR加密聊天", layout=layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window
    if event is None or event == 'Exit':
        break
    if event == '生成二维码':
        window.Element('_Info_').update('已生成二维码到剪贴板')
    if event == '获取二维码信息':
        pass

window.close()