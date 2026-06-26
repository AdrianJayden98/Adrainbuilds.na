# AI Developer Prompt: Services Preview Section
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
**Current state:** Hero section and Credibility Strip are complete and locked. This is the **third section** on the homepage.

**Why this section exists:** To qualify leads by showing what Adrian offers and what it costs. Namibian SMEs are price-sensitive but value-clarity-seeking. Showing ranges filters out tire-kickers and attracts serious inquiries.

---

## TASK

Build a **Services Preview** section — three pricing tier cards plus a retainer callout — that converts visitors into quote requests.

This section must feel like a natural continuation of the hero's visual language while serving a distinct purpose: answering "What do you offer, and can I afford it?"

---

## DESIGN SPECIFICATION

### Section Container

```css
.services-section {
  background-color: #242323;  /* Same as hero — seamless flow, credibility strip was the breath */
  padding: 80px 20px;         /* Generous vertical space — this is a heavy content section */
  width: 100%;
}
```

**Rules:**
- No border-top or border-bottom
- Full-width background, content constrained to max-width 1200px centered
- The section needs to feel substantial — 80px top/bottom padding minimum

---

### Section Header

```
What I Build
Websites that win you customers — at a price that makes sense for Namibian SMEs.
```

| Element | Font | Weight | Size | Line-Height | Color |
|---------|------|--------|------|-------------|-------|
| Heading "What I Build" | Syne | 700 | 48px | 1.1 | `#AEA7A3` |
| Subheading | DM Sans | 400 | 18px | 1.6 | `#959595` |

**Rules:**
- Heading: left-aligned, max-width 600px
- Subheading: left-aligned below heading, max-width 600px
- On mobile: heading 36px, subheading 16px
- No center alignment — left-aligned feels more direct and personal

---

### Three-Tier Cards (Desktop ≥1024px)

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  What I Build                                               │
│  Websites that win you customers...                         │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │              │  │  ★ MOST      │  │              │     │
│  │  STARTER     │  │  POPULAR     │  │  PREMIUM     │     │
│  │              │  │              │  │              │     │
│  │  From        │  │  From        │  │  From        │     │
│  │  N$8,000     │  │  N$18,000    │  │  N$35,000    │     │
│  │              │  │              │  │              │     │
│  │  Best for:   │  │  Best for:   │  │  Best for:   │     │
│  │  new         │  │  established │  │  businesses  │     │
│  │  businesses  │  │  SMEs ready  │  │  needing     │     │
│  │              │  │  to convert  │  │  custom work │     │
│  │              │  │  visitors    │  │              │     │
│  │  • Feature   │  │  • Feature   │  │  • Feature   │     │
│  │  • Feature   │  │  • Feature   │  │  • Feature   │     │
│  │  • Feature   │  │  • Feature   │  │  • Feature   │     │
│  │  • Feature   │  │  • Feature   │  │  • Feature   │     │
│  │              │  │  • Feature   │  │  • Feature   │     │
│  │              │  │  • Feature   │  │  • Feature   │     │
│  │              │  │              │  │              │     │
│  │  [Get a     │  │  [Get a     │  │  [Get a     │     │
│  │   Quote]    │  │   Quote]    │  │   Quote]    │     │
│  │              │  │              │  │              │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                             │
│              ┌─────────────────────────────┐              │
│              │  Need ongoing support?        │              │
│              │  Retainer from N$2,000/month  │              │
│              │  [Learn More →]               │              │
│              └─────────────────────────────┘              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Layout:**
- 3 columns, equal width
- Gap: 24px
- Cards have consistent internal padding: 32px

---

### Card Design

**Base Card:**
```css
.service-card {
  background-color: #363636;  /* Dark gray, lighter than section bg */
  border: 1px solid #525254;  /* Subtle border for definition */
  border-radius: 8px;
  padding: 32px;
  display: flex;
  flex-direction: column;
  height: 100%;  /* Equal height cards in grid */
}
```

**Featured Card (Growth — middle):**
```css
.service-card--featured {
  background-color: #2E2E2E;  /* Slightly lighter than base — stands out */
  border: 2px solid #795238;  /* Warm brown accent border */
  transform: translateY(-8px);  /* Elevated physically */
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.3);
}
```

**Rules:**
- Featured card is the visual anchor — the eye goes there first
- Elevation (`translateY(-8px)`) must not cause overflow or overlap issues
- On mobile, featured card appears first in the stack

---

### Card Content Structure

Each card contains:

1. **Tier name** (top)
   ```css
   font-family: 'Syne', sans-serif;
   font-weight: 700;
   font-size: 24px;
   color: #AEA7A3;
   margin-bottom: 8px;
   ```

2. **"MOST POPULAR" badge** (featured card only)
   ```css
   display: inline-block;
   background-color: #795238;
   color: #242323;
   font-family: 'DM Sans', sans-serif;
   font-weight: 500;
   font-size: 12px;
   text-transform: uppercase;
   letter-spacing: 1px;
   padding: 4px 12px;
   border-radius: 4px;
   margin-bottom: 16px;
   ```

3. **Price**
   ```css
   font-family: 'Syne', sans-serif;
   font-weight: 700;
   font-size: 36px;
   color: #F8F9FB;  /* Off-white for maximum contrast */
   margin-bottom: 4px;
   ```
   Sub-line: "Starting price" in `#959595`, 14px

4. **"Best for" description**
   ```css
   font-family: 'DM Sans', sans-serif;
   font-weight: 400;
   font-size: 15px;
   color: #959595;
   line-height: 1.5;
   margin-bottom: 24px;
   ```

5. **Feature list** (bullets)
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
   padding-left: 20px;
   position: relative;
   margin-bottom: 12px;
   ```
   Bullet marker: small checkmark or dot in `#795238`, positioned absolute left

6. **CTA Button** (bottom, always at card bottom)
   ```css
   margin-top: auto;  /* Pushes button to bottom of card */
   ```
   Same styling as hero CTA but full-width within card:
   ```css
   display: block;
   width: 100%;
   padding: 14px 24px;
   background-color: #795238;
   color: #242323;
   font-family: 'DM Sans', sans-serif;
   font-weight: 500;
   font-size: 15px;
   text-align: center;
   border-radius: 4px;
   text-decoration: none;
   transition: background-color 300ms ease, transform 300ms ease, box-shadow 300ms ease;
   ```
   Hover: `background-color: #8B6348`, `transform: translateY(-2px)`, `box-shadow: 0 8px 24px rgba(121, 82, 56, 0.3)`

---

### CONTENT (USE EXACTLY)

#### Card 1: Starter

```
Tier:        Starter
Price:       From N$8,000
Best for:    New businesses and solo entrepreneurs who need a professional online presence fast.

Features:
• 1–3 pages (Home, About, Contact)
• Mobile-friendly design
• Contact form + WhatsApp integration
• Basic on-page SEO
• 1 week delivery
• 1 round of revisions
```

#### Card 2: Growth (FEATURED)

```
Tier:        Growth
Badge:       MOST POPULAR
Price:       From N$18,000
Best for:    Established SMEs ready to turn visitors into customers.

Features:
• 3–6 pages with clear conversion flow
• Content Management System (WordPress)
• Speed optimized (fast load times)
• Google Analytics setup
• Contact forms + WhatsApp Business
• On-page SEO + sitemap submission
• 2 weeks delivery
• 2 rounds of revisions
```

#### Card 3: Premium

```
Tier:        Premium
Price:       From N$35,000
Best for:    Businesses needing custom functionality or advanced performance.

Features:
• 6+ pages, custom design
• Custom features (booking, membership, etc.)
• Advanced SEO strategy
• Performance monitoring setup
• Priority support (48h response)
• 3–4 weeks delivery
• 3 rounds of revisions
```

**Rules:**
- "From N$X,000" — "From" is critical. These are starting prices, not fixed.
- No "starting from" on the price line itself — "From" is part of the price display
- Feature lists are honest — no "unlimited revisions" or "lifetime support"
- Delivery timelines are estimates, not guarantees — "1 week" not "7 days"

---

### Retainer Callout (Below Cards)

```
Heading:     Need ongoing support?
Body:        Monthly maintenance, updates, and priority support — so your site stays fast and secure.
Price:       From N$2,000/month
CTA:         Learn More →
```

**Design:**
- Not a card — a horizontal banner/row
- Background: `#2E2E2E` (same as credibility strip — creates rhythm)
- Padding: 32px
- Border-radius: 8px
- Left side: text content
- Right side: CTA button (or CTA below on mobile)
- Layout: flex row, space-between, align-center

```css
.retainer-callout {
  background-color: #2E2E2E;
  border-radius: 8px;
  padding: 32px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 24px;
  margin-top: 48px;
}
```

**On mobile:** Stack vertically, CTA full-width below text.

---

## RESPONSIVE BREAKPOINTS

| Breakpoint | Layout |
|------------|--------|
| ≥1024px | 3 cards side by side, featured card elevated |
| 768–1023px | 3 cards side by side, smaller padding (24px), featured card not elevated (no room) |
| <768px | Stacked vertically, featured card FIRST, full-width cards |

**Mobile adjustments:**
- Section padding: 60px 20px
- Card padding: 24px
- Price: 28px
- Tier name: 20px
- Gap between cards: 16px

---

## INTERACTION & MOTION

### Card Hover (desktop only)
```css
.service-card:hover {
  border-color: #6A6A6A;  /* Slightly brighter border */
  transition: border-color 300ms ease;
}

.service-card--featured:hover {
  border-color: #8B6348;  /* Warmer border on hover */
  transform: translateY(-10px);  /* Slightly more lift */
  transition: border-color 300ms ease, transform 300ms ease;
}
```

**Rules:**
- Non-featured cards: subtle border brightening only — no lift (they're not the focus)
- Featured card: maintains elevation + slightly more lift on hover
- No shadow changes on non-featured cards

### Scroll Animation (optional, consistent with credibility strip)
If the page uses IntersectionObserver for scroll-triggered animations:

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
  transition-delay: 0ms;  /* Featured card animates first or simultaneously */
}

.service-card:nth-child(1) { transition-delay: 100ms; }
.service-card:nth-child(2) { transition-delay: 0ms; }   /* Featured first */
.service-card:nth-child(3) { transition-delay: 200ms; }
```

**Rules:**
- If credibility strip has no scroll animation, skip this — consistency matters
- If implementing, use the same IntersectionObserver threshold (0.2)
- Respect `prefers-reduced-motion`

---

## ACCESSIBILITY

- Semantic HTML:
  - `<section>` with `aria-label="Services and pricing"`
  - Cards: `<article>` elements
  - Feature lists: `<ul>` with `<li>`
  - CTA buttons: `<a>` with descriptive text (not "Click here")
- Color contrast:
  - Price `#F8F9FB` on `#363636` = 10.5:1 ✓
  - Feature text `#AEA7A3` on `#363636` = 5.2:1 ✓
  - Badge text `#242323` on `#795238` = 4.6:1 ✓ (large text)
- Focus states:
  - CTA buttons: `outline: 2px solid #AEA7A3, outline-offset: 4px`
  - Cards: no focus needed (not interactive)
- Screen readers:
  - "MOST POPULAR" badge should be announced before the tier name
  - Feature list items are clear and scannable

---

## PERFORMANCE

- No images in this section — CSS-only
- No external libraries
- If using scroll animation, reuse the same IntersectionObserver from credibility strip (don't create a new one)
- Target: No impact on Lighthouse Performance score

---

## INTEGRATION WITH EXISTING SECTIONS

DOM order:
```html
<body>
  <header class="hero">...</header>
  <section class="credibility-strip" aria-label="Why work with me">...</section>
  <section class="services-section" aria-label="Services and pricing">
    ...
  </section>
</body>
```

Visual flow:
- Hero: `#242323` (near black)
- Credibility Strip: `#2E2E2E` (lighter charcoal — breath)
- Services: `#242323` (back to near black — section feels grounded)

---

## NO-GO LIST (Do NOT implement)

- [ ] No toggle switches (monthly/yearly) — Adrian doesn't offer subscription tiers
- [ ] No "Compare plans" table — 3 cards are clearer
- [ ] No strikethrough "original prices" — no fake discounts
- [ ] No "Limited time offer" urgency tactics — not his brand
- [ ] No checkmark/X comparison graphics — keep it clean
- [ ] No popups or modals for "Get a quote" — link to contact section or mailto
- [ ] No carousel or slider for cards
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

- [ ] Section heading and subheading left-aligned, readable
- [ ] 3 cards visible in horizontal row on desktop (≥1024px), featured card elevated
- [ ] Featured card has "MOST POPULAR" badge, warm brown border, slight elevation
- [ ] Cards equal height on desktop (buttons align at bottom)
- [ ] On tablet (768–1023px): 3 cards side by side, no elevation (space constraint)
- [ ] On mobile (<768px): stacked vertically, featured card first, full-width
- [ ] All prices show "From N$X,000" — "From" is present and visible
- [ ] Feature lists use warm brown (`#795238`) bullet markers
- [ ] CTA buttons full-width within cards, hover state works
- [ ] Retainer callout appears below cards, horizontal on desktop, stacked on mobile
- [ ] No fake urgency, no fake discounts, no subscription toggles
- [ ] Lighthouse Accessibility score ≥95
- [ ] No layout shift, overflow, or broken text wrapping at any breakpoint

---

*Prompt version 1.0 — Services Preview, 3-tier cards + retainer callout*
