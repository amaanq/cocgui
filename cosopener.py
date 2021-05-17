import json
import os
import urllib.request
import webbrowser
from dotenv import load_dotenv as dotenv

dotenv()

k = os.getenv("homeoffice")

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
                        responseclan = urllib.request.urlopen(requestclan).read().decode('UTF-8')
                        dataclan = json.loads(responseclan)
                        self.clanmembersraw = dataclan['memberList']
                        self.clanmembers = ''
                        for i in self.clanmembersraw:
                            self.clanmembers += 'Tag: ' + i['tag'] + ' Name: ' + i['name'] + '\n'
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
                        self.dead='Yes'
                else:
                        self.dead='No'

                try:
                        self.legendinfo = self.data['legendStatistics']
                        self.bestrank = self.legendinfo['bestSeason']['rank']
                        self.bestpb = self.legendinfo['bestSeason']['trophies']
                except:
                        self.bestrank= 'Never finished in legends'
                        self.bestpb=''

def tag(tag, cp=''):
    if cp == 'cl':
        i = 'history/log/'
    elif cp == 'pl':
        i = 'history/progress-log/'
    else:
        i = ''
    try:
        webbrowser.open('https://www.clashofstats.com/players/{}/{}'.format(tag, i))
    except:
        return ("{} is not a valid tag".format(tag))
