# AI Developer Prompt: Selected Work Section
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
**Tech stack:** Static HTML/CSS/JS. Single-file `index.html` with embedded CSS.
**Current state:** Hero section, Credibility Strip, and Services Preview are complete and locked. This is the **fourth section** on the homepage.

**Case study available:** TMU Cash Loan — a cash loan/microfinance business in Namibia. Adrian redesigned their website and handed it over in September 2025. The site has generated 893+ inquiries/leads since launch.

**Assets provided:**
- Before screenshot: `TMU before.png` — shows the old website (green-heavy, cluttered, dated design)
- After screenshot: `TMU after.png` — shows the redesigned website (clean, modern, clear CTA)
- Live site: `https://www.tmucapital.com/`

---

## TASK

Build a **Selected Work** section featuring one strong case study: TMU Cash Loan. This section must feel like a natural continuation of the dark, matte brand while showcasing real results.

The section answers: "Can this person actually build something that works?" The answer is yes — 893 inquiries prove it.

---

## DESIGN SPECIFICATION

### Section Container

```css
.work-section {
  background-color: #242323;  /* Same as hero and services — continuous dark canvas */
  padding: 100px 20px;        /* Generous vertical space */
  width: 100%;
  position: relative;
  overflow: hidden;
}
```

**Rules:**
- No border-top or border-bottom
- Full-width background, content constrained to max-width 1200px centered

---

### Section Header

```
Selected Work
Real projects. Real results.
```

| Element | Font | Weight | Size | Line-Height | Color |
|---------|------|--------|------|-------------|-------|
| Heading "Selected Work" | Syne | 700 | 42px | 1.1 | `#AEA7A3` |
| Subheading | DM Sans | 400 | 18px | 1.6 | `#959595` |

**Positioning:** Left-aligned, max-width 600px, margin-bottom 64px.

**On mobile:** heading 32px, subheading 16px.

---

### Case Study Card: TMU Cash Loan

**Layout (Desktop ≥1024px):**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Selected Work                                              │
│  Real projects. Real results.                                │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │  [BEFORE IMAGE]              [AFTER IMAGE]          │   │
│  │  ┌──────────────┐            ┌──────────────┐      │   │
│  │  │              │     →      │              │      │   │
│  │  │  Old site    │            │  New site    │      │   │
│  │  │  screenshot  │            │  screenshot  │      │   │
│  │  │              │            │              │      │   │
│  │  └──────────────┘            └──────────────┘      │   │
│  │                                                     │   │
│  │  TMU Cash Loan                                      │   │
│  │  Namibian microfinance website redesign             │   │
│  │                                                     │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐          │   │
│  │  │ 893+     │  │ WhatsApp │  │ AI       │          │   │
│  │  │ Inquiries│  │ Chat     │  │ Chatbot  │          │   │
│  │  │ since    │  │          │  │          │          │   │
│  │  │ launch   │  │          │  │          │          │   │
│  │  └──────────┘  └──────────┘  └──────────┘          │   │
│  │                                                     │   │
│  │  [View Live Site →]                                 │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

### Before/After Image Comparison

**Layout:** Two images side by side, connected by a subtle arrow or "→" between them.

```css
.work-comparison {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: 16px;
  align-items: center;
  margin-bottom: 40px;
}

.work-image {
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid #363636;
}

.work-image img {
  width: 100%;
  height: auto;
  display: block;
}

.work-arrow {
  color: #795238;
  font-size: 24px;
  font-weight: 700;
}
```

**Image labels (small, above each image):**
```css
.work-image-label {
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  color: #525254;
  margin-bottom: 8px;
}
```
- Left label: "Before"
- Right label: "After"

**Rules:**
- Images are screenshots — use `<img>` with proper `alt` text
- Maintain aspect ratio — `height: auto`, no cropping
- Border adds definition without gloss
- On mobile: stack vertically (Before on top, After below), arrow becomes "↓" or is removed

---

### Case Study Title & Description

```
Title:       TMU Cash Loan
Category:    Namibian microfinance website redesign
```

```css
.work-title {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 28px;
  color: #AEA7A3;
  margin-bottom: 8px;
}

.work-category {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 16px;
  color: #959595;
  margin-bottom: 32px;
}
```

---

### Results / Features Row

Three small cards or stat blocks in a horizontal row:

```css
.work-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-bottom: 32px;
}

.work-stat {
  background-color: #363636;
  border: 1px solid #4A4A4A;
  border-radius: 12px;
  padding: 24px;
  text-align: center;
}

.work-stat-number {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 32px;
  color: #F8F9FB;
  line-height: 1;
  margin-bottom: 8px;
}

.work-stat-label {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 13px;
  color: #959595;
  line-height: 1.4;
}
```

**Content:**

| Stat | Number | Label |
|------|--------|-------|
| 1 | 893+ | Inquiries since launch |
| 2 | — | WhatsApp Integration |
| 3 | — | AI Chatbot for FAQ |

**Rules:**
- "893+" is the hero number — largest, most prominent
- Other stats are feature highlights, not numbers (since we don't have those metrics)
- For non-number stats, use an icon or checkmark instead of a number
- All three blocks should feel visually balanced

**Alternative for stats 2 & 3 (if icons preferred):**
```css
.work-stat-icon {
  color: #795238;
  font-size: 24px;
  margin-bottom: 12px;
}
```
- Use simple inline SVG icons (checkmark, WhatsApp icon, robot icon)
- Icon + label, no number

---

### CTA Button

```
View Live Site →
```

```css
.work-cta {
  display: inline-block;
  padding: 14px 28px;
  background-color: transparent;
  color: #AEA7A3;
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  font-size: 15px;
  border-radius: 8px;
  border: 1px solid #4A4A4A;
  text-decoration: none;
  transition: background-color 300ms ease, color 300ms ease, border-color 300ms ease;
}

.work-cta:hover {
  background-color: #795238;
  color: #242323;
  border-color: #795238;
}
```

**Link:** `https://www.tmucapital.com/` — opens in new tab (`target="_blank" rel="noopener noreferrer"`)

---

### Case Study Card Container

```css
.work-card {
  background-color: #2E2E2E;
  border: 1px solid #363636;
  border-radius: 20px;
  padding: 48px;
  max-width: 100%;
}
```

**Rules:**
- Matte finish — no blur, no gloss, no transparency
- Rounded corners (20px) — consistent with services cards
- Subtle border for definition
- Padding: 48px desktop, 32px mobile

---

## RESPONSIVE BREAKPOINTS

| Breakpoint | Layout |
|------------|--------|
| ≥1024px | Before/After side by side, 3 stats in row, CTA inline |
| 768–1023px | Before/After side by side (smaller), 3 stats in row, CTA inline |
| <768px | Before/After stacked (Before top, After below), stats stacked or 2+1 grid, CTA full-width |

**Mobile adjustments:**
- Section padding: 80px 20px
- Card padding: 32px
- Before/After images: full-width, stacked, arrow removed or becomes "↓"
- Stats: 2 columns (893+ spans full width above, or all 3 stack vertically)
- Title: 24px

---

## CONTENT (USE EXACTLY)

### Section Header
```
Selected Work
Real projects. Real results.
```

### Case Study
```
Title:       TMU Cash Loan
Category:    Namibian microfinance website redesign

Before/After:
- Before: [TMU before.png] — label: "Before"
- After: [TMU after.png] — label: "After"

Stats:
1. 893+ Inquiries since launch
2. WhatsApp Integration
3. AI Chatbot for FAQ

CTA: View Live Site →
Link: https://www.tmucapital.com/
```

**Rules:**
- "893+" — the plus sign matters. It implies ongoing growth.
- "Inquiries since launch" — not "leads generated by Adrian" (we can't prove attribution), but "since launch" is factual
- "September 2025" — don't mention the handover date unless it adds context; "since launch" is cleaner
- WhatsApp and AI Chatbot are features built, not results — present them as capabilities demonstrated

---

## INTERACTION & MOTION

### Card Hover
```css
.work-card:hover {
  border-color: #4A4A4A;
  transition: border-color 300ms ease;
}
```

**Rules:**
- Subtle border brightening only
- No lift, no shadow expansion — the card is large enough already

### Image Hover
```css
.work-image:hover img {
  transform: scale(1.02);
  transition: transform 400ms ease;
}

.work-image {
  overflow: hidden;  /* Contains the scale */
}
```

**Rules:**
- Very subtle zoom — 1.02, not 1.1
- Smooth transition
- On mobile: disable hover zoom (touch devices)

### CTA Hover
As specified above — border fill with warm brown.

### Scroll Animation (optional, consistent with previous sections)
If IntersectionObserver is used:

```css
.work-card {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 600ms ease, transform 600ms ease;
}

.work-card.visible {
  opacity: 1;
  transform: translateY(0);
}
```

Respect `prefers-reduced-motion`.

---

## ACCESSIBILITY

- Semantic HTML:
  - `<section>` with `aria-label="Selected work"`
  - Case study card: `<article>`
  - Before/After images: `<figure>` with `<figcaption>`
  - Stats: `<dl>` (definition list) or `<ul>` with proper structure
- Image alt text:
  - Before: "TMU Cash Loan website before redesign — cluttered green layout with loan calculator"
  - After: "TMU Cash Loan website after redesign — clean modern layout with clear call-to-action"
- CTA: `target="_blank"` must have `rel="noopener noreferrer"` and visually indicate external link (the "→" arrow does this)
- Color contrast:
  - Stat numbers `#F8F9FB` on `#363636` = 10.5:1 ✓
  - Title `#AEA7A3` on `#2E2E2E` = 5.4:1 ✓

---

## PERFORMANCE

- Images: Use the provided PNG screenshots. Optimize with `loading="lazy"` since this section is below the fold.
- Image sizing: Max-width 100%, height auto. Consider `srcset` if providing multiple sizes.
- No external libraries
- Target: Images load without layout shift

---

## INTEGRATION WITH EXISTING SECTIONS

DOM order:
```html
<body>
  <header class="hero">...</header>
  <section class="credibility-strip" aria-label="Why work with me">...</section>
  <section class="services-section" aria-label="Services and pricing">...</section>
  <section class="work-section" aria-label="Selected work">
    ...
  </section>
</body>
```

Visual flow:
- Hero: `#242323`
- Credibility Strip: `#2E2E2E` (breath)
- Services: `#242323`
- Selected Work: `#242323` (continuous dark canvas)

---

## NO-GO LIST (Do NOT implement)

- [ ] No slider or carousel for before/after — static side-by-side is clearer
- [ ] No "drag to compare" before/after widget — overkill for one case study
- [ ] No fake additional projects — only TMU Cash Loan is shown
- [ ] No "View Case Study" modal or separate page — link directly to live site
- [ ] No video backgrounds
- [ ] No parallax effects
- [ ] No glossy effects, glassmorphism, or blur

---

## DELIVERABLE

An updated `index.html` containing:
1. All existing hero section code (unchanged)
2. All existing credibility strip code (unchanged)
3. All existing services preview code (unchanged)
4. The new Selected Work section immediately after services preview
5. Embedded CSS for the new section
6. Image references to `TMU before.png` and `TMU after.png` (assume same directory)
7. No console errors
8. No visual regressions to previous sections

---

## VERIFICATION CHECKLIST

- [ ] Section heading and subheading left-aligned, readable
- [ ] Before/After images side by side on desktop, stacked on mobile
- [ ] Images have "Before" / "After" labels above them
- [ ] Arrow "→" between images on desktop, removed or "↓" on mobile
- [ ] Case study card has matte finish, rounded corners (20px), subtle border
- [ ] 3 stat blocks visible: "893+ Inquiries", "WhatsApp Integration", "AI Chatbot"
- [ ] "893+" is the largest/most prominent stat
- [ ] CTA "View Live Site →" links to `https://www.tmucapital.com/` in new tab
- [ ] CTA hover: border fills with warm brown, text turns dark
- [ ] Image hover: subtle 1.02 scale, contained within border-radius
- [ ] On mobile: images stack, stats stack or 2+1 grid, CTA full-width
- [ ] Alt text on images is descriptive and accurate
- [ ] Lighthouse Accessibility score ≥95
- [ ] No layout shift, overflow, or broken text wrapping at any breakpoint

---

*Prompt version 1.0 — Selected Work, TMU Cash Loan case study*
