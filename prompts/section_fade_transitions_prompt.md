# AI Developer Prompt: Section Fade Transitions
## For Cursor, GitHub Copilot, or similar AI coding agents

---

## ROLE DEFINITION

You are a **Frontend Developer & UI Engineer** specializing in:
- Semantic, accessible HTML
- Modern CSS (linear-gradients, transitions, responsive design)
- Visual polish and seamless section transitions
- Performance-first development

You write **production-ready code** — not prototypes. Every line must be intentional, commented where logic is non-obvious, and follow modern best practices.

---

## PROJECT CONTEXT

**Client:** Adrian M. — Freelance Web Developer based in Windhoek, Namibia.
**Positioning:** "Friendly & approachable local dev" serving Namibian SMEs.
**Brand:** Personal brand (not agency). Warm, grounded, cinematic.
**Tech stack:** Static HTML/CSS/JS. Multi-page static site (Option A).
**Current state:** 5-page site built (Home, Contact, Services, Work, About). Shared CSS in `css/styles.css`. Shared JS in `js/main.js`.

**Design reference:** Client provided a Japan tour landing page image showing seamless gradient fade transitions between sections — no hard lines, no visible borders, just smooth color blending as the user scrolls. The hero image fades into content, and dark sections breathe into lighter ones.

**Client requirement:** Replace all hard section transitions (solid color shifts) with gradient fade transitions. Keep the matte, non-glossy finish. No blur, no glassmorphism.

---

## TASK

Implement **gradient fade transitions** between all sections across all 5 pages. Remove every hard color boundary and visible divider line. The result should feel like a continuous, cinematic scroll — each section flows into the next without the user noticing where one ends and another begins.

---

## DESIGN SPECIFICATION

### The Fade System

Instead of solid `background-color` shifts, use `linear-gradient` backgrounds that transition smoothly between adjacent section colors. The gradient zone is **15% of the section height** — enough to feel seamless, not so much that it dominates.

**Two color palette values used in fades:**
- `--bg-dark: #242323` (near black — primary section background)
- `--bg-light: #2E2E2E` (charcoal — secondary/breath section background)

### Transition Map (Homepage)

| Section | Previous Color | Current Color | Fade Type | Gradient Direction |
|---------|---------------|---------------|-----------|-------------------|
| **Hero** | — | `#242323` | None (top of page) | — |
| **Credibility Strip** | `#242323` | `#2E2E2E` | Dark → Light | `to bottom` |
| **Services Preview** | `#2E2E2E` | `#242323` | Light → Dark | `to bottom` |
| **Selected Work** | `#242323` | `#242323` | Same color | No gradient needed |
| **Final CTA** | `#242323` | `#242323` | Same color | No gradient needed |
| **Footer** | `#242323` | Image + overlay | Dark → Image | `to bottom` on overlay |

**Note:** Process and About sections were removed from homepage in the trim. They exist on Services and About pages respectively.

### Transition Map (Services Page)

| Section | Previous Color | Current Color | Fade Type |
|---------|---------------|---------------|-----------|
| **Page Header** | — | `#242323` | None |
| **Pricing Tiers** | `#242323` | `#242323` | Same color, no gradient |
| **Process** | `#242323` | `#2E2E2E` | Dark → Light |
| **Retainer** | `#2E2E2E` | `#242323` | Light → Dark |
| **FAQ** | `#242323` | `#2E2E2E` | Dark → Light |
| **Final CTA** | `#2E2E2E` | `#242323` | Light → Dark |
| **Footer** | `#242323` | Image + overlay | Dark → Image |

### Transition Map (Work Page)

| Section | Previous Color | Current Color | Fade Type |
|---------|---------------|---------------|-----------|
| **Page Header** | — | `#242323` | None |
| **Case Study** | `#242323` | `#242323` | Same color, no gradient |
| **Project Details** | `#242323` | `#2E2E2E` | Dark → Light |
| **Results** | `#2E2E2E` | `#242323` | Light → Dark |
| **Future Work** | `#242323` | `#2E2E2E` | Dark → Light |
| **Final CTA** | `#2E2E2E` | `#242323` | Light → Dark |
| **Footer** | `#242323` | Image + overlay | Dark → Image |

### Transition Map (About Page)

| Section | Previous Color | Current Color | Fade Type |
|---------|---------------|---------------|-----------|
| **Page Header** | — | `#242323` | None |
| **Intro** | `#242323` | `#242323` | Same color, no gradient |
| **Why** | `#242323` | `#2E2E2E` | Dark → Light |
| **Approach** | `#2E2E2E` | `#242323` | Light → Dark |
| **Credentials** | `#242323` | `#2E2E2E` | Dark → Light |
| **Personal** | `#2E2E2E` | `#242323` | Light → Dark |
| **Final CTA** | `#242323` | `#242323` | Same color, no gradient |
| **Footer** | `#242323` | Image + overlay | Dark → Image |

### Transition Map (Contact Page)

| Section | Previous Color | Current Color | Fade Type |
|---------|---------------|---------------|-----------|
| **Page Header** | — | `#242323` | None |
| **Contact Methods** | `#242323` | `#2E2E2E` | Dark → Light |
| **Form** | `#2E2E2E` | `#242323` | Light → Dark |
| **FAQ** | `#242323` | `#2E2E2E` | Dark → Light |
| **Footer** | `#2E2E2E` | Image + overlay | Light → Image |

---

## CSS IMPLEMENTATION

### Gradient Formula

For **Dark → Light** transitions:
```css
.section-name {
  background: linear-gradient(
    to bottom,
    #242323 0%,      /* Start: previous section color (dark) */
    #242323 10%,     /* Hold dark for a bit */
    #2E2E2E 25%,     /* Transition zone (15% gradient) */
    #2E2E2E 100%     /* End: current section color (light) */
  );
  padding-top: 100px;  /* Extra space for gradient */
  padding-bottom: 80px;
}
```

For **Light → Dark** transitions:
```css
.section-name {
  background: linear-gradient(
    to bottom,
    #2E2E2E 0%,      /* Start: previous section color (light) */
    #2E2E2E 10%,     /* Hold light for a bit */
    #242323 25%,     /* Transition zone (15% gradient) */
    #242323 100%     /* End: current section color (dark) */
  );
  padding-top: 100px;
  padding-bottom: 80px;
}
```

For **Same color** sections (no gradient needed):
```css
.section-name {
  background-color: #242323;  /* or #2E2E2E */
  padding-top: 80px;
  padding-bottom: 80px;
}
```

**Rules:**
- The gradient starts with the **previous section's color** and ends with the **current section's color**
- 10% hold + 15% transition = 25% gradient zone before solid color begins
- This creates a "fade-in" effect as the user scrolls into the section
- `padding-top: 100px` (instead of 80px) accommodates the gradient zone without crowding content

---

## SECTION-BY-SECTION UPDATES

### HOMEPAGE (`index.html`)

#### 1. Hero Section
```css
.hero {
  background-color: #242323;
  /* No change — top of page, no previous section */
}
```

#### 2. Credibility Strip
```css
.credibility-strip {
  background: linear-gradient(
    to bottom,
    #242323 0%,
    #242323 10%,
    #2E2E2E 25%,
    #2E2E2E 100%
  );
  padding-top: 100px;
  padding-bottom: 80px;
}
```

**Remove:** `background-color: #2E2E2E;` (old solid color)

#### 3. Services Preview
```css
.services-section {
  background: linear-gradient(
    to bottom,
    #2E2E2E 0%,
    #2E2E2E 10%,
    #242323 25%,
    #242323 100%
  );
  padding-top: 100px;
  padding-bottom: 80px;
  position: relative;  /* For background headline */
}
```

**Remove:** `background-color: #242323;` (old solid color)

**Note:** The "SERVICES" background headline must still work. Ensure `z-index` layering is correct:
```css
.services-bg-headline {
  z-index: 0;
}

.services-content {
  position: relative;
  z-index: 1;
}
```

#### 4. Selected Work
```css
.work-section {
  background-color: #242323;
  padding-top: 80px;  /* No gradient needed — same color as previous */
  padding-bottom: 80px;
}
```

**No change needed** — Services and Work are both `#242323`, so no gradient.

#### 5. Final CTA
```css
.final-cta-section {
  background-color: #242323;
  padding-top: 100px;  /* Slightly more for visual weight */
  padding-bottom: 100px;
}
```

**No gradient needed** — same color as Selected Work.

#### 6. Footer
```css
.footer-section {
  position: relative;
  padding-top: 80px;
  padding-bottom: 40px;
  /* Background image + overlay handled separately */
}

/* Add fade from dark into footer image */
.footer-section::before {
  content: '';
  position: absolute;
  top: -80px;
  left: 0;
  right: 0;
  height: 80px;
  background: linear-gradient(
    to bottom,
    #242323 0%,
    transparent 100%
  );
  z-index: 2;  /* Above image, below content */
  pointer-events: none;
}
```

**Note:** The footer already has `::before` for the image and `::after` for the dark overlay. The new gradient `::before` must be carefully layered:

```css
.footer-section::before {
  /* Image layer — keep existing */
  background-image: url('Desert in Namibia.jpeg');
  background-size: cover;
  background-position: center;
  z-index: 0;
}

.footer-section::after {
  /* Dark overlay — keep existing */
  background: linear-gradient(
    to bottom,
    rgba(36, 35, 35, 0.92) 0%,
    rgba(36, 35, 35, 0.85) 50%,
    rgba(36, 35, 35, 0.95) 100%
  );
  z-index: 1;
}

.footer-fade-top {
  /* NEW: Fade from Final CTA into footer image */
  position: absolute;
  top: -80px;
  left: 0;
  right: 0;
  height: 80px;
  background: linear-gradient(
    to bottom,
    #242323 0%,
    transparent 100%
  );
  z-index: 2;
  pointer-events: none;
}
```

**Alternative (cleaner):** Instead of a pseudo-element, add a dedicated `<div>`:
```html
<footer class="footer-section">
  <div class="footer-fade-top" aria-hidden="true"></div>
  <!-- footer content -->
</footer>
```

```css
.footer-fade-top {
  position: absolute;
  top: -80px;
  left: 0;
  right: 0;
  height: 80px;
  background: linear-gradient(
    to bottom,
    #242323 0%,
    transparent 100%
  );
  z-index: 2;
  pointer-events: none;
}
```

---

### SERVICES PAGE (`services.html`)

#### 1. Page Header
```css
.page-header {
  background-color: #242323;
  /* No change — top of page */
}
```

#### 2. Pricing Tiers
```css
.services-pricing {
  background-color: #242323;
  padding-top: 80px;
  padding-bottom: 80px;
  position: relative;
}
```

**No gradient** — same color as page header.

#### 3. Process Section
```css
.process-section {
  background: linear-gradient(
    to bottom,
    #242323 0%,
    #242323 10%,
    #2E2E2E 25%,
    #2E2E2E 100%
  );
  padding-top: 100px;
  padding-bottom: 80px;
}
```

**Remove:** `background-color: #2E2E2E;`

#### 4. Retainer Section
```css
.retainer-section {
  background: linear-gradient(
    to bottom,
    #2E2E2E 0%,
    #2E2E2E 10%,
    #242323 25%,
    #242323 100%
  );
  padding-top: 100px;
  padding-bottom: 80px;
}
```

**Remove:** `background-color: #242323;`

#### 5. FAQ Section
```css
.services-faq {
  background: linear-gradient(
    to bottom,
    #242323 0%,
    #242323 10%,
    #2E2E2E 25%,
    #2E2E2E 100%
  );
  padding-top: 100px;
  padding-bottom: 80px;
}
```

**Remove:** `background-color: #2E2E2E;`

#### 6. Final CTA
```css
.final-cta-section {
  background: linear-gradient(
    to bottom,
    #2E2E2E 0%,
    #2E2E2E 10%,
    #242323 25%,
    #242323 100%
  );
  padding-top: 100px;
  padding-bottom: 100px;
}
```

**Remove:** `background-color: #242323;`

#### 7. Footer
Same as homepage footer — add `.footer-fade-top` element.

---

### WORK PAGE (`work.html`)

#### 1. Page Header
```css
.page-header {
  background-color: #242323;
  /* No change */
}
```

#### 2. Case Study Featured
```css
.case-study-featured {
  background-color: #242323;
  padding-top: 0;      /* Flows directly from header */
  padding-bottom: 80px;
}
```

**No gradient** — same color as header.

#### 3. Project Details
```css
.project-details {
  background: linear-gradient(
    to bottom,
    #242323 0%,
    #242323 10%,
    #2E2E2E 25%,
    #2E2E2E 100%
  );
  padding-top: 100px;
  padding-bottom: 80px;
}
```

**Remove:** `background-color: #2E2E2E;`

#### 4. Results
```css
.project-results {
  background: linear-gradient(
    to bottom,
    #2E2E2E 0%,
    #2E2E2E 10%,
    #242323 25%,
    #242323 100%
  );
  padding-top: 100px;
  padding-bottom: 80px;
}
```

**Remove:** `background-color: #242323;`

#### 5. Future Work
```css
.future-work {
  background: linear-gradient(
    to bottom,
    #242323 0%,
    #242323 10%,
    #2E2E2E 25%,
    #2E2E2E 100%
  );
  padding-top: 100px;
  padding-bottom: 80px;
}
```

**Remove:** `background-color: #2E2E2E;`

#### 6. Final CTA
```css
.final-cta-section {
  background: linear-gradient(
    to bottom,
    #2E2E2E 0%,
    #2E2E2E 10%,
    #242323 25%,
    #242323 100%
  );
  padding-top: 100px;
  padding-bottom: 100px;
}
```

**Remove:** `background-color: #242323;`

#### 7. Footer
Same as homepage — add `.footer-fade-top`.

---

### ABOUT PAGE (`about.html`)

#### 1. Page Header
```css
.page-header {
  background-color: #242323;
  /* No change */
}
```

#### 2. Intro
```css
.about-intro {
  background-color: #242323;
  padding-top: 40px;   /* Less padding — flows from header */
  padding-bottom: 80px;
}
```

**No gradient** — same color as header.

#### 3. Why
```css
.about-why {
  background: linear-gradient(
    to bottom,
    #242323 0%,
    #242323 10%,
    #2E2E2E 25%,
    #2E2E2E 100%
  );
  padding-top: 100px;
  padding-bottom: 80px;
}
```

**Remove:** `background-color: #2E2E2E;`

#### 4. Approach
```css
.about-approach {
  background: linear-gradient(
    to bottom,
    #2E2E2E 0%,
    #2E2E2E 10%,
    #242323 25%,
    #242323 100%
  );
  padding-top: 100px;
  padding-bottom: 80px;
}
```

**Remove:** `background-color: #242323;`

#### 5. Credentials
```css
.about-credentials {
  background: linear-gradient(
    to bottom,
    #242323 0%,
    #242323 10%,
    #2E2E2E 25%,
    #2E2E2E 100%
  );
  padding-top: 100px;
  padding-bottom: 80px;
}
```

**Remove:** `background-color: #2E2E2E;`

#### 6. Personal
```css
.about-personal {
  background: linear-gradient(
    to bottom,
    #2E2E2E 0%,
    #2E2E2E 10%,
    #242323 25%,
    #242323 100%
  );
  padding-top: 100px;
  padding-bottom: 80px;
}
```

**Remove:** `background-color: #242323;`

#### 7. Final CTA
```css
.final-cta-section {
  background-color: #242323;
  padding-top: 100px;
  padding-bottom: 100px;
}
```

**No gradient** — same color as Personal section end.

#### 8. Footer
Same as homepage — add `.footer-fade-top`.

---

### CONTACT PAGE (`contact.html`)

#### 1. Page Header
```css
.page-header {
  background-color: #242323;
  /* No change */
}
```

#### 2. Contact Methods
```css
.contact-methods {
  background: linear-gradient(
    to bottom,
    #242323 0%,
    #242323 10%,
    #2E2E2E 25%,
    #2E2E2E 100%
  );
  padding-top: 100px;
  padding-bottom: 80px;
}
```

**Remove:** `background-color: #2E2E2E;`

#### 3. Form Section
```css
.contact-form-section {
  background: linear-gradient(
    to bottom,
    #2E2E2E 0%,
    #2E2E2E 10%,
    #242323 25%,
    #242323 100%
  );
  padding-top: 100px;
  padding-bottom: 80px;
}
```

**Remove:** `background-color: #242323;`

#### 4. FAQ
```css
.contact-faq {
  background: linear-gradient(
    to bottom,
    #242323 0%,
    #242323 10%,
    #2E2E2E 25%,
    #2E2E2E 100%
  );
  padding-top: 100px;
  padding-bottom: 80px;
}
```

**Remove:** `background-color: #2E2E2E;`

#### 5. Footer
Same as homepage — add `.footer-fade-top`.

---

## SHARED CSS ORGANIZATION

In `css/styles.css`, organize all section backgrounds in one clearly commented block:

```css
/* ========================================
   SECTION BACKGROUNDS & FADE TRANSITIONS
   ========================================

   Gradient formula for Dark → Light:
   background: linear-gradient(
     to bottom,
     #242323 0%,      // Previous section color (dark)
     #242323 10%,     // Hold
     #2E2E2E 25%,     // Transition (15% zone)
     #2E2E2E 100%     // Current section color (light)
   );
   padding-top: 100px;

   Gradient formula for Light → Dark:
   background: linear-gradient(
     to bottom,
     #2E2E2E 0%,      // Previous section color (light)
     #2E2E2E 10%,     // Hold
     #242323 25%,     // Transition (15% zone)
     #242323 100%     // Current section color (dark)
   );
   padding-top: 100px;

   Same color (no gradient):
   background-color: #242323;  // or #2E2E2E
   padding-top: 80px;
*/

/* --- HOMEPAGE --- */
.hero { background-color: #242323; }

.credibility-strip {
  background: linear-gradient(to bottom, #242323 0%, #242323 10%, #2E2E2E 25%, #2E2E2E 100%);
  padding-top: 100px;
  padding-bottom: 80px;
}

.services-section {
  background: linear-gradient(to bottom, #2E2E2E 0%, #2E2E2E 10%, #242323 25%, #242323 100%);
  padding-top: 100px;
  padding-bottom: 80px;
}

.work-section {
  background-color: #242323;
  padding-top: 80px;
  padding-bottom: 80px;
}

.final-cta-section {
  background-color: #242323;
  padding-top: 100px;
  padding-bottom: 100px;
}

/* --- SERVICES PAGE --- */
.services-pricing {
  background-color: #242323;
  padding-top: 80px;
  padding-bottom: 80px;
}

.process-section {
  background: linear-gradient(to bottom, #242323 0%, #242323 10%, #2E2E2E 25%, #2E2E2E 100%);
  padding-top: 100px;
  padding-bottom: 80px;
}

.retainer-section {
  background: linear-gradient(to bottom, #2E2E2E 0%, #2E2E2E 10%, #242323 25%, #242323 100%);
  padding-top: 100px;
  padding-bottom: 80px;
}

.services-faq {
  background: linear-gradient(to bottom, #242323 0%, #242323 10%, #2E2E2E 25%, #2E2E2E 100%);
  padding-top: 100px;
  padding-bottom: 80px;
}

/* --- WORK PAGE --- */
.case-study-featured {
  background-color: #242323;
  padding-top: 0;
  padding-bottom: 80px;
}

.project-details {
  background: linear-gradient(to bottom, #242323 0%, #242323 10%, #2E2E2E 25%, #2E2E2E 100%);
  padding-top: 100px;
  padding-bottom: 80px;
}

.project-results {
  background: linear-gradient(to bottom, #2E2E2E 0%, #2E2E2E 10%, #242323 25%, #242323 100%);
  padding-top: 100px;
  padding-bottom: 80px;
}

.future-work {
  background: linear-gradient(to bottom, #242323 0%, #242323 10%, #2E2E2E 25%, #2E2E2E 100%);
  padding-top: 100px;
  padding-bottom: 80px;
}

/* --- ABOUT PAGE --- */
.about-intro {
  background-color: #242323;
  padding-top: 40px;
  padding-bottom: 80px;
}

.about-why {
  background: linear-gradient(to bottom, #242323 0%, #242323 10%, #2E2E2E 25%, #2E2E2E 100%);
  padding-top: 100px;
  padding-bottom: 80px;
}

.about-approach {
  background: linear-gradient(to bottom, #2E2E2E 0%, #2E2E2E 10%, #242323 25%, #242323 100%);
  padding-top: 100px;
  padding-bottom: 80px;
}

.about-credentials {
  background: linear-gradient(to bottom, #242323 0%, #242323 10%, #2E2E2E 25%, #2E2E2E 100%);
  padding-top: 100px;
  padding-bottom: 80px;
}

.about-personal {
  background: linear-gradient(to bottom, #2E2E2E 0%, #2E2E2E 10%, #242323 25%, #242323 100%);
  padding-top: 100px;
  padding-bottom: 80px;
}

/* --- CONTACT PAGE --- */
.contact-methods {
  background: linear-gradient(to bottom, #242323 0%, #242323 10%, #2E2E2E 25%, #2E2E2E 100%);
  padding-top: 100px;
  padding-bottom: 80px;
}

.contact-form-section {
  background: linear-gradient(to bottom, #2E2E2E 0%, #2E2E2E 10%, #242323 25%, #242323 100%);
  padding-top: 100px;
  padding-bottom: 80px;
}

.contact-faq {
  background: linear-gradient(to bottom, #242323 0%, #242323 10%, #2E2E2E 25%, #2E2E2E 100%);
  padding-top: 100px;
  padding-bottom: 80px;
}

/* --- FOOTER (ALL PAGES) --- */
.footer-section {
  position: relative;
  padding-top: 80px;
  padding-bottom: 40px;
  /* Image + overlay handled by existing ::before and ::after */
}

.footer-fade-top {
  position: absolute;
  top: -80px;
  left: 0;
  right: 0;
  height: 80px;
  background: linear-gradient(to bottom, #242323 0%, transparent 100%);
  z-index: 2;
  pointer-events: none;
}
```

---

## HTML UPDATES

### Footer HTML (All Pages)

Update the footer on **all 5 pages** to include the fade element:

```html
<footer class="footer-section">
  <div class="footer-fade-top" aria-hidden="true"></div>

  <!-- existing footer content -->
  <div class="footer-brand">...</div>
  <div class="footer-divider"></div>
  <nav class="footer-nav" aria-label="Footer navigation">...</nav>
  <div class="footer-socials">...</div>
  <div class="footer-copyright">...</div>
</footer>
```

**No other HTML changes needed** — the gradient backgrounds are pure CSS.

---

## RESPONSIVE ADJUSTMENTS

On mobile, the gradient zone may feel too large relative to screen height. Adjust:

```css
@media (max-width: 768px) {
  /* Reduce gradient zone on mobile */
  .credibility-strip,
  .services-section,
  .process-section,
  .retainer-section,
  .services-faq,
  .project-details,
  .project-results,
  .future-work,
  .about-why,
  .about-approach,
  .about-credentials,
  .about-personal,
  .contact-methods,
  .contact-form-section,
  .contact-faq {
    background: linear-gradient(
      to bottom,
      var(--prev-color) 0%,
      var(--prev-color) 5%,    /* Smaller hold */
      var(--curr-color) 15%,    /* Smaller transition (10%) */
      var(--curr-color) 100%
    );
    padding-top: 80px;  /* Less top padding */
  }
}
```

**Note:** CSS custom properties (`var(--prev-color)`) are used here for illustration. In actual implementation, write the full gradient for each section as shown in the desktop rules above, but with adjusted percentages.

**Mobile gradient percentages:**
- Hold: 5% (down from 10%)
- Transition: 10% (down from 15%)
- Padding-top: 80px (down from 100px)

---

## ACCESSIBILITY

- `.footer-fade-top` has `aria-hidden="true"` — decorative only
- No content is hidden or obscured by gradients
- Color contrast remains unchanged (gradients are between existing brand colors)
- `prefers-reduced-motion`: gradients are static, no animation — no change needed

---

## PERFORMANCE

- Gradients are CSS-only — no images, no performance cost
- No `backdrop-filter` or blur — keeps it matte and fast
- Target: No impact on Lighthouse Performance score

---

## NO-GO LIST

- [ ] No `backdrop-filter: blur()` on gradients — matte finish only
- [ ] No `background-attachment: fixed` on gradients — causes jank on mobile
- [ ] No animated gradients (shifting colors) — static only
- [ ] No radial or conical gradients — linear only, consistent direction
- [ ] No additional colors introduced — only `#242323` and `#2E2E2E`

---

## DELIVERABLE

1. Updated `css/styles.css` with all gradient backgrounds organized in one block
2. Updated HTML on all 5 pages: footer gets `.footer-fade-top` element
3. Old solid `background-color` rules removed from sections that now use gradients
4. No console errors
5. Responsive gradients on mobile (smaller transition zones)

---

## VERIFICATION CHECKLIST

- [ ] All hard section boundaries removed — no visible lines between sections
- [ ] Homepage: Hero → Credibility → Services → Work → Final CTA → Footer all flow seamlessly
- [ ] Services page: Header → Pricing → Process → Retainer → FAQ → CTA → Footer flow seamlessly
- [ ] Work page: Header → Case Study → Details → Results → Future → CTA → Footer flow seamlessly
- [ ] About page: Header → Intro → Why → Approach → Credentials → Personal → CTA → Footer flow seamlessly
- [ ] Contact page: Header → Methods → Form → FAQ → Footer flow seamlessly
- [ ] Footer has `.footer-fade-top` element on all 5 pages
- [ ] Footer image fades in from dark, not a hard cut
- [ ] Services "SERVICES" background headline still visible and correctly layered
- [ ] No content is obscured or unreadable due to gradients
- [ ] Mobile: gradients are subtler (10% zone vs 15%), padding reduced
- [ ] No `border-top` or `border-bottom` on any section
- [ ] Lighthouse Performance ≥90, Accessibility ≥95

---

*Prompt version 1.0 — Section fade transitions, global component*
