<!-- badges: start -->
[![Website](https://img.shields.io/badge/website-live-brightgreen.svg)](https://ubc-mds.github.io/programming-in-python-for-data-science/)
[![Built with Quarto](https://img.shields.io/badge/built%20with-Quarto-75AADB.svg)](https://quarto.org)
[![Instructional material: CC BY-NC-SA 4.0](https://img.shields.io/badge/instructional%20material-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE.md)
[![Software: MIT](https://img.shields.io/badge/software-MIT-blue.svg)](LICENSE.md)
<!-- badges: end -->

# Programming in Python for Data Science

This repository holds the [Quarto](https://quarto.org) source for **Programming in Python for Data
Science**, a UBC Extended Learning's [Key Capabilities in Data Science
program](https://extendedlearning.ubc.ca/programs-credentials/key-capabilities-data-science-certificate) course.

The rendered course is published at
**<https://ubc-mds.github.io/programming-in-python-for-data-science/>**.

The course teaches data analysis in Python, including:

- Processing tabular data with `pandas`.
- Visualizing processed data with `altair`.
- Working with numerical data using `numpy`.
- Iteration, flow control, function design, testing, and debugging skills.
  
It assumes no prior programming experience.

Every exercise runs in the browser through [Quarto Live](https://github.com/r-wasm/quarto-live) and `Pyodide`, so learners need nothing installed to take the course — the setup below is only for people editing the material.

## Course Instructors

- [Socorro Dominguez Vidana](https://ht-data.com/about)

## Former Course Instructors

- [Celine Siliang Liu](https://www.linkedin.com/in/siliangliu/)
  
## Contributors

This course was built and is maintained by many people from UBC MDS program.

- [Tomas Beuzen](https://www.tomasbeuzen.com/)
- [Hayley Boyce](https://www.hayleyfboyce.com)
- [Mike Gelbart](https://www.mikegelbart.com/)
- [Tim Head](https://betatim.github.io/)
- [Varada Kolhatkar](https://kvarada.github.io/)
- [Joel Ostblom](https://joelostblom.com/)
- [Tiffany Timbers](https://www.tiffanytimbers.com/)
- [Elijah Willie](https://www.linkedin.com/in/elijah-willie-203845b9/)
- [Mengxin (Betty) Zhao](https://www.linkedin.com/in/mengxinzhao/)

### Attribution

- Material adapted from UBC's [DSCI 511: Python Programming for Data
  Science](https://pages.github.ubc.ca/MDS-2020-21/DSCI_511_py-prog_students/README.html) by
  [Tom Beuzen](https://www.tomasbeuzen.com/).
- The cereal dataset: [80 Cereals](https://www.kaggle.com/crawford/80-cereals/) (c) by
  [Chris Crawford](https://www.linkedin.com/in/crawforc3/), licensed under
  [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/).

## Tips for Contributing

Issues and bug reports are always welcome — please
[open an issue](https://github.com/UBC-MDS/programming-in-python-for-data-science/issues).

For changes, branch off `master` and open a pull request. Every pull request automatically gets a preview deployment of the full site (see [Deployment](#deployment)), so you can check how your change renders before it is merged. Because the material is course content, prose edits matter as much as code edits:

- Keep the conversational voice of the surrounding text
- Slide speaker notes come from the videos' scripts.

A previous version of the course material was developed using [Ines Montani](https://ines.io/) Spacy's teaching framework. 

## What this repository contains

The course is nine modules plus a bonus module and a closing section:

| Module | Topic |
| --- | --- |
| M0 | Welcome to Programming in Python for Data Science |
| M1 | Python & Pandas — An Unexpected Friendship |
| M2 | Not So Scary Wrangling (Table Manipulation and Chaining) |
| M3 | Tidy Data and Joining Dataframes |
| M4 | Python Without the "Eek" (Basic Python) |
| M5 | Making Choices and Repeating Iterations |
| M6 | Function Fundamentals and Best Practices |
| M7 | Importing Files and the Coding Style Guide |
| M8 | A Slice of NumPy and Advanced Data Wrangling |
| Bonus | Bonus module |
| — | Module closing remarks |

Each module directory holds the module's pages, and a `slides/` subdirectory holding its [reveal.js](https://quarto.org/docs/presentations/revealjs/) decks.

### Repository layout

| Path | What it is |
| --- | --- |
| `_quarto.yml` | Project config: render list, resources, and the hand-maintained sidebar |
| `modules/` | All course content — the only directory that is rendered |
| `data/` | CSV/Excel datasets used by lessons and exercises |
| `src/utils.py` | Shared Python helpers: display settings, Altair theme, exercise checkers |
| `src/quiz.js` | The `generateQuiz()` multiple-choice widget |
| `static/` | Images, logos, and other media |
| `styles.scss` | Site and slide theming |
| `_extensions/` | Vendored [Quarto Live](https://github.com/r-wasm/quarto-live) extension |
| `docs/` | Syllabus and the video screen-recording workflow |

In previous `git` commits (Up to commit `c363d86fb411dbfc7e2dbcbd38cee62d7aac8984`), you can find the folders `chapters/`, `exercises/`, and `junk/`. These are legacy content from the course's pre-Quarto platform. They are
not built and not maintained but can be used as a reference for the original exercise numbering.

## How it works

`_quarto.yml` drives everything:

- **`execute-dir: project`** — code cells resolve paths from the repository root, so a lesson reads
  `data/canucks.csv`, never a path relative to its own `.qmd`.
- **`render:`** includes only `modules/**/*.qmd`. Anything outside `modules/` is not built.
- **`resources:`** copies `styles.scss`, `src/utils.py`, and `data/` into the site unexecuted. A separate top-level **`pyodide:`** block copies the same files into the browser's virtual filesystem so in-page code can read them.
- **The sidebar `contents:` list is written by hand.** A new page will not appear on the site until it is added there.

Pages come in three shapes:

1. **Video and slides** — `format: html`, a tabset holding a YouTube embed and an `<iframe>` pointing at the page's rendered reveal.js deck.
2. **Quiz** — `format: html`, loading `src/quiz.js` and calling `generateQuiz()` once per question.
3. **Live coding exercise** — `format: live-html`, using `{pyodide}` cells that execute in the learner's browser. A cell tagged `#| exercise: <slug>` holds the fill-in-the-blank starter; a second cell with the same slug and `#| check: true` asserts against the learner's `result` and reports back through the helpers in `src/utils.py`. Matching `.hint` and `.solution` blocks are keyed by the same slug.

## Running the site locally

### System requirements

- [Quarto](https://quarto.org/docs/get-started/) 1.6 or newer (1.6.43 is what CI uses)
- Python 3.11 or 3.12
- The packages listed in `environment.yaml` (`pandas`, `altair`, `jupyter`, `openpyxl`, and others)

### Setup

```bash
git clone git@github.com:UBC-MDS/programming-in-python-for-data-science.git
cd programming-in-python-for-data-science
conda env create -f environment.yaml
conda activate kcds-prog
```

The environment is named `kcds-prog` and pins Quarto itself, so activating it gives you a matching Quarto.

### Build

```bash
quarto preview   # local server with live reload — the usual way to work
quarto render    # full static build into _site/
```

To rebuild a single page instead of the whole site:

```bash
quarto render modules/module1/module1-01-introduction_to_dataframes.qmd
```

A full `quarto render` executes every `reveal.js` deck through Jupyter and takes a while, so prefer `quarto preview` or a single-file render while editing.

### Troubleshooting

Rendering **any** page starts a local Jupyter kernel — including `live-html` pages, whose `{pyodide}` cells run in the browser rather than locally. No `.qmd` pins a kernel with a `jupyter:` key, so Quarto
picks the first Python kernelspec it finds. If a stale kernelspec on your machine points at an interpreter that no longer exists, the render fails with a `FileNotFoundError` naming a path that has nothing to do with this repository. Check with:

```bash
jupyter kernelspec list
```

and remove or repair any entry pointing at a deleted environment.

`_site/` and `.quarto/` are build output. Neither belongs in a commit.

## Deployment

| Workflow | Trigger | Result |
| --- | --- | --- |
| `.github/workflows/publish.yaml` | Push to `master` | Renders the site and pushes `_site/` to the `gh-pages` branch |
| `.github/workflows/pr-preview.yaml` | Pull request against `master` | Builds and deploys a preview, removed when the PR closes |

Both build the environment from `environment.yaml` with micromamba and run `quarto render`, so a change that renders cleanly for you locally will render in CI.

## License

This repository carries two licenses, split between the instructional material and the software that frames it:

- **Instructional material** — the course content — is licensed
  [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
- **Software** — the framework used to build and host the material — is licensed under the MIT License.

See [`LICENSE.md`](LICENSE.md) for the full text of both.
