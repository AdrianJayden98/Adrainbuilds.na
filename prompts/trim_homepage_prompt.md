# AI Developer Prompt: Trim Homepage for Multi-Page Transition
## For Cursor, GitHub Copilot, or similar AI coding agents

---

## ROLE DEFINITION

You are a **Frontend Developer & UI Engineer** specializing in:
- Semantic, accessible HTML
- Modern CSS (Flexbox, Grid, custom properties)
- Clean, conversion-focused UI components
- Performance-first development
- Responsive design with mobile-first approach
- Code refactoring and extraction

You write **production-ready code** — not prototypes. Every line must be intentional, commented where logic is non-obvious, and follow modern best practices.

---

## PROJECT CONTEXT

**Client:** Adrian M. — Freelance Web Developer based in Windhoek, Namibia.
**Positioning:** "Friendly & approachable local dev" serving Namibian SMEs.
**Brand:** Personal brand (not agency). Warm, grounded, cinematic.
**Tech stack:** Static HTML/CSS/JS. Transitioning from single-page to multi-page.
**Current state:** A complete single-page `index.html` exists with 8 sections: Hero, Credibility Strip, Services Preview, Selected Work, Process, About Snippet, Final CTA, and Footer.

**Goal:** Trim the homepage to a lean, conversion-focused landing page. Remove sections that now have dedicated pages. Update navigation to point to new pages.

---

## TASK

Trim the existing `index.html` homepage by removing two sections and updating navigation/links throughout. Extract shared CSS into a separate file. The result is a clean, fast-loading homepage that funnels visitors to deeper pages.

---

## SECTIONS TO REMOVE

### 1. Process Section
**Remove entirely.** This content moves to `/services`.

**What to remove:**
- `<section class="process-section">` and all its children
- All `.process-*` CSS rules
- Any `.process-*` JavaScript (IntersectionObserver targets, etc.)

### 2. About Snippet Section
**Remove entirely.** This content moves to `/about`.

**What to remove:**
- `<section class="about-section">` and all its children
- All `.about-*` CSS rules
- Any `.about-*` JavaScript (IntersectionObserver targets, etc.)

**Exception:** The hero cutout image stays — it's used in the hero section, not the About Snippet. Do not remove the hero image.

---

## SECTIONS TO KEEP (WITH MODIFICATIONS)

### 1. Hero Section — KEEP AS-IS
No changes to layout, content, or styling.

**One addition:** Update nav links if a nav element exists in the hero.

### 2. Credibility Strip — KEEP AS-IS
No changes.

### 3. Services Preview — KEEP BUT TRIM

**Keep:**
- Section heading: "What I Build"
- Subheading: "Websites that win you customers..."
- 3 tier cards (Starter, Growth, Premium)
- Card design, colors, hover states
- "MOST POPULAR" badge on Growth
- Retainer callout

**Modify:**
- Change CTA buttons from "Get a Quote" to "View Details →"
- Link CTA buttons to `/services` (not mailto or anchor)
- Remove detailed feature lists from cards — keep only:
  - Starter: "1–3 pages · Mobile-friendly · Contact form"
  - Growth: "3–6 pages · CMS · SEO · Analytics"
  - Premium: "6+ pages · Custom features · Advanced SEO"
- Remove "Starting price" sub-label under price
- Retainer CTA: "Learn More →" linking to `/services`

**CSS to modify:**
```css
/* Feature lists on homepage cards — simplified */
.service-card-features {
  list-style: none;
  padding: 0;
  margin: 0 0 24px 0;
}

.service-card-features li {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 14px;
  color: #959595;
  line-height: 1.6;
  margin-bottom: 8px;
}

/* No bullet markers needed — simple text list */
```

### 4. Selected Work — KEEP BUT TRIM

**Keep:**
- Section heading: "Selected Work"
- Subheading: "Real projects. Real results."
- Before/After comparison
- TMU Cash Loan title and category
- 893+ stat block
- "View Live Site →" CTA

**Modify:**
- Add a secondary CTA below the live site link:
  ```
  [See All Work →]
  ```
  - Links to `/work`
  - Style: text-link, not button — secondary to "View Live Site"
  - Color: `#795238`, hover: `#8B6348`
  - Font: DM Sans, 14px, with arrow

**CSS addition:**
```css
.work-see-all {
  display: inline-block;
  margin-top: 16px;
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  font-size: 14px;
  color: #795238;
  text-decoration: none;
  transition: color 200ms ease;
}

.work-see-all:hover {
  color: #8B6348;
}
```

### 5. Final CTA — KEEP AS-IS
No changes to layout or content.

**One addition:** If the CTA button links to a contact form anchor, change to `/contact`.

### 6. Footer — KEEP AS-IS
No changes to layout or content.

**One addition:** Ensure footer nav links point to new pages:
- Home → `/`
- Services → `/services`
- Work → `/work`
- About → `/about`

---

## NAVIGATION UPDATES

If the hero or footer contains navigation, update all links:

| Label | Old Link | New Link |
|-------|----------|----------|
| Home | `#` or `/` | `/` |
| Services | `#services` | `/services` |
| Work | `#work` | `/work` |
| About | `#about` or not present | `/about` |
| Contact | `mailto:` or `#contact` | `/contact` |

**Rules:**
- All links are page-to-page, not anchor links
- Use relative paths (`/services`, not `https://adrianm.dev/services`)
- Add `target="_self"` explicitly (or omit — default is fine)

---

## CSS EXTRACTION

Extract all embedded CSS from `index.html` into a new file `css/styles.css`.

**Steps:**
1. Create `css/` directory
2. Create `css/styles.css`
3. Copy everything inside `<style>` tags from `index.html`
4. Remove `.process-*` and `.about-*` rules
5. Update any rules as specified above (services CTAs, feature lists)
6. Link in HTML head:
   ```html
   <link rel="stylesheet" href="css/styles.css">
   ```

**What stays in HTML (inline):**
- Nothing — all CSS moves to external file
- Exception: Critical CSS for above-the-fold content can stay if performance demands it, but for this site size, external file is fine

---

## NEW HOMEPAGE STRUCTURE

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Adrian M. — Freelance Web Developer | Windhoek, Namibia</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>

  <!-- 1. HERO -->
  <header class="hero">...</header>

  <!-- 2. CREDIBILITY STRIP -->
  <section class="credibility-strip" aria-label="Why work with me">...</section>

  <!-- 3. SERVICES PREVIEW (trimmed) -->
  <section class="services-section" aria-label="Services preview">...</section>

  <!-- 4. SELECTED WORK (trimmed) -->
  <section class="work-section" aria-label="Selected work">...</section>

  <!-- 5. FINAL CTA -->
  <section class="final-cta-section" aria-label="Get in touch">...</section>

  <!-- 6. FOOTER -->
  <footer class="footer-section">...</footer>

  <script src="js/main.js"></script>
</body>
</html>
```

**6 sections total** (down from 8).

---

## JS EXTRACTION (If Applicable)

If `index.html` contains embedded JavaScript:
1. Create `js/` directory
2. Create `js/main.js`
3. Copy all JS from `<script>` tags
4. Remove any code targeting removed sections (Process, About)
5. Link in HTML before closing `</body>`:
   ```html
   <script src="js/main.js"></script>
   ```

**What to remove from JS:**
- IntersectionObserver entries for `.process-step` and `.about-*`
- Any scroll-trigger handlers for removed sections
- Any anchor-link smooth-scroll for `#process` or `#about`

---

## FILE STRUCTURE AFTER TRIM

```
/
├── index.html              (trimmed homepage)
├── css/
│   └── styles.css          (extracted + cleaned)
├── js/
│   └── main.js             (extracted + cleaned, if JS exists)
└── images/
    ├── hero-cutout.png
    ├── TMU-before.png
    ├── TMU-after.png
    └── desert-namibia.jpeg
```

---

## RESPONSIVE CHECK

After trimming, verify at all breakpoints:
- 375px, 768px, 1024px, 1440px, 1920px
- No layout shifts from removed sections
- Services cards still align properly with simplified content
- Selected Work still displays before/after correctly
- Footer nav links work (even though pages don't exist yet)

---

## ACCESSIBILITY CHECK

- Heading hierarchy: Ensure `<h1>` is only in hero, `<h2>` for each remaining section
- Section `aria-label` attributes: Update if section purpose changed
- All links have descriptive text
- Color contrast unchanged (no new colors introduced)

---

## NO-GO LIST (Do NOT Do)

- [ ] Do not rename CSS classes — keep existing naming for consistency
- [ ] Do not restructure remaining sections — only remove, don't redesign
- [ ] Do not add new animations or effects
- [ ] Do not change color palette or typography
- [ ] Do not remove the hero cutout image
- [ ] Do not modify the footer desert background image
- [ ] Do not create the new pages (`services.html`, etc.) — this prompt is homepage-only

---

## DELIVERABLE

1. Updated `index.html` with 6 sections (Process and About removed)
2. New `css/styles.css` with extracted, cleaned CSS
3. New `js/main.js` with extracted, cleaned JS (if applicable)
4. All nav links updated to point to future pages (`/services`, `/work`, `/about`, `/contact`)
5. Services cards trimmed with "View Details →" CTAs
6. Selected Work enhanced with "See All Work →" link
7. No console errors
8. No visual regressions
9. Lighthouse score maintained or improved

---

## VERIFICATION CHECKLIST

- [ ] Process section completely removed from HTML, CSS, and JS
- [ ] About Snippet section completely removed from HTML, CSS, and JS
- [ ] Homepage has exactly 6 sections: Hero, Credibility, Services, Work, Final CTA, Footer
- [ ] CSS extracted to `css/styles.css` and linked in HTML head
- [ ] JS extracted to `js/main.js` and linked before `</body>`
- [ ] Services cards have "View Details →" linking to `/services`
- [ ] Services cards have simplified feature lists (3 bullets max)
- [ ] Selected Work has "See All Work →" linking to `/work`
- [ ] All nav links point to page URLs, not anchors
- [ ] Footer nav links: Home `/`, Services `/services`, Work `/work`, About `/about`
- [ ] No broken links or 404s (pages don't exist yet, but links are correct)
- [ ] Responsive at 375px, 768px, 1024px, 1440px
- [ ] No layout shift, overflow, or broken text wrapping
- [ ] Lighthouse Performance ≥90, Accessibility ≥95

---

*Prompt version 1.0 — Homepage trim for multi-page transition*
