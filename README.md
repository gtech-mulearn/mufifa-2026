<div align="center">

![μFIFA World Cup 2026](docs/assets/mufifa-banner.jpg)

[![μFIFA Profile Validator](https://github.com/GizzZmo/mufifa-2026/actions/workflows/validate-profile.yml/badge.svg)](https://github.com/GizzZmo/mufifa-2026/actions/workflows/validate-profile.yml)
[![Discord](https://img.shields.io/discord/771670169691881483?color=7289da&label=Discord&logo=discord&logoColor=white)](https://discord.com/channels/771670169691881483/1157030408874106991)
[![License](https://img.shields.io/github/license/GizzZmo/mufifa-2026?color=blue)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#)

</div>

---

# μFIFA World Cup 2026

**The Festival of Innovation, Fellowship & Achievement by μLearn.**

This isn't just a challenge, it's a World Cup. You'll represent a Nation, play for a Squad Domain, and compete on live leaderboards, all while building real work that belongs in your portfolio.

Our mission: surface Kerala's most versatile innovators across Maker, Coder, Designer, and Strategist disciplines, and connect them with each other, with startups, and with the world.

> 👋 **New to GitHub or Markdown?** No worries. You don't need any prior experience.
> Read the **[Complete Beginner Guide →](./docs/GETTING_STARTED.md)** before proceeding. It covers everything from creating a GitHub account to submitting your first Pull Request, step by step.

---

## Table of Contents

- [About](#about)
- [Squad Domains](#squad-domains)
- [How to Participate](#how-to-participate)
- [Leaderboard](#leaderboard)
- [Profile Validation](#profile-validation)
- [Live Gamification & Automated Assets](#-live-gamification--automated-assets-phases-1-2--3-complete)
- [Multi-Paradigm Multi-Language (MPML) System Roadmap](#️-multi-paradigm-multi-language-mpml-system-roadmap)
- [FAQ](#faq)

---

## About

**μFIFA World Cup 2026** is μLearn's flagship community tournament, a gamified, open-source way of celebrating builders. Instead of a traditional hackathon, μFIFA turns contribution into a season-long sport:

- 🌍 **Represent a Nation** — pick a country to compete for on the global standings.
- 🛡️ **Play for a Squad Domain** — Coder, Designer, Maker, or Strategist, based on the kind of work you do best.
- 🏆 **Compete on live leaderboards** — karma, contributions, and community engagement are tracked and published weekly.
- 📁 **Build a real portfolio** — every submission lives in this repository as a Pull Request, so your profile and your work stay on GitHub forever.

The whole experience is powered by an automated, open-source pipeline: profile validation, markdown linting, dynamic SVG badge generation, a JSON leaderboard feed, multi-language auto-grading, and an interactive React dashboard, all running on GitHub Actions. See the [Live Gamification & Automated Assets](#-live-gamification--automated-assets-phases-1-2--3-complete) section below for the full list of automation features, and the [MPML Roadmap](./docs/ROADMAP.md) for where the project is headed.

**Who is it for?** Anyone in the μLearn community, students, developers, designers, hardware tinkerers, and community organizers alike, who wants to showcase their work and compete alongside their peers.

---

## Squad Domains

Every player belongs to one or more Squad Domains. Your domain reflects the kind of work you do.

| Domain | Who it's for |
|--------|--------------|
| **Coder** | Developers, engineers, competitive programmers, open-source contributors |
| **Designer** | UI/UX designers, visual artists, motion designers, brand creators |
| **Maker** | Hardware hackers, robotics builders, IoT engineers, fabricators |
| **Strategist** | Product thinkers, community builders, program managers, marketers |

You can select multiple domains if your work spans them. Your Squad Domain appears on your profile and determines your leaderboard category.

---

## How to Participate

### Step 1: Join the μLearn Community

Register on the μLearn platform [here](https://app.mulearn.org/register).

Watch the [Onboarding Video](https://www.youtube.com/watch?v=IwpOmzSqYao) before proceeding. It walks you through creating your account, joining the Discord server, and getting your MUID.

### Step 2: Get your MUID

<img width="400" alt="Register on μLearn" src="./docs/assets/getmu.png">

*Screenshot: registering on the μLearn platform and starting the onboarding flow.*

Follow the onboarding workflow. Connect your Discord account to obtain your MUID (μLearn User ID).

<img width="400" alt="Get your MUID" src="./docs/assets/muid.png">

*Screenshot: your MUID, shown once your Discord account is linked. You'll need this for your profile card embed in Step 4.*

### Step 3: Create Your Profile

Fork this repository, create your player card in the `/profile` directory, and open a Pull Request.

**1. Fork the repository**

Fork [this repository](https://github.com/gtech-mulearn/mufifa-2026) to your own GitHub profile.

**2. Create your profile file**

Create a new Markdown file inside `/profile`, named using your MUID:

```
profile/yourname@mulearn.md
```

**3. Fill out your profile**

Use [TEMPLATE.md](./TEMPLATE.md) as the base. See [this example profile](./profile/sachinrajm@mulearn.md) for reference.

**4. Open a Pull Request**

Submit a PR targeting the `main` branch. Your profile is now on the pitch.

### Step 4: Link Your μLearn Profile Card

Your profile card displays your live karma rank and squad domain progress on the μLearn leaderboard.

**1. Get your embed link**

Go to the [μLearn Discord server](https://discord.com/channels/771670169691881483/1157030408874106991), run `/get-embed-link`, and copy the link.

**2. Paste it into your profile file**

Add the embed link to the **Profile Card** section at the bottom of your profile.

**3. Open a Pull Request**

Submit a PR to `main`. Your live profile card will render immediately.

Your profile page will be live at:

```
https://gtech-mulearn.github.io/mufifa-2026/profile/[your-muid]
```

### Step 5: Join the Discord

Join the [μFIFA Discord server](https://discord.com/channels/771670169691881483/1157030408874106991), your tournament home base.

| Channel | Purpose |
|---------|---------|
| `#μfifa-announcement` | Match week releases, Nation standings, and Player of the Match awards |
| `#μfifa-introduction` | Share your profile page link with `#mufifa2026-intro` to introduce yourself |
| `#μfifa-submission` | Submit completed tasks with your MUID and deliverable links |
| μFIFA Watch Party | Voice channel for live calls, office hours, and watch sessions |

> New to Markdown? [Introduction to Markdown](https://discord.com/channels/771670169691881483/1115381777792499805/1115727847647092808)

---

## Leaderboard

Nation standings, Squad Domain rankings, and individual μPoint scores are tracked in the [LEADERBOARD.md](./docs/LEADERBOARD.md). Standings update every Friday.

---

## Profile Validation

Every profile is automatically validated, both locally before you commit and on GitHub when you open a PR.

**What gets checked:**

| Check | Rule |
|-------|------|
| Filename | Must follow `yourname@mulearn.md` format |
| Header | Must include Squad Domain(s) and FIFA Nation |
| About Me | Minimum 200 characters |
| Top-level sections | `## FIFA World Cup Corner` and `## Portfolio Highlights` must be present |
| Required sections | All `####` sub-sections must be present |
| Section content | Sections must not contain only placeholder text |
| Profile Card | Embed must use your actual MUID |
| MUID consistency | Filename and embed MUID must match |
| Markdown Formatting | Strict conformance to standard Markdown rules via `markdownlint` |

**Set up the pre-commit hook** (one time, after cloning):

```sh
sh scripts/install-hooks.sh
```

Every time you `git commit` a profile file, the validator and `markdownlint` run automatically and block the commit with a clear message if anything's wrong.

**Run the validator manually:**

```sh
python3 scripts/validate_profile.py profile/yourname@mulearn.md
```

The same check runs on every PR via GitHub Actions.

---

## 🚀 Live Gamification & Automated Assets (Phases 1, 2 & 3 Complete)

The tournament has now integrated the following automated features from our Roadmap:
* **Strict Markdown Conformance**: Uses `markdownlint` in our CI and pre-commit hooks to keep all profiles perfectly formatted.
* **Dynamic SVG Badges**: Our CI automatically reads `docs/LEADERBOARD.md` and generates custom high-quality SVG badges for performers, deployed directly to GitHub Pages.
* **Leaderboard Data Feed**: A `leaderboard.json` feed is periodically generated, allowing community developers to build their own live dashboards.
* **Multi-Language Testing Sandbox**: GitHub workflows now support running and grading unit tests in Python, Node.js, Go, and Rust.
* **Automatic Pull Request Reviewer**: AI-based code review bot leaves inline comments on PR code flaws or security issues.
* **Automated Certificate Generation**: Compiles proof of work into beautiful PDF certificates published as release artifacts.
* **Full Tournament Dashboard**: An open-source, interactive React site fetching JSON artifacts for live leaderboards and charts.

---

## 🗺️ Multi-Paradigm Multi-Language (MPML) System Roadmap

We are scaling μFIFA 2026 into a full-featured, automated tournament engine. Phase 1, 2 & 3 are complete! Check out our **[Multi-Paradigm Multi-Language System Roadmap](./docs/ROADMAP.md)** to see our progress:
* **Multi-Paradigm Validation Models**: Declarative, functional, and object-oriented validation rules.
* **Multi-Language Sandbox**: Auto-grading pipelines for Python, Node.js (TS/JS), Bash, Go, and Rust.
* **CI/CD Automation & Badges**: Dynamic SVG badges pushed to dashboards and automated PR preview generation.
* **Assets & Build Artifacts**: Exportable participant portfolios and JSON leaderboard CDN data feeds.

Contributions to the validator infrastructure are highly encouraged!

---

## FAQ

**Do I need coding experience to participate?**
No. Squad Domains cover Coding, Design, Maker/hardware, and Strategy work, so there's a track for every kind of builder.

**I don't have a GitHub account. Where do I start?**
Start with the **[Complete Beginner Guide](./docs/GETTING_STARTED.md)**. It walks through account creation, forking, and opening your first Pull Request.

**My profile PR failed validation. What do I do?**
Check the CI log on your PR for the specific rule that failed, cross-reference it with the [Profile Validation](#profile-validation) table above, then run the validator locally with `python3 scripts/validate_profile.py profile/yourname@mulearn.md` before pushing again.

**Where can I see the current standings?**
The [LEADERBOARD.md](./docs/LEADERBOARD.md) is the source of truth and updates every Friday. A live, interactive view is also available via the [Tournament Dashboard](./dashboard).

**How do I get help if I'm stuck?**
Join the [μFIFA Discord server](https://discord.com/channels/771670169691881483/1157030408874106991) and ask in `#μfifa-submission` or the μFIFA Watch Party voice channel.

---

<div align="center">

μFIFA World Cup 2026 · μLearn Foundation · Festival of Innovation, Fellowship & Achievement

</div>
