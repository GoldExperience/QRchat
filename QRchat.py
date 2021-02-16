import qrcode
from pyzbar.pyzbar import decode
import cv2
import pyautogui
import numpy as np
import PySimpleGUI as sg
import win32clipboard as clip
import win32con
from io import BytesIO


def setImage(frame):
    output = BytesIO()
    frame.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    clip.OpenClipboard()
    clip.EmptyClipboard()
    clip.SetClipboardData(win32con.CF_DIB, data)
    clip.CloseClipboard()


def get_QR_content():
    frame = pyautogui.screenshot()
    barcords = decode(frame)
    text_info = ''
    qr_count = 0
    for barcode in barcords:
        # x, y, w, h = barcode.rect
        barcode_info = barcode.data.decode('utf-8')
        text_info += barcode_info + '\n'
        qr_count += 1
    return text_info, qr_count


sg.theme('DarkAmber')

layout = [
    [sg.Text("输入信息")],
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
        frame = qrcode.make(values['_textBox_'])
        setImage(frame)
        window.Element('_Info_').update('已生成二维码到剪贴板')
    if event == '获取二维码信息':
        text, count = get_QR_content()
        if (count == 0):
            window.Element('_Info_').update('没有找到二维码')
        window.Element('_textBox_').update(text)
        window.Element('_Info_').update(f'找到了{count}个二维码')

window.close()
