from telethon.sync import TelegramClient, events
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl import functions,types
import time,asyncio,os,random
from telethon import errors
from telethon import utils
from datetime import datetime,timedelta

from importlib import reload

def buka(n):
    o=open("NewTextDocument.txt","r").read().splitlines()
    for ni in o:
        #print(ni)
        if n in ni:
            return(ni.split(n+"=")[1])
 
balesan=["Pesan kaka sudah di teruskan ke pemilik akun ini.\n ","Sudah saya ingatkan ke pemilik akun untuk membalas chat kaka.\n ","Tunggu sebentar ya kak. pemilik akunnya slow respon. Maaf.\n ","Agaknya pemilik akun ini masih sibuk (slow respon). Maaf.\n ","Sudah saya ingatkan ke pemilik akun ini.\n "]
ayu=(b'\xf0\x9f\x92\x8b').decode()
teks1="\n\n Saya assisten nya @nokos_easy\n Saya akan menghubungi pemilik akun ini segera\n Mohon bersabar menunggu. Terima kasih\n\nSilahkan Kaka baca tulisan ini sebentar::\n \n [-Tentang Nokos](https://telegra.ph/Seputar-Nokos-03-03)\n\n [-Tentang Video easy](https://telegra.ph/seputar-pideo-nokos-easy-03-03)\n\nKalaumasih ada yang bingung boleh ditanyakan kesini nnti akan segera di balas oleh @nokos_easy langsung. Atau kirimkan foto transferannya pasti dijawab cepet.. hehehe ^_^\nSalam [Assisten_Hyun-Ae](https://telegra.ph/Halo-Kaka-04-12) "+ayu
sp=(b'\xf0\x9f\x94\x89 ').decode()
fwp=[]
jfwp=0
urutpk=0


#bots=TelegramClient('bot',api,app).start(bot_token=Token)

Token=os.environ.get("Token")
api=os.environ.get("api")
app=os.environ.get("app")

async def main4():
    bos=await TelegramClient('bot',api,app).start(bot_token=Token)
    print("SIBOT ready") #TheCxxxBot
    print(await bos.get_me())
    async with bos  as bot:
        print("BOT HADIR")
        print("bot dah sulit")
        @bot.on(events.NewMessage())
        async def bacabot(event):
            if event.is_private:
                if event.message.message=="x":await bot.disconnect()
                elif "?start=" in event.message.message:
                    for tt in event.raw_text:
                        if "?start=" in tt:break
                    tul=tt+"\n"
                    try:
                        t1=tt.split(".me/")[1].split("?start=")
                        t2=t1[0];t3=t1[1]
                        tul+="Bot : "+t2+"\n"
                        tul+="Link: "+t3
                    except:
                        tul+="Error"
                    await event.respond(tul)
                        
                else:
                    await event.reply("yes")
            elif event.chat_id ==kgbid:
                if "Assisten1 online" in event.text:await event.respond("TheCanduBot online")
        await bot.run_until_disconnected()
        

spt = (os.environ.get("spt"))

async def main3(s3,s2,s1,s0):
    pengkoleksi=s0
    global urutpk
    print("koleksi akun :"+s0)  
    pkk= TelegramClient(StringSession(s3),s2,s1)
    await pkk.send_message(kgb,s0+ " Online")
    async with pkk as pk:
        jfwp=0
        async for dd in pk.iter_dialogs():
            if dd.name==spt:
                #print(dd.stringify())
                urutpk=int(dd.message.message.split()[2])
                break
        print("urut",urutpk)
        await pk.send_message(kgb,"Account "+pengkoleksi+ " starting ...")
        @pk.on(events.NewMessage())
        async def bacapk(event):
            global fwp,jfwp,urutpk
            if event.is_private:
                
                
                #print(event.stringify())
                if event.message.media.document.attributes[0].duration>140:
                    print("ada videonya")
                    fwp.append(event.message)
                    jfwp+=1
                    print("jes")
                        
                
                if jfwp==1:
                    print("jos")
                    while pk.is_connected():
                        if len(fwp)>0:
                                #pengirim= await event.get_sender()
                            #print(fwp[0].stringify())
                            pengirim=str(fwp[0].peer_id.user_id)
                            await pk.send_file(dd,fwp[0].media,caption=pengkoleksi+" "+pengirim+" "+str(urutpk+1))
                            urutpk+=1
                            fwp.pop(0)
                            await asyncio.sleep(2)
                        else:
                            await asyncio.sleep(30)
            elif event.chat_id ==kgbid:
                if event.text=="pengkoleksi off":
                    await pk.disconnect()
                    print("pengkoleksi dimatikan")
                elif event.text=="x":
                    await pk.disconnect()
                elif "Assisten1 online" in event.text:await event.respond(pengkoleksi+" online")
        await pk.run_until_disconnected()
sipk=0
kgbmialc = (os.environ.get("kgbmialc")).split()
#kgbmialc = (os. environ.get("kgbmialc")).split()
mialc=kgbmialc[1]
kgb = kgbmialc[0]
AccB = (os.environ.get("AccB")).split()
print(AccB)
AccBa= AccB[0]
AccBb= int(AccB[1])
AccBc= AccB[2]
async def main2():
    print("masuk2")  
    print((AccBa),AccBb,AccBc)
    as2= TelegramClient(StringSession(AccBa),AccBb,AccBc)
    async with as2 as asisten2:
        await asisten2.send_message(kgb,"Assisten2 online")
        @asisten2.on(events.NewMessage())
        async def bacaasisten(event):
            #global sipk
            if event.chat_id == kgbid:
                if "Assisten1 online" in event.text:await event.respond("Assisten2 online")
                elif event.text=="x":
                    await asisten2.disconnect()
                
            elif event.is_private:
                
                try:
                    await event.forward_to(mialc)
                except:
                    await asisten1.send_message(mialc,"cant download \n__________\n"+event.text)
                await asyncio.sleep(2)
                kodemedia=(b'\xf0\x9f\x92\xac').decode()
                kodepic=(b'\xf0\x9f\x8e\x9e\xef\xb8\x8f').decode()
                await asisten2.send_message(kgb,(kodemedia if event.file== None else kodepic)+" [Laporan.xls](https://gmail.com/) -"+str((event.message.id)))
                sudahkontak=0
                await asyncio.sleep(2)
                if sudahkontak==0:
                    pengirim= await event.get_sender()
                    print("pengirim "+pengirim.first_name)
                    try:
                        mojawab=(sp+"Halo Kak "+pengirim.first_name+" @"+pengirim.username)
                    except: 
                        mojawab=(sp+"Halo Kak "+pengirim.first_name)
                    mojawab+=teks1+"\n\nKontak @nokos_easy ya kak"
                
                await event.respond(mojawab,link_preview=False)
                
        await asisten2.run_until_disconnected()

#titip=b'\xf0\x9f\x94\xbc'
jalan2=0
jalanjam=0

AccA = (os.environ.get("AccA")).split()
AccAa= AccA[2]
AccAb= int(AccA[1])
AccAc= AccA[0]
kgbid= int(os.environ.get("kgbid"))

async def main():
    print("masuk1")  
    #print(AccAa,AccAb,AccAc)
    as1= TelegramClient(StringSession(AccAc),AccAb,AccAa)
    print("yos")
    
    async with as1 as asisten1:
        print(await as1.get_me())
        await asisten1.send_message(kgb,"check system from dyno",schedule=timedelta(minutes=1))
        
        @asisten1.on(events.NewMessage())
        async def bacaasisten(event):
            
            global jalan2,jalanjam,sipk     
                        
            if event.is_private:
                pengirim= await event.get_sender()
                print("pengirim "+pengirim.first_name)
                try:
                    await event.forward_to(mialc)
                except:
                    await asisten1.send_message(mialc,"cant download "+pengirim.first_name)
                await asyncio.sleep(2)
                kodemedia=(b'\xf0\x9f\x92\xac').decode()
                kodepic=(b'\xf0\x9f\x8e\x9e\xef\xb8\x8f').decode()
                await asisten1.send_message(kgb,(kodemedia if event.file== None else kodepic)+" [Laporan.xls](https://gmail.com/) -"+str((event.message.id))+" "+pengirim.first_name[:5])
                sudahkontak=0
                await asyncio.sleep(2)
                async for m in asisten1.iter_messages(pengirim,limit=7):
                    try:
                        if "Sapa_Hyun-Ae" in m.message:
                            await asisten1.delete_messages(pengirim,m.id)
                            sudahkontak=1;break
                        if "Assisten_Hyun-Ae" in m.message:
                            sudahkontak=1;break
                    except:pass
                if sudahkontak==0:
                    try:
                        mojawab=(sp+"Halo Kak "+pengirim.first_name+" @"+pengirim.username)
                    except: 
                        mojawab=(sp+"Halo Kak "+pengirim.first_name)
                    mojawab+=teks1
                else:
                    teksb=b'\xf0\x9f\x91\xa9\xe2\x80\x8d\xf0\x9f\x8f\xab'
                    mojawab=sp+random.choice(balesan)+teksb.decode()+"[Sapa_Hyun-Ae](https://telegra.ph/Halo-Kaka-04-12) "
                await event.respond(mojawab,link_preview=False)
                print("TERjawab")
                    
                
                #if event.text=="x":await asisten1.disconnect()
            elif event.chat_id ==kgbid:
                print(event.text)

                if event.text=="check system from dyno":
                    print("test")
                    #await asyncio.sleep(7)
                    #await event.respond("Assisten1 online")
                    #await asisten1.send_message(kgb,"check system from dyno2",schedule=timedelta(minutes=1))
        
                    print("mau")
                    if jalan2==0:
                        jalan2=1
                        print("jalankan")
                        await main2()
                elif event.text[:12]=="pengkoleksi ":
                    try :
                        sipik=event.text.split()
                        print("PENGKOLEKSI ",sipik)
                        s3=sipik[1];s2=int(sipik[2]);s1=sipik[3];s0=sipik[4]
                        try:
                            await main3(s3,s2,s1,s0)
                        except: 
                            await event.respond("sulit direalisasi")
                    except:
                        await event.respond("pengkoleksi not in list2")
                    print("teste")
                    #await asyncio.sleep(7)
                    #await event.respond("Assisten1 online")
                    #await asisten1.send_message(kgb,"Assisten1 online",schedule=timedelta(minutes=1))
        
                elif event.text=="x":
                    await asisten1.disconnect()
                elif event.text=="check system":
                    await event.respond("Assisten1 online")
                    print("mau")
                    if jalan2==0:
                        jalan2=1
                        print("jalankan")
                        await main2()
                elif "Assisten2" in event.text:
                    if jalanjam==0:
                        jalanjam=1
                        print("ngejam")
                        while True:
                            await asyncio.sleep(6)
                            await event.respond("Assisten1 online . check system")
                            await asyncio.sleep(10*60)
                    if sipk==0:
                        sipk=1
                        #await main4()

                elif "baca " == event.text[:5]:
                    delit=0
                    ketemu=[]
                    ANGKA=0
                    try:
                        try:
                            try:
                                dicari=int(event.text.split()[1])
                                ANGKA=1
                            except:dicari=(event.text.split()[1])
                        except:
                            delit=await event.reply("baca apa tu")
                            return
                        try:
                            d=await asisten1.get_dialogs()
                            print(len(d))
                        except:
                            print("gak isa")
                        for i in range (len(d)):
                            dd=d[i]
                            try:
                                #print(i,dd.entity.first_name, dd.id)
                                if dd.entity.first_name==None:
                                    #print("dil")
                                    await asisten1.delete_dialog(dd)
                                    continue
                                #print(dd.entity.first_name[:len(event.text.split()[1])])
                                if ANGKA==0:cari=dd.entity.first_name[:len(event.text.split()[1])]
                                else:cari=dd.id
                                if cari==dicari:
                                    ketemu.append(dd)
                            except:pass
                                #print(i,"---",dd.entity.title)
                                #except:print(dd.entity.stringify())
                    except:
                        delit=await event.reply("salah ketemu ketemu "+event.text.split()[1])
                        print(delit)
                        return
                    if len(ketemu)==0:
                        delit=await event.reply("gak ketemu "+event.text.split()[1])
                    elif len(ketemu)>1:
                        diketemu=""
                        for kete in ketemu:
                            diketemu+=kete.entity.first_name+" "+kete.id
                            diketemu+="\n"
                        delit=await event.reply("ketemu banyak : \n"+diketemu)
                    elif len(ketemu)==1:
                        if len(event.text.split())==2:
                            teks=""
                            async for m in asisten1.iter_messages(ketemu[0],limit=20):
                                teks+="\n"+(((b'\xf0\x9f\x94\xba').decode()) if m.out else ((b'\xf0\x9f\x94\xbd').decode()))
                                if m.media:
                                    #print(m.media.stringify())
                                    """
                                    if "webp" in m.media.document.mime_type:
                                        teks+="\n"+(b'\xf0\x9f\x85\xb1\xef\xb8\x8f').decode()+"\n"
                                    elif "sticker" in m.media.document.mime_type:
                                        teks+="\n"+(b'\xf0\x9f\x85\xb1\xef\xb8\x8f').decode()+"\n"
                                    """
                                    if m.sticker:teks+="\n"+(b'\xf0\x9f\x85\xb1\xef\xb8\x8f').decode()+"\n"
                                    else:
                                        teks+="\n"+(b'\xf0\x9f\x8e\xb4').decode()
                                        if m.message=="":teks+="\n"
                                        await asisten1.forward_messages(kgb,m)
                                        await asyncio.sleep(2)
                                if m.message!="":teks+="\n"+m.message+"\n"
                            #input()
                            delit= await event.respond(teks)
                        elif len(event.text.split())>2:
                            pes=event.text.find(" ",5)
                            pesan=event.text[pes+1:]
                            await asisten1.send_message(ketemu[0],pesan)
                            await asyncio.sleep(2)
                        await asyncio.sleep(20)
                    #print(delit)
                    """
                    await asyncio.sleep(20)
                        await asisten1.delete_messages(delit)"""

                

                elif event.text=="sibot" :
                    #reload(sibot)
                    await asyncio.sleep(5)
                    await main4()
                
                print("chat_id",event.chat_id,event.text)
        print("brrrrr")
        await asisten1.run_until_disconnected()

asyncio.run(main())
