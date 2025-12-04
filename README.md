# documentarian

[![Deploy Docusaurus to GitHub Pages](https://github.com/smichalski17-dev/documentarian/actions/workflows/deploy.yml/badge.svg)](https://github.com/smichalski17-dev/documentarian/actions/workflows/deploy.yml)

Documentation website built on Docusaurus showcasing the work of Susan Michalski.

## Deploy

- Source: GitHub Pages is configured to deploy from branch `gh-pages`, folder `/` (root).
- Workflow: `.github/workflows/deploy.yml` builds from `./my-website` and publishes `./my-website/build` via `peaceiris/actions-gh-pages`.
- Trigger: Pushes to `main` or manual dispatch run the deploy workflow.
