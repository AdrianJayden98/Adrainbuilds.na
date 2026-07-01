# AI Developer Prompt: About Page
## For Cursor, GitHub Copilot, or similar AI coding agents

---

## ROLE DEFINITION

You are a **Frontend Developer & UI Engineer** specializing in:
- Semantic, accessible HTML
- Modern CSS (Flexbox, Grid, custom properties)
- Clean, conversion-focused UI components
- Performance-first development
- Responsive design with mobile-first approach

You write **production-ready code** — not prototypes. Every line must be intentional, commented where logic is non-obvious, and follow modern best practices.

---

## PROJECT CONTEXT

**Client:** Adrian M. — Freelance Web Developer based in Windhoek, Namibia.
**Positioning:** "Friendly & approachable local dev" serving Namibian SMEs.
**Brand:** Personal brand (not agency). Warm, grounded, cinematic.
**Tech stack:** Static HTML/CSS/JS. Multi-page static site (Option A).
**Current state:** Homepage, Contact, Services, and Work pages are built. Shared CSS in `css/styles.css`, shared JS in `js/main.js`. This is the fifth and final page.

**Content available:**
- Hero cutout image (reused — Adrian looking at camera, transparent background)
- Goldstone Software Engineering Institute (academic background)
- Location: Windhoek, Namibia
- Capacity: 1–2 projects at a time, 3–4 hours/day
- Target market: Namibian SMEs
- Positioning: Friendly & approachable, not premium agency

**Why this page exists:** The homepage had a brief "About Snippet" that was removed. This page tells the full story — who Adrian is, why he does this work, and why Namibian SMEs should trust him. It's not a resume. It's a conversation.

---

## TASK

Build an **About page** (`about.html`) that humanizes Adrian's brand and deepens trust. The tone is warm, personal, and confident — not corporate, not self-congratulatory. A Namibian SME owner should finish this page thinking, "This person gets it."

---

## FILE STRUCTURE

```
/
├── index.html
├── contact.html
├── services.html
├── work.html
├── about.html            (this file)
├── css/
│   └── styles.css        (shared — link this)
├── js/
│   └── main.js           (shared — link this)
└── images/
    ├── hero-cutout.png     (reused)
    └── desert-namibia.jpeg
```

---

## PAGE STRUCTURE

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>About — Adrian M. | Freelance Web Developer | Windhoek, Namibia</title>
  <meta name="description" content="Meet Adrian M., freelance web developer in Windhoek. Building websites that help Namibian SMEs grow.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>

  <!-- NAVIGATION -->
  <nav class="site-nav">...</nav>

  <!-- PAGE HEADER -->
  <header class="page-header">...</header>

  <!-- INTRO: IMAGE + STORY -->
  <section class="about-intro" aria-label="About Adrian">...</section>

  <!-- WHY I DO THIS -->
  <section class="about-why" aria-label="Why I do this work">...</section>

  <!-- HOW I WORK -->
  <section class="about-approach" aria-label="My approach">...</section>

  <!-- CREDENTIALS -->
  <section class="about-credentials" aria-label="Background and education">...</section>

  <!-- PERSONAL -->
  <section class="about-personal" aria-label="Beyond work">...</section>

  <!-- FINAL CTA -->
  <section class="final-cta-section" aria-label="Get in touch">...</section>

  <!-- FOOTER -->
  <footer class="footer-section">...</footer>

  <script src="js/main.js"></script>
</body>
</html>
```

---

## 1. NAVIGATION

Reuse the same nav component. About link highlighted in `#795238`.

**"Get Started" button:** Links to `/contact`.

---

## 2. PAGE HEADER

```css
.page-header {
  background-color: #242323;
  padding: 140px 20px 60px;
  text-align: center;
}
```

**Content:**
```
Heading:    About
Subheading: The person behind the websites.
```

| Element | Font | Weight | Size | Color |
|---------|------|--------|------|-------|
| Heading | Syne | 700 | 48px | `#AEA7A3` |
| Subheading | DM Sans | 400 | 18px | `#959595` |

**On mobile:** heading 36px, subheading 16px.

---

## 3. INTRO: IMAGE + STORY

### Section Container

```css
.about-intro {
  background-color: #242323;
  padding: 40px 20px 80px;
}

.about-intro-container {
  max-width: 1000px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
  align-items: center;
}
```

### Image (Reused from Hero)

```css
.about-intro-image {
  position: relative;
}

.about-intro-image img {
  width: 100%;
  max-width: 400px;
  height: auto;
  display: block;
  margin: 0 auto;
  filter: drop-shadow(0 20px 60px rgba(0, 0, 0, 0.4));
}
```

**Rules:**
- Reuse the **same cutout image** as the hero — `hero-cutout.png`
- Different treatment: smaller scale (~400px max), centered, no text overlap
- The image feels more "portrait" here, less "monumental" than the hero
- Alt text: "Adrian M., freelance web developer in Windhoek, Namibia"

### Text Block

```css
.about-intro-text {
  max-width: 480px;
}

.about-intro-text p {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 16px;
  color: #959595;
  line-height: 1.7;
  margin-bottom: 20px;
}

.about-intro-text p:first-child::first-letter {
  font-family: 'Syne', sans-serif;
  font-weight: 800;
  font-size: 48px;
  float: left;
  line-height: 1;
  padding-right: 12px;
  color: #795238;
}
```

**Content:**
```
I'm Adrian — a web developer based in Windhoek, Namibia. I build websites for small and medium businesses who know they need a proper online presence but don't have the time or team to make it happen.

Before I started freelancing, I studied software engineering at Goldstone Software Engineering Institute. That gave me the technical foundation. But what I really learned was that most businesses don't need fancy technology — they need something that works, something their customers can actually use, and something that doesn't break the bank.

That's what I focus on. Clean, fast, reliable websites that help Namibian businesses get found, get trusted, and get customers.
```

**Rules:**
- First paragraph has a drop cap "I" in warm brown — editorial touch
- "Don't have the time or team" — acknowledges SME reality
- "Doesn't break the bank" — price sensitivity addressed
- Plain language throughout — no "leveraging synergies"

**On mobile:** Stack vertically, image on top, text below. Drop cap removed or reduced.

---

## 4. WHY I DO THIS

### Section Container

```css
.about-why {
  background-color: #2E2E2E;
  padding: 80px 20px;
}

.about-why-container {
  max-width: 700px;
  margin: 0 auto;
  text-align: center;
}
```

### Content

```
Heading:    Why Namibian SMEs?
Body:       I grew up here. I know how Namibian businesses operate — tight budgets, small teams, and the constant pressure to look professional while staying lean. I've seen friends and family struggle with websites that cost too much, took too long, or broke the moment they needed an update.

            I also know that a good website is one of the highest-ROI investments a small business can make. It works 24/7. It doesn't call in sick. And when it's done right, it brings in customers while you sleep.

            That's why I keep my process simple, my pricing transparent, and my focus on what actually moves the needle for your business.
```

```css
.about-why-heading {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 28px;
  color: #AEA7A3;
  margin-bottom: 24px;
}

.about-why-body {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 16px;
  color: #959595;
  line-height: 1.7;
}

.about-why-body p {
  margin-bottom: 16px;
}
```

**Rules:**
- "I grew up here" — local credibility, not just "I work here"
- "Tight budgets, small teams" — shows he understands the market
- "Friends and family struggle" — personal stake, not just business
- "Brings in customers while you sleep" — business outcome
- "What actually moves the needle" — focuses on results, not features

---

## 5. HOW I WORK

### Section Container

```css
.about-approach {
  background-color: #242323;
  padding: 80px 20px;
}

.about-approach-container {
  max-width: 1000px;
  margin: 0 auto;
}
```

### Section Heading

```
Heading:    How I Work
Subheading: Small scale. Real attention. No assembly line.
```

```css
.about-approach-heading {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 28px;
  color: #AEA7A3;
  text-align: center;
  margin-bottom: 8px;
}

.about-approach-subheading {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 16px;
  color: #959595;
  text-align: center;
  margin-bottom: 48px;
}
```

### 3 Principles (Cards)

```css
.about-principles-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.about-principle-card {
  background-color: #363636;
  border: 1px solid #4A4A4A;
  border-radius: 16px;
  padding: 32px;
}

.about-principle-number {
  font-family: 'Syne', sans-serif;
  font-weight: 800;
  font-size: 14px;
  color: #795238;
  letter-spacing: 2px;
  margin-bottom: 12px;
}

.about-principle-title {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 20px;
  color: #AEA7A3;
  margin-bottom: 12px;
}

.about-principle-desc {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 15px;
  color: #959595;
  line-height: 1.6;
}
```

**Principles:**

| # | Title | Description |
|---|-------|-------------|
| 01 | **I Take on 1–2 Projects at a Time** | This isn't a factory. When I work with you, you have my full attention. I don't juggle ten clients and hope nobody notices. |
| 02 | **I Explain Things in Plain Language** | No jargon, no "synergy," no making you feel stupid for asking questions. If you don't understand something, I haven't explained it well enough. |
| 03 | **I Build It to Last** | No shortcuts that break in three months. No plugins that stop updating. I write clean code that the next developer can pick up — even if that's not me. |

**Rules:**
- "This isn't a factory" — direct, anti-agency positioning
- "No making you feel stupid" — addresses a real fear
- "Even if that's not me" — honest about freelancer turnover, builds trust
- Numbers are 01, 02, 03 — consistent with Process section

**On mobile:** Stack vertically.

---

## 6. CREDENTIALS

### Section Container

```css
.about-credentials {
  background-color: #2E2E2E;
  padding: 80px 20px;
}

.about-credentials-container {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}
```

### Content

```
Heading:    Background
```

```css
.about-credentials-heading {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 28px;
  color: #AEA7A3;
  margin-bottom: 32px;
}
```

### Credential Items (Horizontal Row)

```css
.about-credentials-row {
  display: flex;
  justify-content: center;
  gap: 48px;
  flex-wrap: wrap;
}

.about-credential {
  text-align: center;
  max-width: 200px;
}

.about-credential-label {
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  color: #525254;
  margin-bottom: 8px;
}

.about-credential-value {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 18px;
  color: #AEA7A3;
}
```

**Credentials:**

| Label | Value |
|-------|-------|
| Education | Goldstone Software Engineering Institute |
| Based In | Windhoek, Namibia |
| Working With | Namibian SMEs |
| Capacity | 1–2 Projects at a Time |

**Rules:**
- No years of experience (don't have enough to claim)
- No "certified expert" badges
- No tech stack logos (React, Node, etc.) — not a CV
- Simple, honest facts

---

## 7. PERSONAL

### Section Container

```css
.about-personal {
  background-color: #242323;
  padding: 80px 20px;
}

.about-personal-container {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
}
```

### Content

```
Heading:    Beyond the Screen
Body:       When I'm not building websites, I'm usually exploring Windhoek's coffee spots, catching up on tech podcasts, or figuring out how to make my next project load even faster. I believe good work comes from a clear head — so I take weekends seriously and don't do all-nighters.

            If you've read this far, we should probably talk.
```

```css
.about-personal-heading {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 28px;
  color: #AEA7A3;
  margin-bottom: 24px;
}

.about-personal-body {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 16px;
  color: #959595;
  line-height: 1.7;
}

.about-personal-body p {
  margin-bottom: 16px;
}
```

**Rules:**
- "Coffee spots, tech podcasts" — human, relatable
- "Don't do all-nighters" — healthy boundaries, implies sustainable work
- "If you've read this far, we should probably talk" — natural CTA, not pushy

---

## 8. FINAL CTA

Reuse the same Final CTA section pattern — adapted for About page context.

```css
.final-cta-section {
  background-color: #242323;
  padding: 100px 20px;
  text-align: center;
}
```

**Content:**
```
Heading:    Sound Like a Fit?
Subheading: I'd love to hear about what you're building.
CTA:        [Get a Free Quote →]
Link:       /contact
```

---

## 9. FOOTER

Reuse the exact same footer from `index.html`. Copy it over.

**Ensure footer nav links:**
- Home → `/`
- Services → `/services`
- Work → `/work`
- About → `/about`

---

## SHARED CSS UPDATES

Add these new rules to `css/styles.css`:

```css
/* ========================================
   ABOUT PAGE STYLES
   ======================================== */

/* Intro */
.about-intro { ... }
.about-intro-container { ... }
.about-intro-image { ... }
.about-intro-text { ... }
.about-intro-text p:first-child::first-letter { ... }

/* Why */
.about-why { ... }
.about-why-heading { ... }
.about-why-body { ... }

/* Approach */
.about-approach { ... }
.about-approach-heading { ... }
.about-principles-grid { ... }
.about-principle-card { ... }

/* Credentials */
.about-credentials { ... }
.about-credentials-row { ... }
.about-credential { ... }

/* Personal */
.about-personal { ... }
.about-personal-heading { ... }
```

---

## SHARED JS UPDATES

No new JS needed for this page. All interactions are hover states and links.

---

## RESPONSIVE BREAKPOINTS

| Breakpoint | Adjustments |
|------------|-------------|
| ≥1024px | Intro: 2 columns, principles 3 columns, credentials horizontal |
| 768–1023px | Intro: 2 columns (smaller gap), principles 3 columns, credentials wrap |
| <768px | Intro: stacked (image top), principles stacked, credentials stacked, drop cap removed or reduced |

---

## ACCESSIBILITY

- Semantic HTML:
  - `<main>` wrapping primary content
  - `<section>` with `aria-label` for each block
- Heading hierarchy:
  - `<h1>`: "About" in page header
  - `<h2>`: "Why Namibian SMEs?", "How I Work", "Background", "Beyond the Screen"
- Image alt text: "Adrian M., freelance web developer in Windhoek, Namibia"
- Color contrast: All existing brand colors pass WCAG AA

---

## PERFORMANCE

- Image: Reused hero cutout — no additional download
- No external libraries
- Target: Lighthouse Performance ≥90

---

## NO-GO LIST

- [ ] No "My Skills" section with progress bars or percentages
- [ ] No tech stack grid (React, Node, WordPress logos)
- [ ] No downloadable resume or CV
- [ ] No timeline of jobs or career history
- [ ] No testimonial quotes (those belong on Work page)
- [ ] No social media feed embed
- [ ] No glossy effects, glassmorphism, or blur

---

## DELIVERABLE

1. New `about.html` file with complete page structure
2. Updated `css/styles.css` with about page styles added
3. Nav links pointing to correct pages
4. Footer copied from homepage with correct links
5. All CTAs link to `/contact`
6. No console errors
7. Responsive at all breakpoints

---

## VERIFICATION CHECKLIST

- [ ] Page title: "About — Adrian M. | Freelance Web Developer | Windhoek, Namibia"
- [ ] Meta description present
- [ ] Nav fixed at top, About link highlighted, "Get Started" button links to `/contact`
- [ ] Page header: "About" + "The person behind the websites.", centered
- [ ] Intro section: 2 columns on desktop, image left, text right
- [ ] Image is reused hero cutout, smaller scale (~400px), centered, no text overlap
- [ ] Drop cap "I" in warm brown on first paragraph
- [ ] Intro text: 3 paragraphs, plain language, personal story
- [ ] "Why Namibian SMEs?" section: centered, 2 paragraphs, emotional + rational
- [ ] "How I Work" section: 3 principle cards, 01–03 numbered, warm brown numbers
- [ ] Cards: "1–2 Projects", "Plain Language", "Build It to Last"
- [ ] Credentials: 4 items horizontal, simple labels + values, no years/exp
- [ ] "Beyond the Screen" section: centered, personal details, "don't do all-nighters"
- [ ] Final CTA: "Sound Like a Fit?" adapted for about context
- [ ] Footer copied, nav links correct
- [ ] Responsive: intro stacks, principles stack, credentials stack on mobile
- [ ] Lighthouse Accessibility ≥95, Performance ≥90

---

*Prompt version 1.0 — About page for multi-page site*
