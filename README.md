# Changsha Street Food Guide

**Live site:** https://changsha-street-food.vercel.app

A practical English-language content site about street food in Changsha, China.

Built as a **content-operations portfolio project**: the goal is to demonstrate a full
content loop — topic selection → keyword targeting → production → measurement → iteration → review.

## What's Inside

- 10 English articles, each targeting one long-tail keyword
- Plain static HTML + CSS, no build step, no framework
- `sitemap.xml` and `robots.txt` for search-engine submission
- Clean semantic markup: `<h1>` / `<h2>`, meta descriptions, internal links between articles

## Site Structure

```
index.html              # Article index (hub page)
articles/*.html         # 10 article pages
assets/style.css        # Shared stylesheet
sitemap.xml             # For Bing / Google submission
robots.txt
build_site.py           # Regenerates the whole site from ARTICLES data
```

## Regenerating Content

Edit `ARTICLES` in `build_site.py`, then:

```bash
python build_site.py
```

After deploying, replace `SITE['url']` with your real domain and re-run so the
sitemap points at the correct URLs.

## Measurement

- Search performance (impressions / clicks / CTR / keywords): **Bing Webmaster Tools**
- On-site behavior: Baidu Tongji or Microsoft Clarity

## Note on Prices

Price figures in the articles are approximate local ranges, included as a sanity
check for readers rather than exact quotes. They are meant to be replaced with
first-hand, verified details.

## Stack

Static HTML · CSS · Deployed on Vercel · No JavaScript dependencies
