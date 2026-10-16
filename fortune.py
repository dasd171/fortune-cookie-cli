import random, datetime, sys
FORTUNES = ["今天适合写代码，不适合改需求。", "你的下一个 bug 会在 5 分钟内自己出现，也会在 5 分钟内自己消失。",
"有人在偷偷 star 你的仓库。", "喝杯水，世界会更清晰。", "好运就藏在你下一次 git commit 里。",
"今天的你比昨天多懂了一个快捷键。", "不要相信能一次跑通的代码。", "一位老朋友会突然给你发消息。",
"午饭吃面，运势加倍。", "你会遇到一个让你开心的 PR。", "休息也是生产力。", "大胆一点，结果会比你想的好。"]
def main():
    seed = datetime.date.today().isoformat() if "--daily" in sys.argv else None
    rng = random.Random(seed)
    print("  _______\n /  🥠   \\\n \\_______/")
    print("签语：", rng.choice(FORTUNES))
    print("幸运数字：", " ".join(str(n) for n in sorted(rng.sample(range(1, 50), 6))))
if __name__ == "__main__": main()
