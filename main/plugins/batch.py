#Tg:mister_invisible/save_restricted
#Github. com/187dasharath

"""
Plugin for both public & private channels!
...................
"""
import logging
import time, os, asyncio

from .. import bot as Drone
from .. import userbot, Bot, AUTH, SUDO_USERS
#from .. import FORCESUB as fs
from main.plugins.pyroplug import check, get_bulk_msg
from main.plugins.helpers import get_link, screenshot

from telethon import events, Button, errors
from telethon.tl.types import DocumentAttributeVideo

from pyrogram import Client 
from pyrogram.errors import FloodWait

#from ethon.pyfunc import video_metadata
#from main.plugins.helpers import force_sub
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)
#ft = f"To use this bot you've to join @{fs}."

batch = []
ids = []

'''async def get_pvt_content(event, chat, id):
    msg = await userbot.get_messages(chat, ids=id)
    await event.client.send_message(event.chat_id, msg) 
'''   
@Drone.on(events.NewMessage(incoming=True, from_users=SUDO_USERS, pattern='/batch'))
async def _batch(event):
    '''
    #if not event.is_private:
    #    return
    # wtf is the use of fsub here if the command is meant for the owner? 
    # well am too lazy to clean 
    #s, r = await force_sub(event.client, fs, event.sender_id, ft) 
    #if s == True:
    #   await event.reply(r)
    #  return       
    '''
    s = False
    if f'{event.sender_id}' in batch:
        return await event.reply("You've already started one batch, wait for it to complete you dumb!")
    async with Drone.conversation(event.chat_id) as conv: 
        if not s:
            await conv.send_message("Send me the message link you want to start saving from, as a reply to this message.", buttons=Button.force_reply())
            try:
                link = await conv.get_reply()
                try:
                    _link = get_link(link.text)
                except Exception:
                    await conv.send_message("No link found.")
            except Exception as e:
                #print(e)
                logger.info(e)
                return await conv.send_message("Cannot wait more longer for your response!")
            await conv.send_message("Send me the number of files/range you want to save from the given message, as a reply to this message.", buttons=Button.force_reply())
            try:
                _range = await conv.get_reply()
            except Exception as e:
                logger.info(e)
                #print(e)
                return await conv.send_message("Cannot wait more longer for your response!")
            try:
                value = int(_range.text)
                if value > 10000000:
                    return await conv.send_message("You can only get upto 10000000 files in a single batch.")
            except ValueError:
                return await conv.send_message("Range must be an integer!")
            for i in range(value):
                ids.append(i)
            s, r = await check(userbot, Bot, _link)
            if s != True:
                await conv.send_message(r)
                return
            batch.append(f'{event.sender_id}')
            cd = await conv.send_message("**Batch process ongoing.**\n\nProcess completed: ", 
                                    buttons=[[Button.inline("CANCEL❌", data="cancel")]])
            co = await run_batch(userbot, Bot, event.sender_id, cd, _link) 
            try: 
                if co == -2:
                    await Bot.send_message(event.sender_id, "Batch successfully completed!")
                    await cd.edit(f"**Batch process ongoing.**\n\nProcess completed: {value} \n\n Batch successfully completed! ")
            except:
                await Bot.send_message(event.sender_id, "ERROR!\n\n maybe last msg didnt exist yet")
            conv.cancel()
            ids.clear()
            batch.clear()

@Drone.on(events.callbackquery.CallbackQuery(data="cancel"))
async def cancel(event):
    ids.clear()
    
async def run_batch(userbot, client, sender, countdown, link):
    for i in range(len(ids)):
        timer = 60
        if i < 25:
            timer = 5
             elif i < 50 and i > 25:
            timer = 10
        elif i < 100 and i > 50:
            timer = 15
        elif i < 200 and i > 150:
            timer = 20
        elif i < 250 and i > 200:
            timer = 25
        elif i < 300 and i > 250:
            timer = 30
        elif i < 500 and i > 400:
            timer = 35
        elif i < 1000 and i > 500:
            timer = 40
        elif i < 1500 and i > 1250:
            timer = 45
        elif i < 1750 and i > 1500:
            timer = 50
        elif i < 2000 and i > 1750:
            timer = 55
        elif i < 2500 and i > 2000:
            timer = 60
        elif i < 3000 and i > 2500:
            timer = 75
        elif i < 3500 and i > 3000:
            timer = 80
        elif i < 4000 and i > 3500:
            timer = 85
        elif i < 4500 and i > 4000:
            timer = 90
        elif i < 5000 and i > 4500:
            timer = 100
        elif i < 5500 and i > 5000:
            timer = 105
        elif i < 6000 and i > 5500:
            timer = 110
        elif i < 6500 and i > 6000:
            timer = 115
        elif i < 7000 and i > 6500:
            timer = 120
        elif i < 7500 and i > 7000:
            timer = 125
        elif i < 8000 and i > 7500:
            timer = 130
        elif i < 8500 and i > 8000:
            timer = 135
        elif i < 9000 and i > 8500:
            timer = 140
        elif i < 9500 and i > 9000:
            timer = 145
        elif i < 10000:
            timer = 150
        elif i < 15000:
            timer = 160
        elif i < 20000:
            timer = 165
        elif i < 25000:
            timer = 170
        elif i < 30000: 
            timer = 180
        elif i < 35000: 
            timer = 190
        elif i < 40000:
            timer = 200
        elif i < 45000: 
            timer = 210
        elif i < 50000:
            timer = 220
        elif i < 55000:
            timer = 230
        elif i < 60000:
            timer = 240
        elif i < 65000:
            timer = 250
        elif i < 70000: 
            timer = 260
        elif i < 75000: 
            timer = 270
        elif i < 80000:
            timer = 280
        elif i < 85000: 
            timer = 290    
        elif i < 100000: 
            timer = 300
        
        
        if 't.me/c/' not in link:
            timer = 2 if i < 25 else 3
        try: 
            count_down = f"**Batch process ongoing.**\n\nProcess completed: {i+1}"
            #a =ids[i]
            try:
                msg_id = int(link.split("/")[-1])
            except ValueError:
                if '?single' not in link:
                    return await client.send_message(sender, "**Invalid Link! .**")
                link_ = link.split("?single")[0]
                msg_id = int(link_.split("/")[-1])
            integer = msg_id + int(ids[i])
            await get_bulk_msg(userbot, client, sender, link, integer)
            protection = await client.send_message(sender, f"Sleeping for `{timer}` seconds to avoid Floodwaits and Protect account!")
            await countdown.edit(count_down, 
                                 buttons=[[Button.inline("CANCEL❌", data="cancel")]])
            await asyncio.sleep(timer)
            await protection.delete()
        except IndexError as ie:
            await client.send_message(sender, f" {i}  {ie}  \n\nBatch ended completed!")
            await countdown.delete()
            break
        except FloodWait as fw:
            if int(fw.value) > 300:
                await client.send_message(sender, f'You have floodwaits of {fw.value} seconds, cancelling batch') 
                ids.clear()
                break
            else:
                fw_alert = await client.send_message(sender, f'Sleeping for {fw.value + 5} second(s) due to telegram flooodwait.')
                ors = fw.value + 5
                await asyncio.sleep(ors)
                await fw_alert.delete()
                try:
                    await get_bulk_msg(userbot, client, sender, link, integer)
                except Exception as e:
                    #print(e)
                    logger.info(e)
                    if countdown.text != count_down:
                        await countdown.edit(count_down, buttons=[[Button.inline("CANCEL❌", data="cancel")]])
        except Exception as e:
            #print(e)
            logger.info(e)
            await client.send_message(sender, f"An error occurred during cloning, batch will continue.\n\n**Error:** {str(e)}")
            if countdown.text != count_down:
                await countdown.edit(count_down, buttons=[[Button.inline("CANCEL❌", data="cancel")]])
        n = i + 1
        if n == len(ids):
            return -2
