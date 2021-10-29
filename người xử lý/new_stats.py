nhập hệ điều hành

nhập khẩu asyncio

từ Ứng dụng khách nhập khẩu pyrogram, bộ lọc

from pyrogram.types import Message

từ pymongo nhập khẩu MongoClient

từ cấu hình nhập BOT_USERNAME, DATABASE_URL dưới dạng db_url

từ lệnh nhập helpers.filters, other_filters

from helpers.decorators import sudo_users_only

users_db = MongoClient (db_url) ['người dùng']

col = users_db ['USER']

grps = users_db ['GROUPS']

@ Client.on_message (command (["gstats", f "gstats @ {BOT_USERNAME}"]) & filter.private & ~ filter.edited)

@sudo_users_only

async def stats (_, m: Message):

  người dùng = col.find ({})

  mfs = []

  cho x trong người dùng:

    mfs.append (x ['user_id'])

    

  tổng = len (mfs)

  

  grp = grps.find ({})

  grps_ = []

  cho x trong grp:

    grps_.append (x ['chat_id'])

    

  total_ = len (grps_)

  

  await m.reply_text(f"👥 Total Users: `{total}`\n💭 Total Groups: `{total_}`")
