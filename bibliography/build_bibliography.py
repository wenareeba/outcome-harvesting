# SPDX-License-Identifier: MIT
"""Build the Outcome Harvesting bibliography from one data table.

Edit SOURCES below, then run:
    python3 bibliography/build_bibliography.py
It writes sources.csv, references.bib, annotated-bibliography.md and verification-queue.md so they never drift apart.

Status codes:
  V  verified: title, year and pages (or report series) confirmed in the document itself, or on the
     journal, publisher or repository page, or by Crossref, October 2026. Only V sources are published.
  L  listed in a published source but not yet confirmed at source. Held back in verification-queue.md
     until confirmed; change to V and rebuild.

Authors are stored with initials only, so no unconfirmed first name is ever published.
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# key, bibtype, authors (BibTeX "and" form), year, title, container, volume, issue, pages, doi, url, status, section, note
SOURCES = [
    # 1. Foundations
    ('wilsongrau2013', 'techreport', 'Wilson-Grau, R. and Britt, H.', '2013', 'Outcome harvesting', 'Ford Foundation, Middle East and North Africa Office, Cairo. May 2012, revised November 2013', '', '', '', '', 'https://www.betterevaluation.org/tools-resources/outcome-harvesting-0', 'V', '1',
     'Start here. The 27-page brief that set out the method: the definition of an outcome (p. 2), the four roles in a harvest (p. 4) and the six steps, one section each from p. 6. This repo cites the November 2013 revision; see errata.'),
    ('wilsongrau2019', 'book', 'Wilson-Grau, R.', '2019', 'Outcome harvesting: Principles, steps, and evaluation applications', 'Information Age Publishing, Charlotte, NC. Evaluation and Society series', '', '', '', '10.1108/978-1-64113-394-4', '', 'V', '1',
     'The full statement of the method. Defines an outcome as an observable change in behaviour (p. 1), gives a chapter to each of the six steps (pp. 29 to 147) and sets out five process principles (pp. 149 to 167) and four content principles (pp. 169 to 187). Copyright 2019; released November 2018. Not open access.'),
    ('wilsongrau2015', 'incollection', 'Wilson-Grau, R. and Kosterink, P. and Scheers, G.', '2015', 'Outcome Harvesting: A developmental evaluation inquiry framework supporting the development of an international social change network', 'Developmental evaluation exemplars: Principles in practice (M. Q. Patton, K. McKegg and N. Wehipeihana, Eds.), Guilford Press', '', '', '', '', '', 'L', '1',
     'OH used as the inquiry framework in a developmental evaluation of a global peacebuilding network.'),
    # 2. Guides and adaptations by others
    ('betterevaluation2024', 'misc', 'Wilson-Grau, R. and Britt, H. and Dewata, Y. and Rogers, P. and Stevens, K.', '2024', 'Outcome harvesting', 'BetterEvaluation, approach page. Original author R. Wilson-Grau; revised by H. Britt, Y. Dewata, P. Rogers and K. Stevens. Last updated 27 June 2024', '', '', '', '', 'https://www.betterevaluation.org/methods-approaches/approaches/outcome-harvesting', 'V', '2',
     'Free overview of the six steps and the nine principles, with links to guides and examples. Its principle names follow Chapter 1 of the book, except one; see errata.'),
    ('worldbank2014guide', 'techreport', 'World Bank', '2014', 'Outcome-based learning field guide: Tools to harvest and monitor outcomes and systematically learn from complex projects', 'World Bank, Washington, DC. Working Paper 90176', '', '', '', '10.1596/20006', '', 'V', '2',
     'Practical tools built from pilots with World Bank teams. Its outcome definition is narrower than the brief: a change in the people, groups, communities or organisations a programme works with directly (p. 9). Open access.'),
    ('intrac2017', 'misc', 'INTRAC', '2017', 'Outcome harvesting', 'M&E Universe, INTRAC', '', '', '', '', 'https://www.intrac.org/wpcms/wp-content/uploads/2017/01/Outcome-harvesting.pdf', 'V', '2',
     'Five-page summary of the steps with a plain list of strengths and weaknesses (p. 3 onwards). Free.'),
    # 3. Method development, comparison and critique
    ('abboud2016', 'article', 'Abboud, R. and Claussen, C.', '2016', 'The use of Outcome Harvesting in learning-oriented and collaborative inquiry approaches to evaluation: An example from Calgary, Alberta', 'Evaluation and Program Planning', '59', '', '47--54', '10.1016/j.evalprogplan.2016.08.005', '', 'V', '3',
     'OH used as a shared learning process across neighbourhood community development projects in Calgary, from 2013, with lessons for others adopting it (p. 47).'),
    ('beardmore2023', 'article', 'Beardmore, A. and Jones, M. and Seal, J.', '2023', 'Outcome harvesting as a methodology for the retrospective evaluation of small-scale community development interventions', 'Evaluation and Program Planning', '97', '', '102235', '10.1016/j.evalprogplan.2023.102235', '', 'V', '3',
     'Tests OH on a place-based community wellbeing project. Finds it promising, with two limits: reaching a broad range of participants, and finding enough time and resources (p. 1). Open access, CC BY 4.0.'),
    ('copestake2017', 'misc', 'Copestake, J.', '2017', 'A family resemblance: Outcome Harvesting and QuIP compared', 'Bath Social and Development Research, blog post, 4 July 2017', '', '', '', '', 'https://bathsdr.org/782-2/', 'V', '3',
     'Short comparison of OH with the Qualitative Impact Protocol, from the QuIP side.'),
    # 4. Applications
    ('worldbank2014cases', 'techreport', 'World Bank', '2014', 'Cases in outcome harvesting: Ten pilot experiences identify new learning from multi-stakeholder projects to improve results', 'World Bank, Washington, DC. Working Paper 90172', '', '', '', '10.1596/20015', '', 'V', '4',
     'Ten pilot harvests in World Bank projects, among them pharmaceutical procurement in Kenya, Tanzania and Uganda (p. 6). Open access.'),
    ('smith2020', 'techreport', 'Smith, R. and Scheers, G. and Robinson, G.', '2020', 'Outcome harvesting evaluation of 20 years of cooperation between the Danish and Ugandan Disability Movements, 1996-2018', 'Disabled Peoples Organisations Denmark (DPOD). Final report, November 2020', '', '', '', '', 'https://www.outcomeharvesting.net/oh-evaluation-reports', 'V', '4',
     'A full harvest from Uganda, from design to outcome database, with its adaptation of the six steps and its substantiation responses in annexes (p. 3).'),
    ('tomei2024', 'article', 'Tomei, G. and Terenzi, L. and Testi, E.', '2024', 'Using Outcome Harvesting to evaluate socio-economic development and social innovation generated by Social Enterprises in complex areas. The case of BADAEL project in Lebanon', 'Evaluation and Program Planning', '106', '', '102475', '10.1016/j.evalprogplan.2024.102475', '', 'V', '4',
     'OH used to evaluate social enterprise development in Lebanon. Details confirmed on the journal and RePEc records; not yet read for this course.'),
    ('hivos2021', 'misc', 'Hivos East Africa', '2021', 'Use of Outcome Harvesting for monitoring and evaluation: Our experiences and lessons learned', 'Hivos', '', '', '', '', 'https://hivos.org/document/lessons-from-outcome-harvesting-in-monitoring-and-evaluation', 'L', '4',
     'Lessons from using OH to monitor the Dialogue and Dissent programme in East Africa.'),
    ('rassmann2013', 'misc', 'Rassmann, K. and Smith, R. and Mauremootoo, J. and Wilson-Grau, R.', '2013', "Retrospective 'outcome harvesting': Generating robust insights", 'BetterEvaluation writeshop series', '', '', '', '', 'https://www.outcomemapping.org/resources/retrospective-outcome-harvesting-generating-robust-insights', 'L', '4',
     'OH used at the end of a global voluntary network programme, BioNET, 2007 to 2011.'),
    ('rassmann2013blog', 'misc', 'Rassmann, K.', '2013', '52 weeks of BetterEvaluation: Week 16: Identifying and documenting emergent outcomes of a global network', 'BetterEvaluation, blog post, 12 April 2013', '', '', '', '', 'https://betterevaluation.org/node/2414', 'V', '4',
     'The blog that introduces the BioNET harvest paper: why a logframe did not fit a global network, and what the harvest found.'),
    # 5. Related approaches
    ('earl2001', 'book', 'Earl, S. and Carden, F. and Smutylo, T.', '2001', 'Outcome mapping: Building learning and reflection into development programs', 'International Development Research Centre, Ottawa', '', '', '', '', 'https://idl-bnc-idrc.dspacedirect.org/bitstream/handle/10625/32122/IDL-32122.pdf', 'L', '5',
     'Where the OH definition of an outcome comes from, as the brief records (Wilson-Grau and Britt 2013, p. 1). Open access.'),
    ('davies2005', 'misc', 'Davies, R. and Dart, J.', '2005', "The 'Most Significant Change' (MSC) technique: A guide to its use", 'Version 1.00, April 2005', '', '', '', '', 'https://susana.org/knowledge-hub/resources?id=4568', 'V', '5',
     'The standard guide to MSC, the other approach that collects stories of change without fixing indicators in advance. Free.'),
    ('copestake2019', 'book', 'Copestake, J. and Morsink, M. and Remnant, F.', '2019', 'Attributing development impact: The Qualitative Impact Protocol case book', 'Practical Action Publishing', '', '', '', '10.3362/9781780447469', '', 'V', '5',
     'Cases using QuIP, which asks intended beneficiaries about change without naming the intervention. Read beside Copestake (2017). Open access.'),
    ('mayne2019', 'article', 'Mayne, J.', '2019', 'Revisiting contribution analysis', 'Canadian Journal of Program Evaluation', '34', '2', '171--191', '10.3138/cjpe.68004', '', 'V', '5',
     'The current statement of Contribution Analysis, the method this course pairs with OH: harvest the outcomes, then test the important ones.'),
    # 6. Complexity-aware monitoring
    ('britt2013', 'techreport', 'Britt, H.', '2013', 'Discussion note: Complexity-aware monitoring', 'USAID, Monitoring and Evaluation Series, Version 2.0, December 2013', '', '', '', '', 'https://www.betterevaluation.org/sites/default/files/Complexity_Aware_Monitoring_2013-12-11_FINAL.pdf', 'V', '6',
     'Places OH among five complexity-aware monitoring approaches (p. 7) and explains why such methods look for unintended as well as intended results (p. 11).'),
]

# What each queued source still needs before it can be published.
NEEDED = {
    'wilsongrau2015': 'Chapter pages, and the year on the copyright page: the publisher lists October 2015, the foreword to Wilson-Grau (2019) cites 2016',
    'hivos2021': 'Publication year and author, which the document does not state',
    'rassmann2013': 'The paper itself; only the introducing blog post has been read',
    'earl2001': 'Year and place on the title page (the file is too large for the current download route)',
}

SECTIONS = {
    "1": ("Foundations: Wilson-Grau's own work", "The brief, the book and one applied chapter. Read the brief first, then the book."),
    "2": ("Guides and adaptations by others", "Free, shorter and practical. Useful when you are running a harvest next month."),
    "3": ("Method development, comparison and critique", "Where others adapt OH, test it, or compare it with other approaches. A small literature so far."),
    "4": ("Applications", "Published harvests, with Africa, Asia and Latin America sought out."),
    "5": ("Related approaches", "Outcome Mapping, Most Significant Change, QuIP and Contribution Analysis."),
    "6": ("Complexity-aware monitoring", "Why methods like OH exist."),
}

FIELDS = ["key","bibtype","authors","year","title","container","volume","issue","pages","doi","url","status","section","note"]


def apa_authors(a):
    names = [n.strip() for n in a.split(" and ")]
    out = []
    for n in names:
        if "," in n:
            last, first = [x.strip() for x in n.split(",", 1)]
            initials = " ".join(p[0] + "." for p in first.replace("-", " ").split() if p[0].isalpha())
            out.append(f"{last}, {initials}")
        else:
            out.append(n)
    if len(out) == 1:
        return out[0]
    return ", ".join(out[:-1]) + ", and " + out[-1]


def end(t):
    return t if t.endswith(("?", "!", ".")) else t + "."


def apa(r):
    s = f"{apa_authors(r['authors'])} ({r.get('yeardisp', r['year'])}). "
    if r["bibtype"] == "article":
        s += f"{end(r['title'])} *{r['container']}*"
        if r["volume"]:
            s += f", {r['volume']}"
        if r["issue"]:
            s += f"({r['issue']})"
        if r["pages"]:
            s += f", {r['pages'].replace('--', ' to ')}"
        s += "."
    elif r["bibtype"] == "incollection":
        s += f"{end(r['title'])} In *{r['container']}*"
        if r["pages"]:
            s += f" (pp. {r['pages'].replace('--', ' to ')})"
        s += "."
    else:
        s += f"*{r['title']}*{'' if r['title'].endswith(('?', '!')) else '.'} {r['container']}."
    if r["doi"]:
        s += f" https://doi.org/{r['doi']}"
    elif r["url"]:
        s += f" {r['url']}"
    return s


def bib(r):
    f = [f"  author = {{{r['authors']}}}", f"  title = {{{r['title']}}}", f"  year = {{{r['year']}}}"]
    t = r["bibtype"]
    field = {"article": "journal", "book": "publisher", "incollection": "booktitle"}.get(t, "institution" if t == "techreport" else "howpublished")
    f.append(f"  {field} = {{{r['container']}}}")
    for k, name in (("volume", "volume"), ("issue", "number"), ("pages", "pages"), ("doi", "doi"), ("url", "url")):
        if r[k]:
            f.append(f"  {name} = {{{r[k]}}}")
    return f"@{t}{{{r['key']},\n" + ",\n".join(f) + "\n}\n"


def main():
    rows = [dict(zip(FIELDS, s)) for s in SOURCES]
    from collections import defaultdict
    groups = defaultdict(list)
    for r in rows:
        if r["status"] == "V":
            groups[(r["authors"], r["year"])].append(r)
    for g in groups.values():
        if len(g) > 1:
            for i, r in enumerate(g):
                r["yeardisp"] = r["year"] + "abcdefgh"[i]
    keys = [r["key"] for r in rows]
    assert len(keys) == len(set(keys)), "duplicate keys"
    assert all(r["section"] in SECTIONS for r in rows), "unknown section"
    assert set(NEEDED) == {r["key"] for r in rows if r["status"] != "V"}, "every queued source needs a NEEDED entry"
    with open(os.path.join(HERE, "sources.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    queue = [r for r in rows if r["status"] != "V"]
    rows = [r for r in rows if r["status"] == "V"]
    with open(os.path.join(HERE, "references.bib"), "w", encoding="utf-8") as fh:
        fh.write("% Outcome Harvesting bibliography: verified sources only.\n% Generated by build_bibliography.py; edit the script, not this file.\n\n")
        fh.write("\n".join(bib(r) for r in rows))
    v = len(rows)
    md = ["# Annotated bibliography", "",
          f"{v} sources on Outcome Harvesting, grouped by use. Every one was verified at source in October 2026: the title, year and pages (or report series) were confirmed in the document itself, or on the journal, publisher or repository page, or by Crossref. Page numbers in the notes were checked against the documents. Sources not yet verified are held back in the [verification queue](verification-queue.md) until they are.", "",
          "Generated from `build_bibliography.py`, which also writes `references.bib` (BibTeX) and `sources.csv`. Citation details that differ between sources are in [`errata.md`](errata.md).", "",
          "## Where to start", "",
          "1. Wilson-Grau and Britt (2013), *Outcome harvesting*. The 27-page brief. Free.",
          "2. Wilson-Grau, Britt, Dewata, Rogers and Stevens (2024), BetterEvaluation's *Outcome harvesting* page. A free overview of the steps and principles.",
          "3. Wilson-Grau (2019), *Outcome harvesting: Principles, steps, and evaluation applications*. The full method.",
          "4. World Bank (2014a), *Outcome-based learning field guide*. Tools you can use straight away. Free.",
          "5. Smith, Scheers and Robinson (2020). A complete harvest from Uganda, start to finish. Free.", ""]
    for sec, (title, blurb) in SECTIONS.items():
        md += [f"## {sec}. {title}", "", blurb, ""]
        for r in [r for r in rows if r["section"] == sec]:
            md.append(f"- {apa(r)}  ")
            md.append(f"  {r['note']}")
        md.append("")
    with open(os.path.join(HERE, "annotated-bibliography.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))
    q = ["# Verification queue", "",
         "Sources found in published listings but not yet confirmed at source. They are **not** in the bibliography or `references.bib` until confirmed.", "",
         "To clear one: confirm title, year and pages (or report series) in the document or on the publisher or repository page, set its status to `V` in `build_bibliography.py`, remove its line from `NEEDED`, and rerun the script.", "",
         "| Source | Note | Still needed |", "|---|---|---|"]
    for r in queue:
        q.append(f"| {apa(r)} | {r['note']} | {NEEDED[r['key']]} |")
    with open(os.path.join(HERE, "verification-queue.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(q) + "\n")
    print(f"{v} published, {len(queue)} queued")


if __name__ == "__main__":
    main()
