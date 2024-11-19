import requests
from datetime import datetime, timedelta
import json
import pandas as pd
import time


url = 'https://ws.xoyo.com/jx3/doujinwz241031/get_rank_list'

# 来源：https://jx3.xoyo.com/p/zt/2024/10/18/tongren-clothes/js/data.js?ver=1.0.0，把前面外装list代码处理一下就好了
name_dic ={
    1: '霸王别姬',
    2: '百雀裘',
    3: '波光摇月',
    4: '不渡山海',
    5: '不染尘',
    6: '沧蝶泪',
    7: '此叶庭庭',
    8: '粗麦包',
    9: '渡君心',
    10: '返魂香',
    11: '梵音妙相',
    12: '伏虎藏龙',
    13: '鹤灵',
    14: '浣轻羽',
    15: '魂赴九幽',
    16: '火啖青园',
    17: '见南山',
    18: '江湖客',
    19: '枯枝繁影',
    20: '快马长安',
    21: '嶙骨',
    22: '流洲照影',
    23: '难渡我',
    24: '青丘旧梦',
    25: '青云来',
    26: '清尘心',
    27: '清莲蛇影',
    28: '穷奇',
    29: '雀别枝',
    30: '神鼬献金',
    31: '神羽坠星',
    32: '石火梦身',
    33: '世上千年',
    34: '蜀中赋',
    35: '松见礼',
    36: '岁焰生花',
    37: '听梨声',
    38: '听涛',
    39: '万物皆一',
    40: '望鹤燕归',
    41: '小龙铃',
    42: '雪覆夜狸',
    43: '燕归梁',
    44: '夜雨寄北',
    45: '一相三昧',
    46: '遗落宝匣',
    47: '余梦',
    48: '跃龙门',
    49: '云华九歌',
    50: '占春风'
}




def get_content(url):
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")
        return None
    
def extract_json(content):
    content = json.loads(content)
    data = content['data']['list']
    return data

def add_to_table(df, data):
    if not data:
        return df
    new_rows = pd.DataFrame(data)
    new_rows['name'] = new_rows['work_id'].map(name_dic)
    new_rows['fetch_time'] = datetime.now().strftime('%Y-%m-%d %H:%M')
    df = pd.concat([df, new_rows], ignore_index=True)
    return df

def create_file():
    df = pd.DataFrame(columns=['work_id', 'name', 'total', 'rank', 'fetch_time'])
    return df




if __name__ == '__main__':
    df = create_file()
    fname = 'votes.csv'
    df.to_csv(fname, index=False)
    start_time = datetime(2024, 11, 19, 14, 1)
    end_time = datetime(2024, 11, 25, 0, 59)
    while True:
        now = datetime.now()
        if start_time <= now <= end_time:
            content = get_content(url)
            if content:
                data = extract_json(content)
                df = add_to_table(df, data)
                df.to_csv(fname, index=False)
            else:
                print("No content retrieved.")
        else:
            print("Current time is outside the specified range.")
            break
        time.sleep(1200)
