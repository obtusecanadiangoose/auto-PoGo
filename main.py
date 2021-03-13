import numpy as np
import cv2
import mss
import mss.tools
import pyautogui
import operator
import time
from PIL import Image, ImageGrab
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from sklearn.cluster import KMeans

"""
TODO:
- Program crashes when tapping on a raid that is in range
"""

def visualize_colors(cluster, centroids):
    labels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
    (hist, _) = np.histogram(cluster.labels_, bins=labels)
    hist = hist.astype("float")
    hist /= hist.sum()

    rect = np.zeros((50, 300, 3), dtype=np.uint8)
    try:
        colors = sorted([(percent, color) for (percent, color) in zip(hist, centroids)])
        return colors[-1][1][0] + colors[-1][1][1] + colors[-1][1][2]
    except:
        return 450
    # print(colors)
    # print(colors[-1][1][1])
    #return colors[-1][1][1]
    
    #return colors[-1]


def stopormon():
    #image = ImageGrab.grab(bbox=(689, 336, 992, 440))
    image = ImageGrab.grab(bbox=(689, 336, 992, 640))
    image.save('stopormon.png')

    image = cv2.imread('stopormon.png')
    #result = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 0, 202])
    upper = np.array([179, 65, 255])

    mask = cv2.inRange(image, lower, upper)
    
    image_to_text = pytesseract.image_to_string(mask, lang='eng')
    print("Poke-name: "+image_to_text)
    if "cp" in image_to_text.lower() or "ce" in image_to_text.lower() \
       or "©" in image_to_text.lower() or "@" in image_to_text.lower():
        return "mon"

    image = ImageGrab.grab(bbox=(608, 1000, 1068, 1030))
    image.save('stopormon.png')
    image = cv2.imread('stopormon.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    reshape = image.reshape((image.shape[0] * image.shape[1], 3))

    cluster = KMeans(n_clusters=5).fit(reshape)
    try:
        visualize = visualize_colors(cluster, cluster.cluster_centers_)
        # visualize = cv2.cvtColor(visualize, cv2.COLOR_RGB2BGR)
        print(str(int(visualize)))
        if int(visualize) >= 449:
            return "pink"
        elif 500 > int(visualize) >= 352:
            return "blue"
        elif 352 > int(visualize) >= 130:
            return "black"
        else:
            return "rocket"
    except:
        return False


def ready2catch():
    #x, y, w, h
    image = ImageGrab.grab(bbox=(1015, 890, 1009 + 45, 890 + 45))
    image.save('ready2catch.png')
    image = cv2.imread('ready2catch.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    reshape = image.reshape((image.shape[0] * image.shape[1], 3))

    cluster = KMeans(n_clusters=5).fit(reshape)
    try:
        visualize = visualize_colors(cluster, cluster.cluster_centers_)
        # visualize = cv2.cvtColor(visualize, cv2.COLOR_RGB2BGR)
        print(str(int(visualize)))
        if 413 <= int(visualize) <= 427:
            print("main")
            return False
        else:
            print("not main")
            return True
    except:
        return False


def getstars():
    image = ImageGrab.grab(bbox=(692, 684, 692 + 30, 684 + 30))
    image.save('getstars.png')
    image = cv2.imread('getstars.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    reshape = image.reshape((image.shape[0] * image.shape[1], 3))

    cluster = KMeans(n_clusters=5).fit(reshape)
    visualize = visualize_colors(cluster, cluster.cluster_centers_)
    # visualize = cv2.cvtColor(visualize, cv2.COLOR_RGB2BGR)
    print(str(int(visualize)))
    if int(visualize) < 730:
        return True
    else:
        return False


def succCatch():
    image = ImageGrab.grab(bbox=(702, 580, 702 + 277, 580 + 80))
    image.save('succCatch.png')
    image = Image.open('succCatch.png')
    image_to_text = pytesseract.image_to_string(image, lang='eng')
    print(image_to_text)
    return "total" in image_to_text.lower()


def checkblacklist():
    #image = ImageGrab.grab(bbox=(689, 336, 992, 440))
    image = ImageGrab.grab(bbox=(689, 336, 992, 640))
    image.save('blacklist.png')

    image = cv2.imread('blacklist.png')
    result = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 0, 202])
    upper = np.array([179, 65, 255])

    mask = cv2.inRange(image, lower, upper)
    image_to_text = pytesseract.image_to_string(mask, lang='eng')
    blacklist = ["hoothoot", "ygon", "yanma", "ursa",
                 "zubat", "spoink", "shuppet", "makuhita",
                 "skarmory", "chinchou", "gastly", "doduo",
                 "heatmor", "chespin", "swinub", "spheal",
                 "noctowl", "Doduo"
                 ]
    print(image_to_text)
    for poke in blacklist:
        if poke in image_to_text[:-2].lower():
            return True
    return False

def isgym():
    time.sleep(3)
    image = ImageGrab.grab(bbox=(721, 115, 936, 142))
    image.save('isgym.png')
    image = Image.open('isgym.png')
    image_to_text = pytesseract.image_to_string(image, lang='eng')
    if "gym" in image_to_text.lower() :
        return True
    else:
        return False

def getpoke():
    image = ImageGrab.grab(bbox=(714, 442, 714 + 252, 442 + 50))
    image.save('getpoke.png')
    image = Image.open('getpoke.png')
    image_to_text = pytesseract.image_to_string(image, lang='eng')
    return image_to_text[:-2]

for i in range(0, 0, -1):
    print(i)
    time.sleep(1)

while True:
    # mainSC()
    #image = ImageGrab.grab(bbox=(609, 300, 609 + 462, 300 + 580))
    image = ImageGrab.grab(bbox=(690, 600, 1019, 853))
    image.save('main.png')

    image = cv2.imread('main.png')
    result = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #old
    lower = np.array([0, 0, 0])
    upper = np.array([6, 255, 241])

    #lower = np.array([0, 0, 0])
    #upper = np.array([33, 255, 130])

    mask = cv2.inRange(image, lower, upper)

    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(mask, kernel, iterations=8)

    contours, hierarchy = cv2.findContours(dilated,
                                cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


    areas = {}
    for dot in contours:
        x, y, w, h = cv2.boundingRect(dot)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        #areas[w * h] = (x + 609 + w // 2, y + 300 + h // 2)
        areas[w * h] = (x + 690 + w // 2, y + 600 + h // 2)
    areas = dict(sorted(areas.items(), key=operator.itemgetter(0)))
    keys = list(areas)
    try:
        areas.pop(keys[-1])
    except:
        pass
    #print(len(areas))
    '''
    for i in range(len(areas)-1, -1, -1):
        pyautogui.moveTo(areas[keys[i]][0], areas[keys[i]][1])
        pyautogui.click()
        time.sleep(3)
        if ready2catch():
            break
    '''
    try:
        #pyautogui.moveTo(areas[keys[0]][0], areas[keys[0]][1])
        pyautogui.moveTo(areas[keys[-2]][0], areas[keys[-2]][1])
        pyautogui.click()
    except:
        pass

    time.sleep(3)
    if ready2catch():

        if isgym():
            print("gym")
            pyautogui.moveTo(1015, 979)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(653, 534)
            pyautogui.dragTo(1025, 534, 0.3, button='left')
            time.sleep(2)
            pyautogui.moveTo(840, 977)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(840, 977)
            pyautogui.click()

        else:
            penis = stopormon()
            if penis == "blue" or penis == "pink":
                print("unspun pokestop")
                pyautogui.moveTo(653, 534)
                pyautogui.dragTo(1025, 534, 0.3, button='left')
                time.sleep(1)
                pyautogui.moveTo(840, 977)
                pyautogui.click()
            #elif penis == "pink":
            #    print("already spun pokestop")
            #    pyautogui.moveTo(840, 977)
            #    pyautogui.click()
            elif penis == "black":
                print("rocketstop")
                pyautogui.moveTo(653, 534)
                pyautogui.dragTo(1025, 534, 0.3, button='left')
                time.sleep(1)
                pyautogui.moveTo(840, 977)
                pyautogui.click()
                time.sleep(1)
                pyautogui.click()
                time.sleep(1)
                pyautogui.click()
                time.sleep(1)
                pyautogui.click()
                time.sleep(1)
                pyautogui.click()
                time.sleep(1)
            elif penis == "rocket":
                print("rocket battle")
                pyautogui.moveTo(840, 977)
                pyautogui.click()
                time.sleep(1)
                pyautogui.click()
                time.sleep(1)
                pyautogui.click()
                time.sleep(1)
                pyautogui.click()
                time.sleep(1)
                pyautogui.click()
                time.sleep(1)

            elif penis == "mon":
                catchscreen = True
                if checkblacklist():
                    print("blacklisted pokemon detected")
                    catchscreen = False
                    pyautogui.moveTo(659, 146)
                    pyautogui.click()

                #if not checkblacklist():
                #    print("blacklisted pokemon detected")
                #    catchscreen = False
                #    pyautogui.moveTo(659, 146)
                #    pyautogui.click()

                throws = 0

                while catchscreen:
                    pyautogui.moveTo(841, 973)
                    pyautogui.dragTo(841, 422, 0.3, button='left')
                    throws += 1
                    print("Throws: " + str(throws))

                    time.sleep(14)

                    if throws == 5:
                        catchscreen = False
                        pyautogui.moveTo(659, 146)
                        pyautogui.click()
                        print("Timed out - Threw 5 balls but couldn't catch it")



                    if not ready2catch():
                        catchscreen = False
                        print("The pokemon must have fled :(")

                    elif succCatch():
                        catchscreen = False
                        time.sleep(3)
                        pyautogui.moveTo(840, 680)
                        pyautogui.click()
                        time.sleep(1)
                        poke = getpoke()
                        '''
                        pyautogui.moveTo(1000, 970)
                        pyautogui.click()
                        time.sleep(1)
                        pyautogui.moveTo(1010, 793)
                        pyautogui.click()
                        time.sleep(1)
                        pyautogui.click()
                        time.sleep(1)
                        stars = getstars()
                        if stars:
                            print("Caught a 3*" + getpoke() + " in " + str(throws) + " throws!")
                            pyautogui.click()
                            time.sleep(1)
                            pyautogui.moveTo(840, 970)
                            pyautogui.click()
                            time.sleep(1)
                        '''
                        if False:
                            pass
                        else:
                            #print("Caught a less than 3* " + getpoke() + " in " + str(throws) + " throws, transferring")
                            print("Caught a "+poke+", Transferring...")
                            pyautogui.click()
                            time.sleep(1)
                            pyautogui.moveTo(1000, 970)
                            pyautogui.click()
                            time.sleep(1)
                            pyautogui.moveTo(1010, 877)
                            pyautogui.click()
                            time.sleep(1)
                            pyautogui.moveTo(844, 620)
                            pyautogui.click()
                            time.sleep(1)


    # print("congrats on the catch!")

    # cv2.imshow('Penis', image)
    # cv2.waitKey(0)

    # cv2.destroyAllWindows()

else:
    print(ready2catch())

# cv2.imshow('mask', mask)
# cv2.waitKey()


# 840, 525
# 590, 275
# 609, 76
