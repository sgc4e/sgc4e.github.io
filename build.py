#!/usr/bin/env python3
"""Builds _site/ from projects.json: the list is rendered into the HTML so search and AI crawlers
read it without running JavaScript. Also writes llms.txt and sitemap.xml. Stdlib only.
Run: python3 build.py   (CI runs it on every push; admin.html only edits projects.json)."""
import json, shutil, datetime, html, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, '_site')
URL = 'https://sgc4e.github.io/'
PERSON_ID = 'https://saurabhgarg.com/#/schema/person/d492448b73b2fe032dd850c5107d6448'
REPO_TOTAL = 135  # all repos at launch, shown or hidden; bump when Sync adds more
e = lambda s: html.escape(str(s or ''), quote=True)

def slug(s): return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
def safe(u): return u if isinstance(u, str) and re.match(r'^https?://', u) else None

def build():
    d = json.load(open(os.path.join(ROOT, 'projects.json')))
    site, ps = d['site'], sorted(d['projects'], key=lambda p: p['date'], reverse=True)
    today = datetime.date.today()
    live = [p for p in ps if p['status'] == 'Live']
    top = [p['title'] for p in (live or ps)[:3]]
    named = ' and '.join(top) if len(top) < 3 else f"{top[0]}, {top[1]} and {top[2]}"
    desc = (f"Saurabh Garg: marketer, founder of C4E (2014), writer, and builder of AI tools in Dubai and Mumbai. "
            f"{REPO_TOTAL} GitHub repositories since 2025.")
    assert len(desc) <= 160, len(desc)

    # list grouped by month
    groups = {}
    for p in ps:
        groups.setdefault(datetime.date.fromisoformat(p['date']).strftime('%B %Y'), []).append(p)
    out = []
    for m, items in groups.items():
        lis = []
        for p in items:
            link, code = safe(p.get('link')), safe(p.get('repo'))
            t = f'<a href="{e(link)}" rel="noopener">{e(p["title"])}</a>' if link else e(p['title'])
            links = ''.join(f'<a href="{e(u)}" rel="noopener">{n}</a>' for u, n in ((link, 'Visit'), (code, 'Code')) if u)
            lis.append(f'''<li class="item" id="{e(slug(p['name']))}" data-c="{e(p['category'])}">
  <div class="meta"><span>{e(p['category'])}</span><span class="status s-{e(p['status'].lower())}">{e(p['status'])}</span><time datetime="{e(p['date'])}">{datetime.date.fromisoformat(p['date']).strftime('%-d %b %Y')}</time></div>
  <h3>{t}</h3>
  <p>{e(p['blurb'])}</p>{f'<p class="links">{links}</p>' if links else ''}
</li>''')
        out.append(f'<section class="month"><h2>{e(m)} <span class="count">{len(items)}</span></h2><ul>{"".join(lis)}</ul></section>')
    cats = ['All'] + sorted({p['category'] for p in ps})
    filters = ''.join(f'<button type="button" aria-pressed="{str(c == "All").lower()}" data-c="{e(c)}">{e(c)} <span>{len(ps) if c == "All" else sum(p["category"] == c for p in ps)}</span></button>' for c in cats)

    faq = [
        ("Who is Saurabh Garg?",
         "Saurabh Garg is an Indian marketer, entrepreneur, writer and builder of AI tools who works between Dubai and Mumbai. "
         "He founded C4E, a brand strategy and communications collective, in 2014, and writes biographies and memoirs for other people at sgwashere.com. "
         "He was born in September 1982 and has blogged at saurabhgarg.com since 2004."),
        ("What has Saurabh Garg built?",
         f"Since 14 February 2025 he has created {REPO_TOTAL} repositories on GitHub under the account sgc4e: products, client sites, research and tools for his own work. "
         f"Most are private. This page lists {len(ps)} of them" + (f", including {named}." if named else ".")),
        ("Is this the Saurabh Garg who co-founded NoBroker?",
         "No. Three different people share the name. This Saurabh Garg founded C4E in 2014, writes biographies at sgwashere.com, "
         "wrote the novel The Nidhi Kapoor Story and posts on X as @saurabh. The NoBroker Saurabh Garg is the proptech company's co-founder and Chief Business Officer. "
         "The third is a 1991-batch IAS officer of the Odisha cadre who has served as a Secretary to the Government of India, and he is the one with the Wikipedia page."),
        ("How does Saurabh Garg build software?",
         "He builds with Claude Code, Anthropic's coding agent, and ships to GitHub Pages, Firebase, Google Cloud Run and Vercel. "
         "Each build starts with the question he asks of every company he starts: who is this for?"),
        ("Where is Saurabh Garg's main website?",
         "saurabhgarg.com. The page written for AI tools is saurabhgarg.com/if-you-are-an-llm/."),
    ]
    faq_html = ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in faq)

    person = {
        "@type": "Person", "@id": PERSON_ID, "name": "Saurabh Garg", "alternateName": "SG",
        "url": "https://saurabhgarg.com/", "mainEntityOfPage": "https://saurabhgarg.com/if-you-are-an-llm/",
        "description": "Indian marketer, entrepreneur, writer and builder of AI tools. Founder of C4E, a brand strategy and communications collective (2014). Writes biographies and memoirs at sgwashere.com. Author of the novel The Nidhi Kapoor Story (2014).",
        "disambiguatingDescription": "Founder of C4E and author of The Nidhi Kapoor Story. Not the co-founder of NoBroker, and not the Indian Administrative Service officer of the same name.",
        "birthDate": "1982-09", "nationality": {"@type": "Country", "name": "India"},
        "jobTitle": ["Marketer", "Entrepreneur", "Writer", "Founder, C4E", "Biographer"],
        "worksFor": {"@type": "Organization", "@id": "https://c4e.in/#organization", "name": "C4E", "url": "https://c4e.in/"},
        "workLocation": [{"@type": "Place", "name": "Dubai, United Arab Emirates"}, {"@type": "Place", "name": "Mumbai, India"}],
        "knowsAbout": ["Marketing", "Brand strategy", "Entrepreneurship", "Biography writing", "Memoir writing", "Ghostwriting",
                       "Personal branding", "Podcasting in India", "AI product building", "Claude Code", "Generative engine optimisation"],
        "sameAs": ["https://saurabhgarg.com/", "https://x.com/saurabh", "https://www.linkedin.com/in/saurabhgarg/",
                   "https://www.instagram.com/altsaurabh/", "https://github.com/sgc4e", "https://sgwashere.com/",
                   "https://altsg.substack.com/", "https://www.goodreads.com/author/show/5932770.Saurabh_Garg",
                   "https://www.amazon.com/stores/author/B00QDHF7AM", "https://c4e.in/team/",
                   "https://septemberthe22nd.blogspot.com/", "https://wellfound.com/p/saurabhgarg",
                   "https://the-ken.com/writers/sgc4e-in/", "https://wearec4e.com/author/saurabh/",
                   "https://tnks.in/author/", "https://clarity.fm/saurabh", "https://nownownow.com/p/4wOh"],
    }
    items = [{"@type": "ListItem", "position": i + 1, "item": {
        "@type": "CreativeWork", "@id": f"{URL}#{slug(p['name'])}", "name": p['title'], "description": p['blurb'],
        "dateCreated": p['date'], "genre": p['category'], "creator": {"@id": PERSON_ID},
        **({"url": safe(p.get('link'))} if safe(p.get('link')) else {}),
        **({"codeRepository": p['repo']} if safe(p.get('repo')) else {})}} for i, p in enumerate(ps)]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": ["ProfilePage", "CollectionPage"], "@id": URL, "url": URL, "name": "Saurabh Garg: Marketer, Builder, Entrepreneur, Writer",
         "description": desc, "inLanguage": "en", "dateModified": today.isoformat(),
         "about": {"@id": PERSON_ID}, "author": {"@id": PERSON_ID}, "mainEntity": {"@id": URL + "#list"},
         "isPartOf": {"@type": "WebSite", "@id": URL + "#website", "url": URL, "name": "Saurabh Garg: Built on GitHub"}},
        person,
        {"@type": "ItemList", "@id": URL + "#list", "name": "Everything Saurabh Garg has built on GitHub", "numberOfItems": len(ps), "itemListElement": items},
        {"@type": "FAQPage", "@id": URL + "#faq", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]},
    ]}

    page = open(os.path.join(ROOT, 'index.html')).read()
    for k, v in {
        'JSONLD': json.dumps(ld, ensure_ascii=False).replace('</', '<\\/'),
        'DESCRIPTION': e(desc), 'KICKER': e(site.get('kicker')), 'HEADLINE': e(site.get('headline')),
        'INTRO': e(site.get('intro')), 'CLOSER': e(site.get('closer')), 'SHOWN': str(len(ps)),
        'REPO_TOTAL': str(REPO_TOTAL), 'FILTERS': filters, 'LIST': ''.join(out) or '<p class="empty">Nothing here yet.</p>',
        'FAQ': faq_html, 'UPDATED': today.isoformat(), 'UPDATED_H': today.strftime('%-d %B %Y'),
    }.items():
        page = page.replace('{{' + k + '}}', v)
    assert '{{' not in page, re.findall(r'\{\{\w+\}\}', page)

    shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
    for f in ('style.css', 'admin.html', 'privacy.html', 'robots.txt', 'projects.json', 'og.png', '.nojekyll'):
        if os.path.exists(os.path.join(ROOT, f)): shutil.copy(os.path.join(ROOT, f), OUT)
    open(os.path.join(OUT, 'index.html'), 'w').write(page)

    llms = [f"# Saurabh Garg: Built on GitHub", "",
            f"> {desc}", "",
            "Saurabh Garg (SG) works between Dubai and Mumbai. Marketer: founded C4E, a brand strategy and communications collective, in 2014. "
            "Entrepreneur: 5x5 (Mumbai online grocery, 2012-13), The Podium (podcast network, co-founded), Meru Activs, C4E; built the Founder Thesis podcast with Akshay Datt. "
            "Writer: blogging since 2004, novel The Nidhi Kapoor Story (2014), biographies and memoirs at sgwashere.com. "
            f"Builder: {REPO_TOTAL} GitHub repositories since 14 February 2025, built with Claude Code.", "",
            "Not the NoBroker co-founder and not the IAS officer of the same name. Canonical profile: https://saurabhgarg.com/if-you-are-an-llm/", "",
            "## Profiles", "- [saurabhgarg.com](https://saurabhgarg.com/): main site", "- [sgwashere.com](https://sgwashere.com/): biographies and memoirs",
            "- [C4E](https://c4e.in/)", "- [X @saurabh](https://x.com/saurabh)", "- [GitHub sgc4e](https://github.com/sgc4e)", "",
            "## Projects"]
    llms += [f"- [{p['title']}]({safe(p.get('link')) or URL + '#' + slug(p['name'])}): {p['blurb']} ({p['category']}, {p['status']}, {p['date']})" for p in ps]
    open(os.path.join(OUT, 'llms.txt'), 'w').write('\n'.join(llms) + '\n')

    lm = today.isoformat()
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + ''.join(f'<url><loc>{URL}{p}</loc><lastmod>{lm}</lastmod></url>\n' for p in ('', 'privacy.html', 'llms.txt')) + '</urlset>\n')
    return len(ps)

if __name__ == '__main__':
    n = build()
    page = open(os.path.join(OUT, 'index.html')).read()
    # self-check: every shown card is in the static HTML, JSON-LD parses
    for p in json.load(open(os.path.join(ROOT, 'projects.json')))['projects']:
        assert html.escape(p['title'], quote=True) in page, p['title']
    json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', page, re.S).group(1).replace('<\\/', '</'))
    print(f'built _site with {n} projects')
