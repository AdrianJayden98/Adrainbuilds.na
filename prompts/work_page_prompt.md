# AI Developer Prompt: Work Page
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
**Current state:** Homepage, Contact page, and Services page are built. Shared CSS in `css/styles.css`, shared JS in `js/main.js`. This is the fourth page.

**Content available:**
- TMU Cash Loan case study: before/after screenshots, 893+ inquiries since launch, WhatsApp integration, AI chatbot, loan calculator
- Live site: `https://www.tmucapital.com/`
- No other completed projects yet — this is a 1-project portfolio with space for future work

**Why this page exists:** Homepage teases work with "See All Work →". This page delivers the full proof. Even with one project, a detailed case study builds more trust than a grid of 6 mediocre thumbnails.

---

## TASK

Build a **Work page** (`work.html`) that showcases Adrian's portfolio. Currently centered on one strong case study (TMU Cash Loan) with placeholder space for future projects. The page must feel substantial and convincing — not apologetic about having only one project.

---

## FILE STRUCTURE

```
/
├── index.html
├── contact.html
├── services.html
├── work.html             (this file)
├── about.html            (future)
├── css/
│   └── styles.css        (shared — link this)
├── js/
│   └── main.js           (shared — link this)
└── images/
    ├── TMU-before.png
    ├── TMU-after.png
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
  <title>Work — Adrian M. | Freelance Web Developer | Windhoek, Namibia</title>
  <meta name="description" content="See websites built by Adrian M. for Namibian businesses. Real projects, real results.">
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

  <!-- FEATURED CASE STUDY: TMU CASH LOAN -->
  <section class="case-study-featured" aria-label="TMU Cash Loan case study">...</section>

  <!-- PROJECT DETAILS -->
  <section class="project-details" aria-label="Project details">...</section>

  <!-- RESULTS -->
  <section class="project-results" aria-label="Results">...</section>

  <!-- FUTURE PROJECTS PLACEHOLDER -->
  <section class="future-work" aria-label="More projects coming">...</section>

  <!-- FINAL CTA -->
  <section class="final-cta-section" aria-label="Start your project">...</section>

  <!-- FOOTER -->
  <footer class="footer-section">...</footer>

  <script src="js/main.js"></script>
</body>
</html>
```

---

## 1. NAVIGATION

Reuse the same nav component. Work link highlighted in `#795238`.

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
Heading:    Selected Work
Subheading: Real projects for real Namibian businesses. Every site is built to perform.
```

| Element | Font | Weight | Size | Color |
|---------|------|--------|------|-------|
| Heading | Syne | 700 | 48px | `#AEA7A3` |
| Subheading | DM Sans | 400 | 18px | `#959595` |

**On mobile:** heading 36px, subheading 16px.

---

## 3. FEATURED CASE STUDY: TMU CASH LOAN

This is the hero section of the Work page. The full case study, not a teaser.

### Section Container

```css
.case-study-featured {
  background-color: #242323;
  padding: 0 20px 80px;  /* No top padding — flows from header */
}

.case-study-container {
  max-width: 1200px;
  margin: 0 auto;
}
```

### Case Study Header

```
Client:      TMU Cash Loan
Industry:    Financial Services / Microfinance
Location:    Windhoek, Namibia
Services:    Website Redesign, WhatsApp Integration, AI Chatbot, Loan Calculator
```

```css
.case-study-client {
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #795238;
  margin-bottom: 12px;
}

.case-study-title {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 36px;
  color: #AEA7A3;
  margin-bottom: 8px;
}

.case-study-meta {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 15px;
  color: #959595;
  margin-bottom: 48px;
}

.case-study-meta span {
  margin-right: 24px;
}

.case-study-meta span::before {
  content: '·';
  margin-right: 24px;
  color: #525254;
}

.case-study-meta span:first-child::before {
  content: none;
}
```

### Before/After Comparison (Large)

```css
.case-study-comparison {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: 24px;
  align-items: center;
  margin-bottom: 48px;
}

.case-study-image {
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid #363636;
}

.case-study-image img {
  width: 100%;
  height: auto;
  display: block;
}

.case-study-arrow {
  color: #795238;
  font-size: 32px;
  font-weight: 700;
}

.case-study-image-label {
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  color: #525254;
  margin-bottom: 8px;
}
```

**Images:**
- Before: `TMU-before.png` — label "Before"
- After: `TMU-after.png` — label "After"
- Arrow: "→" between them

**On mobile:** Stack vertically, arrow becomes "↓" or removed.

### Case Study Description

```css
.case-study-description {
  max-width: 700px;
  margin: 0 auto 48px;
}

.case-study-description p {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 16px;
  color: #959595;
  line-height: 1.7;
  margin-bottom: 16px;
}
```

**Content:**
```
TMU Cash Loan is a Namibian microfinance company offering quick loans to individuals and small businesses. Their old website was cluttered, hard to navigate, and didn't convert visitors into applicants.

I redesigned the site from the ground up — clean layout, clear calls-to-action, and a loan calculator that lets visitors see exactly what they'd pay before applying. I also integrated WhatsApp Business so inquiries come straight to their team, and built an AI chatbot to handle common questions 24/7.

The result: a professional, trustworthy site that turns browsers into leads.
```

**Rules:**
- Plain language — no jargon
- Focus on the problem and solution, not just the tech
- "Turns browsers into leads" — business outcome, not just "looks better"

### Live Site CTA

```css
.case-study-live-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 14px 28px;
  background-color: transparent;
  color: #AEA7A3;
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  font-size: 15px;
  border: 1px solid #4A4A4A;
  border-radius: 8px;
  text-decoration: none;
  transition: background-color 300ms ease, color 300ms ease, border-color 300ms ease;
}

.case-study-live-link:hover {
  background-color: #795238;
  color: #242323;
  border-color: #795238;
}
```

Content: `View Live Site →`  
Link: `https://www.tmucapital.com/` (opens new tab)

---

## 4. PROJECT DETAILS

### Section Container

```css
.project-details {
  background-color: #2E2E2E;  /* Lighter breath section */
  padding: 80px 20px;
}

.project-details-container {
  max-width: 1000px;
  margin: 0 auto;
}
```

### Section Heading

```
What Was Built
```
```css
font-family: 'Syne', sans-serif;
font-weight: 700;
font-size: 28px;
color: #AEA7A3;
text-align: center;
margin-bottom: 48px;
```

### Feature Grid (3 columns)

```css
.project-features-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.project-feature-card {
  background-color: #363636;
  border: 1px solid #4A4A4A;
  border-radius: 16px;
  padding: 32px;
}

.project-feature-icon {
  color: #795238;
  font-size: 24px;
  margin-bottom: 16px;
}

.project-feature-title {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 18px;
  color: #AEA7A3;
  margin-bottom: 8px;
}

.project-feature-desc {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 14px;
  color: #959595;
  line-height: 1.6;
}
```

**Features:**

| Feature | Description | Icon |
|---------|-------------|------|
| **Responsive Design** | Works perfectly on phones, tablets, and desktops. Most visitors browse on mobile — the site is built mobile-first. | Phone/desktop icon |
| **Loan Calculator** | Interactive tool that shows visitors their repayment breakdown before they apply. Reduces friction and builds trust. | Calculator icon |
| **WhatsApp Integration** | One-click chat button connects visitors directly to TMU's team. The channel Namibians actually use. | WhatsApp icon |
| **AI Chatbot** | 24/7 automated answers to common questions. Frees up the team and captures leads after hours. | Robot/message icon |
| **Speed Optimized** | Fast load times on Namibian mobile networks. No one waits for a slow site. | Lightning/zap icon |
| **SEO Ready** | Proper structure, meta tags, and sitemap submission so Google can find the site. | Search/magnifier icon |

**Rules:**
- Each feature explains the *benefit*, not just the tech
- "The channel Namibians actually use" — local context
- "Frees up the team" — business outcome
- Icons are inline SVGs, simple line style, warm brown color

**On mobile:** 2 columns on tablet, 1 column on phone.

---

## 5. RESULTS

### Section Container

```css
.project-results {
  background-color: #242323;
  padding: 80px 20px;
}

.project-results-container {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}
```

### Section Heading

```
The Results
```
```css
font-family: 'Syne', sans-serif;
font-weight: 700;
font-size: 28px;
color: #AEA7A3;
margin-bottom: 16px;
```

### Big Stat

```css
.project-stat-number {
  font-family: 'Syne', sans-serif;
  font-weight: 800;
  font-size: clamp(64px, 10vw, 120px);
  color: #F8F9FB;
  line-height: 1;
  margin-bottom: 8px;
}

.project-stat-label {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 18px;
  color: #959595;
  margin-bottom: 48px;
}
```

Content:
```
893+
Inquiries generated since launch
```

**Rules:**
- "893+" is massive — the visual anchor of the page
- "Inquiries generated since launch" — honest framing (not "by Adrian", but "since launch")
- The "+" is part of the number, same size

### Supporting Stats (Below Big Stat)

```css
.project-stats-row {
  display: flex;
  justify-content: center;
  gap: 48px;
  flex-wrap: wrap;
}

.project-stat-item {
  text-align: center;
}

.project-stat-item-number {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 32px;
  color: #AEA7A3;
}

.project-stat-item-label {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 14px;
  color: #959595;
}
```

**Content:**

| Stat | Label |
|------|-------|
| 4 | Pages built |
| 3 | Custom features |
| 1 | Happy client |

**Rules:**
- "Happy client" — warm, human, not "Satisfied stakeholder"
- These are modest but honest — don't inflate

### Timeline Note

```css
.project-timeline {
  margin-top: 48px;
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 14px;
  color: #525254;
}
```

Content:
```
Launched September 2025 · Ongoing support
```

---

## 6. FUTURE PROJECTS PLACEHOLDER

### Section Container

```css
.future-work {
  background-color: #2E2E2E;
  padding: 80px 20px;
}

.future-work-container {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
}
```

### Content

```
Heading:    More Projects Coming
Body:       I'm currently working with Namibian SMEs in hospitality, retail, and professional services. New case studies will be added here as projects launch.

CTA:        [Your Project Could Be Next →]
Link:       /contact
```

```css
.future-work-heading {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 24px;
  color: #AEA7A3;
  margin-bottom: 16px;
}

.future-work-body {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 16px;
  color: #959595;
  line-height: 1.6;
  margin-bottom: 24px;
}

.future-work-cta {
  display: inline-block;
  padding: 14px 28px;
  background-color: transparent;
  color: #795238;
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  font-size: 15px;
  border: 1px solid #795238;
  border-radius: 8px;
  text-decoration: none;
  transition: background-color 300ms ease, color 300ms ease;
}

.future-work-cta:hover {
  background-color: #795238;
  color: #242323;
}
```

**Rules:**
- Honest about having one project — no fake portfolio pieces
- "Your Project Could Be Next" — turns scarcity into opportunity
- Industries mentioned (hospitality, retail, professional services) — hints at target niches without committing
- Warm, not apologetic

---

## 7. FINAL CTA

Reuse the same Final CTA section pattern — adapted for Work page context.

```css
.final-cta-section {
  background-color: #242323;
  padding: 100px 20px;
  text-align: center;
}
```

**Content:**
```
Heading:    Like What You See?
Subheading: Let's build something that works for your business.
CTA:        [Get a Free Quote →]
Link:       /contact
```

---

## 8. FOOTER

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
   WORK PAGE STYLES
   ======================================== */

/* Case study */
.case-study-featured { ... }
.case-study-client { ... }
.case-study-title { ... }
.case-study-comparison { ... }
.case-study-image { ... }
.case-study-description { ... }
.case-study-live-link { ... }

/* Project details */
.project-details { ... }
.project-features-grid { ... }
.project-feature-card { ... }

/* Results */
.project-results { ... }
.project-stat-number { ... }
.project-stats-row { ... }

/* Future work */
.future-work { ... }
.future-work-cta { ... }
```

---

## SHARED JS UPDATES

No new JS needed for this page. All interactions are hover states and links.

---

## RESPONSIVE BREAKPOINTS

| Breakpoint | Adjustments |
|------------|-------------|
| ≥1024px | Before/After side by side, 3 feature columns, stats row horizontal |
| 768–1023px | Before/After side by side (smaller), 2 feature columns, stats row wraps |
| <768px | Before/After stacked, 1 feature column, stats stack vertically, big stat 64px |

---

## ACCESSIBILITY

- Semantic HTML:
  - `<main>` wrapping primary content
  - `<section>` with `aria-label` for each block
  - Before/After images: `<figure>` with `<figcaption>`
- Image alt text:
  - Before: "TMU Cash Loan website before redesign — cluttered green layout with loan calculator"
  - After: "TMU Cash Loan website after redesign — clean modern layout with clear call-to-action"
- Color contrast: All existing brand colors pass WCAG AA
- Focus states: All interactive elements have visible focus

---

## PERFORMANCE

- Images: TMU before/after screenshots — optimize, use `loading="lazy"` (below fold)
- No external libraries
- Target: Lighthouse Performance ≥90

---

## NO-GO LIST

- [ ] No fake projects — only TMU Cash Loan is shown
- [ ] No "View Case Study" buttons that open modals — link directly to live site
- [ ] No project filtering or category tabs — not enough projects yet
- [ ] No testimonial quotes from TMU client — don't have permission yet
- [ ] No "Before/After" slider widget — static side-by-side is clearer
- [ ] No glossy effects, glassmorphism, or blur

---

## DELIVERABLE

1. New `work.html` file with complete page structure
2. Updated `css/styles.css` with work page styles added
3. Nav links pointing to correct pages
4. Footer copied from homepage with correct links
5. All CTAs link to `/contact`
6. No console errors
7. Responsive at all breakpoints

---

## VERIFICATION CHECKLIST

- [ ] Page title: "Work — Adrian M. | Freelance Web Developer | Windhoek, Namibia"
- [ ] Meta description present
- [ ] Nav fixed at top, Work link highlighted, "Get Started" button links to `/contact`
- [ ] Page header: "Selected Work" + subheading, centered
- [ ] Case study client label: "TMU Cash Loan" in warm brown
- [ ] Case study title: "TMU Cash Loan" in Syne
- [ ] Meta info: Industry, Location, Services — separated by dots
- [ ] Before/After comparison: side by side on desktop, stacked on mobile
- [ ] Before/After labels above each image
- [ ] Case study description: 3 paragraphs, plain language, business-focused
- [ ] "View Live Site →" button, links to `https://www.tmucapital.com/`, new tab
- [ ] Project details: 6 feature cards in 3-column grid
- [ ] Each feature card: icon, title, benefit-focused description
- [ ] Results: "893+" massive stat, supporting stats below
- [ ] Timeline: "Launched September 2025 · Ongoing support"
- [ ] Future work placeholder: honest, warm, "Your Project Could Be Next"
- [ ] Final CTA: "Like What You See?" adapted for work context
- [ ] Footer copied, nav links correct
- [ ] Responsive: images stack, features go 2→1 column, stats stack on mobile
- [ ] Lighthouse Accessibility ≥95, Performance ≥90

---

*Prompt version 1.0 — Work page for multi-page site*
