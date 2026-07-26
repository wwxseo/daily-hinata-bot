# 🏐 Daily Haikyuu Bot (每日排球少年机器人)

> 一个基于 GitHub Actions 的零成本 Telegram 机器人，每日定时推送《排球少年！！》高清壁纸与正能量语录。

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/你的GitHub用户名/仓库名称/daily.yml?label=Build)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📖 项目简介

这是一个完全自动化、**零成本**运行的 Telegram 机器人。它利用 **GitHub Actions** 的定时任务功能，每天自动从 **Wallhaven** 获取一张《排球少年！！》的高清壁纸，并从 **一言 (Hitokoto)** 获取一句随机的动漫/哲学语录，推送到你的 Telegram 频道或群组。

**无需购买服务器，无需维护，Fork 即用！**

### ✨ 功能亮点

- **📅 每日定时推送**：默认每天北京时间早上 8:00 推送（时间可自定义）。
- **🖼️ 高清壁纸源**：接入 Wallhaven API，获取高质量二次元壁纸（支持随机筛选）。
- **💬 每日语录**：随机附带一句动漫或文学金句，每天都有新感觉。
- **🚀 Serverless**：完全依赖 GitHub Actions 运行，无需 VPS。
- **🛡️ 稳定可靠**：使用官方 API 接口，无需处理复杂的反爬虫验证。

---

## 📸 效果预览

<!-- 建议把你刚才那张成功的手机截图放在这里，非常直观 -->
![Screenshot_2025-12-21-00-21-50-77_948cd9899890cbd5c2798760b2b95377](https://github.com/user-attachments/assets/7cd983e7-c06a-4634-9cb1-277572c89418)

---

## 🚀 快速部署 (如何拥有自己的机器人)

你不需要懂代码，只需要按照以下步骤操作即可。

### 1. Fork 本仓库
点击页面右上角的 **Fork** 按钮，将本项目复制到你自己的 GitHub 账号下。

### 2. 准备 Telegram 机器人
1. 在 Telegram 中搜索 `@BotFather`。
2. 发送 `/newbot` 创建新机器人，获取 **Token**。
3. 创建一个频道 (Channel) 或群组，将机器人拉入并设为**管理员**。
4. 获取你的 **Chat ID** (可以使用 `@getidsbot` 获取)。

### 3. 配置 GitHub Secrets
为了安全起见，不要将 Token 直接写在代码里。请在你的 GitHub 仓库中配置环境变量：

1. 进入仓库的 **Settings** -> **Secrets and variables** -> **Actions**。
2. 点击 **New repository secret**，添加以下两个变量：

| Name | Value (填入你的值) | 说明 |
| :--- | :--- | :--- |
| `BOT_TOKEN` | `123456:ABC-Def...` | 从 BotFather 获取的 Token |
| `CHAT_ID` | `-100xxxxxxx` | 你的频道或群组 ID (频道ID通常以 -100 开头) |

### 4. 启用定时任务
1. 点击仓库上方的 **Actions** 标签。
2. 你可能会看到一个警告："Workflows aren't being run on this forked repository"，点击绿色的 **I understand my workflows, go ahead and enable them**。
3. 在左侧选择 **Daily Hinata Push**，手动点击 **Run workflow** 测试一次。
4. 测试成功后，机器人将在每天固定时间自动运行。

---

## ⚙️ 自定义配置

### 修改推送时间
打开 `.github/workflows/daily.yml` 文件，修改 `cron` 表达式：

```yaml
on:
  schedule:
    # 每天 UTC 时间 0:00 (北京时间 8:00)
    - cron: '0 0 * * *'
如果你想改成北京时间早上 9 点，将第一个 0 改为 1 即可。
```
### 修改图片搜索关键词
打开 `main.py` 文件，找到 `url` 变量：
```# q=haikyuu 表示搜索排球少年，你可以改成 q=hinata shoyo (只看日向翔阳)
url = "https://wallhaven.cc/api/v1/search?q=haikyuu&categories=010&purity=100&sorting=random"
```
## 🛠️ 技术栈
Python 3
GitHub Actions (CI/CD)
Requests (HTTP Library)
Telegram Bot API
Wallhaven API (Image Source)
Hitokoto API (Quote Source)
## 🤝 致谢
感谢以下服务提供的免费 API：

- [Wallhaven](https://wallhaven.cc) - 最好的二次元壁纸站
- [Hitokoto 一言](https://hitokoto.cn) - 感动人心的文字
- 
## 📄 License
本项目采用 MIT License 开源协议。
---

## 📅 历史归档 (History)

| 日期 | 每日语录 | 精彩壁纸 |
| :--- | :--- | :---: |
<!-- HISTORY_START -->
| 2026-07-26 | “作业忘写，因而立于廊，最上川。”<br>——《日常》 | <img src='https://w.wallhaven.cc/full/5d/wallhaven-5dggj3.jpg' height='150'> |

| 2026-07-25 | “憧憬是距离理解最遥远的感情。”<br>——《BLEACH》 | <img src='https://w.wallhaven.cc/full/e7/wallhaven-e7ypeo.jpg' height='150'> |

| 2026-07-24 | “你们人类让我明白了一个道理，那就是这个世界是不讲道理的”<br>——《刺客伍六七》 | <img src='https://w.wallhaven.cc/full/wq/wallhaven-wq8eer.png' height='150'> |

| 2026-07-23 | “跌跌撞撞的成长，又美又疼才是本质。”<br>——《哥斯拉不说话》 | <img src='https://w.wallhaven.cc/full/wy/wallhaven-wyxpr7.jpg' height='150'> |

| 2026-07-22 | “人生于我，一场豪赌而已。”<br>——《赡养人类》 | <img src='https://w.wallhaven.cc/full/wq/wallhaven-wq8eer.png' height='150'> |

| 2026-07-21 | “世界历史的最后一个阶段是它的悲剧。”<br>——《黑格尔法哲学批判导言》 | <img src='https://w.wallhaven.cc/full/gj/wallhaven-gj2x57.jpg' height='150'> |

| 2026-07-20 | “死生，命也，其有夜旦之常，天也。人之有所不得与，皆物之情也。”<br>——《庄子·大宗师》 | <img src='https://w.wallhaven.cc/full/2k/wallhaven-2k591y.png' height='150'> |

| 2026-07-19 | “我的一生，无怨无悔！”<br>——《北斗神拳》 | <img src='https://w.wallhaven.cc/full/vm/wallhaven-vmrypp.png' height='150'> |

| 2026-07-18 | “我思故我在。”<br>——《谈谈方法》 | <img src='https://w.wallhaven.cc/full/k9/wallhaven-k96kxm.jpg' height='150'> |

| 2026-07-17 | “死亡是所有人的共同幸福。”<br>——《最不幸的人》 | <img src='https://w.wallhaven.cc/full/o5/wallhaven-o5vx5m.jpg' height='150'> |

| 2026-07-16 | “死亡是所有人的共同幸福。”<br>——《最不幸的人》 | <img src='https://w.wallhaven.cc/full/p9/wallhaven-p9v89e.jpg' height='150'> |

| 2026-07-15 | “遇到事情不能坐以待毙。”<br>——《捷德奥特曼》 | <img src='https://w.wallhaven.cc/full/d5/wallhaven-d5qe8g.jpg' height='150'> |

| 2026-07-14 | “对不起，风太大了，我听不清。”<br>——《东京巴比伦》 | <img src='https://w.wallhaven.cc/full/e7/wallhaven-e7ypeo.jpg' height='150'> |

| 2026-07-13 | “无暇为五条悟的死哀悼，被投入到战场的是……雷神，鹿紫云一。”<br>——《咒术回战》 | <img src='https://w.wallhaven.cc/full/vm/wallhaven-vmrovl.png' height='150'> |

| 2026-07-11 | “任尘世繁华，唯有守护你的一切，才是我此生唯一的使命。”<br>——《次元战争·红龙》 | <img src='https://w.wallhaven.cc/full/g7/wallhaven-g7z3z3.jpg' height='150'> |

| 2026-07-10 | “当连自己的路途也看不见时，人便不该不理一切地疯狂奔跑。”<br>——《海虎Ⅱ》 | <img src='https://w.wallhaven.cc/full/mp/wallhaven-mp33vk.jpg' height='150'> |

| 2026-07-09 | “あなたは敵だけど悪くない。”<br>——《火影忍者》 | <img src='https://w.wallhaven.cc/full/p8/wallhaven-p8grxj.jpg' height='150'> |

| 2026-07-08 | “为学日益，为道日损。”<br>——《道德经》 | <img src='https://w.wallhaven.cc/full/r2/wallhaven-r2eemj.png' height='150'> |

| 2026-07-07 | “不可以逃避！活下去！活下去也是一种战斗！”<br>——《机动战士高达独角兽》 | <img src='https://w.wallhaven.cc/full/j5/wallhaven-j5jppq.png' height='150'> |

| 2026-07-06 | “对于我们的幸福来说，别人的看法在本质上来讲并不十分重要。”<br>——《人生的智慧》 | <img src='https://w.wallhaven.cc/full/r7/wallhaven-r7zoq7.jpg' height='150'> |

| 2026-07-05 | “前天是小兔子，昨天是小鹿，今天是你。”<br>——《Clannad》 | <img src='https://w.wallhaven.cc/full/o5/wallhaven-o5vx5m.jpg' height='150'> |

| 2026-07-04 | “我们登上并非我们所选择的舞台，演出并非我们所选择的剧本。”<br>——《Enchiridion》 | <img src='https://w.wallhaven.cc/full/2k/wallhaven-2k5dwx.png' height='150'> |

| 2026-07-03 | “人生于我，一场豪赌而已。”<br>——《赡养人类》 | <img src='https://w.wallhaven.cc/full/j5/wallhaven-j5jppq.png' height='150'> |

| 2026-07-02 | “物质与意识的辩证关系：物质决定意识，意识反作用于物质。”<br>——《唯物主义哲学》 | <img src='https://w.wallhaven.cc/full/od/wallhaven-od2vy5.jpg' height='150'> |

| 2026-07-01 | “应该在肩膀上长着自己的脑袋。”<br>——《弗拉基米尔.伊里奇.列宁》 | <img src='https://w.wallhaven.cc/full/lq/wallhaven-lq7ky2.jpg' height='150'> |

| 2026-06-30 | “吾尝终日不食，终夜不寝，以思无益，不如学也。”<br>——《论语》 | <img src='https://w.wallhaven.cc/full/72/wallhaven-723o1y.jpg' height='150'> |

| 2026-06-29 | “所谓辉煌的人生，不过是欲望的囚徒。”<br>——《网络》 | <img src='https://w.wallhaven.cc/full/6d/wallhaven-6dgkd6.jpg' height='150'> |

| 2026-06-28 | “方生方死，方死方生，方可方不可，方不可方可。”<br>——《齐物论》 | <img src='https://w.wallhaven.cc/full/3k/wallhaven-3kewyv.png' height='150'> |

| 2026-06-27 | “あなたは敵だけど悪くない。”<br>——《火影忍者》 | <img src='https://w.wallhaven.cc/full/q6/wallhaven-q6ow85.jpg' height='150'> |

| 2026-06-26 | “不幸的是我们等了那么多年，幸运的我们那么多年过去还一直在一起”<br>——《薄荷之夏》 | <img src='https://w.wallhaven.cc/full/gp/wallhaven-gpx8pl.jpg' height='150'> |

| 2026-06-25 | “人生不如意十有八九！”<br>——《龙与虎》 | <img src='https://w.wallhaven.cc/full/p2/wallhaven-p299ve.jpg' height='150'> |

| 2026-06-24 | “爱欲于人，犹如执炬，逆风而行，必有烧手之患。”<br>——《四十二章经》 | <img src='https://w.wallhaven.cc/full/vm/wallhaven-vmrovl.png' height='150'> |

| 2026-06-23 | “如果不能忠于自己的心，胜负又有什么价值呢？”<br>——《塔希里亚故事集》 | <img src='https://w.wallhaven.cc/full/w8/wallhaven-w8rl5q.png' height='150'> |

| 2026-06-22 | “蔷薇不管被冠以什么名字，却依旧可以芳香扑鼻。”<br>——《我的青春恋爱物语果然有问题》 | <img src='https://w.wallhaven.cc/full/j8/wallhaven-j8xxqq.jpg' height='150'> |

| 2026-06-21 | “求你，保护那孩子，消除灾厄，抹除祸事。哪怕⋯⋯那是我自己……”<br>——《食灵》 | <img src='https://w.wallhaven.cc/full/6q/wallhaven-6qddg6.jpg' height='150'> |

| 2026-06-20 | “今天的风儿有些喧嚣啊。”<br>——《男子高中生的日常》 | <img src='https://w.wallhaven.cc/full/w8/wallhaven-w8rl5q.png' height='150'> |

| 2026-06-19 | “越想贴近事实，不明白的事情就越多。”<br>——《宝石之国》 | <img src='https://w.wallhaven.cc/full/mp/wallhaven-mp33vk.jpg' height='150'> |

| 2026-06-18 | “有形的东西迟早会凋零，但只有回忆是永远不会凋零的。”<br>——《火影忍者》 | <img src='https://w.wallhaven.cc/full/7p/wallhaven-7po3pv.jpg' height='150'> |

| 2026-06-17 | “前进吧，星星在你的头上闪耀哦！”<br>——《四月是你的谎言》 | <img src='https://w.wallhaven.cc/full/1k/wallhaven-1klx23.png' height='150'> |

| 2026-06-16 | “休息对于生存而言，也是紧要问题”<br>——《虫师》 | <img src='https://w.wallhaven.cc/full/q6/wallhaven-q6ow85.jpg' height='150'> |

| 2026-06-15 | “两个人从监狱的窗户往外看，一个看见了土地，一个看见了星星。”<br>——《jojo的奇妙冒险》 | <img src='https://w.wallhaven.cc/full/2k/wallhaven-2k591y.png' height='150'> |

| 2026-06-14 | “哲学家们只是用不同的方式解释世界，而问题在于改变世界。”<br>——《关于费尔巴哈的提纲》 | <img src='https://w.wallhaven.cc/full/r2/wallhaven-r2eemj.png' height='150'> |

| 2026-06-13 | “恋爱不是谈出来的，而是陷进去的。”<br>——《GAMER电玩咖！》 | <img src='https://w.wallhaven.cc/full/x1/wallhaven-x1273z.png' height='150'> |

| 2026-06-12 | “爱,其实很简单，困难的是去接受它。”<br>——《通灵王》 | <img src='https://w.wallhaven.cc/full/m9/wallhaven-m9dv18.jpg' height='150'> |

| 2026-06-11 | “我们是学生，学生就要有学生的样子。”<br>——《JOJO的奇妙冒险》 | <img src='https://w.wallhaven.cc/full/l8/wallhaven-l8v2d2.jpg' height='150'> |

| 2026-06-10 | “Stay hungry, Stay foolish.”<br>——《乔布斯斯坦福大学毕业演讲》 | <img src='https://w.wallhaven.cc/full/72/wallhaven-723o1y.jpg' height='150'> |

| 2026-06-09 | “在某种意义上说即令这世界全不存在，音乐却还存在。”<br>——《作为意志和表象的世界》 | <img src='https://w.wallhaven.cc/full/6o/wallhaven-6ojjy7.jpg' height='150'> |

| 2026-06-08 | “如果喜欢，就把这一切当作是荣耀，而不是炫耀。”<br>——《全职高手》 | <img src='https://w.wallhaven.cc/full/1k/wallhaven-1klx23.png' height='150'> |

| 2026-06-07 | “以有涯随无涯，殆已！已而为知者，殆而已矣！”<br>——《庄子》 | <img src='https://w.wallhaven.cc/full/m3/wallhaven-m3evd1.jpg' height='150'> |

| 2026-06-06 | “我们所爱之物昭示着我们究竟是谁。”<br>——《托马斯·阿奎纳》 | <img src='https://w.wallhaven.cc/full/7p/wallhaven-7po3pv.jpg' height='150'> |

| 2026-06-05 | “以有涯随无涯，殆已！已而为知者，殆而已矣！”<br>——《庄子》 | <img src='https://w.wallhaven.cc/full/2k/wallhaven-2k5dwx.png' height='150'> |

| 2026-06-04 | “龙儿是我的，谁都不准碰！”<br>——《龙虎斗》 | <img src='https://w.wallhaven.cc/full/8x/wallhaven-8x1d5y.png' height='150'> |

| 2026-06-03 | “是不是现在踏出这一步，下决定的是他。”<br>——《电波教师》 | <img src='https://w.wallhaven.cc/full/q2/wallhaven-q25god.png' height='150'> |

| 2026-06-02 | “如果当初握住的不是硬币，而是勇者的手......”<br>——《中二病也要谈恋爱 恋！》 | <img src='https://w.wallhaven.cc/full/od/wallhaven-od55vm.jpg' height='150'> |

| 2026-06-01 | “因为失去,所以明白。”<br>——《火影忍者》 | <img src='https://w.wallhaven.cc/full/96/wallhaven-96kkq8.jpg' height='150'> |

| 2026-05-31 | “一个人若是没有热情，他将一事无成，而热情的基点正是责任心。”<br>——《名人名言》 | <img src='https://w.wallhaven.cc/full/8x/wallhaven-8x1d5y.png' height='150'> |

| 2026-05-30 | “无论乌云有多浓厚，星星也一定还在，只是暂时看不到了而已。”<br>——《电波女与青春男》 | <img src='https://w.wallhaven.cc/full/md/wallhaven-mdmrok.png' height='150'> |

| 2026-05-29 | “人类的伟大之处就在于面对恐惧时的崇高姿态。”<br>——《JOJO的奇妙冒险》 | <img src='https://w.wallhaven.cc/full/6o/wallhaven-6ojjy7.jpg' height='150'> |

| 2026-05-28 | “温柔正确的人总是难以生存，因为这世界既不温柔，也不正确。”<br>——《我的青春恋爱物语果然有问题》 | <img src='https://w.wallhaven.cc/full/5d/wallhaven-5d85j9.png' height='150'> |

| 2026-05-27 | “憧憬，是距离了解最遥远的一种感情。”<br>——《BLEACH》 | <img src='https://w.wallhaven.cc/full/w8/wallhaven-w8eer6.jpg' height='150'> |

| 2026-05-26 | “荣格感到惊异，并向他指出有很多具骷髅，而不是只有一具。”<br>——《千高原》 | <img src='https://w.wallhaven.cc/full/j8/wallhaven-j8xxqq.jpg' height='150'> |

| 2026-05-25 | “其实美丽的故事都是没有结局的，只因为它没有结局所以才会美丽。”<br>——《萤火之森》 | <img src='https://w.wallhaven.cc/full/2k/wallhaven-2k5dwx.png' height='150'> |

| 2026-05-24 | “天欲使其灭亡，必先使其疯狂。”<br>——《佚名》 | <img src='https://w.wallhaven.cc/full/eo/wallhaven-eo19p8.jpg' height='150'> |

| 2026-05-23 | “只顾眼前的利益而任人摆布……我已经……受够了……”<br>——《电锯人》 | <img src='https://w.wallhaven.cc/full/m9/wallhaven-m9dv18.jpg' height='150'> |

| 2026-05-22 | “我的一生，无怨无悔！”<br>——《北斗神拳》 | <img src='https://w.wallhaven.cc/full/76/wallhaven-76ppov.jpg' height='150'> |

| 2026-05-21 | “吾心吾行澄如明镜，所作所为皆为正义。”<br>——《JOJO的奇妙冒险》 | <img src='https://w.wallhaven.cc/full/o3/wallhaven-o37xkl.jpg' height='150'> |

| 2026-05-20 | “我们要一直往上爬，总有一天抵达月亮吧。”<br>——《少女终末旅行》 | <img src='https://w.wallhaven.cc/full/q6/wallhaven-q6ow85.jpg' height='150'> |

| 2026-05-19 | “老是低着头，幸福可是会离你而去的喔。”<br>——《我们的仙境》 | <img src='https://w.wallhaven.cc/full/r7/wallhaven-r7zoq7.jpg' height='150'> |

| 2026-05-18 | “人总是贪婪的，就像最开始，我也只是想知道你的名字。”<br>——《你的名字》 | <img src='https://w.wallhaven.cc/full/q6/wallhaven-q6ow85.jpg' height='150'> |

| 2026-05-17 | “任何一件事都具有两面性。”<br>——《弗拉基米尔·伊里奇·列宁》 | <img src='https://w.wallhaven.cc/full/8x/wallhaven-8x1d5y.png' height='150'> |

| 2026-05-16 | “行百里者半九十。”<br>——《战国策·秦策五·谓秦王》 | <img src='https://w.wallhaven.cc/full/qd/wallhaven-qd83vl.png' height='150'> |

| 2026-05-15 | “你处在幸福的未知之中，不用去管白天的责任和问题。”<br>——《从早“茫”到晚》 | <img src='https://w.wallhaven.cc/full/w8/wallhaven-w8r6vr.png' height='150'> |

| 2026-05-14 | “自己不经意的一句话，触动了别人的心。”<br>——《恋如雨止》 | <img src='https://w.wallhaven.cc/full/lm/wallhaven-lm5gq2.png' height='150'> |

| 2026-05-13 | “从0开始，直到1。”<br>——《Love Live!》 | <img src='https://w.wallhaven.cc/full/2k/wallhaven-2k5dwx.png' height='150'> |

| 2026-05-12 | “人类的赞歌就是勇气的赞歌。”<br>——《JOJO的奇妙冒险》 | <img src='https://w.wallhaven.cc/full/r2/wallhaven-r2eemj.png' height='150'> |

| 2026-05-11 | “那些听不见音乐的人以为跳舞的人疯了。”<br>——《上帝死了》 | <img src='https://w.wallhaven.cc/full/3k/wallhaven-3ke5q3.png' height='150'> |

| 2026-05-10 | “哲学家们只是用不同的方式解释世界，而问题在于改变世界。”<br>——《关于费尔巴哈的提纲》 | <img src='https://w.wallhaven.cc/full/vm/wallhaven-vmrypp.png' height='150'> |

| 2026-05-09 | “无论在哪里遇到你，我都会喜欢上你。”<br>——《AngleBeats!》 | <img src='https://w.wallhaven.cc/full/qd/wallhaven-qd8gz7.jpg' height='150'> |

| 2026-05-08 | “憧憬是距离理解最遥远的感情。”<br>——《蓝染惣右介》 | <img src='https://w.wallhaven.cc/full/e7/wallhaven-e7ypeo.jpg' height='150'> |

| 2026-05-07 | “不可结缘，徒留寂寞……”<br>——《夏目友人帐》 | <img src='https://w.wallhaven.cc/full/8x/wallhaven-8x1d5y.png' height='150'> |

| 2026-05-06 | “世上所以不公平之事是由于当事人能力不足所致。”<br>——《金木研》 | <img src='https://w.wallhaven.cc/full/r2/wallhaven-r2eemj.png' height='150'> |

| 2026-05-05 | “爱与友情以及勇气改变不了一个人，只有受伤才能让人成长。”<br>——《我的青春恋爱物语果然有问题》 | <img src='https://w.wallhaven.cc/full/qd/wallhaven-qdzz8d.jpg' height='150'> |

| 2026-05-04 | “如果有一个喜欢你的人出现，一定不要凶她哦！”<br>——《次元战争·红龙》 | <img src='https://w.wallhaven.cc/full/3k/wallhaven-3kewyv.png' height='150'> |

| 2026-05-03 | “我问你：你是我的Master吗？”<br>——《命运守护夜》 | <img src='https://w.wallhaven.cc/full/vm/wallhaven-vmrypp.png' height='150'> |

| 2026-05-02 | “行远自迩，登高自卑。”<br>——《礼记》 | <img src='https://w.wallhaven.cc/full/2k/wallhaven-2k591y.png' height='150'> |

| 2026-05-01 | “如果书像是寻宝一样被发现，书会比较高兴。”<br>——《我想吃掉你的胰脏》 | <img src='https://w.wallhaven.cc/full/m9/wallhaven-m9dv18.jpg' height='150'> |

| 2026-04-30 | “我不相信人类......但是，我相信人类的“可能性””<br>——《游戏人生》 | <img src='https://w.wallhaven.cc/full/5w/wallhaven-5wjej7.jpg' height='150'> |

| 2026-04-29 | “孤独的人不会伤害别人，只会不断地伤害自己罢了。”<br>——《我的青春恋爱物语果然有问题》 | <img src='https://w.wallhaven.cc/full/zx/wallhaven-zxroyw.jpg' height='150'> |

| 2026-04-28 | “为什么要担心？如果努力了，担心不会让结果变得更好。”<br>——《迪士尼》 | <img src='https://w.wallhaven.cc/full/3k/wallhaven-3klly6.jpg' height='150'> |

| 2026-04-27 | “若以色见我，以音声求我，是人行邪道，不能见如来。”<br>——《金刚经》 | <img src='https://w.wallhaven.cc/full/8x/wallhaven-8x1d5y.png' height='150'> |

| 2026-04-26 | “每一个不曾起舞的日子，都是对生命的辜负。”<br>——《尼采》 | <img src='https://w.wallhaven.cc/full/yx/wallhaven-yx3v9g.jpg' height='150'> |

| 2026-04-25 | “末将于禁，愿为曹家世代赴汤蹈火。”<br>——《镇魂街》 | <img src='https://w.wallhaven.cc/full/w8/wallhaven-w8r6vr.png' height='150'> |

| 2026-04-24 | “每一个不曾起舞的日子，都是对生命的辜负。”<br>——《尼采》 | <img src='https://w.wallhaven.cc/full/j8/wallhaven-j8xxqq.jpg' height='150'> |

| 2026-04-23 | “我们要一直往上爬，总有一天抵达月亮吧。”<br>——《少女终末旅行》 | <img src='https://w.wallhaven.cc/full/r2/wallhaven-r26vz1.jpg' height='150'> |

| 2026-04-22 | “人生没有彩排，只有现场直播，所以做最好的自己。”<br>——《Internet》 | <img src='https://w.wallhaven.cc/full/r7/wallhaven-r7zoq7.jpg' height='150'> |

| 2026-04-21 | “真羡慕你啊……有那么多同伴在等你。”<br>——《少女终末旅行》 | <img src='https://w.wallhaven.cc/full/72/wallhaven-723o1y.jpg' height='150'> |

| 2026-04-20 | “花早晚会凋谢，记忆最终也会消散。”<br>——《镇魂街》 | <img src='https://w.wallhaven.cc/full/8x/wallhaven-8x1d5y.png' height='150'> |

| 2026-04-19 | “喜欢你，因为我喜欢你，比地球上任何人都，喜欢你...”<br>——《名侦探柯南》 | <img src='https://w.wallhaven.cc/full/yx/wallhaven-yx3v9g.jpg' height='150'> |

| 2026-04-18 | “我又不是因为你们的评价才去当的英雄，是因为我想当才去当的。”<br>——《一拳超人》 | <img src='https://w.wallhaven.cc/full/k9/wallhaven-k96kxm.jpg' height='150'> |

| 2026-04-17 | “真羡慕你啊……有那么多同伴在等你。”<br>——《少女终末旅行》 | <img src='https://w.wallhaven.cc/full/m3/wallhaven-m3vd3k.jpg' height='150'> |

| 2026-04-15 | “人类的伟大之处就在于面对恐惧时的崇高姿态。”<br>——《JOJO的奇妙冒险》 | <img src='https://w.wallhaven.cc/full/qd/wallhaven-qdzz8d.jpg' height='150'> |

| 2026-04-14 | “每当心情郁闷的时候，用手托腮就好，手臂会因为帮上忙而开心的。”<br>——《四月是你的谎言》 | <img src='https://w.wallhaven.cc/full/j5/wallhaven-j5d6j5.jpg' height='150'> |

| 2026-04-13 | “要改变别人的心真是件很难办的事，不过改变自己要容易一点。”<br>——《XXXHolic》 | <img src='https://w.wallhaven.cc/full/2k/wallhaven-2k591y.png' height='150'> |

| 2026-04-12 | “不幸的是我们等了那么多年，幸运的我们那么多年过去还一直在一起”<br>——《薄荷之夏》 | <img src='https://w.wallhaven.cc/full/72/wallhaven-723o1y.jpg' height='150'> |

| 2026-04-11 | “为者常成，行者常至。”<br>——《晏子春秋·内篇杂下》 | <img src='https://w.wallhaven.cc/full/vg/wallhaven-vge7r8.jpg' height='150'> |

| 2026-04-10 | “无暇为五条悟的死哀悼，被投入到战场的是……雷神，鹿紫云一。”<br>——《咒术回战》 | <img src='https://w.wallhaven.cc/full/3k/wallhaven-3klly6.jpg' height='150'> |

| 2026-04-09 | “风吹柳叶遮黄雀，薄翅不觉已落蝉。”<br>——《我为苍生》 | <img src='https://w.wallhaven.cc/full/d5/wallhaven-d5qe8g.jpg' height='150'> |

| 2026-04-08 | “憧憬是距离理解最遥远的感情。”<br>——《BLEACH》 | <img src='https://w.wallhaven.cc/full/3k/wallhaven-3kewyv.png' height='150'> |

| 2026-04-07 | “我们没有永恒的朋友，也没有永恒的敌人，只有永恒的利益。”<br>——《亨利·坦普尔》 | <img src='https://w.wallhaven.cc/full/od/wallhaven-odx5j7.png' height='150'> |

| 2026-04-06 | “憧憬是距离理解最遥远的感情。”<br>——《蓝染惣右介》 | <img src='https://w.wallhaven.cc/full/j5/wallhaven-j5jppq.png' height='150'> |

| 2026-04-05 | “任何一件事都具有两面性。”<br>——《弗拉基米尔·伊里奇·列宁》 | <img src='https://w.wallhaven.cc/full/qd/wallhaven-qd83vl.png' height='150'> |

| 2026-04-04 | “人类的伟大之处就在于面对恐惧时的崇高姿态。”<br>——《JOJO的奇妙冒险》 | <img src='https://w.wallhaven.cc/full/j8/wallhaven-j8xxqq.jpg' height='150'> |

| 2026-04-03 | “你背朝太阳，就只能看到自己的影子。”<br>——《纪伯伦语录》 | <img src='https://w.wallhaven.cc/full/2k/wallhaven-2k591y.png' height='150'> |

| 2026-04-02 | “我们是学生，学生就要有学生的样子。”<br>——《JOJO的奇妙冒险》 | <img src='https://w.wallhaven.cc/full/8x/wallhaven-8x1d5y.png' height='150'> |

| 2026-04-01 | “吾尝终日不食，终夜不寝，以思无益，不如学也。”<br>——《论语》 | <img src='https://w.wallhaven.cc/full/j5/wallhaven-j5jppq.png' height='150'> |

| 2026-03-31 | “纵然变化，依然故我。”<br>——《墓志铭》 | <img src='https://w.wallhaven.cc/full/j5/wallhaven-j5d6j5.jpg' height='150'> |

| 2026-03-30 | “把同班的可爱女同学娶回家就是我最大的梦想”<br>——《月色真美》 | <img src='https://w.wallhaven.cc/full/95/wallhaven-95y27k.png' height='150'> |

| 2026-03-29 | “一个人决定寂寞，和另一个人相互依偎又有什么错”<br>——《人渣的本愿》 | <img src='https://w.wallhaven.cc/full/7p/wallhaven-7po3pv.jpg' height='150'> |

| 2026-03-28 | “我们的科学永远只是找到近似真理。”<br>——《爱因斯坦》 | <img src='https://w.wallhaven.cc/full/8x/wallhaven-8x1d5y.png' height='150'> |

| 2026-03-27 | “博学而笃志，切问而近思。”<br>——《论语·子张》 | <img src='https://w.wallhaven.cc/full/ox/wallhaven-oxkdrm.png' height='150'> |

| 2026-03-26 | “井底之蛙不曾见过大海，但见过湛蓝的天空。”<br>——《知晓天空之蓝的人啊》 | <img src='https://w.wallhaven.cc/full/l3/wallhaven-l33zjy.jpg' height='150'> |

| 2026-03-25 | “小鸟......是无法追上飞龙的。”<br>——《加油大魔王》 | <img src='https://w.wallhaven.cc/full/od/wallhaven-odx5j7.png' height='150'> |

| 2026-03-24 | “为了爱，与梦想！”<br>——《眼大人》 | <img src='https://w.wallhaven.cc/full/gp/wallhaven-gpx8pl.jpg' height='150'> |

| 2026-03-23 | “加油”<br>——《自编》 | <img src='https://w.wallhaven.cc/full/m3/wallhaven-m3vd3k.jpg' height='150'> |

| 2026-03-22 | “学而不厌，诲人不倦。”<br>——《论语·述而》 | <img src='https://w.wallhaven.cc/full/w8/wallhaven-w8r6vr.png' height='150'> |

| 2026-03-21 | “努力吧！就算再寂寞！也要努力活下去！”<br>——《鬼灭之刃》 | <img src='https://w.wallhaven.cc/full/yj/wallhaven-yjxx3k.jpg' height='150'> |

| 2026-03-20 | “末将于禁，愿为曹家世代赴汤蹈火。”<br>——《镇魂街》 | <img src='https://w.wallhaven.cc/full/8o/wallhaven-8o5xlk.png' height='150'> |

| 2026-03-19 | “认真的思索，真诚的明辨是非，有这种态度，大概可算是善良吧。”<br>——《沉默的大多数》 | <img src='https://w.wallhaven.cc/full/g7/wallhaven-g7z3z3.jpg' height='150'> |

| 2026-03-18 | “一点星光，在心上就能反射出太阳。”<br>——《星光效应》 | <img src='https://w.wallhaven.cc/full/lq/wallhaven-lq88vr.jpg' height='150'> |

| 2026-03-17 | “无法逃避的是自我，而无法挽回的是过去。”<br>——《机动战士高达》 | <img src='https://w.wallhaven.cc/full/vg/wallhaven-vge7r8.jpg' height='150'> |

| 2026-03-16 | “很多事只是最初看起来有意义，但经过多次重复就慢慢失去了意义。”<br>——《人生的智慧》 | <img src='https://w.wallhaven.cc/full/7p/wallhaven-7po3pv.jpg' height='150'> |

| 2026-03-15 | “今后无论发生什么事也好，这个左手上的⋯⋯都是同伴的记号！”<br>——《海贼王》 | <img src='https://w.wallhaven.cc/full/6d/wallhaven-6dgkd6.jpg' height='150'> |

| 2026-03-14 | “跌跌撞撞的成长，又美又疼才是本质。”<br>——《哥斯拉不说话》 | <img src='https://w.wallhaven.cc/full/wy/wallhaven-wyxpr7.jpg' height='150'> |

| 2026-03-13 | “爱,其实很简单，困难的是去接受它。”<br>——《通灵王》 | <img src='https://w.wallhaven.cc/full/6q/wallhaven-6qjovx.png' height='150'> |

| 2026-03-12 | “两个人从监狱的窗户往外看，一个看见了土地，一个看见了星星。”<br>——《jojo的奇妙冒险》 | <img src='https://w.wallhaven.cc/full/95/wallhaven-95y27k.png' height='150'> |

| 2026-03-11 | “取法于上，仅得为中；取法于中，故为其下。”<br>——《每日一习话》 | <img src='https://w.wallhaven.cc/full/1j/wallhaven-1jmxp9.jpg' height='150'> |

| 2026-03-10 | “如果不能忠于自己的心，胜负又有什么价值呢？”<br>——《塔希里亚故事集》 | <img src='https://w.wallhaven.cc/full/0w/wallhaven-0w26ex.png' height='150'> |

| 2026-03-09 | “生命如同寓言，其价值不在于长短，而在于内容。”<br>——《塞涅卡》 | <img src='https://w.wallhaven.cc/full/3k/wallhaven-3klly6.jpg' height='150'> |

| 2026-03-08 | “爱与友情以及勇气改变不了一个人，只有受伤才能让人成长。”<br>——《我的青春恋爱物语果然有问题》 | <img src='https://w.wallhaven.cc/full/lq/wallhaven-lq7ky2.jpg' height='150'> |

| 2026-03-07 | “乘上与平时相反的列车，为了去见从未见过的风景。”<br>——《比宇宙更远的地方》 | <img src='https://w.wallhaven.cc/full/j5/wallhaven-j5jppq.png' height='150'> |

| 2026-03-06 | “如果真是这样， 就由我来把彭格列毁灭！”<br>——《家庭教师》 | <img src='https://w.wallhaven.cc/full/8o/wallhaven-8o5xlk.png' height='150'> |

| 2026-03-05 | “如果你能在浪费时间中获得乐趣，就不算浪费时间。”<br>——《罗素》 | <img src='https://w.wallhaven.cc/full/r2/wallhaven-r26vz1.jpg' height='150'> |

| 2026-03-04 | “梦想是一个天真的词，实现梦想是一个残酷的词”<br>——《哆啦A梦》 | <img src='https://w.wallhaven.cc/full/r2/wallhaven-r2eemj.png' height='150'> |

| 2026-03-03 | “不可结缘,徒增寂寞”<br>——《夏目友人帐》 | <img src='https://w.wallhaven.cc/full/8x/wallhaven-8x5562.jpg' height='150'> |

| 2026-03-02 | “一起去看星星吧。”<br>——《未来日记》 | <img src='https://w.wallhaven.cc/full/j3/wallhaven-j35qvp.jpg' height='150'> |

| 2026-03-01 | “圣人不死，大盗不止。”<br>——《庄子·外篇·胠箧第十》 | <img src='https://w.wallhaven.cc/full/p8/wallhaven-p8grxj.jpg' height='150'> |

| 2026-02-28 | “我不是天生的王者 但我骨子里流动着不让我低头的血液”<br>——《海贼王》 | <img src='https://w.wallhaven.cc/full/l8/wallhaven-l8v2d2.jpg' height='150'> |

| 2026-02-27 | “不服从命令的人是人渣，抛弃同伴的人连人渣都不如。”<br>——《火影忍者》 | <img src='https://w.wallhaven.cc/full/3k/wallhaven-3kewyv.png' height='150'> |

| 2026-02-26 | “我们的学生会长，比高达还强。”<br>——《旋风管家》 | <img src='https://w.wallhaven.cc/full/0p/wallhaven-0pr29j.png' height='150'> |

| 2026-02-25 | “今后无论发生什么事也好，这个左手上的⋯⋯都是同伴的记号！”<br>——《海贼王》 | <img src='https://w.wallhaven.cc/full/lm/wallhaven-lmlp22.jpg' height='150'> |

| 2026-02-24 | “努力吧！就算再寂寞！也要努力活下去！”<br>——《鬼灭之刃》 | <img src='https://w.wallhaven.cc/full/d5/wallhaven-d5qe8g.jpg' height='150'> |

| 2026-02-23 | “我的一生，无怨无悔！”<br>——《北斗神拳》 | <img src='https://w.wallhaven.cc/full/72/wallhaven-723o1y.jpg' height='150'> |

| 2026-02-22 | “谁是我们的敌人，谁是我们的朋友，这是革命的首要问题。”<br>——《毛主席语录》 | <img src='https://w.wallhaven.cc/full/m3/wallhaven-m3vd3k.jpg' height='150'> |

| 2026-02-21 | “军人天生就舍弃了战斗的意义！”<br>——《机动战士高达00》 | <img src='https://w.wallhaven.cc/full/xl/wallhaven-xlx1mv.png' height='150'> |

| 2026-02-20 | “不拼尽全力去试一下，又怎么会知道啊”<br>——《刺客伍六七》 | <img src='https://w.wallhaven.cc/full/od/wallhaven-od55vm.jpg' height='150'> |

| 2026-02-19 | “不要轻易的口出狂言，那样只会透露出你的软弱。”<br>——《BLEACH》 | <img src='https://w.wallhaven.cc/full/l8/wallhaven-l8v2dr.jpg' height='150'> |

| 2026-02-18 | “时间是存在者的时间。”<br>——《存在与时间》 | <img src='https://w.wallhaven.cc/full/m9/wallhaven-m9dv18.jpg' height='150'> |

| 2026-02-17 | “愿你有一天，能和你最重要的人重逢。”<br>——《可塑性记忆》 | <img src='https://w.wallhaven.cc/full/od/wallhaven-od2vy5.jpg' height='150'> |

| 2026-02-16 | “我只是不想再失去他——哪怕是仅存在一瞬的幻影！”<br>——《加油大魔王》 | <img src='https://w.wallhaven.cc/full/d5/wallhaven-d5qe8g.jpg' height='150'> |

| 2026-02-15 | “我命令你，喜欢我！”<br>——《加油大魔王》 | <img src='https://w.wallhaven.cc/full/o3/wallhaven-o37xkl.jpg' height='150'> |

| 2026-02-14 | “只有分离后才能懂的事，却没有了感慨的时间。”<br>——《宝石之国》 | <img src='https://w.wallhaven.cc/full/lq/wallhaven-lq7ky2.jpg' height='150'> |

| 2026-02-13 | “既然今天是昨天，那么睡到明天就好。”<br>——《青春猪头少年不会梦到兔女郎学姐》 | <img src='https://w.wallhaven.cc/full/q2/wallhaven-q25god.png' height='150'> |

| 2026-02-12 | “忘掉一个人的劣根性就像把千辛万苦赚来的钱扔掉一样。”<br>——《人生的智慧》 | <img src='https://w.wallhaven.cc/full/zx/wallhaven-zxroyw.jpg' height='150'> |

| 2026-02-11 | “憧憬是距离理解最遥远的感情。”<br>——《BLEACH》 | <img src='https://w.wallhaven.cc/full/r7/wallhaven-r7zoq7.jpg' height='150'> |

| 2026-02-10 | “人总是贪婪的，就像最开始，我也只是想知道你的名字。”<br>——《你的名字》 | <img src='https://w.wallhaven.cc/full/d5/wallhaven-d5qe8g.jpg' height='150'> |

| 2026-02-09 | “憧憬是距离理解最遥远的感情。”<br>——《BLEACH》 | <img src='https://w.wallhaven.cc/full/m3/wallhaven-m3evd1.jpg' height='150'> |

| 2026-02-08 | “不是别人，是我，承认了你的价值。”<br>——《fate/zero》 | <img src='https://w.wallhaven.cc/full/r7/wallhaven-r7zoq7.jpg' height='150'> |

| 2026-02-07 | “奇迹不是免费的，如果你祈求了希望，也会散播出同等的绝望。”<br>——《魔法少女小圆》 | <img src='https://w.wallhaven.cc/full/xl/wallhaven-xlx1mv.png' height='150'> |

| 2026-02-06 | “夕阳真是耀眼无比啊。”<br>——《女高中生的虚度日常》 | <img src='https://w.wallhaven.cc/full/3k/wallhaven-3klly6.jpg' height='150'> |

| 2026-02-05 | “纵然变化，依然故我。”<br>——《墓志铭》 | <img src='https://w.wallhaven.cc/full/k9/wallhaven-k96kxm.jpg' height='150'> |

| 2026-02-04 | “此时此刻的咱啊，能和汝在一起，是最幸福的了。”<br>——《狼与香辛料》 | <img src='https://w.wallhaven.cc/full/eo/wallhaven-eo19p8.jpg' height='150'> |

| 2026-02-03 | “あなたは敵だけど悪くない。”<br>——《火影忍者》 | <img src='https://w.wallhaven.cc/full/zx/wallhaven-zxrq3o.png' height='150'> |

| 2026-02-02 | “爱,其实很简单，困难的是去接受它。”<br>——《通灵王》 | <img src='https://w.wallhaven.cc/full/r2/wallhaven-r2eemj.png' height='150'> |

| 2026-02-01 | “如果不能忠于自己的心，胜负又有什么价值呢？”<br>——《塔希里亚故事集》 | <img src='https://w.wallhaven.cc/full/vm/wallhaven-vmrypp.png' height='150'> |

| 2026-01-31 | “所谓觉悟，乃是在漆黑的荒原中，开辟出一条属于自己的星光大道！”<br>——《意大利黑手党第二任教父》 | <img src='https://w.wallhaven.cc/full/p8/wallhaven-p8grxj.jpg' height='150'> |

| 2026-01-30 | “幸运的人一生都在被童年治愈，不幸的人一生都在治愈童年。”<br>——《阿尔弗雷德·阿德勒》 | <img src='https://w.wallhaven.cc/full/qd/wallhaven-qd8gz7.jpg' height='150'> |

| 2026-01-29 | “身为冒险者，如果安静的老死在床上，那简直就是耻辱！”<br>——《恶魔法则》 | <img src='https://w.wallhaven.cc/full/q2/wallhaven-q25god.png' height='150'> |

| 2026-01-28 | “最折磨人的或许不是一场惨烈战争，而是烦琐的日常生活。”<br>——《亦舒》 | <img src='https://w.wallhaven.cc/full/6q/wallhaven-6qddg6.jpg' height='150'> |

| 2026-01-27 | “身为冒险者，如果安静的老死在床上，那简直就是耻辱！”<br>——《恶魔法则》 | <img src='https://w.wallhaven.cc/full/wy/wallhaven-wy33zx.jpg' height='150'> |

| 2026-01-26 | “此时此刻的咱啊，能和汝在一起，是最幸福的了。”<br>——《狼与香辛料》 | <img src='https://w.wallhaven.cc/full/6o/wallhaven-6ojjy7.jpg' height='150'> |

| 2026-01-25 | “沒有永远下不停的雨。”<br>——《秋之回憶》 | <img src='https://w.wallhaven.cc/full/r2/wallhaven-r2eemj.png' height='150'> |

| 2026-01-24 | “孤独的人不会伤害别人，只会不断地伤害自己罢了。”<br>——《我的青春恋爱物语果然有问题》 | <img src='https://w.wallhaven.cc/full/zx/wallhaven-zxroyw.jpg' height='150'> |

| 2026-01-23 | “人，百年一世；龙，百年一岁。君生吾已老，君未变，而吾已老。”<br>——《妖怪名单》 | <img src='https://w.wallhaven.cc/full/l8/wallhaven-l8v2dr.jpg' height='150'> |

| 2026-01-22 | “假如我们相遇，肯定一眼就能认出彼此”<br>——《你的名字》 | <img src='https://w.wallhaven.cc/full/d5/wallhaven-d5qe8g.jpg' height='150'> |

| 2026-01-21 | “熬得住无人问津的日子，方可配得起诗和远方。”<br>——《网络》 | <img src='https://w.wallhaven.cc/full/ox/wallhaven-oxkdrm.png' height='150'> |

| 2026-01-20 | “失去故土的花朵，回不去，却也离不开。”<br>——《长歌行》 | <img src='https://w.wallhaven.cc/full/vg/wallhaven-vge7r8.jpg' height='150'> |

| 2026-01-19 | “信心这个东西，什么时候都像个高楼大厦，但是里面会长白蚁。”<br>——《沉默的大多数》 | <img src='https://w.wallhaven.cc/full/3k/wallhaven-3kewyv.png' height='150'> |

| 2026-01-18 | “前天是兔子，昨天是小鹿，今天是你”<br>——《Clannad》 | <img src='https://w.wallhaven.cc/full/r7/wallhaven-r7zoq7.jpg' height='150'> |

| 2026-01-17 | “曾经发生过的事情不可能忘记，只不过是想不起而已。”<br>——《千与千寻》 | <img src='https://w.wallhaven.cc/full/5d/wallhaven-5d8ky5.jpg' height='150'> |

| 2026-01-16 | “不幸的是我们等了那么多年，幸运的我们那么多年过去还一直在一起”<br>——《薄荷之夏》 | <img src='https://w.wallhaven.cc/full/j3/wallhaven-j35qvp.jpg' height='150'> |

| 2026-01-15 | “哲学的基本问题是思维和存在的关系问题。”<br>——《哲学的基本问题》 | <img src='https://w.wallhaven.cc/full/k9/wallhaven-k961vd.png' height='150'> |

| 2026-01-14 | “巧合是上帝默默操控世界的方式。”<br>——《佚名》 | <img src='https://w.wallhaven.cc/full/eo/wallhaven-eo19p8.jpg' height='150'> |

| 2026-01-13 | “如果你都不知道自己想去哪里，那去哪里都是一样的。”<br>——《柴郡猫》 | <img src='https://w.wallhaven.cc/full/yj/wallhaven-yjxx3k.jpg' height='150'> |

| 2026-01-12 | “苹果是给那些为了爱选择死亡的人的奖励”<br>——《回转企鹅罐》 | <img src='https://w.wallhaven.cc/full/od/wallhaven-od2vy5.jpg' height='150'> |

| 2026-01-11 | “别忘了，我们是羊村守护者！”<br>——《羊村守护者》 | <img src='https://w.wallhaven.cc/full/3k/wallhaven-3klly6.jpg' height='150'> |

| 2026-01-10 | “跌跌撞撞的成长，又美又疼才是本质。”<br>——《哥斯拉不说话》 | <img src='https://w.wallhaven.cc/full/yj/wallhaven-yjrgqg.png' height='150'> |

| 2026-01-09 | “最短的捷径就是绕远路。”<br>——《STEEL BALL RUN》 | <img src='https://w.wallhaven.cc/full/1k/wallhaven-1klx23.png' height='150'> |

| 2026-01-08 | “爱,其实很简单，困难的是去接受它。”<br>——《通灵王》 | <img src='https://w.wallhaven.cc/full/j5/wallhaven-j5jppq.png' height='150'> |

| 2026-01-07 | “风吹柳叶遮黄雀，薄翅不觉已落蝉。”<br>——《我为苍生》 | <img src='https://w.wallhaven.cc/full/x1/wallhaven-x1273z.png' height='150'> |

| 2026-01-06 | “赢得了时间就是赢得了一切。”<br>——《弗拉基米尔·伊里奇·列宁》 | <img src='https://w.wallhaven.cc/full/2k/wallhaven-2k5dwx.png' height='150'> |

| 2026-01-05 | “美好的人眼里映出的世界也是美好的。”<br>——《ARIA》 | <img src='https://w.wallhaven.cc/full/m3/wallhaven-m3evd1.jpg' height='150'> |

| 2026-01-04 | “就算风吹散了冰雪，想念也会留存下来。”<br>——《滑头鬼之孙》 | <img src='https://w.wallhaven.cc/full/m3/wallhaven-m3vd3k.jpg' height='150'> |

| 2026-01-03 | “任尘世繁华，唯有守护你的一切，才是我此生唯一的使命。”<br>——《次元战争·红龙》 | <img src='https://w.wallhaven.cc/full/md/wallhaven-mdmrok.png' height='150'> |

| 2026-01-02 | “用我的左手将你那个不可理喻的幻想粉碎掉！”<br>——《魔法禁书目录》 | <img src='https://w.wallhaven.cc/full/od/wallhaven-od2vy5.jpg' height='150'> |

| 2026-01-01 | “跌跌撞撞的成长，又美又疼才是本质。”<br>——《哥斯拉不说话》 | <img src='https://w.wallhaven.cc/full/zx/wallhaven-zxyyrg.jpg' height='150'> |

| 2025-12-31 | “我命令你，喜欢我！”<br>——《加油大魔王》 | <img src='https://w.wallhaven.cc/full/lq/wallhaven-lq7ky2.jpg' height='150'> |

| 2025-12-30 | “一定没有问题的！”<br>——《魔卡少女樱》 | <img src='https://w.wallhaven.cc/full/lq/wallhaven-lq7ky2.jpg' height='150'> |

| 2025-12-29 | “就算风吹散了冰雪，想念也会留存下来。”<br>——《滑头鬼之孙》 | <img src='https://w.wallhaven.cc/full/72/wallhaven-723o1y.jpg' height='150'> |

| 2025-12-28 | “打架这玩意，不就是为了守护什么东西吗？”<br>——《银魂》 | <img src='https://w.wallhaven.cc/full/r7/wallhaven-r7zoq7.jpg' height='150'> |

| 2025-12-27 | “须知政权是由枪杆子中取得的。”<br>——《八七会议报告》 | <img src='https://w.wallhaven.cc/full/vg/wallhaven-vge7r8.jpg' height='150'> |

| 2025-12-26 | “人生于我，一场豪赌而已。”<br>——《赡养人类》 | <img src='https://w.wallhaven.cc/full/3k/wallhaven-3kewyv.png' height='150'> |

| 2025-12-25 | “学而不厌，诲人不倦。”<br>——《论语·述而》 | <img src='https://w.wallhaven.cc/full/72/wallhaven-723o1y.jpg' height='150'> |

| 2025-12-24 | “如果当初握住的不是硬币，而是勇者的手......”<br>——《中二病也要谈恋爱 恋！》 | <img src='https://w.wallhaven.cc/full/wy/wallhaven-wy33zx.jpg' height='150'> |

| 2025-12-23 | “最短的捷径就是绕远路。”<br>——《STEEL BALL RUN》 | <img src='https://w.wallhaven.cc/full/l8/wallhaven-l8v2dr.jpg' height='150'> |

| 2025-12-22 | “就算天塌下来变成一片废墟，他的脸色也不会有丝毫变化。”<br>——《人生的智慧》 | <img src='https://w.wallhaven.cc/full/vm/wallhaven-vmrovl.png' height='150'> |

| 2025-12-21 | “不可结缘，徒留寂寞……”<br>——《夏目友人帐》 | <img src='https://w.wallhaven.cc/full/72/wallhaven-723o1y.jpg' height='150'> |

| 2025-12-20 | “师者，所以传道授业解惑也。”<br>——《师说》 | <img src='https://w.wallhaven.cc/full/r2/wallhaven-r2eemj.png' height='150'> |

| 2025-12-20 | “学而不厌，诲人不倦。”<br>——《论语·述而》 | <img src='https://w.wallhaven.cc/full/5d/wallhaven-5d85j9.png' height='150'> |

<!-- HISTORY_END -->
