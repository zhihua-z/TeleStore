from aiotg import Bot, Chat
import aiohttp
import json
import utils

with open('token.myconf') as f, open('category.json') as c:
    token = json.loads(f.read())
    category = json.loads(c.read())

bot = Bot(**token)

@bot.command(r"/echo (.+)")
def echo(chat: Chat, match):
    print(match)
    return chat.reply(match.group(1))

@bot.command("/fetch")
async def async_fecth(chat: Chat, match):
    url = "http://www.gamersky.com/ent/111/"
    async with aiohttp.ClientSession() as sesssion:
        async with sesssion.get(url) as resp:
            info = ' version: {}\n status :{}\n method: {}\n url: {}\n'.format(
                resp.version, resp.status, resp.method, resp.url)
            await chat.send_text(info)

bot.run(debug=True)
