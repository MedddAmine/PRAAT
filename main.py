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
    #if it detects any color other than white in the vertical line it means that it reached the base line and modify the vertical variable
    while im1.getpixel((xBORDER, i)) == color:
        i = i + 1
    i=i+5

def SelectParts():
    global x
    #if it detects any color other than white in the horizontal line it means that it reached the voice it press down in the left button in the mouse
    while im1.getpixel((x, i)) == color:
        x = x + 1
    pyautogui.moveTo(x, i)
    pyautogui.mouseDown(button='left')
    #if it detects the color white in the horizontal line it means that it reached the end of the voice it press up in the left button in the mouse which ends the selection
    while im1.getpixel((x, i)) != color or im1.getpixel((x+5, i)) != color or im1.getpixel((x+3, i)) != color:
        x = x + 5
    pyautogui.moveTo(x, i)
    pyautogui.mouseUp(button='left')
def Save():
    for save in range(0,12):
        SelectParts()
        #Pressing File button coordinates (x,y)
        pyautogui.click(5, 35)
        #Pressing Save as wav button coordinates (x,y)
        pyautogui.click(5,120)
        #File extracted name
        number = str(save+1)
        pyautogui.write(number+'.wav')
        pyautogui.press('enter')

def main():
    DetectBaseAudio()
    Save()

main()
