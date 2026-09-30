"""
IndexNow 一键提交脚本
=====================================
作用：把 sitemap.xml 里的所有 URL 一次性推送给 Bing（及其他支持 IndexNow 的引擎）。
原理：IndexNow 是 Bing 主导的开放协议，一次提交同步通知 Bing / Yandex / Naver / Seznam 等。

用法：
    python submit_indexnow.py

以后每次改完文章、重新跑完 build_site.py，再跑一次这个脚本，
Bing 就会在几分钟内来抓取，不用等爬虫排期。
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request

# ============ 配置区（站点域名换了才需要改） ============
SITE_HOST = "changsha-street-food.vercel.app"
INDEXNOW_KEY = "f665029a880f3529140f0860af9005de"
SITEMAP_FILE = "sitemap.xml"
# ======================================================

ENDPOINTS = [
    "https://api.indexnow.org/indexnow",   # 总入口，自动分发到所有参与引擎
    "https://www.bing.com/indexnow",       # Bing 专用，提交记录会出现在 BWT 的 IndexNow 面板
]


def read_urls(path: str) -> list[str]:
    """从 sitemap.xml 里抽出所有 <loc> 地址"""
    if not os.path.exists(path):
        sys.exit(f"找不到 {path}，请先运行 build_site.py 生成站点")
    xml = open(path, encoding="utf-8").read()
    urls = re.findall(r"<loc>\s*(.*?)\s*</loc>", xml)
    return urls


def submit(endpoint: str, urls: list[str]) -> None:
    payload = {
        "host": SITE_HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"https://{SITE_HOST}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        endpoint,
        data=body,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            print(f"  [{r.status}] {endpoint}  —— 已提交 {len(urls)} 条")
    except urllib.error.HTTPError as e:
        hint = {
            400: "请求格式错误",
            403: "密钥文件没生效：确认 https://{host}/{key}.txt 能打开且内容与密钥完全一致".format(
                host=SITE_HOST, key=INDEXNOW_KEY
            ),
            422: "URL 与 host 不匹配",
            429: "提交过于频繁，稍后再试",
        }.get(e.code, "未知错误")
        print(f"  [{e.code}] {endpoint}  —— {hint}")
    except Exception as e:  # 网络层异常
        print(f"  [失败] {endpoint}  —— {e}")


def main() -> None:
    urls = read_urls(SITEMAP_FILE)
    print(f"从 {SITEMAP_FILE} 读到 {len(urls)} 条 URL：")
    for u in urls:
        print(f"  - {u}")
    print("\n开始提交到 IndexNow …")
    for ep in ENDPOINTS:
        submit(ep, urls)
    print("\n完成。几分钟后可在 Bing Webmaster Tools → IndexNow 面板看到记录。")


if __name__ == "__main__":
    main()
