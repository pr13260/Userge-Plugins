# Copyright (C) 2020-2022 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.

""" ytmusic """
import os
import base64

YTM_OAUTH = base64.b64decode(os.environ.get("YTM_OAUTH")).decode("utf-8")
os.system("touch /app/ytm.json")
file = open("/app/ytm.json", "w")
n = file.write(YTM_OAUTH)
file.close()
