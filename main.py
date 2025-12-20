import cloudscraper
import os
import random
import time
import requests # 用于发送 Telegram 消息

# 1. 获取 GitHub Secrets
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def get_daily_quote():
    # 获取语录
    api_url = "https://v1.hitokoto.cn/?c=a&c=b&c=k"
    scraper = cloudscraper.create_scraper()
    try:
        res = scraper.get(api_url, timeout=5)
        if res.status_code == 200:
            data = res.json()
            return f"“{data.get('hitokoto')}”\n——《{data.get('from')}》"
    except Exception:
        pass
    return "“排球是永远向上看的运动！”\n——《排球少年！！》"

def get_haikyuu_image():
    # === 目标：Safebooru ===
    # === 标签：haikyuu!! (排球少年全系列) + rating:general (全年龄) ===
    # json=1 是为了确保返回 JSON 格式
    base_url = "https://safebooru.donmai.us/posts.json"
    params = {
        "tags": "haikyuu!! rating:general",
        "limit": 20,
        "json": 1
    }
    
    print(f"正在请求 Safebooru: {base_url} 参数: {params}")
    
    # === 关键：创建一个模拟 Chrome 浏览器的爬虫 ===
    scraper = cloudscraper.create_scraper(browser={'browser': 'chrome', 'platform': 'windows', 'desktop': True})
    
    try:
        response = scraper.get(base_url, params=params, timeout=15)
        print(f"Safebooru 响应状态码: {response.status_code}")
        
        if response.status_code == 200:
            posts = response.json()
            if posts and len(posts) > 0:
                post = random.choice(posts)
                # Safebooru 的图片链接字段通常是 file_url
                img_url = post.get('file_url') or post.get('large_file_url') or post.get('preview_file_url')
                print(f"成功获取图片链接: {img_url}")
                return img_url
            else:
                print("错误：搜索结果为空 (可能是标签写错了或者没有图)")
        else:
            print(f"错误：被拦截或拒绝 (Status {response.status_code})")
            # 打印一点点内容看看是什么错误
            print(f"错误详情: {response.text[:200]}")
            
    except Exception as e:
        print(f"请求异常: {e}")
    return None

def send_telegram(img_url):
    quote_text = get_daily_quote()
    
    send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    caption_text = f"{quote_text}\n\n🏐 <b>每日排球少年</b>\n#Haikyuu"

    payload = {
        "chat_id": CHAT_ID,
        "photo": img_url,
        "caption": caption_text,
        "parse_mode": "HTML"
    }
    
    try:
        print("正在推送给 Telegram...")
        # 发送消息不需要 cloudscraper，用普通的 requests 就行
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
        print("=== 任务开始 (Cloudscraper + Safebooru + Haikyuu全员) ===")
        pic = get_haikyuu_image()
        
        if pic:
            send_telegram(pic)
            print("=== 任务完成 ===")
        else:
            print("=== 任务失败：未获取到图片 ===")
            exit(1)
