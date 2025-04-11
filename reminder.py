import requests
import json
import datetime

def send_feishu_reminder():
    webhook = "https://open.feishu.cn/open-apis/bot/v2/hook/69366465-244b-418f-8600-f9185ebf8792"  # 替换成你的
    msg = {
        "msg_type": "text",
        "content": {
            "text": f"📢 每周提醒：今天是 {datetime.datetime.now().strftime('%Y-%m-%d')}，请记得更新工时信息！"
        }
    }
    headers = {"Content-Type": "application/json"}
    res = requests.post(webhook, headers=headers, data=json.dumps(msg))
    print(f"状态码: {res.status_code}，返回: {res.text}")

if __name__ == "__main__":
    send_feishu_reminder()
