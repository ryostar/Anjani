"""Bot tools"""
# Copyright (C) 2020 - 2021  UserbotIndo Team, <https://github.com/userbotindo.git>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import time
from random import choice
from typing import Union
from uuid import uuid4


def get_readable_time(seconds: int) -> str:
    """get human readable time from seconds."""
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    for count in range(1, 4):
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for index in enumerate(time_list):
        time_list[index[0]] = str(time_list[index[0]]) + time_suffix_list[index[0]]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


async def extract_time(time_text) -> Union[int, bool]:
    """Extract time from time flags"""
    if any(time_text.endswith(unit) for unit in ("m", "h", "d")):
        unit = time_text[-1]
        time_num = time_text[:-1]
        if not time_num.isdigit():
            return False

        if unit == "m":
            bantime = int(time.time() + int(time_num) * 60)
        elif unit == "h":
            bantime = int(time.time() + int(time_num) * 60 * 60)
        elif unit == "d":
            bantime = int(time.time() + int(time_num) * 24 * 60 * 60)
        return bantime
    return False


async def nekobin(client, data: str) -> str:
    """return the nekobin pasted key"""
    async with client.http.post(
        "https://nekobin.com/api/documents",
        json={"content": data},
    ) as resp:
        if resp.status != 200:
            response = await resp.json()
            key = response["result"]["key"]
            return key
    return None


def format_integer(number: int, separator: str = ".") -> str:
    """make an integer easy to read"""
    return "{:,}".format(number).replace(",", separator)


def rand_array(array: list):
    """pick an item randomly from list"""
    return choice(array)


def rand_key():
    """generates a random key"""
    return str(uuid4())
