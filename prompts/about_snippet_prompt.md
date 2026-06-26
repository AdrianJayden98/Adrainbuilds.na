# AI Developer Prompt: About Snippet Section
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
**Current state:** Hero, Credibility Strip, Services Preview, Selected Work, and Process sections are complete and locked. This is the **sixth section** on the homepage.

**Key requirement:** Reuse the same cutout image from the hero section — the high-res PNG with transparent background of Adrian looking at camera.

**Why this section exists:** By this point, the visitor has seen what Adrian does, what he charges, proof he can deliver, and how he works. The About Snippet answers: "But who is this person, really?" It adds warmth and humanizes the brand before the final CTA.

---

## TASK

Build an **About Snippet** section — not a full About page, just a brief, warm introduction that reuses the hero cutout image in a new composition. This section should feel like Adrian turning to the visitor and saying, "Here's a bit more about me."

---

## DESIGN SPECIFICATION

### Section Container

```css
.about-section {
  background-color: #242323;  /* Back to dark — creates rhythm after the lighter process section */
  padding: 100px 20px;
  width: 100%;
  overflow: hidden;
}
```

**Rules:**
- No border-top or border-bottom
- Full-width background, content constrained to max-width 1200px centered

---

### Section Layout (Desktop ≥1024px)

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ┌──────────────────────────┐  ┌─────────────────────────┐  │
│  │                          │  │                         │  │
│  │  A Bit About Me          │  │                         │  │
│  │                          │  │      [CUTOUT IMAGE]     │  │
│  │  I'm Adrian — a web      │  │      Reused from hero   │  │
│  │  developer based in      │  │      but positioned     │  │
│  │  Windhoek. I build       │  │      differently:       │  │
│  │  websites that help      │  │                         │  │
│  │  Namibian businesses     │  │      • Larger scale     │  │
│  │  get found, get trusted, │  │      • Different crop   │  │
│  │  and get customers.      │  │      • Facing slightly  │  │
│  │                          │  │        toward text      │  │
│  │  Before this, I studied  │  │                         │  │
│  │  software engineering    │  │                         │  │
│  │  at Goldstone Institute. │  │                         │  │
│  │  Now I work with local   │  │                         │  │
│  │  SMEs because I believe  │  │                         │  │
│  │  good websites shouldn't │  │                         │  │
│  │  be a luxury.            │  │                         │  │
│  │                          │  │                         │  │
│  │  When I'm not coding,    │  │                         │  │
│  │  you'll find me [personal│  │                         │  │
│  │  detail — see content].  │  │                         │  │
│  │                          │  │                         │  │
│  │  [Let's Talk →]          │  │                         │  │
│  │                          │  │                         │  │
│  └──────────────────────────┘  └─────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Layout:**
- Two-column: text left (~55%), image right (~45%)
- Text block vertically centered
- Image: larger than hero, different positioning — not a duplicate composition

---

### Text Block

**Section label (small, above heading):**
```css
font-family: 'DM Sans', sans-serif;
font-weight: 500;
font-size: 12px;
text-transform: uppercase;
letter-spacing: 2px;
color: #795238;  /* Warm brown accent */
margin-bottom: 16px;
```
Content: `A Bit About Me`

**Heading:**
```css
font-family: 'Syne', sans-serif;
font-weight: 700;
font-size: 36px;
color: #AEA7A3;
line-height: 1.2;
margin-bottom: 24px;
```
Content: `I'm Adrian — a web developer based in Windhoek.`

**Body paragraphs:**
```css
font-family: 'DM Sans', sans-serif;
font-weight: 400;
font-size: 16px;
color: #959595;
line-height: 1.7;
margin-bottom: 16px;
```

**CTA:**
```css
font-family: 'DM Sans', sans-serif;
font-weight: 500;
font-size: 15px;
color: #AEA7A3;
text-decoration: none;
border-bottom: 1px solid #795238;
padding-bottom: 2px;
transition: color 200ms ease, border-color 200ms ease;
```
Content: `Let's Talk →`
Hover: color → `#F8F9FB`, border-color → `#8B6348`

---

### Image Block (Reused Cutout)

```css
.about-image {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.about-image img {
  max-height: 500px;        /* Larger than hero */
  width: auto;
  object-fit: contain;
  filter: drop-shadow(0 20px 60px rgba(0, 0, 0, 0.4));
}
```

**Key differences from hero usage:**
- **Scale:** Larger — ~500px max-height vs ~75–85vh in hero. More intimate, less monumental.
- **Position:** Centered in the right column, not bottom-aligned. More balanced, less dramatic.
- **Crop:** If possible via CSS `object-position`, focus on upper body/face — the hero showed full figure, here we can zoom slightly on the person.
- **Shadow:** Same drop shadow style as hero (`0 20px 60px rgba(0,0,0,0.4)`) — consistency.
- **No text overlap:** The image sits cleanly in its own space — no typography layered over it.

**Rules:**
- Use the **same image file** as the hero — do not duplicate or rename
- Apply different sizing/positioning via CSS only
- Alt text: "Adrian M., freelance web developer in Windhoek, Namibia"

---

## CONTENT (USE EXACTLY)

### Section Label
```
A Bit About Me
```

### Heading
```
I'm Adrian — a web developer based in Windhoek.
```

### Body Paragraph 1
```
I build websites that help Namibian businesses get found, get trusted, and get customers. Most of my clients are SMEs who know they need a proper online presence but don't know where to start — so I handle the technical side and explain things in plain language.
```

### Body Paragraph 2
```
Before this, I studied software engineering at Goldstone Software Engineering Institute. Now I work with local businesses because I believe good websites shouldn't be a luxury reserved for big companies with big budgets.
```

### Body Paragraph 3 (Personal Touch)
```
When I'm not coding, you'll find me exploring Windhoek's coffee spots or catching up on tech podcasts. I take on 1–2 projects at a time so I can give each one real attention.
```

**Note:** The personal detail (coffee spots, podcasts) adds warmth and approachability. If Adrian wants to change this later, it's a single line swap.

### CTA
```
Let's Talk →
```
- Links to: `#contact` (anchor link to contact section below) or `mailto:hello@adrianm.dev`

---

## RESPONSIVE BREAKPOINTS

| Breakpoint | Layout |
|------------|--------|
| ≥1024px | Two columns, text left, image right |
| 768–1023px | Two columns, smaller image (~350px max-height), tighter gap |
| <768px | Stacked: text first, image below, centered. Image max-height 320px |

**Mobile adjustments:**
- Section padding: 80px 20px
- Heading: 28px
- Body: 15px
- Image: centered, smaller, possibly circular crop (180px diameter) if the full cutout feels too large stacked
- CTA: full-width button style instead of text-link (more tappable)

---

## INTERACTION & MOTION

### Text Reveal (optional, consistent with previous sections)
If IntersectionObserver is used:

```css
.about-text {
  opacity: 0;
  transform: translateX(-20px);
  transition: opacity 600ms ease, transform 600ms ease;
}

.about-image {
  opacity: 0;
  transform: translateX(20px);
  transition: opacity 600ms ease, transform 600ms ease;
}

.about-text.visible,
.about-image.visible {
  opacity: 1;
  transform: translateX(0);
}
```

Respect `prefers-reduced-motion`.

### CTA Hover
```css
.about-cta:hover {
  color: #F8F9FB;
  border-color: #8B6348;
}
```

---

## ACCESSIBILITY

- Semantic HTML:
  - `<section>` with `aria-label="About Adrian"`
  - Text: `<article>` or `<div>` with proper heading hierarchy
  - Image: `<figure>` with `<figcaption>` optional
- Image alt text: "Adrian M., freelance web developer in Windhoek, Namibia"
- Color contrast:
  - Heading `#AEA7A3` on `#242323` = 5.8:1 ✓
  - Body `#959595` on `#242323` = 5.1:1 ✓
- CTA focus state: `outline: 2px solid #AEA7A3, outline-offset: 4px`

---

## PERFORMANCE

- Image is reused — no additional download
- Same optimization as hero: WebP with PNG fallback, preloaded if above fold
- Target: No additional performance cost

---

## INTEGRATION WITH EXISTING SECTIONS

DOM order:
```html
<body>
  <header class="hero">...</header>
  <section class="credibility-strip" aria-label="Why work with me">...</section>
  <section class="services-section" aria-label="Services and pricing">...</section>
  <section class="work-section" aria-label="Selected work">...</section>
  <section class="process-section" aria-label="How we work">...</section>
  <section class="about-section" aria-label="About Adrian">
    ...
  </section>
</body>
```

Visual flow:
- Hero: `#242323`
- Credibility Strip: `#2E2E2E` (breath)
- Services: `#242323`
- Selected Work: `#242323`
- Process: `#2E2E2E` (breath)
- About: `#242323` (back to dark)

---

## NO-GO LIST (Do NOT implement)

- [ ] No full resume or CV-style timeline
- [ ] No "My Skills" progress bars or percentages
- [ ] No tech stack icons grid (React, Node, etc.)
- [ ] No downloadable PDF or "View Full Resume" link
- [ ] No separate About page link (this is the snippet, the full story stays here)
- [ ] No social media feed embed
- [ ] No background images or video
- [ ] No parallax effects
- [ ] No glossy effects, glassmorphism, or blur

---

## DELIVERABLE

An updated `index.html` containing:
1. All existing hero section code (unchanged)
2. All existing credibility strip code (unchanged)
3. All existing services preview code (unchanged)
4. All existing selected work code (unchanged)
5. All existing process section code (unchanged)
6. The new About Snippet section immediately after Process
7. Embedded CSS for the new section
8. Image reference reusing the same cutout file as the hero
9. No console errors
10. No visual regressions to previous sections

---

## VERIFICATION CHECKLIST

- [ ] Section label "A Bit About Me" in warm brown, uppercase, letter-spaced
- [ ] Heading "I'm Adrian — a web developer based in Windhoek." in Syne, left-aligned
- [ ] 3 body paragraphs in DM Sans, readable line-height (1.7)
- [ ] CTA "Let's Talk →" as text-link with underline, hover brightens
- [ ] Image reused from hero — same file, different CSS sizing/positioning
- [ ] Image is larger and more centered than hero usage — feels intimate, not monumental
- [ ] On desktop: two-column layout, text left, image right
- [ ] On mobile: stacked, text first, image below (possibly circular crop)
- [ ] No skills bars, no tech icons, no resume timeline
- [ ] Lighthouse Accessibility score ≥95
- [ ] No layout shift, overflow, or broken text wrapping at any breakpoint

---

*Prompt version 1.0 — About Snippet, reused hero cutout*
