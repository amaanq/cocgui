import PySimpleGUI as sg
import urllib.request
import json, random, os, concurrent.futures, email, imaplib
from ppadb.client import Client as adb
from time import time, sleep
if __name__ != "__main__":
    from projectgui.message import message
    from projectgui.mailmaker import e_mail
    from projectgui.cosopener import tag
    from projectgui.scidcodepuller import code
else:
    from message import message
    from mailmaker import e_mail
    from scidcodepuller import code
    from cosopener import tag
from math import floor
from pyperclip import copy
from winsound import Beep
from google_trans_new import google_translator
from dotenv import load_dotenv as dotenv

dotenv()
nox0 = os.getenv("nox0")
nox = os.getenv("nox")
k = os.getenv("homeoffice")

class BurnerMaker:
    def __init__(self):
        try:
            self.client = adb(host="127.0.0.1", port=5037) 
            self.devices = self.client.devices()
        except:
            pass
        self.apk = "cock.apk"
        self.res = [960, 540]
        self.clicks = (514, 249)
        self.chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '"', '#', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '@', '[', ']', '^', '_', '{', '}']

    def mp(self, cmd):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = [executor.submit(cmd, dev) for dev in self.devices]
        
    def refresh(self):
        self.client = adb(host="127.0.0.1", port=5037)
        self.devices = self.client.devices() 

    def install(self, dev):
        if "com.supercell.clashofclans" not in dev.list_packages():
            dev.install(self.apk)
            print("installed apk for {}".format(dev))
    
    def calctuple(self, dev, x, y):
        return (x, y)
    
    def click(self, dev):
        dev.shell("input touchscreen tap {} {}".format(self.clicks[0], self.clicks[1]))
    
    def clickat(self, dev, x, y):
        #a, b = self.calctuple(dev, x, y)
        dev.shell("input touchscreen tap {} {}".format(x, y))
    
    def hold(self, dev, x, y, time):
        #a, b = self.calctuple(dev, x, y)
        dev.shell("input touchscreen swipe {} {} {} {} {}".format(x, y, x, y, time))
    
    def makename(self, dev):
        i = random.randint(4, 14)
        s = ''
        for j in range(i):
            s+=random.choice(self.chars)
        print(s)
        dev.shell("input keyboard text {}".format(s))
    
    def write(self, dev, st):
        dev.shell("input keyboard text {}".format(st))
    
    def home(self, dev):
        dev.shell("input keyevent KEYCODE_HOME")

    def back(self, dev):
        dev.shell("input keyevent KEYCODE_BACK")
    
    def appmenu(self, dev):
        dev.shell("input keyevent KEYCODE_APP_SWITCH")
    
    def open(self, dev):
        #.723, .313
        x, y = 960*.723, 540*.313
        dev.shell("input touchscreen tap {} {}".format(x, y))

    def popup(self, dev):
        x, y = 960*.640, 540*.200
        dev.shell("input touchscreen tap {} {}".format(x, y))

    def clearapps(self, dev):
        x, y = 960*.723, 540*.100
        dev.shell("input touchscreen tap {} {}".format(x, y))
    
    def make_email(self):
        emaill = "projectgui/old.txt"
        with open(emaill) as f:
            z = f.read()
            first = z[0:13]
            last = z[-11:]
            zz = z.split(first)
            zzz = zz[1].split(last)
            num = zzz[0]
            letter = num[0]
            nums = num[1:]
        alpha = [chr(i) for i in range(97, 123)]
        if int(nums) < 99:
            i_num = int(nums)+1
            nums = str(i_num)
        else:
            al = alpha.index(letter)
            al += 1
            letter = alpha[al]
            nums = '1'
        newmail = first+letter+nums+last
        with open(emaill, 'w') as f:
            f.write(newmail)
        return newmail

    def connect2scid(self, devall):
        if devall == ("all"):
            for dev in self.devices:
                emaill = self.make_email()
                self.clickat(dev, 469, 179)
                self.write(dev, emaill)
                self.clickat(dev, 469, 230)
                self.write(dev, emaill)
                self.clickat(dev, 808, 334)
                recent = "projectgui/recent.txt"
                with open(recent) as f:
                    recentcode = f.read()
                code1 = recentcode
                code2 = recentcode
                s = time()
                e = time()
                while (code1 == recentcode or code2 == recentcode) and e-s <= 6:
                    host = 'imap.gmail.com'
                    username = os.getenv("email")
                    password = os.getenv("passw")
                    mail = imaplib.IMAP4_SSL(host)
                    mail.login(username, password)
                    mail.select('inbox')
                    _, search_data = mail.search(None, 'ALL')
                    num1 = search_data[0].split()[-1]
                    num2 = search_data[0].split()[-2]
                    _, data1 = mail.fetch(num1, '(BODY.PEEK[HEADER])')
                    _, data2 = mail.fetch(num2, '(BODY.PEEK[HEADER])')
                    _, b1 = data1[0]
                    _, b2 = data2[0]
                    e_m1 = email.message_from_bytes(b1)
                    e_m2 = email.message_from_bytes(b2)
                    it1 = e_m1.items()
                    it2 = e_m2.items()
                    subject1 = it1[16][1]
                    subject2 = it2[16][1]
                    code1 = subject1[-8:-1]
                    code2 = subject2[-8:-1]
                    code1 = code1.replace(' ', '')
                    code2 = code2.replace(' ', '')
                    try:
                        int(code1)
                        with open(recent, 'w') as f:
                            f.write(code1)
                        code = code1
                    except:
                        int(code2)
                        with open(recent, 'w') as f:
                            f.write(code2)
                        code = code2
                    e=time()
                self.clickat(dev, 530, 291)
                self.write(dev, code)
                self.clickat(dev, 800, 358)
        else:
            emaill = self.make_email()
            self.clickat(devall, 469, 179)
            self.write(devall, emaill)
            self.clickat(devall, 469, 230)
            self.write(devall, emaill)
            self.clickat(devall, 808, 334)
            recent = "recent.txt"
            with open(recent) as f:
                recentcode = f.read()
            code1 = recentcode
            code2 = recentcode
            s = time()
            e = time()
            while (code1 == recentcode or code2 == recentcode) and e-s <= 6:
                host = 'imap.gmail.com'
                username = os.getenv("email")
                password = os.getenv("passw")
                mail = imaplib.IMAP4_SSL(host)
                mail.login(username, password)
                mail.select('inbox')
                _, search_data = mail.search(None, 'ALL')
                num1 = search_data[0].split()[-1]
                num2 = search_data[0].split()[-2]
                _, data1 = mail.fetch(num1, '(BODY.PEEK[HEADER])')
                _, data2 = mail.fetch(num2, '(BODY.PEEK[HEADER])')
                _, b1 = data1[0]
                _, b2 = data2[0]
                e_m1 = email.message_from_bytes(b1)
                e_m2 = email.message_from_bytes(b2)
                it1 = e_m1.items()
                it2 = e_m2.items()
                subject1 = it1[16][1]
                subject2 = it2[16][1]
                code1 = subject1[-8:-1]
                code2 = subject2[-8:-1]
                code1 = code1.replace(' ', '')
                code2 = code2.replace(' ', '')
                try:
                    int(code1)
                    with open(recent, 'w') as f:
                        f.write(code1)
                    z = 1
                except:
                    int(code2)
                    with open(recent, 'w') as f:
                        f.write(code2)
                    z = 0
                e=time()
            code = code1 if z else code2
            self.clickat(devall, 530, 291)
            self.write(devall, code)
            self.clickat(devall, 800, 358)


    def do_tutorial(self, dev):
        self.click(dev)
        self.click(dev)
        self.click(dev)
        self.click(dev)
        self.clickat(dev, 894, 464)
        sleep(1)
        self.clickat(dev, 478, 328) #initial cannon
        self.clickat(dev, 426, 171)
        self.clickat(dev, 480, 436)
        sleep(1.5)
        self.clickat(dev, 534, 434)
        sleep(15)
        self.click(dev)
        self.click(dev)
        self.click(dev)
        sleep(1)
        self.clickat(dev, 353, 339)
        sleep(3)
        self.clickat(dev, 138, 483) #wizard battle
        self.hold(dev, 444, 225, 2000) #hold wiz
        sleep(12)
        self.clickat(dev, 484, 476) #go home
        sleep(1)
        self.click(dev) 
        self.clickat(dev, 894, 464) #bhut
        sleep(1)
        self.clickat(dev, 478, 328)
        self.clickat(dev, 518, 98)
        self.click(dev) 
        self.clickat(dev, 894, 464) #elix collector
        sleep(1)
        self.clickat(dev, 478, 328) 
        self.clickat(dev, 446, 256)
        self.clickat(dev, 480, 436)
        self.click(dev) 
        self.click(dev) 
        self.clickat(dev, 894, 464) #elix storage
        sleep(1)
        self.clickat(dev, 478, 328)
        self.clickat(dev, 658, 173)
        self.clickat(dev, 480, 436)
        self.click(dev) 
        self.clickat(dev, 894, 464) #gold storage
        sleep(1)
        self.clickat(dev, 478, 328)
        self.clickat(dev, 423, 65)
        self.clickat(dev, 480, 436)
        self.click(dev) 
        self.clickat(dev, 894, 464)
        sleep(2)
        self.clickat(dev, 98, 319) #barracks
        self.clickat(dev, 346, 229)
        self.clickat(dev, 480, 436)
        self.clickat(dev, 530, 440)
        self.hold(dev, 94, 324, 2000) #train barbs
        self.clickat(dev, 714, 233) #gem barbs
        self.click(dev) #exit training menu
        sleep(.5)
        self.clickat(dev, 60, 466) #click battle
        sleep(.5)
        self.clickat(dev, 648, 349) #click attack
        self.clickat(dev, 138, 483) #click barbs
        self.hold(dev, 300, 255, 4500) #hold barbs
        sleep(15) 
        self.clickat(dev, 484, 476) #go home
        sleep(1)
        self.click(dev) 
        self.makename(dev)
        self.clickat(dev, 479, 171)
        self.click(dev) 
        self.clickat(dev, 600, 366) #age thingy
        self.clickat(dev, 600, 366)
        self.clickat(dev, 600, 446)
        self.clickat(dev, 505, 300)
        self.clickat(dev, 531, 441)
        self.clickat(dev, 484, 475)
        self.clickat(dev, 584, 434)
        self.click(dev) 
        self.clickat(dev, 36, 31)
        self.clickat(dev, 914, 380)
        self.click(dev) 
        self.clickat(dev, 921, 390)
        self.clickat(dev, 740, 95)
        self.clickat(dev, 921, 38)
        self.clickat(dev, 768, 425)
        self.clickat(dev, 815, 300)
        self.clickat(dev, 469, 179)
        self.clickat(dev, 469, 230)
        self.clickat(dev, 808, 334)

def runnox(i):
        arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        i = str(i)
        try:
            if i == "0":
                with open(nox0, "w") as f:
                    f.write(a)
            elif i == "all":
                for j in range(10):
                    with open(nox+"{}_conf.ini".format(j), "w") as f:
                        f.write(a)
                with open(nox0, "w") as f:
                    f.write(a) 
            else:
                with open(nox+"{}_conf.ini".format(i), "w") as f:
                    f.write(a)
        except Exception as e:
            print(repr(e))

'''if __name__ == "__main__":
    with open('../apikey.txt') as f:
        k = f.read()
else:
    with open('apikey.txt') as f:
        k = f.read()'''

a = """[setting]
cpu=1
h_dpi=160
h_resolution=960x540
isChangeResolution=YES
manual_perform=true
mem=1200
performance_type=1
system_type=7
frames=50
audio_card=false
v_dpi=160
v_resolution=720x1280
last_player_width=772
last_player_heigh
last_player_posx=798
last_player_posy=413
computer_resolution_width=2560
computer_resolution_height=1400

[toolbar_setting]
display_toolbar_add_apk=true
display_toolbar_clip_cursor=true
display_toolbar_close_all=true
display_toolbar_double_fingers=true
display_toolbar_full_screen=true
display_toolbar_keyboard_control=true
display_toolbar_live_streaming=false
display_toolbar_multiplayer=true
display_toolbar_mute=false
display_toolbar_reboot=true
display_toolbar_rom_keys=true
display_toolbar_rom_menu=true
display_toolbar_rotate=false
display_toolbar_screen_cap=true
display_toolbar_script_record=true
display_toolbar_settings_usb=true
display_toolbar_shake=false
display_toolbar_share_folder=true
display_toolbar_synchronous_operate=true
display_toolbar_video_record=false
display_toolbar_virtual_position=true
display_toolbar_volumn_down=false
display_toolbar_volumn_up=false


[sync]
sync_dlg_height=360
sync_dlg_width=512
"""

class Account:
    def __init__(self, tag):
        key = k.rstrip('\n')
        if tag[0] == '#':
            tag = tag[1:]
        url = "https://api.clashofclans.com/v1"
        endpoint = '/players/%23'+tag
        request = urllib.request.Request(
            url+endpoint,
            None,
            {
                "Authorization": "Bearer %s" % key
            }
        )
        response = urllib.request.urlopen(request).read().decode('UTF-8')
        data = json.loads(response)

        self.data = data
        self.name = data['name']
        self.tag = data['tag']
        self.th = data['townHallLevel']
        self.xp = data['expLevel']
        self.pb = data['bestTrophies']
        self.cups = data['trophies']
        self.donations = data['donationsReceived']
        self.donated = data['donations']
        self.ws = data['warStars']
        try:
            self.clan = data['clan']['name']
            self.clanlevel = data['clan']['clanLevel']
            self.clantag = data['clan']['tag'][1:]
            endpoint3 = '/clans/%23'+self.clantag
            requestclan = urllib.request.Request(
                url+endpoint3,
                None,
                {
                    "Authorization": "Bearer %s" % key
                }
            )
            responseclan = urllib.request.urlopen(
                requestclan).read().decode('UTF-8')
            dataclan = json.loads(responseclan)
            self.clanmembersraw = dataclan['memberList']
            self.clanmembers = ''
            for i in self.clanmembersraw:
                self.clanmembers += 'Tag: ' + \
                    i['tag'] + ' Name: ' + i['name'] + '\n'
        except:
            self.clan = 'Not in a clan'
            self.clanlevel = 'Not in a clan'
        try:
            self.bk = data['heroes'][0]['level']
        except:
            self.bk = 0
        try:
            self.aq = data['heroes'][1]['level']
        except:
            self.aq = 0
        try:
            self.gw = data['heroes'][2]['level']
        except:
            self.gw = 0
        try:
            self.rc = data['heroes'][3]['level']
        except:
            self.rc = 0
        try:
            self.bh = data['builderHallLevel']
        except:
            self.bh = 'Boat not built'
        try:
            self.league = data['league']['name']
        except:
            self.league = 'Leagueless'

        self.faggot = 'Neox'

        if self.league == 'Leagueless' and self.donated == 0 and self.donations == 0:
            self.dead = 'Yes'
        else:
            self.dead = 'No'

        try:
            self.legendinfo = self.data['legendStatistics']
            self.bestrank = self.legendinfo['bestSeason']['rank']
            self.bestpb = self.legendinfo['bestSeason']['trophies']
        except:
            self.bestrank = 'Never finished in legends'
            self.bestpb = ''


def is_active(tag):
    x = Account(tag)
    metric = 0
    if x.donated == 0:
        metric += 1.1
    if x.donations == 0:
        metric += 1.1
    if x.league == 'Leagueless':
        metric += 1.1
    if x.clan == 'Not in a clan':
        metric += .7

    if metric >= 3 and x.clan != 'Not in a clan':
        metric += .6

    if metric >= 3 and (x.donations == 0 or x.donated == 0):
        metric -= .6

    if metric >= 3 and x.league != 'Leagueless':
        metric -= .6

    if metric >= 1.8 and metric < 3 and x.clan != 'Not in a clan' and x.donations != 0:
        metric -= .2

    if metric >= 1.8 and metric < 3 and x.clan != 'Not in a clan' and x.donated != 0:
        metric -= .4

    if metric >= 1.8 and metric < 3 and x.clan != 'Not in a clan' and x.league == 'Leagueless':
        metric += .2

    if x.donations > 1000:
        metric -= .4

    metric *= 2.5

    return x.name, metric


def get(tag, num):
    tag = tag.upper().strip()
    try:
        acc = Account(tag)
    except:
        print('{} is not a valid tag'.format(tag))
    if tag[0] == '#':
        tag = tag[1:]
    if num == '':
        num = '12345'
    num_l = [int(j) for i in num.split() for j in i]
    info = ''
    try:
        for i in num_l:
            if 1 == i:
                info += "Name: {} \n".format(acc.name)
            if 2 == i:
                info += "Tag: {} \n".format(acc.tag)
            if 3 == i:
                info += "TH: {} \n".format(acc.th)
            if 4 == i:
                info += "XP: {} \n".format(acc.xp)
            if 5 == i and acc.clan != 'Not in a clan':
                info += "Clan: {} \n".format(acc.clan)
        copy(info)
    except:
        info = 'error, {} is not a valid tag'.format(tag)
        copy(info)


def rungui():
    bm = BurnerMaker()
    colors = ['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4',
              'DarkGreen5', 'DarkGreen6', 'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12', 'DarkGrey13', 'DarkGrey14', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkPurple7', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Python', 'Reddit',
              'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']

    #theme = input('Color Theme? Hit enter for DarkAmber by default, type list for a list of choices => ')
    theme = random.choice(colors)
    if theme == 'list':
        for i in colors:
            print(i)
    if theme.strip() == '':
        theme = 'DarkAmber'

    selection = ["all", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    width = len(selection)+1

    sg.theme(theme)
    layout = [
              [sg.Text('Welcome! The buttons are pretty self-explanatory...')],

              [sg.Button('Make email'), sg.Button('Copy scid code'), sg.Button(
                  'Make a message'), sg.Button('Sound On', button_color=('white', 'green'), key='_B_')],

              [sg.Text('Enter a tag: (to get info from, or open its\' cos profile)'), sg.InputText(
                  size=(10, 1), key='-TINPUT-')],

              [sg.Text('Info? (1 for Name, 2 for Tag, 3 for TH, 4 for XP, 5 for Clan): '),
              sg.InputText(size=(5, 1), key='-NINPUT-')],

              [sg.Text('Cos settings? (Clan Log or Player Log? Leave blank if none.) cl/pl'),
               sg.InputText(size=(4, 1), key='-CINPUT-')],

              [sg.Text('Notification frequency? (between 37 and 32767):'),
               sg.InputText(size=(8, 1), key='sound')],

              [sg.Text('Notification duration? (ms):'),
               sg.InputText(size=(6, 1), key='time')],

              [sg.Button('Copy acc info'), sg.Button('Open cos'), sg.Button('Check if active'), sg.Button('Cancel')],

              [sg.Text('Modify which Nox?'), sg.Combo(selection, size=(10, 5), enable_events=True, key='inox'), sg.Button("Modify Nox Files")],

              [sg.Text("ADB Commands"), sg.Button("Install Modded APK"), sg.Button("Open Clash"), sg.Button("Click Popup")],

              [sg.Button("Home"), sg.Button("Back"), sg.Button("Recent Apps"), sg.Button("Clear Recent"), sg.Button("Refresh Device List")],

              [sg.Text(size=(40, 1), key='-OUTPUT-')],

              [sg.Text('Made by @theunknown.coc/Gulag_Recroot#6800',size=(40, 1))]
              ]
            
    window = sg.Window("Coc Tools", layout)
    down = True

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

        elif event == 'Make email':
            start = time()
            e_mail()
            end = time()
            window['-OUTPUT-'].update(
                'Done! Took {:.2f} seconds to make a new email'.format(end-start))

        elif event == 'Copy scid code':
            start = time()
            try:
                code()
                if down:
                    if values['sound'] == '':
                        values['sound'] = 40
                    if values['time'] == '':
                        values['time'] = 250
                    Beep(int(values['sound']), int(values['time']))
                end = time()
                window['-OUTPUT-'].update(
                    'Done! Took {:.2f} seconds to copy the scid code.'.format(end-start))
            except Exception as e:
                window['-OUTPUT-'].update(
                    '{}'.format(repr(e)))
            
        elif event == 'Copy acc info':
            start = time()
            try:
                get(values['-TINPUT-'], values['-NINPUT-'])
                end = time()
                window['-OUTPUT-'].update('Done! Took {:.2f} seconds to copy {}\'s data.'.format(
                    end-start, Account(values['-TINPUT-']).name))
            except Exception as e:
                window['-OUTPUT-'].update(
                    '{}'.format(repr(e)))

        elif event == 'Make a message':
            start = time()
            message()
            end = time()
            window['-OUTPUT-'].update(
                'Done! Took {:.2f} seconds to copy a message.'.format(end-start))

        elif event == 'Open cos':
            start = time()
            tag(values['-TINPUT-'], values['-CINPUT-'])
            end = time()
            window['-OUTPUT-'].update('Done! Took {:.2f} seconds to open {}\'s cos page'.format(
                end-start, Account(values['-TINPUT-']).name))

        elif event == 'Check if active':
            start = time()
            x, y = is_active(values['-TINPUT-'])
            if floor(y) == 8:
                i = 'an'
            else:
                i = 'a'
            end = time()
            window['-OUTPUT-'].update('Done! '+'{} is rated '.format(x) +
                                      i+' {} out of 10 for inactivity.'.format(y))

        elif event == '_B_':
            down = not down
            window.Element('_B_').Update(('Sound Off', 'Sound On')[
                down], button_color=(('white', ('red', 'green')[down])))
        
        elif event == "Modify Nox Files":
            start = time()
            runnox(values['inox'])
            end = time()
            window['-OUTPUT-'].update('Done! Took {:.2f} seconds'.format(end-start))

        elif event == "Install Modded APK":
            if values['inox'] != "all":
                print('installing for one')
                bm.install(bm.devices[values['inox']])
            else:
                print('installing for all')
                bm.mp(bm.install)

        elif event == "Refresh Device List":
            bm.refresh()

        elif event == "Open Clash":
            if values['inox'] != "all":
                print('opening for one')
                bm.open(bm.devices[values['inox']])
            else:
                print('opening for all')
                bm.mp(bm.open)
        
        elif event == "Click Popup":
            if values['inox'] != "all":
                print('popup for one')
                bm.install(bm.popup[values['inox']])
            else:
                print('popup for all')
                bm.mp(bm.popup)

        elif event == "Home":
            if values['inox'] != "all":
                print('home for one')
                bm.install(bm.home[values['inox']])
            else:
                print('home for all')
                bm.mp(bm.home)

        elif event == "Back":
            if values['inox'] != "all":
                print('back for one')
                bm.install(bm.back[values['inox']])
            else:
                print('back for all')
                bm.mp(bm.back)

        elif event == "Recent Apps":
            if values['inox'] != "all":
                print('recent apps for one')
                bm.install(bm.appmenu[values['inox']])
            else:
                print('recent apps for all')
                bm.mp(bm.appmenu)
        
        elif event == "Clear Recent":
            if values['inox'] != "all":
                print('clear recent for one')
                bm.install(bm.clearapps[values['inox']])
            else:
                print('clear apps for all')
                bm.mp(bm.clearapps)

    window.close()


if __name__ == "__main__":
    rungui()
