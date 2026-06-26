# AI Developer Prompt: Credibility Strip Section
## For Cursor, GitHub Copilot, or similar AI coding agents

---

## ROLE DEFINITION

You are a **Frontend Developer & UI Engineer** specializing in:
- Semantic, accessible HTML
- Modern CSS (Flexbox, Grid, custom properties)
- Clean, minimal UI components
- Performance-first development
- Responsive design with mobile-first approach

You write **production-ready code** — not prototypes. Every line must be intentional, commented where logic is non-obvious, and follow modern best practices.

---

## PROJECT CONTEXT

**Client:** Adrian M. — Freelance Web Developer based in Windhoek, Namibia.
**Positioning:** "Friendly & approachable local dev" serving Namibian SMEs.
**Brand:** Personal brand (not agency). Warm, grounded, cinematic.
**Tech stack:** Static HTML/CSS/JS. Single-file `index.html` with embedded CSS.
**Current state:** The hero section is complete and locked. This is the **second section** on the homepage, appearing immediately below the hero.

**Why this section exists:** The client has no client testimonials or logos yet (1–2 current clients, early stage). Instead of faking social proof, this section communicates reliability through direct commitments and context signals.

---

## TASK

Build a **Credibility Strip** — a horizontal section below the hero that communicates trust through the developer's own commitments, not third-party validation.

This section must feel like a natural continuation of the hero's visual language while serving a distinct purpose: answering "Why should I trust this person?" without using testimonials, logos, or stats the client doesn't have.

---

## DESIGN SPECIFICATION

### Section Container

```css
.credibility-strip {
  background-color: #2E2E2E;  /* Slightly lighter than hero bg (#242323) — creates separation */
  padding: 48px 0;              /* Vertical breathing room */
  width: 100%;
}
```

**Rules:**
- No border-top or border-bottom — the color shift alone creates the separation
- No shadow, no gradient, no decorative elements
- Full-width background, content constrained to max-width 1200px centered

---

### Content Structure

Four items in a horizontal row. Each item is a **signal of reliability**:

| # | Label | Sub-label | Icon (optional) |
|---|-------|-----------|-----------------|
| 1 | **Based in Windhoek** | Serving Namibian SMEs | Map pin or location marker |
| 2 | **Replies within 24 hours** | No ghosting, no delays | Clock or message icon |
| 3 | **Fixed quotes** | No hidden fees, no surprises | Document or shield icon |
| 4 | **Weekly updates** | You always know the status | Checkmark or refresh icon |

**Rules:**
- All four items must be visible on desktop without scrolling
- On mobile, stack vertically (4 rows) or 2×2 grid
- No fake numbers ("100+ clients", "5 years experience") — the client doesn't have these yet
- Language is plain, direct, confident — not salesy

---

### Typography

| Element | Font | Weight | Size | Line-Height | Color |
|---------|------|--------|------|-------------|-------|
| Label | DM Sans | 500 | 16px | 1.3 | `#AEA7A3` |
| Sub-label | DM Sans | 400 | 14px | 1.4 | `#959595` |

**Rules:**
- Labels are sentence case, not uppercase — friendlier tone
- Sub-labels are lighter weight and color, clearly subordinate
- No all-caps anywhere in this section

---

### Layout (Desktop ≥1024px)

```
┌─────────────────────────────────────────────────────────────┐
│  Background: #2E2E2E                                        │
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌────┐│
│  │ [Icon]      │  │ [Icon]      │  │ [Icon]      │  │[Ic]││
│  │ Based in    │  │ Replies     │  │ Fixed       │  │Wee ││
│  │ Windhoek    │  │ within      │  │ quotes      │  │upd ││
│  │ Serving     │  │ 24 hours    │  │ No hidden   │  │You ││
│  │ Namibian    │  │ No ghosting │  │ fees        │  │alwa││
│  │ SMEs        │  │             │  │             │  │know││
│  └─────────────┘  └─────────────┘  └─────────────┘  └────┘│
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

- 4 columns, equal width
- Gap between columns: 32px
- Content within each column: left-aligned
- Icon (if used) above the label, 24px size, color `#795238` (warm brown accent)
- Icon-to-label gap: 12px

---

### Layout (Tablet 768px–1023px)

- 2×2 grid
- Gap: 24px
- Padding: 40px 24px

---

### Layout (Mobile <768px)

- Single column, stacked vertically
- Each item: horizontal row (icon left, text right) OR vertical stack
- Gap between items: 24px
- Padding: 32px 20px
- Preferred: horizontal row — icon 24px, text block to the right, saves vertical space

```
┌─────────────────────────────┐
│  [Icon]  Based in Windhoek   │
│          Serving Namibian    │
│          SMEs                │
│                             │
│  [Icon]  Replies within      │
│          24 hours            │
│          No ghosting         │
│                             │
│  ...etc                     │
└─────────────────────────────┘
```

---

### Icons

**Option A: SVG Icons (preferred)**
Use inline SVGs for each icon — no icon library dependency. Keep them simple, line-style, 24px, stroke-width 1.5px.

| Item | SVG Concept |
|------|-------------|
| Based in Windhoek | Map pin / location marker |
| Replies within 24h | Clock or speech bubble with clock |
| Fixed quotes | Document with checkmark or shield |
| Weekly updates | Circular arrows or checkmark list |

**Icon color:** `#795238` (warm brown accent) — ties to hero CTA color

**Option B: No icons**
If SVGs feel like too much for this pass, use a small decorative dot or dash in `#795238` as a visual marker before each label. The text must carry the weight.

**Rules:**
- Icons are supplementary — if they fail to load, the text still communicates fully
- No emojis in place of icons (inconsistent rendering, accessibility issues)
- Icons should not animate

---

### Spacing & Rhythm

```css
.credibility-strip {
  padding: 48px 20px;  /* Mobile default */
}

@media (min-width: 768px) {
  .credibility-strip {
    padding: 48px 24px;
  }
}

@media (min-width: 1024px) {
  .credibility-strip {
    padding: 48px 0;  /* Content container handles horizontal padding */
  }
}

.credibility-grid {
  display: grid;
  grid-template-columns: 1fr;  /* Mobile */
  gap: 24px;
  max-width: 1200px;
  margin: 0 auto;
}

@media (min-width: 768px) {
  .credibility-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 32px;
  }
}

@media (min-width: 1024px) {
  .credibility-grid {
    grid-template-columns: repeat(4, 1fr);
    gap: 32px;
  }
}
```

---

## CONTENT (USE EXACTLY)

### Item 1
```
Label:       Based in Windhoek
Sub-label:   Serving Namibian SMEs
```

### Item 2
```
Label:       Replies within 24 hours
Sub-label:   No ghosting, no delays
```

### Item 3
```
Label:       Fixed quotes
Sub-label:   No hidden fees, no surprises
```

### Item 4
```
Label:       Weekly updates
Sub-label:   You always know the status
```

**Rules:**
- No changes to copy without client approval
- Tone is plain, direct, confident — matching the "friendly & approachable" positioning
- "No ghosting" is slightly informal but fits the brand — keep it

---

## INTERACTION & MOTION

### On Scroll Into View (optional enhancement)
If the hero has scroll-triggered animations, this section should animate in subtly when it enters the viewport:

```css
.credibility-item {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 600ms ease, transform 600ms ease;
}

.credibility-item.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Stagger: 100ms between items */
.credibility-item:nth-child(1) { transition-delay: 0ms; }
.credibility-item:nth-child(2) { transition-delay: 100ms; }
.credibility-item:nth-child(3) { transition-delay: 200ms; }
.credibility-item:nth-child(4) { transition-delay: 300ms; }
```

**Rules:**
- Use IntersectionObserver to trigger (not scroll events)
- Animation is subtle — fade + small lift, not dramatic
- If `prefers-reduced-motion: reduce`, items appear instantly (opacity 1, no transform)
- If the hero doesn't have scroll animations, skip this — consistency matters more than effects

### Hover States (desktop only)
```css
.credibility-item:hover .credibility-label {
  color: #F8F9FB;  /* Slight brightening — off-white from brand kit */
  transition: color 200ms ease;
}
```

**Rules:**
- Subtle only — no background change, no border, no scale
- The hover effect should feel like a gentle acknowledgment, not a call to action

---

## ACCESSIBILITY

- Semantic HTML: `<section>` with `aria-label="Why work with me"`
- Each item: `<article>` or `<div>` with proper heading structure
- Icons: `aria-hidden="true"` if decorative, or `role="img"` with `aria-label` if meaningful
- Color contrast:
  - Label `#AEA7A3` on `#2E2E2E` = 5.4:1 ✓ (passes AA)
  - Sub-label `#959595` on `#2E2E2E` = 4.7:1 ✓ (passes AA for large text, borderline for small — acceptable for secondary text)
- Keyboard: No interactive elements in this section (no tab stops needed)

---

## PERFORMANCE

- No images — CSS and SVG only
- No external libraries
- If using IntersectionObserver for scroll animation, use a simple threshold of 0.2
- Target: No impact on Lighthouse Performance score

---

## INTEGRATION WITH EXISTING HERO

This section sits **immediately below** the hero section in the DOM:

```html
<body>
  <header class="hero">...</header>

  <section class="credibility-strip" aria-label="Why work with me">
    ...
  </section>

  <!-- Next section: Services Preview -->
</body>
```

**Visual flow:**
- Hero: `#242323` (near black)
- Credibility Strip: `#2E2E2E` (slightly lighter charcoal)
- The color shift creates a subtle "breathing" effect between sections
- No hard lines, no borders — the palette does the work

---

## NO-GO LIST (Do NOT implement)

- [ ] No fake testimonials or quotes
- [ ] No client logos (the client doesn't have permission or quantity yet)
- [ ] No star ratings
- [ ] No "Trusted by..." language
- [ ] No counters or animated numbers ("100+ projects")
- [ ] No carousel or slider
- [ ] No background images or video
- [ ] No parallax effects
- [ ] No border-top/bottom on the section

---

## DELIVERABLE

An updated `index.html` containing:
1. All existing hero section code (unchanged)
2. The new credibility strip section immediately after the hero
3. Embedded CSS for the new section
4. No console errors
5. No visual regressions to the hero

---

## VERIFICATION CHECKLIST

- [ ] Section appears immediately below hero with correct background color shift
- [ ] 4 items visible in horizontal row on desktop (≥1024px)
- [ ] 2×2 grid on tablet (768–1023px)
- [ ] Stacked vertically on mobile (<768px), readable without zoom
- [ ] Icons (or markers) present and consistent in `#795238`
- [ ] Typography matches spec: DM Sans, correct weights, sizes, colors
- [ ] No fake social proof — all content is honest commitment-based
- [ ] Scroll animation (if implemented) uses IntersectionObserver and respects reduced motion
- [ ] Lighthouse Accessibility score ≥95
- [ ] No layout shift or overflow at any breakpoint

---

*Prompt version 1.0 — Credibility Strip, Option 2 implementation*
