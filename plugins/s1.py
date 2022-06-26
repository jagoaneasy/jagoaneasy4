from pyrogram import Client,filters
import datetime, time, os,base64, traceback
import asyncio
import databasefile
kgbid= ""
rangkumanch=-1001332075031


namabot=""
temp=[0,0,0]
ttg1="**Bot : @"
ttg2="\nBot ini dibuat untuk kalian"

async def carikgbid(c):
    try:
        p=c.get_chat("kntrgabut").id
        return(p)
    except:return(-100128418631)

async def encode(string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.urlsafe_b64encode(string_bytes)
    base64_string = (base64_bytes.decode("ascii")).strip("=")
    return base64_string
  
async def decode(base64_string):
    base64_string = base64_string.strip("=") 
    base64_bytes = (base64_string + "=" * (-len(base64_string) % 4)).encode("ascii")
    string_bytes = base64.urlsafe_b64decode(base64_bytes) 
    string = string_bytes.decode("ascii")
    return string

async def susun(no1,no2=0):
  global namabot
  if namabot=="":
    namabot=await c.get_me().username
  teks="cwmrt-"+str(no1)
  if no2!=0:
    teks+="-"+str(no2)
  x=""
  try:
    x=await encode (teks)
  except:return(x)
  teks="http://t.me/"+namabot+"?start="+x
  return(teks)
  
  
async def bongkar(teks):
  no1=0
  no2=0
  try:
    teks=decode(teks)
    teks=teks.split("-")
    if len(teks)>1:
      if (int(teks[2])+123)%321==0:
        no2=(int(teks[2])+123)//321
    if (int(teks[1])+321)%123==0:
      no1=(int(teks[1])+321)//123
  except:
    if no1==0:return ([])
  x=[]
  if no1!=0:
    if no2!=0:
      for xx in range (no1,no2+1):
        x.append(xx)
    else:x=[no1,no1+1]
  return(x)
  
@Client.on_message(filters.channel)
async def drlaporan(c,p):
  global namabot,kgbid
  try:
    if kgbid=="":
        kgbid=await carikgbid(c)
    if p.chat.id==kgbid:
      if "ten1" in p.text:
        if namabot=="":
          namabot=await c.get_me().username
        teks="Bot ready "+namabot
        await p.reply(teks)
  except Exception as e:
    print(namabot,":",e)
      
@Client.on_message(filters.private & filters.commands["about","start"])
async def distart(c,p):
  global temp,namabot
  try:
    if p.text=="/startadmin":
      temp[0]=p.chat.id
      await p.reply("Anda saat ini menjadi admin")
    elif p.text=="/about":
      teks=ttg1
      if namabot="":
        try:namabot=await c.get_me().username
        except:pass
      teks+=namabot+ttg2
      await p.reply(teks)
    elif p.text=="/start":
      teks=ttg1
      if namabot="":
        try:namabot=await c.get_me().username
        except:pass
      teks+=namabot+ttg2
      await p.reply(teks)
    elif "/start " in p.text[:7]:
      if len(p.text)>7:
        kode=[]
        try:kode=await bongkar(p.text.split()[1])
        except:kode=[]
        for x in kode:
          m=await c.get_messages(rangkumanch,x)
          await m.copy(p.chat.id)
  except Exception:
    print(namabot,":",traceback.format_exc())
    
@Client.on_message(filters.private)
async def isian(c,p):
  global temp,namabot
  try:
    if p.chat.id == temp[0]:
      if p.media:
        x= await p.forward(rangkumanch)     
        if temp[1]==0:
          temp[1]=x
        elif temp[2]==0:
          temp[2]=x.id
        else:
          temp[3]=x.id
      elif p.text:
        link=await susun(temp[2],temp[3])
        await x.copy(rangkumanch,caption=p.text+"\n\nLINK : "+link)
  except Exception:
    print(namabot,":",traceback.format_exc())
