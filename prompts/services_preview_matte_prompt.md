# AI Developer Prompt: Services Preview Section (Restyled)
## For Cursor, GitHub Copilot, or similar AI coding agents

---

## ROLE DEFINITION

You are a **Frontend Developer & UI Engineer** specializing in:
- Semantic, accessible HTML
- Modern CSS (Flexbox, Grid, custom properties, backdrop-filter)
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
**Current state:** Hero section and Credibility Strip are complete and locked. This is the **third section** on the homepage.

**Design reference:** The client has provided a pricing section reference image showing:
- 3 dark cards with rounded corners (16px+ radius)
- A large "Pricing" display headline behind the cards
- Subtle glass/blur effects on the cards
- Clean feature lists with checkmark bullets
- Centered layout with generous spacing

**Client instruction:** Follow the same UI/UX structure and mood as the reference, but **remove all gloss, shine, and glassmorphic blur effects**. The result should feel dark, grounded, and matte — consistent with the warm, approachable brand.

---

## TASK

Build a **Services Preview** section that adapts the reference's structural language (3 cards, large background headline, rounded corners, clean feature lists) to Adrian's matte, warm brand palette. No glossy effects. No glassmorphism. No reflective surfaces.

---

## DESIGN SPECIFICATION

### Section Container

```css
.services-section {
  background-color: #242323;  /* Same as hero — seamless dark canvas */
  padding: 120px 20px 80px;   /* Extra top padding for the large background headline */
  width: 100%;
  position: relative;         /* For the background headline positioning */
  overflow: hidden;           /* Background headline may bleed — contain it */
}
```

**Rules:**
- No border-top or border-bottom
- Full-width background, content constrained to max-width 1200px centered
- The large background headline sits behind the cards — `position: absolute`, `z-index: 0`
- Cards sit above at `z-index: 1`

---

### Background Display Headline (Behind Cards)

```
SERVICES
```

**Purpose:** Creates depth and visual drama without glossy effects. The word is large, faint, and sits behind the cards as a structural layer.

```css
.services-bg-headline {
  position: absolute;
  top: 40px;                    /* Sits above the cards, partially visible */
  left: 50%;
  transform: translateX(-50%);
  font-family: 'Syne', sans-serif;
  font-weight: 800;
  font-size: clamp(80px, 12vw, 160px);  /* Massive, responsive */
  color: #363636;               /* Barely visible against #242323 bg — matte, not glossy */
  letter-spacing: -2px;
  text-transform: uppercase;
  white-space: nowrap;
  z-index: 0;
  pointer-events: none;         /* Not interactive */
  user-select: none;
}
```

**Rules:**
- NO `backdrop-filter`, NO `filter: blur()`, NO `opacity` tricks
- NO gradient overlays, NO shine effects
- Color `#363636` on `#242323` creates subtle contrast — matte and intentional
- The headline should feel like a watermark or embossed stamp, not a light reflection
- On mobile: `font-size: clamp(60px, 15vw, 100px)` — still large but doesn't crowd cards

---

### Section Header (Above Cards)

```
What I Build
Websites that win you customers — at a price that makes sense for Namibian SMEs.
```

| Element | Font | Weight | Size | Line-Height | Color |
|---------|------|--------|------|-------------|-------|
| Heading "What I Build" | Syne | 700 | 42px | 1.1 | `#AEA7A3` |
| Subheading | DM Sans | 400 | 18px | 1.6 | `#959595` |

**Positioning:** Centered above the cards, `z-index: 1`, `position: relative`.

**On mobile:** heading 32px, subheading 16px.

---

### Three-Tier Cards (Desktop ≥1024px)

```
                    ┌─────────────────────────────────────┐
                    │                                     │
    ┌──────────┐    │  S E R V I C E S  (faint, behind) │    ┌──────────┐
    │          │    │                                     │    │          │
    │ STARTER  │    │                                     │    │ PREMIUM  │
    │          │    │    ┌─────────────────────────┐    │    │          │
    │ From     │    │    │                         │    │    │ From     │
    │ N$8,000  │    │    │       GROWTH            │    │    │ N$35,000 │
    │          │    │    │       ★ MOST POPULAR    │    │    │          │
    │ [features]│   │    │       From N$18,000     │    │    │ [features]│
    │          │    │    │                         │    │    │          │
    │ [Get     │    │    │       [features]         │    │    │ [Get     │
    │  Quote]  │    │    │                         │    │    │  Quote]  │
    │          │    │    │       [Get Quote]       │    │    │          │
    └──────────┘    │    └─────────────────────────┘    │    └──────────┘
                    │                                     │
                    └─────────────────────────────────────┘
```

**Layout:**
- 3 columns, equal width
- Gap: 24px
- Cards have consistent internal padding: 40px
- Cards are vertically aligned at top (not equal height — the featured card may be taller naturally)

---

### Card Design (MATTE — NO GLOSS)

**Base Card:**
```css
.service-card {
  background-color: #363636;      /* Solid matte dark gray — no transparency, no blur */
  border: 1px solid #4A4A4A;    /* Subtle border, slightly lighter than card bg */
  border-radius: 20px;          /* Generous rounding — from reference */
  padding: 40px;
  display: flex;
  flex-direction: column;
  position: relative;
  z-index: 1;
}
```

**Featured Card (Growth — center):**
```css
.service-card--featured {
  background-color: #2E2E2E;    /* Slightly lighter than base — stands out matte-style */
  border: 2px solid #795238;      /* Warm brown accent border — matte, not glowing */
  transform: translateY(-12px); /* Elevated physically, not via shadow intensity */
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);  /* Deep, soft, matte shadow — no highlight */
}
```

**Rules — NO GLOSS:**
- NO `backdrop-filter: blur()` — cards are solid, not glass
- NO `background: rgba(255,255,255,0.05)` — no transparency
- NO `box-shadow: inset 0 1px 0 rgba(255,255,255,0.1)` — no top highlight/gloss line
- NO `filter: brightness()` or `filter: contrast()` tricks
- NO `linear-gradient` overlays on cards — solid colors only
- NO `border-top: 1px solid rgba(255,255,255,0.1)` — no faux light reflection
- The featured card's elevation comes from `transform` + deep shadow, not from a lighter top edge

---

### Card Content Structure

1. **Tier name** (top)
   ```css
   font-family: 'Syne', sans-serif;
   font-weight: 700;
   font-size: 22px;
   color: #AEA7A3;
   margin-bottom: 4px;
   text-transform: uppercase;
   letter-spacing: 1px;
   ```

2. **"MOST POPULAR" badge** (featured card only)
   ```css
   display: inline-block;
   background-color: #795238;      /* Warm brown — matte, not glossy */
   color: #242323;
   font-family: 'DM Sans', sans-serif;
   font-weight: 500;
   font-size: 11px;
   text-transform: uppercase;
   letter-spacing: 1.5px;
   padding: 6px 14px;
   border-radius: 20px;            /* Pill shape from reference */
   margin-bottom: 20px;
   ```

3. **Price**
   ```css
   font-family: 'Syne', sans-serif;
   font-weight: 700;
   font-size: 42px;
   color: #F8F9FB;                 /* Off-white for maximum contrast */
   margin-bottom: 4px;
   line-height: 1;
   ```
   Sub-line: "Starting price" in `#959595`, 13px, letter-spacing 0.5px

4. **Divider line**
   ```css
   width: 100%;
   height: 1px;
   background-color: #4A4A4A;      /* Subtle separator — matte */
   margin: 24px 0;
   ```
   NO gradient on the divider — solid color only

5. **"Best for" description**
   ```css
   font-family: 'DM Sans', sans-serif;
   font-weight: 400;
   font-size: 15px;
   color: #959595;
   line-height: 1.5;
   margin-bottom: 24px;
   ```

6. **Feature list** (bullets)
   ```css
   list-style: none;
   padding: 0;
   margin: 0 0 32px 0;
   ```
   Each item:
   ```css
   font-family: 'DM Sans', sans-serif;
   font-weight: 400;
   font-size: 14px;
   color: #AEA7A3;
   line-height: 1.6;
   padding-left: 28px;
   position: relative;
   margin-bottom: 14px;
   ```
   Bullet marker: small checkmark SVG or character (✓) in `#795238`, positioned absolute left, 16px size

7. **CTA Button** (bottom)
   ```css
   margin-top: auto;               /* Pushes to bottom */
   display: block;
   width: 100%;
   padding: 16px 24px;
   background-color: transparent;
   color: #AEA7A3;
   font-family: 'DM Sans', sans-serif;
   font-weight: 500;
   font-size: 15px;
   text-align: center;
   border-radius: 12px;            /* Rounded from reference */
   border: 1px solid #4A4A4A;      /* Subtle border — matte */
   text-decoration: none;
   transition: background-color 300ms ease, color 300ms ease, border-color 300ms ease, transform 300ms ease;
   ```

   **Featured card CTA (inverted):**
   ```css
   .service-card--featured .service-cta {
     background-color: #795238;    /* Warm brown fill */
     color: #242323;                 /* Dark text */
     border: 1px solid #795238;
   }
   ```

   **Hover states:**
   ```css
   .service-cta:hover {
     background-color: #4A4A4A;
     color: #F8F9FB;
     border-color: #6A6A6A;
   }

   .service-card--featured .service-cta:hover {
     background-color: #8B6348;      /* Lighter warm brown */
     color: #242323;
     border-color: #8B6348;
     transform: translateY(-2px);
     box-shadow: 0 8px 24px rgba(121, 82, 56, 0.3);
   }
   ```

---

### CONTENT (USE EXACTLY)

#### Card 1: Starter

```
Tier:        STARTER
Price:       From N$8,000
Sub-label:   Starting price
Best for:    New businesses and solo entrepreneurs who need a professional online presence fast.

Features:
✓ 1–3 pages (Home, About, Contact)
✓ Mobile-friendly design
✓ Contact form + WhatsApp integration
✓ Basic on-page SEO
✓ 1 week delivery
✓ 1 round of revisions

CTA:         Get a Quote
```

#### Card 2: Growth (FEATURED)

```
Tier:        GROWTH
Badge:       MOST POPULAR
Price:       From N$18,000
Sub-label:   Starting price
Best for:    Established SMEs ready to turn visitors into customers.

Features:
✓ 3–6 pages with clear conversion flow
✓ Content Management System (WordPress)
✓ Speed optimized (fast load times)
✓ Google Analytics setup
✓ Contact forms + WhatsApp Business
✓ On-page SEO + sitemap submission
✓ 2 weeks delivery
✓ 2 rounds of revisions

CTA:         Get a Quote
```

#### Card 3: Premium

```
Tier:        PREMIUM
Price:       From N$35,000
Sub-label:   Starting price
Best for:    Businesses needing custom functionality or advanced performance.

Features:
✓ 6+ pages, custom design
✓ Custom features (booking, membership, etc.)
✓ Advanced SEO strategy
✓ Performance monitoring setup
✓ Priority support (48h response)
✓ 3–4 weeks delivery
✓ 3 rounds of revisions

CTA:         Get a Quote
```

**Rules:**
- "From N$X,000" — "From" is critical. These are starting prices.
- Feature lists are honest — no "unlimited" anything
- Delivery timelines are estimates

---

### Retainer Callout (Below Cards)

```
Heading:     Need ongoing support?
Body:        Monthly maintenance, updates, and priority support — so your site stays fast and secure.
Price:       From N$2,000/month
CTA:         Learn More →
```

**Design:**
- Not a card — a clean horizontal row
- Background: transparent (inherits `#242323` from section)
- Top border: `1px solid #363636` — subtle separator from cards above
- Padding: 48px 0 0
- Layout: flex row, space-between, align-center
- Left: text block
- Right: text-link CTA (not a button — different hierarchy from cards)

```css
.retainer-callout {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 24px;
  padding-top: 48px;
  border-top: 1px solid #363636;
  margin-top: 48px;
  position: relative;
  z-index: 1;
}

.retainer-cta {
  color: #795238;
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  font-size: 15px;
  text-decoration: none;
  transition: color 200ms ease;
}

.retainer-cta:hover {
  color: #8B6348;
}
```

**On mobile:** Stack vertically, CTA below text, left-aligned.

---

## RESPONSIVE BREAKPOINTS

| Breakpoint | Layout |
|------------|--------|
| ≥1024px | 3 cards side by side, featured card elevated (-12px), background headline visible |
| 768–1023px | 3 cards side by side, smaller padding (32px), featured card not elevated, background headline smaller |
| <768px | Stacked vertically, featured card FIRST, background headline hidden or very small, full-width cards |

**Mobile adjustments:**
- Section padding: 80px 20px 60px
- Card padding: 32px
- Card border-radius: 16px
- Price: 32px
- Tier name: 18px
- Background headline: hidden or `font-size: 60px`, `opacity: 0.3`
- Gap between cards: 16px

---

## INTERACTION & MOTION

### Card Hover (desktop only)
```css
.service-card:hover {
  border-color: #5A5A5A;         /* Slightly brighter border — matte */
  transition: border-color 300ms ease;
}

.service-card--featured:hover {
  border-color: #8B6348;          /* Warmer border on hover */
  transform: translateY(-14px);   /* Slightly more lift */
  transition: border-color 300ms ease, transform 300ms ease;
}
```

**Rules:**
- NO hover glow effects
- NO `box-shadow` expansion on non-featured cards
- NO `filter: brightness(1.1)` or similar
- The featured card's hover is the only one with lift + shadow change

### Scroll Animation (optional, consistent with previous sections)
If IntersectionObserver is used elsewhere:

```css
.service-card {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 600ms ease, transform 600ms ease;
}

.service-card.visible {
  opacity: 1;
  transform: translateY(0);
}

.service-card--featured {
  transition-delay: 0ms;
}

.service-card:nth-child(1) { transition-delay: 100ms; }
.service-card:nth-child(2) { transition-delay: 0ms; }
.service-card:nth-child(3) { transition-delay: 200ms; }
```

Respect `prefers-reduced-motion`.

---

## ACCESSIBILITY

- Semantic HTML:
  - `<section>` with `aria-label="Services and pricing"`
  - Cards: `<article>` elements
  - Feature lists: `<ul>` with `<li>`
  - CTA buttons: `<a>` with descriptive text
- Background headline: `aria-hidden="true"` — decorative only
- Color contrast:
  - Price `#F8F9FB` on `#363636` = 10.5:1 ✓
  - Feature text `#AEA7A3` on `#363636` = 5.2:1 ✓
  - Badge text `#242323` on `#795238` = 4.6:1 ✓
- Focus states:
  - CTA buttons: `outline: 2px solid #AEA7A3, outline-offset: 4px`

---

## PERFORMANCE

- No images in this section
- No external libraries
- `backdrop-filter` is NOT used — no performance penalty from blur
- Reuse existing IntersectionObserver if present
- Target: No impact on Lighthouse Performance score

---

## INTEGRATION WITH EXISTING SECTIONS

DOM order:
```html
<body>
  <header class="hero">...</header>
  <section class="credibility-strip" aria-label="Why work with me">...</section>
  <section class="services-section" aria-label="Services and pricing">
    <div class="services-bg-headline" aria-hidden="true">SERVICES</div>
    <div class="services-content">
      <h2>What I Build</h2>
      <p>...</p>
      <div class="services-grid">...</div>
      <div class="retainer-callout">...</div>
    </div>
  </section>
</body>
```

---

## NO-GO LIST (Do NOT implement)

- [ ] NO `backdrop-filter: blur()` — matte solid cards only
- [ ] NO `background: rgba(...)` with transparency — solid colors only
- [ ] NO `box-shadow: inset` with white/light values — no faux gloss
- [ ] NO `border-top` or `border-bottom` with light colors — no highlight lines
- [ ] NO `filter: brightness()`, `filter: contrast()`, `filter: saturate()`
- [ ] NO gradient overlays on cards or background
- [ ] NO toggle switches (monthly/yearly)
- [ ] No strikethrough "original prices" — no fake discounts
- [ ] No "Limited time offer" urgency
- [ ] No carousel or slider
- [ ] No background images or video
- [ ] No parallax effects

---

## DELIVERABLE

An updated `index.html` containing:
1. All existing hero section code (unchanged)
2. All existing credibility strip code (unchanged)
3. The new services preview section immediately after credibility strip
4. Embedded CSS for the new section
5. No console errors
6. No visual regressions to previous sections

---

## VERIFICATION CHECKLIST

- [ ] Background "SERVICES" headline is faint, matte, not glossy — visible but not distracting
- [ ] 3 cards visible in horizontal row on desktop (≥1024px), featured card elevated
- [ ] Cards have rounded corners (20px), solid matte backgrounds, no blur or transparency
- [ ] Featured card has "MOST POPULAR" badge, warm brown border, slight elevation
- [ ] NO glossy highlights, NO light reflections, NO glass effects on any card
- [ ] Divider lines between price and features are solid, not gradient
- [ ] CTA buttons: outline style on base cards, filled on featured card
- [ ] On mobile (<768px): stacked, featured first, background headline hidden or minimal
- [ ] All prices show "From N$X,000"
- [ ] Retainer callout appears below cards, clean horizontal layout
- [ ] Lighthouse Accessibility score ≥95
- [ ] No layout shift, overflow, or broken text wrapping at any breakpoint

---

*Prompt version 2.0 — Services Preview, matte restyle from reference*
