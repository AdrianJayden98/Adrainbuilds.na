# AI Developer Prompt: Footer Section
## For Cursor, GitHub Copilot, or similar AI coding agents

---

## ROLE DEFINITION

You are a **Frontend Developer & UI Engineer** specializing in:
- Semantic, accessible HTML
- Modern CSS (Flexbox, Grid, custom properties)
- Image optimization and responsive backgrounds
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
**Current state:** Hero, Credibility Strip, Services Preview, Selected Work, Process, About Snippet, and Final CTA sections are complete and locked. This is the **footer** — the final element of the homepage.

**Asset provided:** `Desert in Namibia.jpeg` — a landscape photo of Namibian sand dunes (warm orange/brown tones, blue sky, natural curves).

**Client question:** Should the image be a strip at the top of the footer, or the full footer background? **Answer: Use it as a full background image for the footer, with a dark overlay.** This creates a stronger visual finish and ties the "local Namibian" positioning into the very last thing visitors see.

---

## TASK

Build a **Footer** section that closes the homepage with a warm, grounded sense of place. The Namibian desert image is used as a full background with a dark overlay, making the footer feel like a window into the landscape Adrian works from.

This is the final impression — it should feel calm, confident, and complete.

---

## DESIGN SPECIFICATION

### Section Container

```css
.footer-section {
  position: relative;
  width: 100%;
  background-color: #242323;  /* Fallback before image loads */
  padding: 80px 20px 40px;    /* Generous top padding, tighter bottom */
  overflow: hidden;
}
```

---

### Background Image with Overlay

```css
.footer-section::before {
  content: '';
  position: absolute;
  inset: 0;  /* top: 0; right: 0; bottom: 0; left: 0 */
  background-image: url('Desert in Namibia.jpeg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  z-index: 0;
}

.footer-section::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    rgba(36, 35, 35, 0.92) 0%,    /* Very dark at top — text readable */
    rgba(36, 35, 35, 0.85) 50%,   /* Slightly lighter middle */
    rgba(36, 35, 35, 0.95) 100%   /* Very dark at bottom — grounded */
  );
  z-index: 1;
}
```

**Rules:**
- Image is `Desert in Namibia.jpeg` — assume same directory as HTML file
- `background-size: cover` — fills the footer, crops gracefully
- `background-position: center` — focuses on the dune curves
- Overlay is a CSS gradient — NOT a solid color. The gradient lets the dunes peek through subtly:
  - Top: very dark (92% opacity) so the first text is perfectly readable
  - Middle: slightly lighter (85%) so the dune shapes are felt, not seen
  - Bottom: very dark (95%) so the footer feels grounded, not floating
- The overlay color `#242323` matches the page background — seamless transition from Final CTA

**Why full background, not a strip:**
- A strip feels decorative. Full background feels immersive.
- The warm orange dunes echo the brand's warm brown accent (`#795238`) — subconscious color harmony.
- It answers "Where is this person?" without saying it.

---

### Content Structure (Above Overlay)

All content sits at `z-index: 2`, above the image and overlay.

```
┌─────────────────────────────────────────────────────────────┐
│  [Desert image with dark gradient overlay — barely visible] │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │  ADRIAN M.                                          │   │
│  │  Freelance Web Developer                            │   │
│  │  Windhoek, Namibia                                  │   │
│  │                                                     │   │
│  │  ─────────────────────────────────────────────────  │   │
│  │                                                     │   │
│  │  Home    Services    Work    Process    About       │   │
│  │                                                     │   │
│  │  ─────────────────────────────────────────────────  │   │
│  │                                                     │   │
│  │  [Instagram]  [LinkedIn]                            │   │
│  │                                                     │   │
│  │  ─────────────────────────────────────────────────  │   │
│  │                                                     │   │
│  │  © 2026 Adrian M. All rights reserved.              │   │
│  │  Built with care in Windhoek, Namibia.              │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

### Footer Content Details

**Brand Block (Top):**
```css
.footer-brand {
  text-align: center;
  margin-bottom: 40px;
}

.footer-brand-name {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 24px;
  color: #AEA7A3;
  margin-bottom: 4px;
}

.footer-brand-role {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 14px;
  color: #959595;
  margin-bottom: 4px;
}

.footer-brand-location {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 13px;
  color: #525254;
}
```

Content:
```
ADRIAN M.
Freelance Web Developer
Windhoek, Namibia
```

**Divider:**
```css
.footer-divider {
  width: 100%;
  max-width: 200px;
  height: 1px;
  background-color: #363636;
  margin: 0 auto 32px;
}
```

**Navigation Links:**
```css
.footer-nav {
  display: flex;
  justify-content: center;
  gap: 32px;
  margin-bottom: 32px;
  flex-wrap: wrap;
}

.footer-nav a {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 14px;
  color: #959595;
  text-decoration: none;
  transition: color 200ms ease;
}

.footer-nav a:hover {
  color: #AEA7A3;
}
```

Links (anchor links to page sections):
- Home → `#`
- Services → `#services`
- Work → `#work`
- Process → `#process`
- About → `#about`

**Rules:**
- These are same-page anchor links — smooth scroll if JS available
- No external links here (those are in the CTA section above)
- If a section ID doesn't exist yet, add `id` attributes to the corresponding sections

**Social Icons:**
```css
.footer-socials {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-bottom: 32px;
}

.footer-socials a {
  color: #525254;
  transition: color 200ms ease;
}

.footer-socials a:hover {
  color: #AEA7A3;
}
```

- Instagram → `https://instagram.com/adrianbuilds.na`
- LinkedIn → `https://linkedin.com/in/adrianm-dev`
- Inline SVG icons, 20px, `aria-label` required
- `target="_blank" rel="noopener noreferrer"`

**Copyright (Bottom):**
```css
.footer-copyright {
  text-align: center;
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 13px;
  color: #525254;
  line-height: 1.6;
}
```

Content:
```
© 2026 Adrian M. All rights reserved.
Built with care in Windhoek, Namibia.
```

**Rules:**
- Year is 2026 — current year
- "Built with care in Windhoek, Namibia." — reinforces local identity one last time
- Two lines, centered, very muted color

---

## RESPONSIVE BREAKPOINTS

| Breakpoint | Adjustments |
|------------|-------------|
| ≥1024px | Full layout as specified, nav links horizontal with 32px gap |
| 768–1023px | Same, padding 60px 20px 32px |
| <768px | Padding 48px 20px 24px, nav links wrap to 2 rows with 20px gap, brand name 20px |

---

## INTERACTION & MOTION

### Nav Link Hover
```css
.footer-nav a:hover {
  color: #AEA7A3;
}
```

### Social Icon Hover
```css
.footer-socials a:hover {
  color: #AEA7A3;
}
```

### Subtle Parallax (Optional, Performance-Careful)
If the client wants the desert image to feel alive:

```css
.footer-section::before {
  background-attachment: fixed;  /* Creates subtle parallax */
}
```

**Rules:**
- This is OPTIONAL — test on mobile first
- `background-attachment: fixed` can cause performance issues on some mobile browsers
- If implementing, provide a fallback:
  ```css
  @media (max-width: 768px) {
    .footer-section::before {
      background-attachment: scroll;
    }
  }
  ```
- If any jank is observed, remove it entirely — the static background is already strong

---

## ACCESSIBILITY

- Semantic HTML:
  - `<footer>` element (not `<section>`)
  - Navigation: `<nav>` with `aria-label="Footer navigation"`
  - Social links: `aria-label` required
- Color contrast:
  - Brand name `#AEA7A3` on dark overlay = 5.8:1 ✓
  - Nav links `#959595` on dark overlay = 5.1:1 ✓
  - Copyright `#525254` on dark overlay = 3.8:1 (borderline — acceptable for fine print, but bump to `#6A6A6A` if failing audit)
- Focus states:
  - Nav links: `outline: 1px solid #AEA7A3, outline-offset: 2px`
  - Social icons: same

---

## PERFORMANCE

- Image: `Desert in Namibia.jpeg` — optimize before deployment:
  - Convert to WebP with JPEG fallback if possible
  - Max width: 1920px (covers most screens)
  - Compress to ~200–400KB
  - Use `loading="lazy"` — footer is below the fold
- Overlay is CSS-only — no performance cost
- No external libraries
- Target: Image should not block First Contentful Paint

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
  <section class="about-section" aria-label="About Adrian">...</section>
  <section class="final-cta-section" aria-label="Get in touch">...</section>

  <footer class="footer-section">
    ...
  </footer>
</body>
```

**Ensure section IDs exist for anchor links:**
```html
<section id="services" class="services-section" aria-label="Services and pricing">...</section>
<section id="work" class="work-section" aria-label="Selected work">...</section>
<section id="process" class="process-section" aria-label="How we work">...</section>
<section id="about" class="about-section" aria-label="About Adrian">...</section>
```

---

## NO-GO LIST (Do NOT implement)

- [ ] No newsletter signup form in footer — already covered in CTA, don't duplicate
- [ ] No "Back to top" button — the nav links serve this purpose
- [ ] No sitemap or extensive link lists — this is a one-page site
- [ ] No third-party widgets (chat, cookies, etc.)
- [ ] No multiple columns of links — keep it minimal
- [ ] No glossy effects, glassmorphism, or blur on the overlay

---

## DELIVERABLE

An updated `index.html` containing:
1. All existing sections (hero, credibility, services, work, process, about, final-cta) — unchanged
2. The new `<footer>` element at the end of `<body>`
3. Embedded CSS for the footer
4. `id` attributes added to Services, Work, Process, and About sections for anchor links
5. Image reference to `Desert in Namibia.jpeg`
6. No console errors
7. No visual regressions to previous sections

---

## VERIFICATION CHECKLIST

- [ ] Desert image loads as full footer background, covers entire section
- [ ] Dark gradient overlay ensures all text is readable — no part of text sits on bright dune areas
- [ ] Dune shapes are subtly visible through overlay — not completely blacked out
- [ ] Brand block centered: "ADRIAN M.", "Freelance Web Developer", "Windhoek, Namibia"
- [ ] Divider line (1px, `#363636`) separates brand from nav
- [ ] Nav links horizontal on desktop, wrap gracefully on mobile: Home, Services, Work, Process, About
- [ ] Nav links are anchor links to corresponding section IDs
- [ ] Social icons (Instagram, LinkedIn) centered below nav
- [ ] Copyright: "© 2026 Adrian M. All rights reserved." + "Built with care in Windhoek, Namibia."
- [ ] All text centered, calm, not competing with the image
- [ ] On mobile: padding reduced, nav wraps, image still covers
- [ ] Image optimized (compressed, lazy-loaded)
- [ ] No newsletter form, no back-to-top button, no chat widget
- [ ] Lighthouse Accessibility score ≥95
- [ ] No layout shift, overflow, or broken text wrapping at any breakpoint

---

*Prompt version 1.0 — Footer with Namibian desert background*
