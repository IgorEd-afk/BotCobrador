import pyautogui
import time
import pandas as pd

pyautogui.hotkey('ctrl','a')


df = pd.read_excel('/home/igor/Documentos/Arquivos/planilha.xlsx')
col1 = df['CLIENTES'].tolist()
col2 = df['DEVENDO'].tolist()
aux = 0

time.sleep(2)
for nome in (col2):
    if nome == 'SIM':
        pyautogui.click(x=263, y=240)
        time.sleep(2)
        pyautogui.write(col1[aux])
        time.sleep(2)
        pyautogui.click(x=244, y=391)
        time.sleep(2)
        pyautogui.click(x=763, y=879)
        time.sleep(2)
        mensagem = f"Ola {col1[aux]}, você pode me enviar seu comprovante de pagamento para dar baixa no sistema?"
        pyautogui.write(mensagem)
        time.sleep(2)
        pyautogui.hotkey('ctrl','a')
        pyautogui.press('backspace')
        pyautogui.click(x=263, y=240)
        pyautogui.hotkey('ctrl','a')
        pyautogui.press('backspace')
    aux +=1

time.sleep(5)

x,y = pyautogui.position()

print(x,y)
#pyautogui.click(x=263, y=240)
