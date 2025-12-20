import requests
import os
import random
import time
from datetime import datetime

# 1. 获取 GitHub Secrets
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# 2. 伪装头 (模拟浏览器访问)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def get_daily_quote():
    """
    获取每日语录
    返回的内容使用 <br> 换行，方便后续插入 README 表格
    """
    api_url = "https://v1.hitokoto.cn/?c=a&c=b&c=k"
    try:
        res = requests.get(api_url, headers=HEADERS, timeout=5)
        if res.status_code == 200:
            data = res.json()
            # 组合语录：内容 + 出处
            return f"“{data.get('hitokoto')}”<br>——《{data.get('from')}》"
    except Exception as e:
        print(f"语录获取失败: {e}")
    
    # 备用语录
    return "“排球是永远向上看的运动！”<br>——《排球少年！！》"

def get_haikyuu_image():
    """
    从 Wallhaven 获取排球少年高清壁纸
    """
    # q=haikyuu: 搜索关键词
    # purity=100: 全年龄
    # sorting=random: 随机排序
    url = "https://wallhaven.cc/api/v1/search?q=haikyuu&categories=010&purity=100&sorting=random"
    
    print(f"正在请求图库: {url}")
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        if response.status_code == 200:
            data = response.json()
            post_list = data.get('data', [])
            if post_list:
                post = random.choice(post_list)
                # path 是原图链接
                return post.get('path')
    except Exception as e:
        print(f"图片请求异常: {e}")
    return None

def update_readme(quote, img_url):
    """
    更新 README.md，写入历史记录
    """
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print("错误：找不到 README.md 文件")
        return

    # 获取今天的日期
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 清理语录：确保没有原始的换行符 \n，否则会破坏 Markdown 表格
    # 我们统一使用 <br> 来换行
    clean_quote = quote.replace("\n", "<br>")
    
    # 构造表格行
    # 使用 height='150' 固定高度，这样表格会非常整齐，不会忽大忽小
    new_row = f"| {today} | {clean_quote} | <img src='{img_url}' height='150'> |\n"

    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 寻找定位标记
        marker = "<!-- HISTORY_START -->"
        if marker in content:
            # 防止同一天重复写入 (如果今天已经发过了，就不再写了)
            if today in content and img_url in content:
                print("⚠️ 今天的内容已经存在于 README，跳过写入。")
                return

            # 在标记后面插入新的一行
            new_content = content.replace(marker, marker + "\n" + new_row)
            
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("✅ README 更新成功！历史记录已添加。")
        else:
            print("⚠️ 未在 README 中找到定位标记 <!-- HISTORY_START -->，无法写入。")
            
    except Exception as e:
        print(f"❌ 更新 README 失败: {e}")

def send_telegram(img_url):
    """
    发送消息到 Telegram
    """
    # 1. 获取语录 (带 <br>)
    quote_html = get_daily_quote()
    
    # 2. 转换语录格式 (Telegram 不支持 <br>，要换成 \n)
    quote_text = quote_html.replace("<br>", "\n")
    
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
        
        if res.status_code == 200:
            # 只有 Telegram 发送成功了，才去写日记 (README)
            print("正在写入历史归档...")
            update_readme(quote_html, img_url)
        else:
            print(f"推送失败原因: {res.text}")
            
    except Exception as e:
        print(f"发送异常: {e}")

if __name__ == "__main__":
    # 检查环境变量
    if not BOT_TOKEN or not CHAT_ID:
        print("致命错误：Secrets (BOT_TOKEN 或 CHAT_ID) 未配置！")
        exit(1)
    else:
        print("=== 任务开始 ===")
        pic = get_haikyuu_image()
        
        if pic:
            print(f"获取图片成功: {pic}")
            send_telegram(pic)
            print("=== 任务完成 ===")
        else:
            print("=== 任务失败：未获取到图片 ===")
            exit(1)
