import requests
import os
import random
import time

# 1. 获取 GitHub Secrets
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# 2. 伪装头 (虽然 Wallhaven 很友好，但带上个身份更保险)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def get_daily_quote():
    # 获取语录
    api_url = "https://v1.hitokoto.cn/?c=a&c=b&c=k"
    try:
        res = requests.get(api_url, headers=HEADERS, timeout=5)
        if res.status_code == 200:
            data = res.json()
            return f"“{data.get('hitokoto')}”\n——《{data.get('from')}》"
    except Exception:
        pass
    return "“排球是永远向上看的运动！”\n——《排球少年！！》"

def get_haikyuu_image():
    # === 目标：Wallhaven (高清壁纸站) ===
    # 文档: https://wallhaven.cc/help/api
    # q=haikyuu : 搜索排球少年
    # categories=010 : 只看动漫分类 (General/Anime/People) -> 010 代表 Anime
    # purity=100 : 只看全年龄 (SFW)
    # sorting=random : 随机排序 (这样每次都不一样)
    url = "https://wallhaven.cc/api/v1/search?q=haikyuu&categories=010&purity=100&sorting=random"
    
    print(f"正在请求 Wallhaven: {url}")
    
    try:
        # Wallhaven 不需要 cloudscraper，直接 requests 即可
        response = requests.get(url, headers=HEADERS, timeout=15)
        print(f"Wallhaven 响应状态码: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            # Wallhaven 的图片列表在 'data' 字段里
            post_list = data.get('data', [])
            
            if post_list and len(post_list) > 0:
                # 随机选一张
                post = random.choice(post_list)
                # 获取图片链接 (path 字段是原图)
                img_url = post.get('path')
                print(f"成功获取图片链接: {img_url}")
                return img_url
            else:
                print("错误：搜索结果为空")
        elif response.status_code == 429:
            print("错误：请求太频繁 (429 Too Many Requests)")
        else:
            print(f"错误：接口返回异常 (Status {response.status_code})")
            print(f"详情: {response.text[:200]}")
            
    except Exception as e:
        print(f"请求异常: {e}")
    return None

def send_telegram(img_url):
    quote_text = get_daily_quote()
    
    send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    caption_text = f"{quote_text}\n\n🏐 <b>每日排球少年</b>\n#Haikyuu #Wallhaven"

    payload = {
        "chat_id": CHAT_ID,
        "photo": img_url,
        "caption": caption_text,
        "parse_mode": "HTML"
    }
    
    try:
        print("正在推送给 Telegram...")
        res = requests.post(send_url, data=payload, timeout=20)
        print(f"Telegram 推送状态: {res.status_code}")
        if res.status_code != 200:
            print(f"推送失败原因: {res.text}")
    except Exception as e:
        print(f"发送异常: {e}")

if __name__ == "__main__":
    if not BOT_TOKEN or not CHAT_ID:
        print("致命错误：Secrets 未配置！")
        exit(1)
    else:
        print("=== 任务开始 (Source: Wallhaven) ===")
        pic = get_haikyuu_image()
        
        if pic:
            send_telegram(pic)
            print("=== 任务完成 ===")
        else:
            print("=== 任务失败：未获取到图片 ===")
            exit(1)
