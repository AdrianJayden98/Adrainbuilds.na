# AI Developer Prompt: Fix Section Fade Transitions
## For Cursor, GitHub Copilot, or similar AI coding agents

---

## ROLE DEFINITION

You are a **Frontend Developer & UI Engineer** specializing in:
- Modern CSS (linear-gradients, pseudo-elements, positioning)
- Visual polish and seamless transitions
- Surgical code fixes — minimal changes, maximum impact

You write **production-ready code** — not prototypes.

---

## PROJECT CONTEXT

**Client:** Adrian M. — Freelance Web Developer, Windhoek, Namibia.
**Current state:** Multi-page site built with section fade transitions, but they still appear as hard lines instead of smooth dissolves.

**Problem:** The current gradient approach puts the fade on the *lower* section (fading in), creating visible boundaries. The gradient zones are also too short (15%) to be perceptible.

**Goal:** Move all gradients to the *upper* section (fading out), increase gradient height, and create true dissolve transitions between sections.

---

## THE FIX

### Core Principle

**Put the gradient on the section ABOVE, fading OUT — not on the section below, fading IN.**

This creates a dissolve effect where the previous section melts into the next.

### Gradient Spec

```css
/* Fade-out gradient on upper section */
.section-upper::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;  /* Increased from 80px */
  background: linear-gradient(
    to bottom,
    transparent 0%,
    [next-section-color] 100%
  );
  pointer-events: none;
  z-index: 2;
}
```

**Rules:**
- Gradient height: **120px** (increased from 80px)
- No hold zone — fade starts immediately from transparent
- `pointer-events: none` — clicks pass through
- `z-index: 2` — above section background, below section content

---

## SECTION-BY-SECTION FIXES

### 1. HOMEPAGE

#### Hero → Credibility Strip

```css
.hero {
  position: relative;
  background-color: #242323;
  /* REMOVE: padding-bottom (if any) — gradient handles the space */
}

.hero::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    #2E2E2E 100%
  );
  pointer-events: none;
  z-index: 2;
}

.credibility-strip {
  background-color: #2E2E2E;  /* SOLID — no gradient */
  padding-top: 80px;
  padding-bottom: 80px;
}
```

**Changes:**
- Add `position: relative` to `.hero`
- Add `.hero::after` with fade to `#2E2E2E`
- `.credibility-strip` becomes solid `#2E2E2E`, remove any gradient

#### Credibility Strip → Services

```css
.credibility-strip {
  position: relative;  /* ADD */
  background-color: #2E2E2E;
}

.credibility-strip::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    #242323 100%
  );
  pointer-events: none;
  z-index: 2;
}

.services-section {
  background-color: #242323;  /* SOLID */
  padding-top: 80px;
  padding-bottom: 80px;
}
```

**Changes:**
- Add `position: relative` to `.credibility-strip`
- Add `.credibility-strip::after` with fade to `#242323`
- `.services-section` becomes solid `#242323`, remove gradient

#### Services → Selected Work (same color, no fade needed)

```css
.services-section {
  position: relative;
  background-color: #242323;
}

/* NO ::after needed — same color as next section */

.work-section {
  background-color: #242323;  /* SOLID */
  padding-top: 80px;
  padding-bottom: 80px;
}
```

#### Selected Work → Final CTA (same color, no fade needed)

```css
.work-section {
  position: relative;
  background-color: #242323;
}

/* NO ::after needed */

.final-cta-section {
  background-color: #242323;  /* SOLID */
  padding-top: 100px;
  padding-bottom: 100px;
}
```

#### Final CTA → Footer (desert image)

```css
.final-cta-section {
  position: relative;
  background-color: #242323;
}

.final-cta-section::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 150px;  /* Taller for image transition */
  background: linear-gradient(
    to bottom,
    transparent 0%,
    rgba(36, 35, 35, 0.7) 70%,
    #242323 100%
  );
  pointer-events: none;
  z-index: 2;
}

.footer-section {
  position: relative;
  padding-top: 80px;
  padding-bottom: 40px;
  /* Image and overlay handled by existing ::before and ::after */
}

.footer-fade-top {
  position: absolute;
  top: -100px;  /* Increased from 80px */
  left: 0;
  right: 0;
  height: 100px;
  background: linear-gradient(
    to bottom,
    #242323 0%,
    rgba(36, 35, 35, 0.5) 40%,
    transparent 100%
  );
  z-index: 3;  /* Above image, below footer content */
  pointer-events: none;
}
```

**Changes:**
- Add `.final-cta-section::after` with fade to dark (preparing for footer image)
- `.footer-fade-top` gradient starts higher (`top: -100px`), fades more gradually
- `z-index: 3` on `.footer-fade-top` to sit above the image layer

---

### 2. SERVICES PAGE

#### Page Header → Pricing (same color, no fade)

```css
.page-header {
  position: relative;
  background-color: #242323;
}

.services-pricing {
  background-color: #242323;  /* SOLID */
  padding-top: 80px;
  padding-bottom: 80px;
}
```

#### Pricing → Process

```css
.services-pricing {
  position: relative;  /* ADD */
  background-color: #242323;
}

.services-pricing::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    #2E2E2E 100%
  );
  pointer-events: none;
  z-index: 2;
}

.process-section {
  background-color: #2E2E2E;  /* SOLID */
  padding-top: 80px;
  padding-bottom: 80px;
}
```

#### Process → Retainer

```css
.process-section {
  position: relative;  /* ADD */
  background-color: #2E2E2E;
}

.process-section::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    #242323 100%
  );
  pointer-events: none;
  z-index: 2;
}

.retainer-section {
  background-color: #242323;  /* SOLID */
  padding-top: 80px;
  padding-bottom: 80px;
}
```

#### Retainer → FAQ

```css
.retainer-section {
  position: relative;  /* ADD */
  background-color: #242323;
}

.retainer-section::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    #2E2E2E 100%
  );
  pointer-events: none;
  z-index: 2;
}

.services-faq {
  background-color: #2E2E2E;  /* SOLID */
  padding-top: 80px;
  padding-bottom: 80px;
}
```

#### FAQ → Final CTA

```css
.services-faq {
  position: relative;  /* ADD */
  background-color: #2E2E2E;
}

.services-faq::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    #242323 100%
  );
  pointer-events: none;
  z-index: 2;
}

.final-cta-section {
  background-color: #242323;  /* SOLID */
  padding-top: 100px;
  padding-bottom: 100px;
}
```

#### Final CTA → Footer (same as homepage)

Reuse the same `.final-cta-section::after` and `.footer-fade-top` as homepage.

---

### 3. WORK PAGE

#### Page Header → Case Study (same color, no fade)

```css
.page-header {
  position: relative;
  background-color: #242323;
}

.case-study-featured {
  background-color: #242323;  /* SOLID */
  padding-top: 0;
  padding-bottom: 80px;
}
```

#### Case Study → Project Details

```css
.case-study-featured {
  position: relative;  /* ADD */
  background-color: #242323;
}

.case-study-featured::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    #2E2E2E 100%
  );
  pointer-events: none;
  z-index: 2;
}

.project-details {
  background-color: #2E2E2E;  /* SOLID */
  padding-top: 80px;
  padding-bottom: 80px;
}
```

#### Project Details → Results

```css
.project-details {
  position: relative;  /* ADD */
  background-color: #2E2E2E;
}

.project-details::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    #242323 100%
  );
  pointer-events: none;
  z-index: 2;
}

.project-results {
  background-color: #242323;  /* SOLID */
  padding-top: 80px;
  padding-bottom: 80px;
}
```

#### Results → Future Work

```css
.project-results {
  position: relative;  /* ADD */
  background-color: #242323;
}

.project-results::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    #2E2E2E 100%
  );
  pointer-events: none;
  z-index: 2;
}

.future-work {
  background-color: #2E2E2E;  /* SOLID */
  padding-top: 80px;
  padding-bottom: 80px;
}
```

#### Future Work → Final CTA

```css
.future-work {
  position: relative;  /* ADD */
  background-color: #2E2E2E;
}

.future-work::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    #242323 100%
  );
  pointer-events: none;
  z-index: 2;
}

.final-cta-section {
  background-color: #242323;  /* SOLID */
  padding-top: 100px;
  padding-bottom: 100px;
}
```

#### Final CTA → Footer (same as homepage)

Reuse homepage footer fade.

---

### 4. ABOUT PAGE

#### Page Header → Intro (same color, no fade)

```css
.page-header {
  position: relative;
  background-color: #242323;
}

.about-intro {
  background-color: #242323;  /* SOLID */
  padding-top: 40px;
  padding-bottom: 80px;
}
```

#### Intro → Why

```css
.about-intro {
  position: relative;  /* ADD */
  background-color: #242323;
}

.about-intro::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    #2E2E2E 100%
  );
  pointer-events: none;
  z-index: 2;
}

.about-why {
  background-color: #2E2E2E;  /* SOLID */
  padding-top: 80px;
  padding-bottom: 80px;
}
```

#### Why → Approach

```css
.about-why {
  position: relative;  /* ADD */
  background-color: #2E2E2E;
}

.about-why::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    #242323 100%
  );
  pointer-events: none;
  z-index: 2;
}

.about-approach {
  background-color: #242323;  /* SOLID */
  padding-top: 80px;
  padding-bottom: 80px;
}
```

#### Approach → Credentials

```css
.about-approach {
  position: relative;  /* ADD */
  background-color: #242323;
}

.about-approach::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    #2E2E2E 100%
  );
  pointer-events: none;
  z-index: 2;
}

.about-credentials {
  background-color: #2E2E2E;  /* SOLID */
  padding-top: 80px;
  padding-bottom: 80px;
}
```

#### Credentials → Personal

```css
.about-credentials {
  position: relative;  /* ADD */
  background-color: #2E2E2E;
}

.about-credentials::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    #242323 100%
  );
  pointer-events: none;
  z-index: 2;
}

.about-personal {
  background-color: #242323;  /* SOLID */
  padding-top: 80px;
  padding-bottom: 80px;
}
```

#### Personal → Final CTA (same color, no fade)

```css
.about-personal {
  position: relative;
  background-color: #242323;
}

/* NO ::after needed */

.final-cta-section {
  background-color: #242323;  /* SOLID */
  padding-top: 100px;
  padding-bottom: 100px;
}
```

#### Final CTA → Footer (same as homepage)

Reuse homepage footer fade.

---

### 5. CONTACT PAGE

#### Page Header → Contact Methods

```css
.page-header {
  position: relative;
  background-color: #242323;
}

.contact-methods {
  background-color: #2E2E2E;  /* SOLID */
  padding-top: 80px;
  padding-bottom: 80px;
}
```

**Note:** Page header has padding-bottom (140px top, 60px bottom). The header itself is a block, so the fade should be on the header:

```css
.page-header {
  position: relative;
  background-color: #242323;
  padding: 140px 20px 60px;
}

.page-header::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    #2E2E2E 100%
  );
  pointer-events: none;
  z-index: 2;
}
```

#### Contact Methods → Form

```css
.contact-methods {
  position: relative;  /* ADD */
  background-color: #2E2E2E;
}

.contact-methods::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    #242323 100%
  );
  pointer-events: none;
  z-index: 2;
}

.contact-form-section {
  background-color: #242323;  /* SOLID */
  padding-top: 80px;
  padding-bottom: 80px;
}
```

#### Form → FAQ

```css
.contact-form-section {
  position: relative;  /* ADD */
  background-color: #242323;
}

.contact-form-section::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    #2E2E2E 100%
  );
  pointer-events: none;
  z-index: 2;
}

.contact-faq {
  background-color: #2E2E2E;  /* SOLID */
  padding-top: 80px;
  padding-bottom: 80px;
}
```

#### FAQ → Footer

```css
.contact-faq {
  position: relative;  /* ADD */
  background-color: #2E2E2E;
}

.contact-faq::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    #242323 100%
  );
  pointer-events: none;
  z-index: 2;
}

.footer-section {
  position: relative;
  padding-top: 80px;
  padding-bottom: 40px;
}
```

**Footer fade:** Same as homepage, but fade starts from `#242323` (not `#2E2E2E` since the FAQ fades to `#242323` before the footer).

---

## CSS CLEANUP

### Remove These Old Rules

From all sections, remove:
- `background: linear-gradient(to bottom, ...)` on the LOWER section
- Any `background` that transitions from previous color to current color
- Keep only `background-color` on lower sections (solid)

### Example Cleanup

```css
/* REMOVE this old pattern from lower sections */
.credibility-strip {
  /* OLD — remove */
  background: linear-gradient(to bottom, #242323 0%, #242323 10%, #2E2E2E 25%, #2E2E2E 100%);
}

/* REPLACE with this */
.credibility-strip {
  background-color: #2E2E2E;  /* SOLID */
}

/* ADD to upper section */
.hero::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  background: linear-gradient(to bottom, transparent 0%, #2E2E2E 100%);
  pointer-events: none;
  z-index: 2;
}
```

---

## SHARED CSS ORGANIZATION

In `css/styles.css`, add all `::after` fade rules in one block:

```css
/* ========================================
   SECTION FADE TRANSITIONS (DISSOLVE)
   ========================================

   Principle: Upper section fades OUT to next section's color.
   Lower section is SOLID — no gradient.
*/

/* --- HOMEPAGE --- */
.hero::after { background: linear-gradient(to bottom, transparent 0%, #2E2E2E 100%); }
.credibility-strip::after { background: linear-gradient(to bottom, transparent 0%, #242323 100%); }
/* Services → Work: same color, no fade */
/* Work → Final CTA: same color, no fade */
.final-cta-section::after { 
  height: 150px;
  background: linear-gradient(to bottom, transparent 0%, rgba(36, 35, 35, 0.7) 70%, #242323 100%); 
}

/* --- SERVICES PAGE --- */
.services-pricing::after { background: linear-gradient(to bottom, transparent 0%, #2E2E2E 100%); }
.process-section::after { background: linear-gradient(to bottom, transparent 0%, #242323 100%); }
.retainer-section::after { background: linear-gradient(to bottom, transparent 0%, #2E2E2E 100%); }
.services-faq::after { background: linear-gradient(to bottom, transparent 0%, #242323 100%); }

/* --- WORK PAGE --- */
.case-study-featured::after { background: linear-gradient(to bottom, transparent 0%, #2E2E2E 100%); }
.project-details::after { background: linear-gradient(to bottom, transparent 0%, #242323 100%); }
.project-results::after { background: linear-gradient(to bottom, transparent 0%, #2E2E2E 100%); }
.future-work::after { background: linear-gradient(to bottom, transparent 0%, #242323 100%); }

/* --- ABOUT PAGE --- */
.about-intro::after { background: linear-gradient(to bottom, transparent 0%, #2E2E2E 100%); }
.about-why::after { background: linear-gradient(to bottom, transparent 0%, #242323 100%); }
.about-approach::after { background: linear-gradient(to bottom, transparent 0%, #2E2E2E 100%); }
.about-credentials::after { background: linear-gradient(to bottom, transparent 0%, #242323 100%); }
/* Personal → Final CTA: same color, no fade */

/* --- CONTACT PAGE --- */
.page-header::after { background: linear-gradient(to bottom, transparent 0%, #2E2E2E 100%); }
.contact-methods::after { background: linear-gradient(to bottom, transparent 0%, #242323 100%); }
.contact-form-section::after { background: linear-gradient(to bottom, transparent 0%, #2E2E2E 100%); }
.contact-faq::after { background: linear-gradient(to bottom, transparent 0%, #242323 100%); }

/* --- FOOTER (ALL PAGES) --- */
.footer-fade-top {
  position: absolute;
  top: -100px;
  left: 0;
  right: 0;
  height: 100px;
  background: linear-gradient(to bottom, #242323 0%, rgba(36, 35, 35, 0.5) 40%, transparent 100%);
  z-index: 3;
  pointer-events: none;
}
```

**Base styles for all `::after` fades:**
```css
.hero::after,
.credibility-strip::after,
.services-pricing::after,
.process-section::after,
.retainer-section::after,
.services-faq::after,
.case-study-featured::after,
.project-details::after,
.project-results::after,
.future-work::after,
.about-intro::after,
.about-why::after,
.about-approach::after,
.about-credentials::after,
.page-header::after,
.contact-methods::after,
.contact-form-section::after,
.contact-faq::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  pointer-events: none;
  z-index: 2;
}

.final-cta-section::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 150px;
  pointer-events: none;
  z-index: 2;
}
```

---

## HTML UPDATES

### Footer (All Pages)

Ensure all 5 pages have the `.footer-fade-top` element:

```html
<footer class="footer-section">
  <div class="footer-fade-top" aria-hidden="true"></div>
  <!-- existing footer content -->
</footer>
```

**No other HTML changes needed.** The `::after` pseudo-elements are pure CSS.

---

## RESPONSIVE

On mobile, reduce gradient height:

```css
@media (max-width: 768px) {
  .hero::after,
  .credibility-strip::after,
  .services-pricing::after,
  .process-section::after,
  .retainer-section::after,
  .services-faq::after,
  .case-study-featured::after,
  .project-details::after,
  .project-results::after,
  .future-work::after,
  .about-intro::after,
  .about-why::after,
  .about-approach::after,
  .about-credentials::after,
  .page-header::after,
  .contact-methods::after,
  .contact-form-section::after,
  .contact-faq::after {
    height: 80px;  /* Reduced from 120px */
  }

  .final-cta-section::after {
    height: 100px;  /* Reduced from 150px */
  }

  .footer-fade-top {
    top: -60px;
    height: 60px;
  }
}
```

---

## VERIFICATION CHECKLIST

- [ ] All lower sections use `background-color` only (solid, no gradient)
- [ ] All upper sections that transition to a different color have `::after` with fade
- [ ] Same-color adjacent sections have NO `::after` fade
- [ ] Gradient height: 120px desktop, 80px mobile
- [ ] Footer fade: `.footer-fade-top` element on all 5 pages
- [ ] Footer fade starts at `top: -100px` (desktop), `-60px` (mobile)
- [ ] `pointer-events: none` on all fade elements
- [ ] `z-index: 2` on section `::after`, `z-index: 3` on `.footer-fade-top`
- [ ] No visible hard lines between any sections
- [ ] Transitions feel like dissolves, not boundaries
- [ ] Lighthouse Performance ≥90

---

*Prompt version 1.0 — Fade transition fix, dissolve approach*
