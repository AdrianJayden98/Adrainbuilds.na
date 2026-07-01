# AI Developer Prompt: Enhanced Page Headers
## For Cursor, GitHub Copilot, or similar AI coding agents

---

## ROLE DEFINITION

You are a **Frontend Developer & UI Engineer** specializing in:
- Semantic, accessible HTML
- Modern CSS (positioning, typography, gradients, responsive design)
- Visual hierarchy and editorial design
- Performance-first development

You write **production-ready code** — not prototypes. Every line must be intentional, commented where logic is non-obvious, and follow modern best practices.

---

## PROJECT CONTEXT

**Client:** Adrian M. — Freelance Web Developer based in Windhoek, Namibia.
**Positioning:** "Friendly & approachable local dev" serving Namibian SMEs.
**Brand:** Personal brand (not agency). Warm, grounded, cinematic.
**Tech stack:** Static HTML/CSS/JS. Multi-page static site (Option A).
**Current state:** 5-page site built (Home, Contact, Services, Work, About). Shared CSS in `css/styles.css`. Shared JS in `js/main.js`.

**Problem:** The page headers on Services, Work, About, and Contact pages are text-only and feel flat compared to the homepage hero. The client wants them more engaging and visually substantial without reusing the homepage cutout image.

**Solution:** Add large display typography (massive faint background text) + a subtle warm brown glow accent behind the heading. This creates depth, visual interest, and consistency with the existing Services section background headline on the homepage.

---

## TASK

Update the **page headers** on all 4 non-homepage pages (Services, Work, About, Contact) with:
1. A massive, faint display text behind the heading (editorial depth)
2. A subtle warm brown glow/orb behind the content (accent depth)
3. Increased vertical padding for more breathing room
4. Clean, consistent styling across all pages

The homepage hero remains unchanged.

---

## FILE STRUCTURE

This is a CSS/HTML update across 4 files:

```
/
├── index.html              (homepage — NO CHANGES)
├── contact.html            (update page header)
├── services.html           (update page header)
├── work.html               (update page header)
├── about.html              (update page header)
├── css/
│   └── styles.css          (add shared page-header styles)
└── js/
    └── main.js             (no changes needed)
```

---

## SHARED CSS (Add to `css/styles.css`)

Add this block to the shared stylesheet. It applies to all 4 non-homepage pages.

```css
/* ========================================
   ENHANCED PAGE HEADERS
   (Services, Work, About, Contact)
   ======================================== */

.page-header {
  position: relative;
  background-color: #242323;
  padding: 160px 20px 100px;  /* Increased from 140px/60px */
  text-align: center;
  overflow: hidden;  /* Contains the massive background text */
}

/* --- Layer 1: Warm brown glow accent (subtle) --- */
.page-header::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 500px;
  height: 500px;
  background: radial-gradient(
    circle,
    rgba(121, 82, 56, 0.12) 0%,    /* Warm brown, very faint */
    transparent 70%
  );
  border-radius: 50%;
  pointer-events: none;
  z-index: 0;
}

/* --- Layer 2: Massive display text (faint watermark) --- */
.page-header-bg-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-family: 'Syne', sans-serif;
  font-weight: 800;
  font-size: clamp(80px, 14vw, 220px);
  color: #2E2E2E;  /* Barely visible against #242323 */
  letter-spacing: -4px;
  text-transform: uppercase;
  white-space: nowrap;
  pointer-events: none;
  user-select: none;
  z-index: 0;
}

/* --- Layer 3: Content (heading + subheading) --- */
.page-header-content {
  position: relative;
  z-index: 1;
}

.page-header h1 {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: clamp(36px, 5vw, 56px);
  color: #AEA7A3;
  line-height: 1.1;
  margin-bottom: 16px;
}

.page-header p {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: clamp(16px, 2vw, 20px);
  color: #959595;
  line-height: 1.6;
  max-width: 560px;
  margin: 0 auto;
}

/* --- Responsive --- */
@media (max-width: 768px) {
  .page-header {
    padding: 120px 20px 60px;
  }

  .page-header::before {
    width: 300px;
    height: 300px;
  }

  .page-header-bg-text {
    font-size: clamp(60px, 18vw, 120px);
    letter-spacing: -2px;
  }

  .page-header h1 {
    font-size: 32px;
  }

  .page-header p {
    font-size: 16px;
  }
}
```

---

## PER-PAGE HTML UPDATES

Update the `<header class="page-header">` section on each of the 4 pages.

### Services Page (`services.html`)

**Replace the existing page header with:**

```html
<header class="page-header">
  <div class="page-header-bg-text" aria-hidden="true">Services</div>
  <div class="page-header-content">
    <h1>What I Build</h1>
    <p>Websites that win you customers — at a price that makes sense for Namibian SMEs.</p>
  </div>
</header>
```

**Changes from old version:**
- Added `page-header-bg-text` div
- Added `page-header-content` wrapper
- Heading changed from "Services" to "What I Build" (more engaging)
- Subheading kept the same
- `aria-hidden="true"` on background text (decorative only)

### Work Page (`work.html`)

**Replace the existing page header with:**

```html
<header class="page-header">
  <div class="page-header-bg-text" aria-hidden="true">Work</div>
  <div class="page-header-content">
    <h1>Selected Work</h1>
    <p>Real projects for real Namibian businesses. Every site is built to perform.</p>
  </div>
</header>
```

### About Page (`about.html`)

**Replace the existing page header with:**

```html
<header class="page-header">
  <div class="page-header-bg-text" aria-hidden="true">About</div>
  <div class="page-header-content">
    <h1>About</h1>
    <p>The person behind the websites.</p>
  </div>
</header>
```

### Contact Page (`contact.html`)

**Replace the existing page header with:**

```html
<header class="page-header">
  <div class="page-header-bg-text" aria-hidden="true">Contact</div>
  <div class="page-header-content">
    <h1>Let's Talk</h1>
    <p>Have a project in mind? Send me a message and I'll get back to you within 24 hours.</p>
  </div>
</header>
```

---

## VISUAL LAYERING (Z-INDEX)

The page header has 3 layers, bottom to top:

```
Z-INDEX 0:  .page-header::before     (warm brown glow — radial gradient)
Z-INDEX 0:  .page-header-bg-text      (massive faint text — "Services", "Work", etc.)
Z-INDEX 1:  .page-header-content      (heading + subheading — readable, sharp)
```

**Rules:**
- Both background layers are at z-index 0 — they don't interact
- The glow is `::before` pseudo-element, the text is a real element
- Content is at z-index 1 — always readable above both
- `pointer-events: none` on background layers — clicks pass through

---

## WHY THIS WORKS

| Element | Purpose | Visual Effect |
|---------|---------|---------------|
| **Warm brown glow** | Adds depth and warmth | Subtle spotlight behind text, ties to brand accent |
| **Massive display text** | Creates scale and editorial feel | "Services" at 220px is dramatic but not distracting |
| **Increased padding** | More breathing room | Feels substantial, not cramped |
| **Layered z-index** | Ensures readability | Content always sits above decorative elements |

**The result:** Page headers feel designed, not default. They have the same cinematic quality as the homepage hero without needing a photo or cutout.

---

## RESPONSIVE BEHAVIOR

| Breakpoint | Adjustments |
|------------|-------------|
| ≥1024px | Full layout: 220px display text, 500px glow, 160px top padding |
| 768–1023px | 160px display text, 400px glow, 140px top padding |
| <768px | 120px display text, 300px glow, 120px top padding, heading 32px |

**On very small screens (375px):** The display text may be partially cropped — this is intentional and acceptable. The text is decorative.

---

## ACCESSIBILITY

- `aria-hidden="true"` on `.page-header-bg-text` — screen readers skip the decorative text
- `aria-hidden="true"` on the glow `::before` — already decorative (pseudo-element)
- Heading hierarchy maintained: `<h1>` is the actual page title
- Color contrast: `#AEA7A3` on `#242323` = 5.8:1 ✓
- No motion or animation — static, no `prefers-reduced-motion` needed

---

## PERFORMANCE

- No images added — pure CSS
- No external libraries
- Radial gradient is GPU-accelerated
- Target: No impact on Lighthouse Performance score

---

## NO-GO LIST

- [ ] No animated gradients — static only
- [ ] No blur or backdrop-filter — matte finish
- [ ] No cutout image reuse — homepage only
- [ ] No background images or video in headers
- [ ] No parallax effects
- [ ] No glossy effects

---

## DELIVERABLE

1. Updated `css/styles.css` with new `.page-header` block
2. Updated HTML on 4 pages (`services.html`, `work.html`, `about.html`, `contact.html`)
3. Homepage (`index.html`) — NO CHANGES
4. No console errors
5. Responsive at all breakpoints

---

## VERIFICATION CHECKLIST

- [ ] Services page: "Services" display text faint behind "What I Build" heading
- [ ] Work page: "Work" display text faint behind "Selected Work" heading
- [ ] About page: "About" display text faint behind "About" heading
- [ ] Contact page: "Contact" display text faint behind "Let's Talk" heading
- [ ] Warm brown glow visible but subtle behind content on all 4 pages
- [ ] Heading text is sharp and readable above both background layers
- [ ] Subheading text is readable and centered
- [ ] Increased padding (160px top, 100px bottom) feels substantial
- [ ] Mobile: display text smaller, glow smaller, padding reduced to 120px/60px
- [ ] No layout shift, overflow, or broken text at any breakpoint
- [ ] `aria-hidden="true"` on all decorative background text
- [ ] Homepage hero — NO CHANGES (remains as-is)
- [ ] Lighthouse Accessibility ≥95, Performance ≥90

---

*Prompt version 1.0 — Enhanced page headers with display typography and glow accent*
