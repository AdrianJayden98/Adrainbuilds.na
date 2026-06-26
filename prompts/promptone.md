
## ROLE DEFINITION

You are a **Frontend Developer & UI Engineer** specializing in:
- Semantic, accessible HTML
- Modern CSS (Flexbox, Grid, custom properties, container queries where appropriate)
- Vanilla JavaScript for progressive enhancement (no frameworks unless specified)
- Performance-first development
- Responsive design with mobile-first approach

You write **production-ready code** — not prototypes. Every line must be intentional, commented where logic is non-obvious, and follow modern best practices.

---

## PROJECT CONTEXT

**Client:** Adrian M. — Freelance Web Developer based in Windhoek, Namibia.
**Positioning:** "Friendly & approachable local dev" serving Namibian SMEs.
**Brand:** Personal brand (not agency). Warm, grounded, cinematic.
**Tech stack:** Static HTML/CSS/JS. No build tools unless client requests. Deploy to Netlify/Vercel.

This is the **Hero Section** of the homepage — the first and most critical impression.

---

## TASK

Build a **single, self-contained hero section** that matches the attached design specification exactly. This file should be a complete, working HTML file that can be opened in a browser immediately.

---

## DESIGN SPECIFICATION (FOLLOW EXACTLY)

### Color Tokens (CSS Custom Properties)
```css
:root {
  --bg-primary: #242323;
  --bg-secondary: #363636;
  --text-primary: #AEA7A3;
  --text-secondary: #959595;
  --text-muted: #525254;
  --accent: #795238;
  --accent-hover: #8B6348;
}
```

### Typography
- **Display font:** Syne (Google Fonts), weight 800 for the name
- **Body font:** DM Sans (Google Fonts), weights 400 and 500
- Load both via Google Fonts CDN with `display=swap`
- Preload the critical font files to prevent FOUT

### Layout Structure

#### Desktop (≥1024px)
- Full viewport height: `100vh`, `min-height: 600px`, `max-height: 900px`
- Two-zone composition:
  - **Left zone (text):** ~50% width, vertically centered, contains all text content
  - **Right zone (image):** ~50% width, contains the cutout photo
- The cutout photo **overlaps** into the left zone by 80–120px — this creates the editorial layered effect
- Cutout is **bottom-aligned** to the viewport (feet near bottom edge, not floating)
- Cutout height is ~75–85% of viewport height
- Text content is vertically centered within its zone

#### Mobile (<768px)
- Stacked layout: text on top, cutout below
- Cutout is centered, ~200–240px wide
- Name stacks if needed: "ADRIAN" / "M." on separate lines
- CTA button is full-width (max 320px), centered

### Content (Copy — Use Exactly)

1. **Location label** (top of text block):
   ```
   WINDHOEK, NAMIBIA
   ```
   - Uppercase, letter-spacing: 1px, color: var(--text-muted), font-size: 14px

2. **Name**:
   ```
   ADRIAN M.
   ```
   - Font: Syne, weight 800, size: 120px desktop / 52px mobile
   - Color: var(--text-primary)
   - Line-height: 0.9
   - Letter-spacing: -2px

3. **Role statement**:
   ```
   Freelance Web Developer
   building fast, reliable websites
   for Namibian businesses.
   ```
   - Font: DM Sans, weight 400, size: 18px desktop / 16px mobile
   - Color: var(--text-secondary)
   - Line-height: 1.5
   - Max 2 lines on desktop

4. **CTA Button**:
   ```
   View My Work →
   ```
   - Background: var(--accent), text: var(--bg-primary)
   - Font: DM Sans, weight 500, size: 16px
   - Padding: 16px 32px
   - Border-radius: 4px (subtle, not pill-shaped)
   - Links to: `#work` (anchor link, section below)

5. **Social Links** (horizontal row below CTA):
   ```
   Instagram    LinkedIn    Email
   ```
   - Font: DM Sans, weight 400, size: 14px
   - Color: var(--text-muted)
   - Spacing: 24px gap between items
   - Links:
     - Instagram: `https://instagram.com/adrianbuilds.na` (opens new tab)
     - LinkedIn: `https://linkedin.com/in/adrianm-dev` (opens new tab)
     - Email: `mailto:hello@adrianm.dev` (replace with actual email when known)
   - Hover: color shifts to var(--text-primary), underline appears

6. **Scroll Indicator** (bottom center, optional but included):
   ```
   Scroll
     ↓
   ```
   - Font: DM Sans, 12px, uppercase, letter-spacing 1px
   - Color: var(--accent)
   - Subtle bounce animation: translateY 0 → 8px → 0, 2s loop

### The Cutout Photo
- **IMPORTANT:** The client will provide a high-res PNG with transparent background. which is @assets/images/image.png
- Apply a subtle drop shadow: `0 20px 60px rgba(0,0,0,0.4)`
- Z-index: Behind the name text, in front of background — the name may partially overlap the shoulder/head
- Alt text: "Adrian M., freelance web developer in Windhoek, Namibia"

### Background
- Solid: var(--bg-primary)
- Optional subtle radial gradient: `radial-gradient(ellipse at center, var(--bg-secondary) 0%, var(--bg-primary) 70%)` — adds depth
- No background image. CSS-only.

---

## ANIMATION & INTERACTION REQUIREMENTS

### On-Load Staggered Reveal
All elements animate in sequence on page load:

1. **Background:** Instant (0ms)
2. **Location label:** Fade in + translateY(-20px → 0), 200ms delay, 600ms duration
3. **Name:** Fade in + translateX(-30px → 0) for "ADRIAN", translateX(30px → 0) for "M." — OR simple fade + translateY. 400ms delay, 700ms duration.
4. **Role text:** Fade in + translateY(20px → 0), 600ms delay, 600ms duration
5. **CTA:** Fade in + translateY(20px → 0), 800ms delay, 600ms duration
6. **Cutout:** Fade in + scale(1.02 → 1.0), 300ms delay, 800ms duration
7. **Social links:** Fade in, 1000ms delay, 500ms duration
8. **Scroll indicator:** Fade in, 1200ms delay, 500ms duration

**Easing:** `cubic-bezier(0.25, 0.1, 0.25, 1)` for all
**Initial state:** All animated elements have `opacity: 0` via CSS, removed by JS or animation class

### Hover States
- **CTA:** Background → var(--accent-hover), `transform: translateY(-2px)`, `box-shadow: 0 8px 24px rgba(121,82,56,0.3)`, transition 300ms
- **Social links:** Color → var(--text-primary), `text-decoration: underline`, transition 200ms
- **Scroll indicator:** No hover effect

### Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
  /* All animations become instant opacity changes, no movement */
}
```

---

## ACCESSIBILITY REQUIREMENTS

- Semantic HTML: `<header>`, `<h1>` for the name, `<p>` for role, `<a>` for CTA and links
- All links have descriptive text (no "click here")
- CTA focus state: `outline: 2px solid var(--text-primary), outline-offset: 4px`
- Social link focus states: same pattern
- Color contrast must pass WCAG AA:
  - Name (#AEA7A3 on #242323) = 5.8:1 ✓
  - CTA text (#242323 on #795238) = 4.6:1 ✓
- Alt text on image as specified above
- Keyboard navigable: Tab order follows visual order

---

## PERFORMANCE REQUIREMENTS

- First Contentful Paint target: <1.5s on simulated 3G
- Preload critical fonts: `<link rel="preload">` for Syne Bold and DM Sans Regular
- Use `font-display: swap` for all fonts
- Cutout image: Use a placeholder for now. In production, serve WebP with PNG fallback
- No external JS libraries. Vanilla JS only.
- CSS should be in a `<style>` block in the same file (self-contained)
- Minimize repaints: Use `transform` and `opacity` for animations only

---

## FILE STRUCTURE

Deliver a **single HTML file** named `index.html` containing:
1. `<!DOCTYPE html>` with lang="en"
2. `<head>` with meta viewport, charset, title ("Adrian M. — Freelance Web Developer | Windhoek, Namibia"), font preloads, Google Fonts link, and embedded CSS
3. `<body>` with the hero section markup and embedded JS
4. No external dependencies except Google Fonts CDN

---

## DELIVERABLE CHECKLIST

Before marking complete, verify:
- [ ] Opens correctly in Chrome, Firefox, Safari, Edge (latest 2 versions)
- [ ] Responsive at 375px, 768px, 1024px, 1440px, 1920px
- [ ] All animations work smoothly (60fps)
- [ ] Reduced motion preference respected
- [ ] All links are functional (even if anchors don't exist yet)
- [ ] No console errors
- [ ] Lighthouse score ≥90 for Performance, Accessibility, Best Practices
- [ ] Placeholder image has a clear comment indicating where to swap the real cutout

---

## STYLE NOTES FOR THE AI

- Write clean, commented code. Every CSS rule should have a purpose.
- Use CSS custom properties (variables) for all colors and repeated values.
- Use `rem` units for typography, `px` for borders and breakpoints.
- Mobile-first media queries: `min-width` approach.
- The design is intentionally minimal — do not add decorative elements not specified.
- The warm brown accent (`#795238`) should feel special, not overused. Only CTA, scroll indicator, and subtle hover effects.
- The overall feel should be: "This person is confident but approachable. They're local. They build websites. I should scroll or click."

---

## QUESTIONS FOR THE CLIENT (If anything is unclear)

1. What is the actual email address for the mailto link?
2. Should the CTA link to an anchor `#work` or a separate `/work` page?
3. Is the LinkedIn URL `linkedin.com/in/adrianm-dev` confirmed and claimed?
4. Any specific tracking (Google Analytics, Meta Pixel) to include?
5. Should the scroll indicator smooth-scroll to the next section or just be decorative?

If no answers are available, use the defaults specified above and add TODO comments.

---

*Prompt version 1.0 — Ready for AI agent execution*
