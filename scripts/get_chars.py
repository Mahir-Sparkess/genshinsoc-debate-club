import re
import requests
import pandas as pd
from tqdm import tqdm

url = "https://genshin-impact.fandom.com/wiki/Characters/List"
regex = "https:\/\/static\.wikia\.nocookie\.net\/gensin-impact\/images\/[\S]\/[\S]+\/Character_(?P<name>[\S]+)_Thumb\.png"

body = requests.get(url).content.decode()

chars = set(re.findall(regex, body))
total_chars = len(set(chars))
characters = re.finditer(regex, body)

count = 0
for char in tqdm(characters, total=total_chars):
    if count == total_chars:
        break
    char_name = char.groupdict()['name']
    img_url = char.group()
    img_data = requests.get(img_url).content

    with open(f"../assets/{char_name}.png", 'wb') as img:
        img.write(img_data)
    count += 1

export_list = pd.DataFrame(chars)
export_list.to_csv("../assets/_char_list.csv", index=False)
print("Done ehe~")
