import cloudscraper
import os
import random
import time

# 1. 获取 GitHub Secrets
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def get_daily_quote():
    # 依然保留语录功能，使用 cloudscraper 请求
    api_url = "https://v1.hitokoto.cn/?c=a&c=b&c=k"
    scraper = cloudscraper.create_scraper() # 创建一个能绕过防护的浏览器实例
    try:
        res = scraper.get(api_url, timeout=10)
        if res.status_code == 200:
            data = res.json()
            return f"“{data.get('hitokoto')}”\n——《{data.get('from')}》"
    except Exception as e:
        print(f"[警告] 获取语录失败: {e}")
    return "“只要球还没落地，就没有输！”\n——《排球少年！！》"

def get_hinata_image():
    # === 更换图源为 Gelbooru ===
    # Gelbooru 对 cloudscraper 非常友好
    # tags=hinata_shouyou 搜索日向翔阳
    # sort:random 随机排序
    # json=1 返回 JSON 格式
    url = "https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&tags=hinata_shouyou+sort:random&limit=20"
    
    print(f"正在请求 Gelbooru 图库: {url}")
    
    # === 核心改动：使用 cloudscraper ===
    # 这行代码会自动处理 'Just a moment...' 这种验证
    scraper = cloudscraper.create_scraper(browser='chrome')
    
    try:
        response = scraper.get(url, timeout=15)
        print(f"图库响应状态码: {response.status_code}")
        
        if response.status_code == 200:
            # Gelbooru 的 JSON 结构可能直接是列表，也可能有 'post' 键
            try:
                data = response.json()
                # 兼容处理：有时候返回的是字典 {'post': [...]}, 有时候直接是列表 [...]
                posts = data.get('post', []) if isinstance(data, dict) else data
                
                if posts and len(posts) > 0:
                    post = random.choice(posts)
                    img_url = post.get('file_url')
                    print(f"成功获取图片链接: {img_url}")
                    return img_url
                else:
                    print("错误：搜索结果为空")
            except Exception as parse_error:
                print(f"解析 JSON 失败: {parse_error}")
                print(f"返回内容: {response.text[:100]}")
        else:
            print(f"错误：依然被拒绝 (Status {response.status_code})")
            
    except Exception as e:
        print(f"请求异常: {e}")
    return None

def send_telegram(img_url):
    quote_text = get_daily_quote()
    # 消息发送依然用普通的 requests 即可，Telegram API 不需要绕过防护
    import requests 
    
    send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    caption_text = f"{quote_text}\n\n🏐 <b>每日日向翔阳</b>\n#Haikyuu #HinataShoyo"

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
        print("=== 任务开始 (使用 Cloudscraper + Gelbooru) ===")
        pic = get_hinata_image()
        
        if pic:
            send_telegram(pic)
            print("=== 任务完成 ===")
        else:
            print("=== 任务失败：未获取到图片 ===")
            exit(1)
