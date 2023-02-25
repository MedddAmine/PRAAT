import pyautogui, time

# pixel border #110, 96
xBORDER = 110
yBORDER = 100
color = (255, 255, 255)
time.sleep(2)
im1 = pyautogui.screenshot()
i: int = 120
x=110

def DetectBaseAudio():
    global i
    pyautogui.moveTo(xBORDER, yBORDER)
    while im1.getpixel((xBORDER, i)) == color:
        i = i + 1
    print(im1.getpixel((i, yBORDER)))
    i=i+5

def SelectParts():
    global x
    while im1.getpixel((x, i)) == color:
        x = x + 1
    pyautogui.moveTo(x, i)
    pyautogui.mouseDown(button='left')
    while im1.getpixel((x, i)) != color or im1.getpixel((x+5, i)) != color or im1.getpixel((x+3, i)) != color:
        x = x + 5
    pyautogui.moveTo(x, i)
    pyautogui.mouseUp(button='left')
def Save():
    for save in range(0,12):
        SelectParts()
        pyautogui.click(5, 35)
        pyautogui.click(5,120)
        number = str(save+1)
        pyautogui.write(number+'.wav')
        pyautogui.press('enter')

def main():
    DetectBaseAudio()
    Save()

main()
