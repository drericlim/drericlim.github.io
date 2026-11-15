#!/usr/bin/env python3
"""Rebuild the publications list on the For professionals page.

Reads _data/publications.json and rewrites everything between the
PUBLICATIONS:START and PUBLICATIONS:END markers in for-professionals/index.html
(the key figures and the full list, by year, newest first).

Run from the repository root:  python3 tools/publications/build.py
"""
import json, re, html, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGE = ROOT / "for-professionals" / "index.html"
DATA = ROOT / "_data" / "publications.json"

# Category shown on the page: (key, plural for the row of categories, singular on each paper)
CATS = [("Randomised trial", "Randomised trials", "Randomised trial"),
        ("Trial protocol", "Trial protocols", "Trial protocol"),
        ("Guideline", "Guidelines", "Guideline"),
        ("Systematic review", "Systematic reviews", "Systematic review"),
        ("Full paper", "Full papers", "Full paper"),
        ("Editorial", "Editorials", "Editorial"),
        ("Letter", "Letters", "Letter"),
        ("Book", "Books and chapters", "Book")]
FOLD = {"Book chapter": "Book", "Invited commentary": "Editorial", "Cochrane review": "Systematic review"}
TOPICS = [("lung-cancer", "Lung cancer"), ("small-cell", "Small cell lung cancer"), ("mesothelioma", "Mesothelioma"),
          ("thymic-mediastinal", "Thymic and mediastinal"), ("pulmonary-metastases", "Pulmonary metastases"),
          ("pleural-disease", "Pleural disease (benign)"), ("other-thoracic", "Other thoracic"),
          ("surgical-technique", "Surgical technique"), ("perioperative-care", "Perioperative care and enhanced recovery"),
          ("drain-management", "Drain management"), ("cardiac-surgery", "Cardiac surgery"),
          ("randomised-trial", "Randomised trial"), ("research-methodology", "Research methodology and statistics"),
          ("cancer-biology", "Cancer biology"), ("screening", "Screening and early detection"),
          ("diagnosis-staging", "Diagnosis, staging and biomarkers"), ("oncology-treatment", "Oncological treatment"),
          ("outcomes-health-services", "Outcomes, quality and health services"), ("training-workforce", "Training and workforce"),
          ("digital-health", "Digital health and patient-reported outcomes"), ("covid-19", "COVID-19")]
e = html.escape

def cat_of(p):
    t = FOLD.get(p.get("type"), p.get("type"))
    return t if t in [c[0] for c in CATS] else "Full paper"

def is_me(n):
    m = re.match(r"^(.+?)\s+([A-Za-z.\-]+)$", (n or "").strip())
    return bool(m) and m.group(1).lower() == "lim" and m.group(2).replace(".", "").upper() in ("E", "EK", "EKS")

def my_index(p):
    i = p.get("my_index")
    if isinstance(i, int) and i >= 0: return i
    return next((k for k, n in enumerate(p.get("authors") or []) if is_me(n)), -1)

def authors(p):
    """First six authors then et al. Professor Lim's name is bold and is never dropped."""
    a = [n for n in (p.get("authors") or []) if n]; me = my_index(p)
    nm = lambda n, i: ("<b>%s</b>" % e(n)) if i == me else e(n)
    if len(a) <= 6: parts = [nm(n, i) for i, n in enumerate(a)]
    else:
        parts = [nm(n, i) for i, n in enumerate(a[:6])]
        if me >= 6: parts += ["…", nm(a[me], me)]
        if me != len(a) - 1: parts.append("et al")
    s = ", ".join(parts).replace(", …, ", ", … ")
    g = p.get("group_author")
    if g: s = (s + "; " + e(g)) if a else e(g)
    return s

def strip_dot(s): return re.sub(r"\.$", "", (s or "").strip())

def cite(p, n):
    doi, pmid = p.get("doi"), p.get("pmid")
    title = e(strip_dot(p.get("title")))
    ti = ('<a class="ti" href="https://doi.org/%s" target="_blank" rel="noopener">%s</a>' % (e(doi), title)) if doi else '<span class="ti">%s</span>' % title
    loc = e(str(p.get("year") or ""))
    if p.get("volume"): loc += ";" + e(str(p["volume"])) + ("(%s)" % e(str(p["issue"])) if p.get("issue") else "")
    if p.get("pages"): loc += ":" + e(str(p["pages"]))
    c = cat_of(p)
    meta = ['<span class="ty">%s</span>' % e(dict((k, s) for k, _, s in CATS)[c])]
    if doi: meta.append('<a href="https://doi.org/%s" target="_blank" rel="noopener">DOI</a>' % e(doi))
    if pmid: meta.append('<a href="https://pubmed.ncbi.nlm.nih.gov/%s/" target="_blank" rel="noopener">PubMed</a>' % e(str(pmid)))
    cc = ('<span class="cc" hidden> · Cited %d</span>' % int(p["citations"])) if p.get("citations") is not None else ""
    au = authors(p)
    return ('<li class="cite" data-cat="%s" data-topics="%s" data-year="%s" data-cites="%d"><span class="no">%d.</span><span>%s%s. <span class="jn">%s.</span> %s.'
            '<span class="meta">%s</span></span></li>') % (e(c), e(" ".join(p.get("topics") or [])), e(str(p.get("year") or "")), int(p.get("citations") or 0), n,
            (au + ". ") if au else "", ti, e(strip_dot(p.get("journal"))), loc, " · ".join(meta) + cc)

def main():
    pubs = json.loads(DATA.read_text(encoding="utf-8"))["publications"]
    pubs.sort(key=lambda p: (-(p.get("year") or 0), "".join(chr(255 - ord(ch)) if ord(ch) < 256 else ch for ch in (p.get("date") or "")), p.get("title") or ""))
    years = [p["year"] for p in pubs if p.get("year")]
    n_rct = sum(1 for p in pubs if cat_of(p) == "Randomised trial"); n_gl = sum(1 for p in pubs if cat_of(p) == "Guideline")
    used = {t for p in pubs for t in (p.get("topics") or [])}
    out = []
    out.append('<ul class="pub-figures reveal" aria-label="Key figures">')
    for n, l in [(len(pubs), "Publications"), (n_rct, "Randomised trials"), (n_gl, "Guidelines"), ("%d–%d" % (min(years), max(years)), "Years in print")]:
        out.append('  <li><div class="n">%s</div><div class="l">%s</div></li>' % (n, l))
    out.append('  <li class="ext"><a href="https://orcid.org/0000-0002-9078-3226" target="_blank" rel="noopener">ORCID record</a><a href="https://pubmed.ncbi.nlm.nih.gov/?term=Lim+E%5BAuthor%5D+Royal+Brompton" target="_blank" rel="noopener">PubMed</a></li>')
    out.append('</ul>')
    out.append('<details class="mod-toggle pub-toggle reveal">')
    out.append('  <summary><span class="t"><span class="t-closed">See all %d publications</span><span class="t-open">Hide the publications</span></span><span class="chev" aria-hidden="true"></span></summary>' % len(pubs))
    out.append('  <div class="pub-body">')
    out.append('    <div class="pub-ctl" hidden>')
    out.append('      <div><label for="pub-q">Search all publications</label><input id="pub-q" type="search" placeholder="Title, author or journal"></div>')
    out.append('      <div><label for="pub-topic">Topic</label><select id="pub-topic"><option value="">All topics</option>%s</select></div>' % "".join('<option value="%s">%s</option>' % (k, e(l)) for k, l in TOPICS if k in used))
    out.append('      <div><label for="pub-sort">Order</label><select id="pub-sort"><option value="year">Newest first</option><option value="cites">Most cited</option></select></div>')
    out.append('    </div>')
    out.append('    <div class="pub-types" id="pub-types" role="group" aria-label="Category" hidden>%s</div>' % ('<button type="button" data-cat="" aria-pressed="true">All<span class="ct"></span></button>' + "".join('<button type="button" data-cat="%s" aria-pressed="false">%s<span class="ct"></span></button>' % (e(k), e(pl)) for k, pl, _ in CATS)))
    out.append('    <p class="pub-count" id="pub-count" aria-live="polite"></p>')
    out.append('    <div id="pub-rows">')
    yr = object(); n = 0
    for p in pubs:
        if p.get("year") != yr:
            if n: out.append('      </ol>')
            yr = p.get("year"); out.append('      <h3 class="pub-year">%s</h3>' % e(str(yr or "Undated"))); out.append('      <ol class="cites">')
        n += 1; out.append('        ' + cite(p, n))
    out.append('      </ol>'); out.append('    </div>')
    out.append('    <button type="button" class="pub-more" id="pub-more" hidden></button>')
    out.append('    <p class="pub-foot">Citations follow the Vancouver style used by PubMed. Each title opens the paper on the publisher’s site.</p>')
    out.append('  </div>'); out.append('</details>')
    s = PAGE.read_text(encoding="utf-8")
    a, b = "<!-- PUBLICATIONS:START (built by tools/publications/build.py; do not edit by hand) -->", "<!-- PUBLICATIONS:END -->"
    if a not in s or b not in s: sys.exit("Markers not found in " + str(PAGE))
    i, j = s.index(a) + len(a), s.index(b)
    PAGE.write_text(s[:i] + "\n" + "\n".join("    " + l for l in out) + "\n    " + s[j:], encoding="utf-8")
    print("Publications list rebuilt: %d papers, %d–%d." % (len(pubs), min(years), max(years)))

if __name__ == "__main__": main()
