<div align="center">

![μFIFA World Cup 2026](docs/assets/mufifa-banner.jpg)

</div>

---

# μFIFA World Cup 2026

**The Festival of Innovation, Fellowship & Achievement by μLearn.**

This isn't just a challenge, it's a World Cup. You'll represent a Nation, play for a Squad Domain, and compete on live leaderboards, all while building real work that belongs in your portfolio.

Our mission: surface Kerala's most versatile innovators across Maker, Coder, Designer, and Strategist disciplines, and connect them with each other, with startups, and with the world.

> 👋 **New to GitHub or Markdown?** No worries. You don't need any prior experience.
> Read the **[Complete Beginner Guide →](./docs/GETTING_STARTED.md)** before proceeding. It covers everything from creating a GitHub account to submitting your first Pull Request, step by step.

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

Follow the onboarding workflow. Connect your Discord account to obtain your MUID (μLearn User ID).

<img width="400" alt="Get your MUID" src="./docs/assets/muid.png">

### Step 3: Create Your Profile

Fork this repository, create your player card in the `/profile` directory, and open a Pull Request.

**1. Fork the repository**

Fork [this repository](https://github.com/gtech-mulearn/mufifa-2026) to your own GitHub profile.

**2. Create your profile file**

Create a new Markdown file inside `/profile`, named using your MUID:

```
ameenas@mulearn.md
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

**Set up the pre-commit hook** (one time, after cloning):

```sh
sh scripts/install-hooks.sh
```

Every time you `git commit` a profile file, the validator runs automatically and blocks the commit with a clear message if anything's wrong.

**Run the validator manually:**

```sh
python3 scripts/validate_profile.py profile/yourname@mulearn.md
```

The same check runs on every PR via GitHub Actions.

---

<div align="center">

μFIFA World Cup 2026 · μLearn Foundation · Festival of Innovation, Fellowship & Achievement

</div>
