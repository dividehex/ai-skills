---
name: github-readme-design
description: Research, write, redesign, or audit a GitHub repository README.md as a polished project landing page with a strong title, honest badges, real live-project screenshots or demos, verified quick start, clear documentation, accessibility, credits, MIT-by-default licensing, and reviewed contribution, security, and conduct files. Use when asked to create, improve, or review a project README or its presentation.
license: MIT
compatibility: opencode
metadata:
  audience: "open-source maintainers and developer-tool authors"
  output: "README.md"
---

# GitHub README Design

Act as a product marketer, information architect, technical writer, and visual designer **without compromising engineering accuracy**. Deliver a README that quickly explains the project's value, looks intentional on GitHub, and helps a real person successfully try the software.

**Core principle:** A beautiful README earns attention; a working README earns trust. Optimize for both. Never fabricate functionality, usage numbers, screenshots, testimonials, compatibility, sponsorship, security claims, or project status to make the page more persuasive.

## When to apply this skill

Use for a new repository README, a substantive README redesign, an above-the-fold polish pass, or an audit of a project's GitHub presentation. Adapt the result to a CLI tool, library, service, hardware project, research repository, app, or early prototype. Treat this as a decision-making guide, **not** a rigid template that forces every project into the same sections.

## 1. Research the repository before writing

1. Inspect the existing `README.md` and nearby documentation without overwriting or discarding useful instructions.
2. Inspect package manifests, entry points, examples, CLI help, config samples, tests, CI workflows, releases/tags, deployment files, existing license declarations, `LICENSE`/`LICENSE.md`/`COPYING`, community files in the root, `.github/`, and `docs/`, account-level community defaults if accessible, and existing media. Identify the *actual* install and run path.
3. Establish the project name, category, target audience, core problem, standout capability, maturity, supported platforms, prerequisites, primary user action, and project maintainer(s) from evidence.
4. Inventory brand assets, real screenshots, recorded demos, architecture diagrams, logos, and their ownership/licensing. Check whether images contain tokens, private URLs, personal data, or unrelated UI. Determine whether the real project can be run and captured safely in the available environment; identify its actual interface or output worth showing.
5. Identify the shortest reproducible happy path: prerequisites → install → configure (if needed) → run → expected result. Prefer an existing tested example over speculative commands.
6. Decide which details deserve the README and which belong in dedicated docs. Preserve accurate warnings, migration information, and important compatibility constraints.
7. If a claim cannot be verified, remove it, qualify it transparently, or note the gap in the delivery summary. Do not turn guesses into finished README copy. Do not insert `TODO`, fake badges, sample statistics, or dummy links into a supposedly finished README.
8. If web access is available and needed, check current external product links and technical claims against authoritative sources; treat repo contents as the primary source for this project's behavior.
9. Establish whether you are working on a new/owner-controlled project or third-party source: inspect provenance, existing license obligations, confirmed copyright holder, and the project's actual contact and security-reporting channels. Do not assume write access implies authority to relicense someone else's code.

### Positioning exercise

Before drafting, privately answer these four questions:

- **Who is it for?** Define the intended reader, not merely "developers."
- **What does it do?** State one concrete outcome without vague adjectives.
- **Why does it matter?** Give the real benefit or differentiator, supported by the project.
- **What should the visitor do next?** Try it, view a demo, read docs, or inspect an example.

Write a plain-language one-sentence positioning line. Prefer "Detects context drift in local AI conversations" to "The revolutionary ultimate AI solution." Avoid unsupported superlatives, SEO keyword stuffing, hype, and marketing claims without evidence.

## 2. Design the first screen as a coherent hero

The top of the README is the project's storefront. Compose it in this visual order:

1. **Project identity:** optional *real* logo or restrained banner, followed by exactly one prominent H1 containing the correct project name.
2. **Value proposition:** a short, specific tagline immediately under the title; optionally one supporting sentence identifying the audience or differentiator.
3. **Trust and status:** one compact, visually consistent badge row, using only meaningful and accurate badges.
4. **Hero proof:** a large, legible product screenshot, short demo animation, or clickable video poster **directly below the title/tagline/badges**. A real product in action beats a decorative stock image.
5. **Next action:** a compact line of descriptive links such as **Quick start · Demo · Documentation** after the hero, or just before it if the hero would otherwise bury navigation. Then start the substantive content.

Do not push the hero below lengthy feature lists, giant tables, multiple badge rows, a full table of contents, or paragraphs of background. **If existing screenshots are absent or unusable, attempt to capture new ones from the actual running project** using the workflow in section 7. If the product has no genuine visual interface, a short *text-based* terminal example or practical API call can serve as its proof; do not invent a UI screenshot.

### Hero design details

- Prefer a well-cropped, crisp, real screenshot that illustrates the primary outcome. Give it a descriptive filename and meaningful alt text.
- Make the main screenshot large enough to read at typical laptop widths; avoid forcing a fixed pixel width that overflows narrow screens. Use a sensible natural aspect ratio and leave uncluttered margins inside the image.
- A custom branded banner is optional. If present, keep it modest so the actual screenshot remains prominent. A banner is not a substitute for a working-product image.
- A hero is usually **one** primary visual. Put secondary screenshots in a focused gallery under Features or Screenshots; add short captions explaining what each proves.
- For a video, put a linked poster/thumbnail prominently under the badges, label the link "Watch the demo" and provide a short description of what viewers will see. Use a stable, accessible destination. A clickable image is the reliable baseline; do not assume embedded `<iframe>`, JavaScript, autoplay, or HTML video will work in a GitHub README.
- Use an animated GIF/WebP only when motion makes the feature clearer and file size remains reasonable. Supply an accessible static alternative or nearby textual explanation, avoid rapid flashing, and never let animation be the sole way to understand a feature.
- Keep visual assets in a predictable repository location such as `docs/assets/` or `assets/`. Prefer repository-relative paths for committed images. Do not hotlink transient screenshots, copy copyrighted art without permission, or imply a demo exists when it does not.
- For light/dark-specific assets, GitHub supports `<picture>` with `prefers-color-scheme` sources and a fallback `<img alt="...">`; use this only when both variants really exist and test both themes.

## 3. Badges: meaningful signals, not decoration

A badge must either answer a visitor's question or lead somewhere useful. Typically use **3–6 badges** in one row, fewer for small or early projects. Choose from relevant categories:

| Category | Only when true and useful | Link destination |
| --- | --- | --- |
| Build/tests | A real, configured CI workflow runs | The workflow or checks page |
| Release/version | Published versions or releases exist | Releases or package registry |
| License | The actual `LICENSE` establishes it | The license file |
| Package/registry | A real published package or image exists | The actual package page |
| Documentation | Usable docs exist | Documentation |
| Support/community | A real discussion/support channel exists | That channel |
| Compatibility | Supported platform/version is confirmed | Relevant compatibility docs |

Badges should share a restrained style and be legible in both GitHub themes. Use descriptive badge alt text such as `CI: passing` rather than `badge`. Dynamic badges must resolve to the correct repository, workflow, package, and branch. Check that third-party badge services are acceptable for the repository's availability/privacy goals; prefer simple static labels or omit the badge if they are not. Avoid vanity metrics, duplicate badges, excessive bright colors, visitor counters, stale "passing" images, and fabricated security or production-ready seals. If CI is failing, do not hide or misrepresent it.

A decorative "Built with X" badge may be appropriate when the technology is genuinely important to users, but do not turn the header into a wall of logos. Place long technology inventories farther down.

## 4. Visual language and layout rules

- **Hierarchy:** one H1; use H2 for major sections and H3 for subsections. Do not skip heading levels solely to change font size. Make headings descriptive and unique.
- **Scanability:** lead paragraphs with the conclusion, keep paragraphs short, and use bullets for parallel features or requirements. Prefer short, meaningful headings to wordplay.
- **Spacing:** separate sections with whitespace; use horizontal rules sparingly. Do not create large blank gaps with repeated `<br>` tags.
- **Alignment:** a centered identity block can create a polished cover, but keep substantive instructions left-aligned. Use standard Markdown wherever possible; minimal GitHub-compatible HTML is acceptable for centering or responsive images. Do not rely on CSS, scripts, unsupported embeds, or elaborate nested HTML tables for layout.
- **Color:** inherit GitHub's theme for body text. Do not hard-code text colors that disappear in dark mode. Limit colored decorations to purposeful visual assets and badges.
- **Emojis:** use selectively, usually no more than one per chosen major heading or CTA, and only when it helps scanning (for example, `🚀 Quick start` or `📸 Screenshots`). A fully emoji-free professional README is also valid. Be consistent; never use emoji instead of words, status text, or alt text.
- **Typography:** favor ordinary Markdown typography, code formatting for commands/paths, and restrained bold for actions. Do not use all-caps headings, ASCII-art logos, ornate Unicode fonts, or text rendered only inside images.
- **Tables:** use for genuine comparisons, configuration references, or a compact feature matrix; avoid very wide tables that break on phones. Use prose or lists for narrative explanations.
- **Navigation:** GitHub already provides an outline from headings; add a small manual table of contents only for a genuinely long README. Check every anchor if you include one.
- **Length:** keep the README focused on understanding and first use. Link advanced configuration, API details, architecture, and exhaustive troubleshooting to maintained documentation when available.

### Reader-first writing

Write in an informative, confident, technically precise voice. Demonstrate value with specific actions, not adjectives. Explain acronyms on first mention if the audience may not know them. Be candid about beta status, incomplete features, paid dependencies, network requirements, platform restrictions, and data handling. Acknowledge limitations without burying the primary value proposition.

## 5. Recommended content architecture

The hero stays first. Select and order the remaining sections by *what the visitor needs next*:

| Section | Purpose | Guidance |
| --- | --- | --- |
| Overview / Why it exists | Define the problem and outcome | 1–3 short paragraphs, or omit if the tagline and example already suffice |
| Features | Explain concrete capabilities | 3–7 specific, benefit-led bullets; avoid a laundry list |
| Quick start | Reach a first working result | Put early; make instructions copy-pasteable and verified |
| Usage / Examples | Show input → action → output | One representative example; include realistic output when verified |
| Screenshots / Demo | Show secondary workflows | Reuse accurate assets, or capture them from the real running project when missing; hero remains above |
| How it works / Architecture | Explain structure and trade-offs | Small diagram or short explanation; link deep docs |
| Configuration | Show common settings | Include defaults, requirements, examples, and secret handling |
| Requirements / Compatibility | Prevent setup surprises | OS, hardware, runtime, GPU, browser, service versions, etc., as applicable |
| Security / Privacy | Explain material trust boundaries | Link `SECURITY.md`; disclose verified relevant risks and data flows |
| Troubleshooting / FAQ | Resolve frequent first-run issues | Address real issues; avoid speculative FAQs |
| Roadmap / Status | Clarify maturity and future work | Include only maintained, evidence-based plans; separate shipped from planned |
| Documentation / Support | Guide continued learning | Link verified docs, issues/discussions, support instructions |
| Contributing | Invite useful contributions | Summarize path and link actual `CONTRIBUTING.md` if present |
| Credits / Acknowledgments | Attribute meaningful work | Name contributors and third-party projects accurately |
| License | Explain reuse terms | State only the license actually present, linked to its file |

Do not create every section by default. For a library, prioritize installation, API example, compatibility, and docs. For a CLI, show actual commands and output. For a GUI, lead with screenshots and a short install/use path. For a self-hosted service, surface required ports, persistent storage, secrets, authentication, and startup. For hardware, include revision, assembly and safety notices, BOM/design-file links, and validation status **only when verified**. For research, identify reproducibility steps, dataset restrictions, methodology, and citation information where relevant.

### Quick start: the conversion point

Quick start must let a visitor accomplish one observable result with the fewest necessary steps:

1. State prerequisites precisely, including versions and hardware only when confirmed.
2. Provide the simplest supported installation path for the intended audience. A container example is good only when the project really supplies and supports one.
3. Show configuration with safe placeholders and a sample file if necessary. Never paste real tokens, passwords, API keys, private URLs, or secret-bearing command histories.
4. Provide complete, correctly ordered, copy-pasteable commands in language-tagged fenced blocks. Use the repository's actual package names, image tags, paths, flags, and entry points.
5. Show a small verified command, HTTP request, UI destination, or expected output so the user can tell it worked. Label illustrative output if it is not a verbatim tested result.
6. State the next useful step and link to advanced setup. Note meaningful costs, downloads, privilege requirements, or outbound connections *before* the command that triggers them.

Avoid `curl | sh` as the unquestioned default; if the project uses it, describe what it does and give an inspectable alternative where feasible. Do not claim installation or tests succeeded unless you actually ran them and observed the result. A doc example that requires privileged operations should state that clearly.

### Features and examples

Each feature should say what a person can *do* and, where relevant, why it helps. Prefer a compact feature table only if it improves scanning. For screenshots, attach each visual to a named workflow. For CLI output, use text instead of a screenshot so users can copy it and assistive technology can read it.

## 6. Credibility, stewardship, and conversion

- Include actionable, descriptive links, not a row of unexplained icons or "click here" links. A tiny "Quick start · Documentation · Report an issue" navigation row often suffices.
- Cite or link benchmark methodology and environment when quoting speed, accuracy, memory usage, cost, or hardware performance. Avoid unqualified comparisons and claimed endorsements.
- Distinguish implemented, experimental, and planned features. Mark deprecated or archived projects prominently and accurately.
- Link to releases, changelog, docs, package registries, source, and issue tracker only when they exist. Prefer stable URLs and repository-relative paths for internal files.
- Keep `Credits` factual: significant contributors, upstream libraries, inspirations, asset creators, and required notices. Follow upstream licenses and attribution requirements. Do not imply endorsement by third parties.
- In `License`, link the repository's **actual** license. Use MIT by default for a new or legitimately owner-controlled unlicensed project, subject to existing rights and any contrary instructions; follow the license workflow in section 7. Public GitHub code is not automatically open source, and a badge must never claim a license before its file exists.
- Create missing `CONTRIBUTING.md`, `SECURITY.md`, and `CODE_OF_CONDUCT.md` as part of this skill and audit/improve existing versions against section 7. Never invent a maintainer contact, private reporting channel, copyright ownership, supported release, or policy enforcement commitment.
- Use a single primary CTA appropriate to the project, not repeated demands to star, subscribe, or sponsor. If inviting stars, place it unobtrusively after the actual value and instructions.

## 7. Repository stewardship and authentic screenshot production

These are **required companion tasks**, not optional README decorations. Do them when creating or substantially improving a project README, subject to the access, ownership, and safety constraints below. Work in the actual repository when available; otherwise provide complete, ready-to-place files when factual inputs are verifiable. Keep changes targeted and review existing documents before editing.

### 7.1 License: MIT unless instructed otherwise

1. Search for `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `NOTICE`, SPDX headers, package-manifest license fields, and relevant upstream, vendored, or asset licenses. Identify who owns the code and whether you have authority to license it.
2. **Default to the standard MIT License** for a new project or an unlicensed project the requesting owner is authorized to license, unless the user specifies another license or existing rights/obligations require different treatment. Create a root `LICENSE` using the unmodified canonical MIT text, a verified copyright holder, and the correct year; never invent or silently substitute a person, company, or date. See https://choosealicense.com/licenses/mit/.
3. **Preserve a valid existing non-MIT license** as an explicit existing project constraint; do not automatically relicense, replace, or remove it. If a user specifically requests a change, first confirm the necessary rights and address third-party contributions and compatibility. An inconsistent or unclear license is a material blocker to resolve, not a reason to slap an MIT badge on the README.
4. Review an existing MIT license for complete canonical text, correct copyright notice, and consistency with package metadata, source headers, README, and third-party notices. Correct demonstrable clerical errors within authorized scope; flag uncertain ownership or conflicting metadata rather than guessing. Do not represent third-party assets or vendored components as MIT merely because the project's own code uses MIT.
5. Add or correct the README license line and badge **only after** the effective repository license is established. Do not present the `license: MIT` metadata at the top of *this skill file* as proof that a target project uses MIT.

### 7.2 Community health: create missing files; audit existing ones

Check the repository root, `.github/`, and `docs/` before creating duplicates; where accessible, check account-level community defaults too. GitHub prioritizes `.github/`, then root, then `docs/` for supported community files. Prefer an existing established location, or root for new standalone files. Explicit, useful repo-specific files are preferable to a duplicated or misleading boilerplate policy. Follow GitHub's community guidance: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file.

- **`CONTRIBUTING.md`:** If missing, create a project-specific guide with prerequisites, actual local setup commands, tests/lint/build commands that exist, how to propose issues and PRs, expected issue/PR information, coding/documentation conventions when verifiable, and links to security and conduct policies. If present, inspect it for obsolete commands, broken paths, contradictory requirements, inaccessible contribution channels, and unsupported promises; update only verified details. Make the first contribution realistically achievable. Source: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors.
- **`SECURITY.md`:** If missing, create an actionable policy identifying actually supported release lines (or accurately describe the support status), **one verified private vulnerability-reporting route**, what report details are helpful, and a coordinated-disclosure request. Prefer the repository's private vulnerability reporting path **only if verified enabled**, or an existing confirmed private maintainer contact. A public issue tracker is *not* a private reporting route. If neither private route nor maintainer authorization is available, do not invent an email, pretend a private form is enabled, or publish an unusable policy as complete; prepare the verifiable portions, flag the exact missing reporting route for the maintainer, and disclose that the file needs completion. Do not invent response-time SLAs, bounty promises, supported versions, or guaranteed remediation dates. If present, verify links, contact ownership, reported version ranges, and compatibility with actual security features. Source: https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/add-security-policy.
- **`CODE_OF_CONDUCT.md`:** If missing, adopt a suitable established code such as Contributor Covenant **3.0** when appropriate, retaining required attribution and license notices and completing project-specific scope, reporting, and realistic enforcement information; the community owner must be willing and able to enforce it. An existing substantive code of conduct may be equally appropriate: audit it for clear behavior expectations, scope, actual confidential reporting path, enforcement responsibility, and attribution. Do not erase a community's chosen policy just to force a different template, or copy a template with `[INSERT CONTACT]`/`[NOTE]` unresolved. When reporting/enforcement contacts are unknown, flag the blocker rather than fabricating one. Source: https://www.contributor-covenant.org/version/3/0/code_of_conduct/ and https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project.

Keep security reporting separate from conduct reporting if the project uses distinct channels; do not assume a GitHub private vulnerability report is an appropriate harassment-reporting mechanism. Never overwrite maintainer-approved commitments or introduce new legal/operational obligations without verifying them. Ensure the README links to the *actual files* using working relative paths, with concise contributing, security-reporting, conduct, and licensing references where useful.

### 7.3 Screenshots: generate authentic captures when none exist

**Default action:** If the project has a visual interface and there is no accurate, usable screenshot, **run the real project and capture screenshots from its live interface.** Do not quietly skip the visual requirement or substitute an AI-generated mockup, stock photo, browser drawing, or invented UI presented as real product evidence.

1. **Find the genuine launch path.** Inspect supported `docker compose`, dev-server, binary, CLI, browser-extension, hardware-viewer, or test/demo instructions. Check whether an already-running local instance is available. Obtain access only through authorized local services or existing approved credentials. Avoid touching unrelated users' accounts or production data.
2. **Use a safe, reproducible demo environment.** Prefer documented demo data, local fixtures, disposable containers, or a clean test profile with **real project code**. Non-sensitive synthetic *input data* is acceptable when clearly representative; a fabricated *application interface* is not. Record setup and environment details needed to repeat the capture. Do not change product code or conceal known defects solely for the picture.
3. **Capture actual rendered output.** Use available screenshot-capable browser automation (e.g., Playwright with Chromium), a desktop capture tool, or the application's own screenshot feature. Navigate to the meaningful workflow; wait for relevant UI to finish rendering and animations/loading spinners to settle; select a realistic viewport and capture a legible image. For a CLI/TUI, prefer a copyable text example, and optionally capture a genuine terminal session if its appearance is important. For a backend/API without a genuine visual UI, use verified request/response text or a truthful architecture diagram instead of inventing a dashboard. For physical hardware, take genuine photos or use documented actual test output, never synthetic product photos masquerading as originals.
4. **Protect privacy before capture.** Prefer demo accounts and redacted source data; inspect the entire frame for secrets, tokens, passwords, customer information, private URLs/IPs, usernames, browser bookmarks, personal files, notifications, and machine identifiers. Remove sensitive information in the underlying demo environment wherever possible; do not rely exclusively on post-capture blur. Do not publish an image that exposes credentials, personally identifying details, confidential data, or unsupported functionality.
5. **Produce usable media.** Commit optimized PNG/WebP (or an appropriate genuine photo format) into a predictable path such as `docs/assets/`; use descriptive names, honest captions, alt text, and repository-relative references. Pick a compelling primary screenshot for the hero **immediately below badges/title**, and put secondary captures near the features they demonstrate. Crop extraneous browser chrome without manipulating the product's appearance or misrepresenting what it does; check mobile legibility, light/dark compatibility, and file size.
6. **Demo video when feasible and useful:** A short recording of the *real* workflow may supplement screenshots. Use a stable linked poster or thumbnail and accessible descriptive text; avoid fabricated interactions, autoplay assumptions, unlicensed audio, or enormous files committed to git. Do not require a video to complete a project that is well demonstrated with screenshots.
7. **Verify and disclose limitations.** Open each produced asset and confirm that it depicts the running project's real state; verify the README renders it correctly. If the application cannot run safely, needed credentials/hardware are unavailable, or capture tooling is missing, do **not** claim a screenshot was created. State precisely what was tried or blocked; use an honest text-based proof in the README, and identify screenshot capture as outstanding rather than shipping a fake or broken asset.

## 8. GitHub implementation constraints

- Deliver a real `README.md` in GitHub Flavored Markdown, preferably at repository root unless the repository's existing conventions require otherwise. Be aware that GitHub gives `.github/README.md` display precedence over root `README.md`; check for conflicting copies rather than assuming the root file will be shown.
- Use relative repository links and media paths where possible. From a root README, an image might be `docs/assets/demo.png` and contributing docs might be `CONTRIBUTING.md`.
- Every image needs useful alt text; if an image is purely decorative and its information is repeated in adjacent text, use appropriate empty alt text where supported. Every video needs a text label and short description or transcript link when available.
- A linked screenshot or poster is the default video treatment. Do not assume GitHub will render raw `<video>`, iframes, autoplay, custom CSS, or JavaScript inside a README.
- Avoid untrusted external image dependencies when an owned, licensed, committed asset will do. Compress media sensibly, check mobile legibility, and avoid giant binaries in git history; consider a stable external demo host for large videos.
- Never place essential instructions inside `<details>`; reserve collapsible sections for optional long output or advanced examples. Do not hide essential accessibility, security, or compatibility information.
- Use language identifiers on fenced code blocks (`bash`, `python`, `json`, `yaml`, etc.). Keep command and output blocks separate when that distinction matters.
- The README is not the whole documentation website. GitHub truncates displayed README content beyond its documented limit; move expansive reference content to separate files rather than relying on a giant landing page.

## 9. Execution workflow

### Phase A — Audit

Read relevant source files and record confirmed facts: actual product behavior, supported setup path, badges, logo/screenshots/video availability, docs/support links, effective license, rights/ownership, community files and reporting channels, and existing attribution. If this is a redesign, preserve vital existing information and working links.

### Phase B — Outline

Choose one primary audience and CTA, then sketch the hero: identity → tagline → badges → hero proof → navigation. Order only the sections that the repo warrants; bring Quick start near the top.

### Phase C — Compose

Write concise, distinct copy. Favor actual examples over claims. Apply section 7: create or audit the license and three community files; use existing trustworthy visuals or launch the actual project and capture missing screenshots. This skill authorizes routine local capture in a safe, permitted environment, **not** access to production accounts or arbitrary third-party services. Never generate a fake product screenshot and present it as real functionality. If capture is genuinely blocked, substitute an honest example, flag the missing screenshot, and never insert a broken-image placeholder.

### Phase D — Validate

Before delivering, run every check feasible in the available environment:

- Confirm there is exactly one meaningful H1, readable H2/H3 structure, a clear first-screen value proposition, and the media is placed directly after badges/title.
- Confirm every badge truthfully represents the actual repo, uses meaningful alt text, and links to a real destination when it purports to be clickable.
- Verify repository-relative paths, image existence, URLs if online access exists, link anchors, file casing, and video destination. Confirm newly captured assets show the actual live project and contain no sensitive data. Ensure no placeholder images, dummy links, or `YOUR_ORG` text remain in the finished README.
- Preview GitHub rendering when possible, including mobile/narrow layout and both light and dark themes; verify image proportions and code block scrolling. If a true GitHub preview is unavailable, say so instead of claiming it was checked.
- Run or otherwise substantiate the Quick start in a safe, permitted environment; check command order, versions, expected results, and destructive effects. If it cannot be run, say "not executed" in the delivery summary.
- Check for secrets, accidental personal information, unlicensed assets, false badges, broken badges, misleading claims, and unsupported compatibility guarantees.
- Confirm the effective license is correct and the README/license badge/package metadata do not conflict. Confirm `CONTRIBUTING.md`, `SECURITY.md`, and `CODE_OF_CONDUCT.md` exist in supported locations and are complete and actionable, or explicitly disclose any blocked contact/ownership facts; recheck existing security warnings, contributor/license obligations, and essential docs links.
- Inspect the diff; only change the README, authorized supporting media, and the license/community files specified by this skill. Do not silently modify source code, CI, or unrelated project files, or relicense existing work. Do not replace the existing README wholesale if doing so would lose material information.

### Phase E — Deliver

Produce the finished, ready-to-commit `README.md`, a verified or newly captured hero screenshot when feasible, and the reviewed/created `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, and `CODE_OF_CONDUCT.md` as applicable. Summarize which files were created, updated, preserved, or blocked, and whether screenshots were captured from a running project. Identify material unverified items (including an unconfirmed private reporting route, links not checked, or a Quick start that could not be executed). Do not ship a skeleton full of placeholders as a completed deliverable. If direct repository write access is unavailable, provide the complete verifiable files and explain where to place them; never claim they were committed.

## 10. Reusable layout blueprint (adapt; do not publish placeholders)

This is **structure, not final copy**. Omit nonexistent media/badges/sections and substitute real verified repository facts. In a real README, include exactly one H1.

````markdown
# Project Name

One sentence describing the specific outcome for a specific audience.

[Build badge linked to real CI] [Release badge linked to real releases] [License badge linked to LICENSE]

[Large real screenshot, or a linked demo poster with meaningful alt text]

**[Quick start](#quick-start) · [Documentation](docs/) · [Demo](real-demo-url)**

## Why this exists

The real problem and the practical outcome, in two or three sentences.

## Features

- **Actual capability:** What users can accomplish.
- **Actual capability:** Why this behavior matters.

## 🚀 Quick start

Prerequisites: confirmed requirements.

```bash
# Verified commands from this repository.
```

Verify the result with a documented action and expected behavior.

## Usage

A realistic example, with its verified result.

## Documentation and support

Links to existing resources.

## Contributing

How to contribute; link to the actual contributing guide when available.

## Credits

Accurate acknowledgments and required upstream attribution.

## License

The real license, linked to the actual license file.
````

## 11. Final quality gate

A README is ready only when a first-time visitor can answer all of these without searching the codebase:

1. What does the project do, and who is it for?
2. What proof of the actual product can I see immediately?
3. Are the prominent badges genuine and useful?
4. What do I need, and how do I get one real result?
5. Where are deeper docs, help, contribution instructions, and limitations?
6. Who deserves credit, and what are the actual reuse terms? Is MIT correctly applied by default where the owner has the right to apply it, or is an existing/directed license accurately preserved?
7. Are `CONTRIBUTING.md`, `SECURITY.md`, and `CODE_OF_CONDUCT.md` present, accurate, and actionable, with real reporting contacts and appropriate attribution?
8. If visuals were missing, did we attempt live-project screenshot capture, verify the resulting image, and explain any genuine blockers?
9. Does the page still work without animations, remote badge services, or a wide desktop screen?

**Reject polish that reduces truthfulness, accessibility, security, or first-run success.**

## Maintainer references

- GitHub: [About repository READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- GitHub: [Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- GitHub: [Quickstart for writing on GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github)
- GitHub: [Community profile standards](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories)
- OpenCode: [Agent Skills](https://opencode.ai/docs/skills)
