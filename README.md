# Outcome Harvesting

[![Content licence: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Code licence: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE-CODE)

A free, page-cited library for Outcome Harvesting (OH): a verified bibliography, design templates, a red team protocol for checking that a harvest was done properly, and, in progress, a short course.

Every source listed here was checked in the document itself or at the publisher, repository or Crossref. Statements about what OH authors say carry page numbers, and those pages are checked against the source text before anything is added. Sources that cannot yet be verified are held back until they can be.

## What Outcome Harvesting is

OH starts from the changes that have actually happened, then traces back to ask whether, and how, an intervention helped bring them about (Wilson-Grau 2019, p. 1). The brief recommends it where the links between cause and effect are unclear, and where what matters is change in what people and organisations do, not a count of activities (Wilson-Grau and Britt 2013, p. 2).

The brief defines an outcome as "a change in the behavior, relationships, actions, activities, policies, or practices of an individual, group, community, organization, or institution" (Wilson-Grau and Britt 2013, p. 2). The 2019 book puts it more tightly: an observable change in behaviour (p. 1). A training delivered is not an outcome. A district council that changes how it budgets because of that training may be.

A harvest runs in six steps (Wilson-Grau and Britt 2013):

1. Design the harvest (p. 6)
2. Review documentation and draft outcome descriptions (p. 10)
3. Engage with change agents to formulate outcome descriptions (p. 13)
4. Substantiate (p. 18)
5. Analyse and interpret (p. 21)
6. Support use of findings (p. 25)

The 2019 book adds nine principles to guide them: five on process (pp. 149 to 167) and four on content (pp. 169 to 187).

OH and contribution analysis fit together. This course suggests a simple pairing: harvest the outcomes, then test the most important ones with [contribution analysis](https://github.com/wenareeba/contribution-analysis). That pairing is course guidance, not a claim from either method's authors.

## Who this is for

- **Evaluators** designing or running a harvest
- **Commissioners and reviewers** judging whether an OH report stands up
- **Students and researchers** learning the method or studying how it is used

## Start here

| If you want to... | Go to |
|---|---|
| Learn OH from scratch | [Lesson 1: What a harvest is for](course/lessons/0001-what-a-harvest-is-for.html) and its [reference card](course/reference/0001-oh-core.html) |
| Design a harvest | [`templates/oh-harvest-design-template.md`](templates/oh-harvest-design-template.md) |
| Check a harvest design or report | [`red-team/oh-red-team-protocol.md`](red-team/oh-red-team-protocol.md) |
| Find the right reading | [`bibliography/annotated-bibliography.md`](bibliography/annotated-bibliography.md) |
| Cite an OH source correctly | [`bibliography/errata.md`](bibliography/errata.md) |
| See which sources are still being checked | [`bibliography/verification-queue.md`](bibliography/verification-queue.md) |

The lessons are interactive web pages. Until the course website is live, download the repository and open them in a browser; GitHub shows HTML files as code.

## What is in the repository

| Folder | Contents | Status |
|---|---|---|
| [`bibliography/`](bibliography/) | 16 sources in six sections, all verified at source, with BibTeX (`references.bib`) and CSV. An errata page records five citation details that differ between sources. Four sources wait in a verification queue. | Published |
| [`course/assets/`](course/assets/) | The stylesheet and script every lesson and reference card uses | Published |
| [`templates/`](templates/) | Five tools: a harvest design template, an outcome description sheet, a substantiation plan, a harvest analysis matrix and a report checklist | Published |
| [`red-team/`](red-team/) | A 33-check audit protocol (8 critical) following the six steps, with five verification questions and a verdict scale | Published |
| [`course/`](course/) | Eight lessons with retrieval quizzes, applied questions, writing tasks with model answers, and a reference card for each | In progress: lessons 1 and 2 of 8 published |

## How the pieces fit

1. **Learn** the method with the course and its reference cards.
2. **Design** a harvest with the template and its worksheets before you start.
3. **Check** the design, and later the draft report, against the red team protocol.
4. **Read further** using the bibliography's "Where to start" list.

## Quality standards

- **Verified sources only.** A source enters the bibliography once its title, year and pages (or report series) are confirmed in the document or at the publisher, repository or Crossref. Authors are recorded with initials, so no unconfirmed first name is published.
- **Page-cited claims.** Statements about the method cite the page they come from, and a script checks each cited passage against the source text.
- **Exact quotations.** A quotation is word for word. Anything else is paraphrased without quotation marks.
- **Corrections are public.** Citation details that differ between sources go in the errata, with the evidence for each.

## Contributing

Suggestions are welcome, especially published harvests from Africa, Asia and Latin America. Until the contributing guide is published, please open an issue with the full citation and where you checked it.

## How to cite

Suggested credit: Wenareeba, Morris. (2026). *Outcome Harvesting: course, bibliography, templates and red team protocol*. GitHub repository. https://github.com/wenareeba/outcome-harvesting

## Licence

- **Written material** (lessons, reference cards, protocol, templates, bibliography notes): [Creative Commons Attribution 4.0 International](LICENSE) (CC BY 4.0). You may share and adapt it, including commercially, if you give credit.
- **Code** (`bibliography/build_bibliography.py`, `course/assets/lesson.js`): [MIT](LICENSE-CODE).
- **Third-party material** quoted or cited here, such as passages from Wilson-Grau and Britt (2013) and Wilson-Grau (2019), stays under its own licence and copyright.

## Key references

Wilson-Grau, R., and Britt, H. (2013). *Outcome harvesting*. Ford Foundation, Middle East and North Africa Office, Cairo. May 2012, revised November 2013. Free. https://www.betterevaluation.org/tools-resources/outcome-harvesting-0

Wilson-Grau, R. (2019). *Outcome harvesting: Principles, steps, and evaluation applications*. Information Age Publishing. https://doi.org/10.1108/978-1-64113-394-4
