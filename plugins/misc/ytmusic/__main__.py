""" telegraph uploader """

# Copyright (C) 2020-2022 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.


from userge import userge, Message, config, pool
from pyrogram.enums import ParseMode

@userge.on_cmd("ytmnow", about={
    'header': "Get Current playing on YTMusic",
    'usage': "{tr}ytmnow to Get Current playing on YTMusic",
    'examples': "{tr}ytmnow to `header|content`"})
async def telegraph_(message: Message):
    await message.edit("`processing...`")
    thumbnail, title, album, art, videourl = get_ytm()
    caption="**Currently Playing on "+message.from_user.first_name+"'s Device\n\n"
    caption+="{title} From {album} By {art}\n"
    caption+="🔗 **[Watch On YT]({videourl})**"
    await message.reply_photo(photo=thumbnail, caption=caption)
    await message.delete()


def get_ytm():
    """ Get data From YTMusic """
    yt = ytmusicapi.YTMusic("/app/ytm.json")
    currently_playing = yt.get_history()
    cp=currently_playing[0]
    videourl="https://www.youtube.com/watch?v="+cp['videoId']
    title=cp['title']
    album=cp['album']['name']
    thumbnails=cp['thumbnails'][1]['url'] or cp['thumbnails'][0]['url']
    artists=cp['artists']
    art=""
    count=0
    for artist in artists:
        art += artists[count]['name']+" & "
        count=count+1
    return thumbnails, title, album, art, videourl
