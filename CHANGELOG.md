# Changelog

Newest first. Each section lists what a release added; the all-versions DOI is 10.5281/zenodo.23514918.

## Version 1.1.2 (2026-10-23)

- Rights review. The README gains a Rights and permissions section: no third-party copies are held, quotations are short and page-cited, the course is independent, and rights holders can ask for any passage to be changed within seven days. The contributing guide forbids adding copies of copyrighted documents or links to unofficial copies.
- Two verbatim definitions now carry quotation marks (Lesson 1, Wilson-Grau and Britt 2013, p. 2; Lesson 2, Wilson-Grau 2019, p. 170). Two passages labelled as paraphrase stayed too close to the book and are rewritten (Lesson 4, p. 57; Lesson 5, p. 99).
- The verification queue no longer links a downloadable copy of a book chapter whose authorisation could not be confirmed; the citation stays.
- README links to Lesson 1, its reference card and the repository map now open the web pages on the course website instead of GitHub's code view.
- Lesson 8 links to the companion Contribution Analysis course, now public ("harvest, then test").
- Keywords in `CITATION.cff` and `.zenodo.json` capitalise Outcome Harvesting.

## Version 1.1.1 (2026-10-23)

- Repository map: the hero now opens with the name, Outcome Harvesting, set large on two lines; the headline moves beneath it as a subtitle.
- Lessons and reference cards restyled to match the repository map: a frosted top bar with the next step, a dark aubergine title band with the lesson number, title, lede and goal, then the light reading page, and a footer carrying the all-versions DOI. Section numbers zero-padded. No lesson text, quiz or citation changed.

## Version 1.1.0 (2026-10-23)

- Repository map redesigned: a dark aubergine hero with the six steps (Wilson-Grau and Britt 2013, pp. 6 to 25) and the counts, then numbered sections on light paper: who it is for, the four parts, the route map, route cards, questions and a footer.
- Every citation now points to the all-versions DOI, 10.5281/zenodo.23514918, which always resolves to the latest version. The suggested citation in the README no longer names a single version.
- Citation title in title case in `CITATION.cff` and `.zenodo.json`, matching the README.
- Errata and Lesson 5: the p. 93 sample-size entry no longer says 51 is wrong. The book does not state its assumed proportion; 51 follows at about 2.5% of outcomes wrong, 89 at the conservative 50%, 78 at the book's own under 10% (p. 95). Every assumption tested still needs over half of a typical harvest.
- Links to the contribution analysis course removed from Lesson 8, the README, the repository map and the Zenodo metadata until that course is public.
- Zenodo DOI added: 10.5281/zenodo.23514918 (all versions) and 10.5281/zenodo.23514919 (version 1.0.0). DOI badge on the README; citation file and suggested citation updated.

## Version 1.0.0 (2026-10-21)

- Repository map as the site's start page (`index.html`), with six routes through the material.
- Contributing guide, code of conduct, issue forms, pull request template, citation file and Zenodo metadata.
- README updated: the course is complete, and the contributing and citation sections point to the new files.
- Eight-lesson course, each lesson with recall questions, one interactive figure, five applied questions, a writing task with a model answer and a reference card. Shared lesson stylesheet and script in `course/assets/`.
- Errata gains a section on figures checked against the book's own arithmetic: the random-sample size on p. 93 and the review rate on p. 45.
- One unsupported quiz feedback line in lessons 3 and 4 replaced.
- Five templates and a 33-check red team protocol (8 critical).
- Annotated bibliography: 16 sources verified at source, in six sections, with BibTeX and CSV; errata page; verification queue for sources not yet verified.
- README, licences (CC BY 4.0 and MIT) and site files.
