# Launch checklist: sg-github-showcase

From master-app-checklist. **B** blocks launch. **30** is due within 30 days.
Mark items that do not apply as `[~]` with the reason.

## Project setup

- [ ] **B** Private GitHub repo, `TASKS.md`, `README.md` and an INDEX.md row exist before the first feature. #process
- [ ] **B** `.env*` is in `.gitignore` and `.env.example` lists every key with no values. #process #security
- [ ] **B** No secrets in git history. A secret scan runs before commit. #process #security
- [ ] **B** Secrets live only in `master.env` or the platform's secret store, never in docs or chat. #process #security
- [ ] **B** Lockfile is committed and the toolchain is pinned with `.nvmrc`, `engines` and CI `node-version-file`. #process
- [ ] **B** New work gets its own folder. A project folder is never the catch-all. #process
- [ ] **B** Host on the domain you own, using infrastructure you already run. Check before creating a new hosting project. #process #brand
- [ ] **30** Lint and typecheck run in CI with zero warnings. #process
- [ ] **30** Dependency updates are automated and an audit runs in CI. #process #security
- [ ] **30** `CLAUDE.md` records project footguns, and each repeated mistake becomes a check. #process
- [ ] **30** Decisions and audits are written to `docs/`, with dates and evidence. #process

## Deploy and prove it is live

- [ ] **B** Deploy script aborts if the tree is dirty or `git rev-list HEAD..origin/main` is non-empty, and re-checks after the build. #deploy
- [ ] **B** Every deploy command names `--project`, plus `--account` where several logins exist. #deploy
- [ ] **B** Deploy refuses when required env vars are missing, and asserts the built bundle contains them. #deploy
- [ ] **B** Post-deploy smoke test fetches each changed URL from a clean network and matches an expected string. #deploy
- [ ] **B** The live URL and commit hash are reported in the same message as the deploy. #deploy
- [ ] **B** Live build stamp equals the git commit actually deployed. #deploy
- [ ] **B** HTML returns `no-cache`, hashed assets return `immutable`, and curl asserts both. #deploy #performance
- [ ] **B** Service worker cache key includes the build hash, or there is no service worker. #deploy
- [ ] **B** Every deep link returns 200 on a cold load. A test confirms the router and host config agree. #deploy #seo
- [ ] **B** Static deploys exclude `.git` and `.claude`. `curl /.git/HEAD` returns 404. #deploy #security
- [ ] **B** File modes are forced to 644 and 755 at deploy. #deploy
- [ ] **B** Security rules, indexes and functions ship from the same repo or the same script as the app. #deploy #security
- [ ] **B** Local dev cannot write to production, and seed or test data never reaches it. #deploy #data
- [ ] **B** Pre-launch builds are noindexed by a single env flag. #deploy #seo
- [ ] **B** Apex and www both resolve, and one redirects to the other. Vendor hosts redirect too. #deploy #seo #brand
- [ ] **B** Tests and typecheck block the deploy, including deploys started by a hook. #deploy
- [ ] **30** The production branch equals live, and previews cannot touch production. #deploy
- [ ] **30** Rollback is written down as one command and has been tried once. #deploy
- [ ] **30** Functions deploy by name. A bare deploy can delete functions missing from source. #deploy
- [ ] **30** Hosting version retention is capped, and the build starts from a clean cache. #deploy

## Data safety

- [ ] **B** One source of truth. A change made in any view appears in all views. #data
- [ ] **B** Every bug fix has a regression test that reproduces the report, then write, reload and confirm on live. #data #process
- [ ] **B** Inbound sync never replaces a newer record. Test: edit, restart, sync, assert. #data
- [ ] **B** New records use `create()` with allocated IDs, never a blind `set()`. #data
- [ ] **B** Quitting and restarting the app loses nothing. #data
- [ ] **B** Take a restorable backup before any wipe, migration or cutover. Rehearse on a throwaway first. #data
- [ ] **B** Importers have golden-file tests against real samples and assert totals against a known figure. #data
- [ ] **B** Records are keyed by a stable ID, and a uniqueness check runs after each ingest. #data
- [ ] **B** Every date is stored in UTC and displayed in a named timezone. Daily jobs fix their clock. #data #reliability
- [ ] **30** Backups are scheduled in open formats outside the web root, and a restore has been performed. #data
- [ ] **30** Destructive actions offer undo or soft delete. #data
- [ ] **30** Migrations copy rather than move, and have `--dry-run` and `--verify`. #data
- [ ] **30** A read-only health script asserts data invariants and exits non-zero. #data
- [ ] **30** Long lists paginate and load in under 2 seconds with the full dataset. #data #performance
- [ ] **30** Indexes are declared in source, and reads at scale are budgeted. #data

## Abuse and cost

- [ ] **B** Every endpoint that spends money or sends mail has a limit tested through the real proxy path. N+1 returns 429. #security #cost
- [ ] **B** Limits survive cold starts and multiple instances. #security #cost
- [ ] **B** Paid AI and email have a per-user cap. #security #cost #ai
- [ ] **B** Public forms have a size cap, a honeypot and a server-side check. Add a captcha when volume justifies it. #security #reliability
- [ ] **B** Emails never repeat user-typed text to third parties. #security #email
- [ ] **B** Uploads are checked by magic bytes and capped by size. #security
- [ ] **30** Billing alerts and a global spend cap are set on every paid provider and cloud account. #security #cost
- [ ] **30** Paid API keys have a health check that catches expired or empty credit. #security #cost #reliability
- [ ] **30** Outbound sending has daily caps and pacing. #security #email

## Security baseline

- [ ] **B** HSTS, nosniff, frame protection, Referrer-Policy and Permissions-Policy are set and asserted on live. #security
- [ ] **B** Errors fail closed and never show stack traces. #security
- [ ] **B** Origin and CSRF checks are tested with browser-shaped requests that carry Origin and the proxy Host. #security
- [ ] **B** No backups, dumps or retired installs under a public web root. #security
- [ ] **30** CSP is enforced without `unsafe-inline` where the stack allows it, with a report endpoint. #security
- [ ] **30** WordPress and shared hosts get a monthly integrity scan and credential rotation. #security
- [ ] **30** Run an OWASP Top 10 2025 pass and aim for ASVS 5.0 Level 2. #security

## Errors and monitoring

- [ ] **B** Empty or non-200 results count as failure, never as success. #reliability
- [ ] **B** A global unhandled-rejection handler shows the user a message. #reliability
- [ ] **B** Every error message says what to do and gives a contact address. #reliability #design
- [ ] **B** Every validator has a fixture that must fail it. #reliability
- [ ] **30** Error tracking is live and tested with a deliberate error. #reliability
- [ ] **30** A health endpoint checks real dependencies, and an external uptime monitor watches it. #reliability
- [ ] **30** Logs are structured, with no personal data or secrets. #reliability #privacy
- [ ] **30** Queues alarm when the failed count is above zero. #reliability #email
- [ ] **30** Sensitive admin actions go in an audit trail. #reliability #security

## Forms and email

- [ ] **B** Each form is submitted for real on live. The record is stored, the owner gets mail, and the test row is then deleted. #email #reliability
- [ ] **B** The lead is stored before the mail is attempted, and mail failure is recorded per lead. #email #data
- [ ] **B** SPF, DKIM and DMARC pass with alignment, shown in a real message's headers. Read the `d=` value. #email
- [ ] **B** The sender domain matches the site. No shared `firebaseapp.com` sender. #email #brand
- [ ] **B** Email sending checks the response, retries and logs the outcome. #email
- [ ] **B** Recipients are never placed in a shared `to:` field. #email
- [ ] **30** Marketing mail has one-click unsubscribe headers and a visible link. Spam rate stays under 0.1%. #email #content
- [ ] **30** Double opt-in uses a confirm button, so mail scanners cannot confirm. #email #legal
- [ ] **30** Drips use `>=` thresholds and a per-run send cap. Crons are unit-tested for fire count. #email
- [ ] **30** Transactional and marketing mail use separate subdomains. #email

## Screens and mobile web

- [ ] **B** Every page has a screenshot check at 375px and desktop, in light and dark, with no horizontal scroll. #design
- [ ] **B** Every modal closes. Every route has a visible way back. Nothing overlaps the notch or status bar. #design #accessibility
- [ ] **B** Text passes AA contrast in every box and table. #design #accessibility
- [ ] **B** Each fetching view has skeleton, empty and error states. #design
- [ ] **B** No page ships without its real image, body copy and rendered text. #design #content
- [ ] **B** All image URLs return 200 after deploy. #design
- [ ] **B** Design direction is approved before the build, with options on one board. #design #brand
- [ ] **B** Imagery fits the audience. Language fits the least technical user. #design #brand #content
- [ ] **B** The no-vibe-coded list is passed, plus a real product demo. #design #brand
- [ ] **30** Currency, geography and legal wording are right for each visitor region. #design #content
- [ ] **30** A global style can never hide component text. Tailwind v4 custom classes go in `@layer components`. #design

## Accessibility and speed

- [ ] **B** Everything works by keyboard, focus is visible, and a skip link exists. #accessibility
- [ ] **B** Touch targets are at least 44px for primary controls. WCAG 2.2 AA sets 24px as the minimum. #accessibility #design
- [ ] **B** Login allows paste and password managers. #accessibility #security
- [ ] **30** Sticky headers never hide the focused element, every drag has a click alternative, and help sits in one place. #accessibility
- [ ] **30** `prefers-reduced-motion` is respected and an automated accessibility check runs in CI. #accessibility
- [ ] **30** Core Web Vitals pass at the 75th percentile: LCP 2.5s or less, INP 200ms or less, CLS 0.1 or less. #accessibility #performance #seo
- [ ] **30** Images are correctly sized and in a modern format, fonts do not block rendering, and analytics stays off the LCP path. #accessibility #performance

## Measurement

- [ ] **B** Funnel events are defined before launch: start, key action, result, payment. #analytics
- [ ] **B** Tracking is verified on live, not just in the code. #analytics
- [ ] **30** First-touch UTM is kept, and conversions are sent from the server. #analytics #social
- [ ] **30** An alert fires when a key event drops to zero. #analytics

## Privacy and legal

- [ ] **B** Privacy policy, terms and a contact or grievance address are live and linked in the footer. #legal
- [ ] **B** Nothing third-party loads before consent for EU and UK visitors. #legal #analytics #privacy
- [ ] **B** Signed-in apps have self-serve delete account and download my data. #legal #privacy
- [ ] **B** Personal data never goes in URL parameters. #legal #privacy #security
- [ ] **30** Consent notice is separate from the terms, lists fields and purposes, and withdrawal is as easy as giving consent. #legal #privacy
- [ ] **30** Breach runbook covers CERT-In's 6 hours and DPDP's detailed 72-hour report. #legal #security
- [ ] **30** Logs are kept 180 days in India for CERT-In, and DPDP's 1-year minimum is planned for. #legal #security
- [ ] **30** Retention is written down and an erasure job exists. #legal #privacy #data
- [ ] **30** If minors can sign up, an age gate or verifiable parental consent exists. #legal #privacy
- [ ] **30** A list of third parties and what each receives is published. #legal #privacy
- [ ] **30** Chatbots say they are AI up front, and AI media is labelled for EU users. #legal #ai
- [ ] **30** Regional rules are checked with counsel: UAE PDPL, DIFC, ADGM, GDPR representative. #legal

## Content and claims

- [ ] **B** Before "done", diff the output against the ask. Every item exists and the counts match. #content #process
- [ ] **B** Every factual claim has an opened primary source. Unverifiable claims get cut. #content #pr #aeo
- [ ] **B** Never invent a testimonial, logo, name or number. #content #brand #pr
- [ ] **B** No fake or test content on live, including demo profiles in sitemaps. #content #seo #data
- [ ] **B** All prose passes the voice guide, and one sample is read by a human before any bulk send. A regex is not a voice check. #content #brand #social #pr
- [ ] **B** Articles carry a visible date and an information-only footer. No countdowns. #content #seo #aeo
- [ ] **B** Regulated topics are reviewed: no performance numbers, no invest-now CTA, no diagnosis claims. #content #legal
- [ ] **30** One facts file feeds schema, llms.txt and visible copy, and a test checks they agree. #content #seo #aeo
- [ ] **30** Public facts are checked by a verifier that opens each URL. #content #aeo

## Search and AI visibility

- [ ] **B** Exactly one H1 per page, with a unique title and description. #seo #content
- [ ] **B** Canonical, OG tags and image are present on every page. #seo #social
- [ ] **B** The sitemap equals the set of indexable 200 URLs. #seo
- [ ] **B** Unknown routes return a real 404 and a useful page. #seo
- [ ] **B** The build fails on dead internal links and redirecting links. #seo
- [ ] **B** Old URLs get 301s, and the target has to do what the source did. #seo
- [ ] **B** Key content is server-rendered or prerendered. #seo #aeo
- [ ] **B** Search Console and Bing are verified, and the sitemap is submitted. #seo #analytics
- [ ] **B** robots.txt and the CDN let in the crawlers you want. Test with `curl -A GPTBot`. Check Cloudflare on day one. #seo #aeo
- [ ] **B** Each AI-bot group in robots.txt repeats the Disallow list, because a named group replaces the wildcard. #seo #aeo #security
- [ ] **B** JSON-LD matches visible content and validates. #seo #aeo
- [ ] **30** Checks run on rendered output, not on source files. #seo #aeo
- [ ] **30** IndexNow pings only changed URLs in the sitemap. #seo
- [ ] **30** Thin pages are noindexed or improved. Comparison pages each get their own data. #seo #content
- [ ] **30** AI citations are monitored on target queries. #seo #aeo
- [ ] **B** Titles and descriptions fit in search results, with no truncated titles. #seo #content
- [ ] **30** Deprecated schema types are banned in code. #seo
- [ ] **30** llms.txt is optional. Add it if cheap, and expect nothing from it. #seo #aeo

## Social sharing

- [ ] **B** Every shareable page has its own title, description and share image, and the link has been pasted into WhatsApp to confirm the preview. #social #seo
- [ ] **B** Organization and Person schema list every real profile in `sameAs`, and the site links to them. #social #seo #aeo
- [ ] **B** Nothing posts to a social account without SG's review. Drafts go to a file. #social #automation
- [ ] **30** A short screen recording of the real product exists for sharing. #social #content
- [ ] **30** Shared links carry UTM tags, so social traffic shows up in analytics. #social #analytics
- [ ] **30** Ad pixels load only after consent, and fire on a tested event. #social #analytics #legal
- [ ] **30** Social API tokens have an expiry alert, and their permissions have been tested. #social #automation
- [ ] **30** Brand handles are claimed on the platforms you will use, and match the name. #social #brand

## PR and press

- [ ] **B** The founder or author has an indexable bio page, a linked byline and one Person node in schema. #pr #seo #aeo #content
- [ ] **30** A press page has a one-line description, founder bio, logo files, facts and a contact. #pr #brand
- [ ] **30** Press mentions are listed on the site and marked up in schema. #pr #aeo
- [ ] **30** Each site has a backlink tracker and a submission pack ready for directories. #pr #seo
- [ ] **30** Every number in a pitch links to a dated source page on the site. #pr #content
- [ ] **30** Pitches pass the newsworthiness and journalist-fit checks before SG sees them. #pr
- [ ] **30** Pitches stay drafts until SG approves them. Sends, replies and coverage are logged in one tracker. #pr #email
- [ ] **30** A holding statement and a named contact exist for apps touching money, health or legal topics. #pr #legal

## Backlinks: the rules

- [ ] **30** Never pay for a link that passes ranking credit. Paid placements carry rel=sponsored or rel=nofollow. #backlinks #seo #pr
- [ ] **30** Badge swaps need SG's OK, per site. They are link exchanges, so a few are fine and a sitewide habit is not. #backlinks #seo
- [ ] **30** No bulk submission tools, link packs or auto-generated directories. #backlinks #seo
- [ ] **30** A nofollow listing still counts when it brings customers, reviews or an AI citation. Judge each site by that, not the followed label alone. #backlinks #seo #aeo
- [ ] **30** Name, one-line description and URL match everywhere, and every live profile goes into `sameAs` in the site's schema. #backlinks #seo #aeo #brand
- [ ] **30** Each submission is logged with its date, live URL and the rel value read from the live page. #backlinks #seo
- [ ] **30** No public phone number or address goes in without SG's OK for that brand. Check the form before signing up. #backlinks #legal

## Backlink sites: launch and software

- [ ] **L** [Product Hunt](https://www.producthunt.com/posts/new). Launch day for any product with users to show. Link: through its own redirect. Free route not read. #backlinks #seo #pr
- [ ] **L** [Show HN](https://news.ycombinator.com/showhn.html). Working product people can try, no landing pages. Link: mostly nofollow. Free. #backlinks #pr
- [ ] **L** [Indie Hackers](https://www.indiehackers.com/products). Product page for founder-led apps. Link: nofollow. #backlinks #seo
- [ ] **L** [AlternativeTo](https://alternativeto.net/software/add/). List against the tool you replace. Listing link not verified. #backlinks #seo
- [ ] **L** [SaaSHub](https://www.saashub.com/services/submit). Software with its own domain, proved by an email on that domain. Link: followed on the Visit button. Free. #backlinks #seo
- [ ] **L** [G2](https://sell.g2.com/create-a-profile). B2B software, profile claim is free. Link: nofollow. #backlinks #seo #aeo
- [ ] **L** [TrustRadius](https://www.trustradius.com/vendors). B2B software with reviews. Link: followed. Terms not read. #backlinks #seo #aeo
- [ ] **L** [Capterra](https://www.capterra.com/vendors/). B2B software. Link not verified. Same owner as [GetApp](https://www.getapp.com/) and [Software Advice](https://www.softwareadvice.com/vendors/). #backlinks #seo
- [ ] **L** [SourceForge](https://sourceforge.net/create/). Open source, can import from GitHub. Link not verified. #backlinks #seo
- [ ] **L** [Slashdot software directory](https://slashdot.org/software/vendors/new). Software vendors. Directory link not verified. #backlinks #seo
- [ ] **L** [Crunchbase](https://www.crunchbase.com/add-new). Any company, for the entity record. Link: nofollow. #backlinks #aeo #pr
- [ ] **L** [Wellfound](https://wellfound.com/company/new). Companies that hire. Link: nofollow on jobs. #backlinks #seo
- [ ] **L** [Peerlist](https://peerlist.io/launchpad). Launch and maker profile. Link: nofollow. #backlinks #seo
- [ ] **L** [Uneed](https://www.uneed.best/submit-a-tool). Launch queue. Link: nofollow until 20 upvotes. Free tier. #backlinks #seo
- [ ] **L** [DevHunt](https://devhunt.org/). Developer tools. Link: followed. Submit route not found. #backlinks #seo
- [ ] **L** [Fazier](https://fazier.com/submit). Launch queue. Link: followed. Free needs a badge on your site, $49 to $69 skips it. #backlinks #seo
- [ ] **L** [Launching Next](https://www.launchingnext.com/submit/). New startups. Link not verified. Free. #backlinks #seo
- [ ] **L** [Startup Stash](https://startupstash.com/add-listing/). Tools for startups. Link not verified. #backlinks #seo
- [ ] **L** [Open Alternative](https://openalternative.co/submit). Open source only, GitHub login. Link: followed. Free. #backlinks #seo

## Backlink sites: AI tools and developers

- [ ] **L** [There's An AI For That](https://theresanaiforthat.com/submit/). AI products. Link not verified. #backlinks #seo #ai
- [ ] **L** [Future Tools](https://futuretools.io/submit-a-tool). AI products, reviewed by hand. Link: through its own redirect. Free. #backlinks #ai
- [ ] **L** [Dang.ai](https://dang.ai/pricing). AI products. Link: followed. Free needs a link back. #backlinks #seo #ai
- [ ] **L** [AI Tools Directory](https://aitoolsdirectory.com/submit-tool). AI consumer products with public pricing. Link: mixed. Free tier. #backlinks #ai
- [ ] **L** [Toolify](https://www.toolify.ai/submit), [TopAI.tools](https://topai.tools/submit) and [AIxploria](https://www.aixploria.com/en/submit-ai-tool-or-feature-company). AI products. Link: nofollow. #backlinks #ai
- [ ] **L** [GitHub](https://github.com/new). Website field and README on a public repo. Link: nofollow. Free. #backlinks #aeo
- [ ] **L** [Awesome lists](https://github.com/sindresorhus/awesome). Pull request to a list that fits. Link: nofollow, but lists get read and copied. Free. #backlinks #content
- [ ] **L** [GitLab](https://gitlab.com/projects/new). Public repo. Link: followed in README. Website field not checked. Free. #backlinks #seo
- [ ] **L** [npm](https://www.npmjs.com/) and [PyPI](https://pypi.org/). Published packages, homepage field. Link: nofollow. #backlinks #seo
- [ ] **L** [Docker Hub](https://hub.docker.com/). Public images. Link: followed in README. Website field not checked. #backlinks #seo
- [ ] **L** [Hugging Face](https://huggingface.co/new-space). Models, datasets or Spaces. Link: nofollow. Free. #backlinks #ai
- [ ] **L** [DEV Community](https://dev.to/new). Profile and real technical posts. Profile link: followed. Free. #backlinks #seo #content
- [ ] **L** [DZone](https://dzone.com/pages/become-a-contributor). Contributed technical articles. Link: followed on the pages seen. #backlinks #seo #content
- [ ] **L** [HackerNoon](https://hackernoon.com/p/write). Contributed articles, edited. Link: ugc. #backlinks #content
- [ ] **L** [Stack Overflow](https://stackoverflow.com/users/signup). Profile website field. Link: followed on a high-reputation profile, low reputation not checked. Free. #backlinks #seo
- [ ] **L** [Google Play](https://play.google.com/console). Android apps, website field. Link: followed. Developer fee applies. #backlinks #seo #mobile
- [ ] **L** [Apple App Store](https://developer.apple.com/programs/). iOS apps. Link: nofollow. Paid programme. #backlinks #mobile
- [ ] **L** [VS Code Marketplace](https://marketplace.visualstudio.com/manage). Extensions. Link: followed on the verified domain, nofollow on Resources. Free. Also [Open VSX](https://open-vsx.org/), JS only, and [JetBrains](https://plugins.jetbrains.com/), not verified. #backlinks #seo
- [ ] **L** [Chrome Web Store](https://chrome.google.com/webstore/devconsole/). Browser extensions. Link appears through JS. #backlinks
- [ ] **L** [Glama](https://glama.ai/mcp/servers), [PulseMCP](https://www.pulsemcp.com/submit), [Smithery](https://smithery.ai/new) and [mcp.so](https://mcp.so/submit?type=server). MCP servers only. Glama links to the GitHub repo with no rel. Others not verified. #backlinks #ai

## Backlink sites: profiles and entity records

- [ ] **L** [Google Business Profile](https://business.google.com/in/business-profile/). Businesses with a real location or service area. Link through JS. Free. #backlinks #seo #aeo
- [ ] **L** [Bing Places](https://www.bing.com/forbusiness/places) and [Apple Business Connect](https://business.apple.com/). Same details as Google. Not verified. #backlinks #seo
- [ ] **L** [Wikidata](https://www.wikidata.org/wiki/Wikidata:Notability). Only when a reliable source exists. Link: nofollow. Direct entity value. #backlinks #aeo
- [ ] **L** [Linktree](https://linktr.ee/register). Link: followed. Free. #backlinks #seo #social
- [ ] **L** [Pinterest](https://www.pinterest.com/business/create/). Visual brands, leave the phone blank. Link: followed on the profile. Free. #backlinks #seo #social
- [ ] **L** [Goodreads Author Program](https://www.goodreads.com/author/program). Published authors. Link: followed. Free. #backlinks #seo #aeo
- [ ] **L** [Reedsy](https://reedsy.com/discovery/). Writers and editors. Link not verified. #backlinks #aeo
- [ ] **L** [Medium](https://medium.com/m/signin). Republish with a canonical. Link: mostly nofollow. Free. #backlinks #content
- [ ] **L** [Substack](https://substack.com/signup). Only with a real newsletter. Link through JS. Free. #backlinks #content #email
- [ ] **L** [YouTube](https://www.youtube.com/about/) and [X](https://x.com/i/flow/signup). Link: through their own redirects. Free. #backlinks #social
- [ ] **L** [Gravatar](https://gravatar.com/), [About.me](https://about.me/signup) and [Flickr](https://identity.flickr.com/sign-up). Founder identity. Link: nofollow. Free tiers. #backlinks #aeo
- [ ] **L** [Speaker Deck](https://speakerdeck.com/signup). Real talks and decks. Link: nofollow. Free. #backlinks #content
- [ ] **L** [Behance](https://www.behance.net/signup). Design work. Link through JS. Free. #backlinks #brand
- [ ] **L** [Brownbook](https://www.brownbook.net/add-business). Business listing, phone optional. Link: followed. Free. #backlinks #seo
- [ ] **L** [Curlie](https://curlie.org/docs/en/add.html). Human-edited, slow and selective. Link: followed. Free. #backlinks #seo
- [ ] **L** [SoMuch](https://www.somuch.com/submit-links/). Queue of weeks to months, skip the paid lane. Link: followed. Free. #backlinks #seo
- [ ] **L** [Hotfrog](https://www.hotfrog.in/register). Shows a street address. Link: nofollow. Free. #backlinks #seo
- [ ] **L** [Trustpilot](https://signup.business.trustpilot.com/create-account). Consumer brands that will answer reviews. Link not verified. Free tier. #backlinks #seo
- [ ] **L** [Clutch](https://clutch.co/get-listed), [GoodFirms](https://www.goodfirms.co/get-listed), [DesignRush](https://www.designrush.com/agency/add-your-agency) and [The Manifest](https://themanifest.com/get-listed). Agencies only. Link: nofollow, The Manifest listing not verified. #backlinks #seo
- [ ] **L** [Startup India](https://www.startupindia.gov.in/). Incorporated Indian startups. Link not verified, a .gov.in profile is worth having. Free. #backlinks #aeo
- [ ] **L** [MAGNiTT](https://magnitt.com/). MENA startups. Link not verified. #backlinks #pr

## Backlink sites: earned through press and podcasts

- [ ] **L** [HARO](https://www.helpareporter.com/). Free daily journalist queries, now run by Featured. Link when quoted. #backlinks #pr
- [ ] **L** [Featured](https://featured.com/pricing). Expert quotes. Free tier gets 2 to 3 opportunities a week. Paid from $29 a month. #backlinks #pr #aeo
- [ ] **L** [Qwoted](https://www.qwoted.com/pricing/). Journalist requests. Free tier: 2 pitches a month, 2-hour delay. #backlinks #pr
- [ ] **L** [SourceBottle](https://www.sourcebottle.com/). Journalist call-outs. Free source profile. #backlinks #pr
- [ ] **L** [MentionMatch](https://mentionmatch.com/). B2B writers, formerly Help a B2B Writer. Pricing not read. #backlinks #pr
- [ ] **L** [PodMatch](https://podmatch.com/pricing). Podcast guest matching, show notes carry the link. Price not read. #backlinks #pr #content
- [ ] **L** [PodcastGuests](https://podcastguests.com/) and [RadioGuestList](https://radioguestlist.com/). Free emails of shows seeking guests. #backlinks #pr
- [ ] **L** [Inc42](https://inc42.com/startup-submission/). Indian startups, for coverage. Link not verified. It also sells a booster pack, which is paid placement. #backlinks #pr
- [ ] **L** [Entrackr](https://entrackr.com/page/contact-us). Indian startup news with real numbers. Link not verified. #backlinks #pr
- [ ] **L** [MediaNama](https://www.medianama.com/contact-us/). Indian tech policy. Link: followed on outside sources. Press email listed. #backlinks #pr
- [ ] **L** [Wamda](https://www.wamda.com/contact). MENA startups, has a story pitch form. Link not verified. #backlinks #pr
- [ ] **L** [Entrepreneur Middle East](https://mena.entrepreneur.com/). UAE and GCC founders, has Submit Article. Link not verified. #backlinks #pr
- [ ] **L** [Khaleej Times](https://www.khaleejtimes.com/contact-us). UAE news desk. Link not verified. #backlinks #pr
- [ ] **L** [Tech in Asia](https://www.techinasia.com/submit). Asian startups. Link through JS. #backlinks #pr
- [ ] **L** [TechCrunch tips](https://techcrunch.com/got-a-tip/). Real news only. Link: nofollow. Free. #backlinks #pr

## Content engine

- [ ] **B** Each article shows one date, and the schema and sitemap `lastmod` agree with it. #content #seo #aeo
- [ ] **B** A visible FAQ matches the FAQ schema word for word. #content #seo #aeo
- [ ] **30** Search data decides the next piece, and a page ranking 4 to 20 gets refreshed before anything new is written. #content #seo
- [ ] **30** Articles use question headings and answer directly under them. #content #aeo
- [ ] **30** Pillar pages link into their cluster, in the body text. #content #seo
- [ ] **30** Blogs have an RSS feed. #content #seo
- [ ] **30** Content offers a sign-up, and the sign-up fires an analytics event. #content #email #analytics
- [ ] **30** Automated publishing ships only items whose primary source was opened. A quiet day publishes nothing. #content #automation #aeo

## Working rules for Claude on any app

- [ ] **B** Ship the change, verify it on live, report the delta. Green tests alone do not count. #process
- [ ] **B** Audits close their P1 and P2 findings in the same run, or list each with a ready fix. #process
- [ ] **B** Check for an existing session, tool or repo before rebuilding. #process
- [ ] **B** Do not stop until the list is done. If something is out of scope, say so. #process
- [ ] **B** Commit, push and publish on "commit". Keep `TASKS.md` updated when each item finishes. #process
- [ ] **30** Parallel work uses a lock for deploys and absolute paths in shell. Fan-out agents save output early. #process
- [ ] **30** Write `HANDOFF.md` before context runs out. #process
