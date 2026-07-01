# AI Developer Prompt: Inner Page Hero Images
## For Cursor, GitHub Copilot, or similar AI coding agents

---

## ROLE DEFINITION

You are a **Frontend Developer & UI Engineer** specializing in:
- Semantic, accessible HTML
- Modern CSS (background images, gradients, responsive design)
- Performance-first development

You write **production-ready code** — not prototypes. Every line must be intentional, commented where logic is non-obvious, and follow modern best practices.

---

## PROJECT CONTEXT

**Client:** Adrian M. — Freelance Web Developer based in Windhoek, Namibia.
**Positioning:** "Friendly & approachable local dev" serving Namibian SMEs.
**Brand:** Personal brand (not agency). Warm, grounded, cinematic.
**Tech stack:** Static HTML/CSS/JS. Multi-page static site (Option A).
**Current state:** 5-page site built (Home, Contact, Services, Work, About). Shared CSS in `css/styles.css`. Shared JS in `js/main.js`.

**Problem:** Inner page heroes (Services, Work, About, Contact) are currently text on flat dark backgrounds — boring and generic.

**Solution:** Add distinctive background images to each inner page hero, with a dark gradient overlay for text readability. The homepage hero with the cutout remains unchanged.

**Assets provided:**
- `Windhoek, Namibia(1).jpeg` — Christuskirche at sunset, warm orange/red sky, iconic Windhoek landmark
- `If You Buy Only One Gadget This Month...` — Dark workspace with keyboard, coffee cup, monitor, phone. Moody, tech-focused.

---

## TASK

Implement image-based heroes for all 4 inner pages (Services, Work, About, Contact). Each page gets a unique image with a dark gradient overlay. Text sits clearly on top. The result feels cinematic, grounded, and distinct per page.

---

## IMAGE ASSIGNMENTS

| Page | Image | Why This Image |
|------|-------|---------------|
| **About** | `Windhoek, Namibia(1).jpeg` | Christuskirche at sunset — iconic, warm, unmistakably Namibian. Perfect for the "who I am" page. |
| **Services** | `If You Buy Only One Gadget This Month...` | Dark workspace — "this is where I build." Moody, professional, hints at craft. |
| **Work** | `Windhoek, Namibia(1).jpeg` (reused, different crop/position) | Same Windhoek warmth, but positioned differently. Or use a project screenshot if available. |
| **Contact** | `If You Buy Only One Gadget This Month...` (reused, different crop/position) | Workspace invites action — "let's build something." |

**Note:** Only 2 unique images provided. Reuse with different `background-position` values to create variety:
- About: `background-position: center 30%` (focus on church)
- Work: `background-position: center 70%` (focus on sky/hills)
- Services: `background-position: center` (full workspace)
- Contact: `background-position: right center` (focus on coffee cup)

---

## SHARED CSS (Add to `css/styles.css`)

```css
/* ========================================
   INNER PAGE HEROES — IMAGE BACKGROUNDS
   ======================================== */

.page-hero {
  position: relative;
  width: 100%;
  min-height: 420px;        /* Desktop */
  max-height: 55vh;
  display: flex;
  align-items: flex-end;    /* Text at bottom */
  padding: 100px 40px 60px; /* Extra top padding for fixed nav */
  overflow: hidden;
}

.page-hero-image {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-repeat: no-repeat;
  z-index: 0;
}

.page-hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    rgba(36, 35, 35, 0.3) 0%,      /* Top: image slightly visible */
    rgba(36, 35, 35, 0.6) 40%,     /* Middle: darker */
    rgba(36, 35, 35, 0.9) 80%,     /* Near bottom: very dark */
    #242323 100%                    /* Bottom: solid for text */
  );
  z-index: 1;
}

.page-hero-content {
  position: relative;
  z-index: 2;
  max-width: 800px;
}

.page-hero h1 {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: clamp(36px, 5vw, 56px);
  color: #AEA7A3;
  line-height: 1.1;
  margin-bottom: 12px;
}

.page-hero p {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 18px;
  color: #959595;
  line-height: 1.5;
  max-width: 500px;
}

/* --- PER-PAGE IMAGE ASSIGNMENTS --- */

/* About — Christuskirche, focus on church */
.page-hero--about .page-hero-image {
  background-image: url('../images/Windhoek-Namibia.jpeg');
  background-position: center 30%;
}

/* Work — Christuskirche, focus on sky/hills */
.page-hero--work .page-hero-image {
  background-image: url('../images/Windhoek-Namibia.jpeg');
  background-position: center 70%;
}

/* Services — Workspace, centered */
.page-hero--services .page-hero-image {
  background-image: url('../images/workspace-dark.jpeg');
  background-position: center;
}

/* Contact — Workspace, focus on coffee cup (right side) */
.page-hero--contact .page-hero-image {
  background-image: url('../images/workspace-dark.jpeg');
  background-position: right center;
}

/* --- RESPONSIVE --- */

@media (max-width: 768px) {
  .page-hero {
    min-height: 320px;
    padding: 80px 20px 40px;
  }

  .page-hero h1 {
    font-size: 32px;
  }

  .page-hero p {
    font-size: 16px;
  }
}
```

**Rules:**
- `inset: 0` is shorthand for `top: 0; right: 0; bottom: 0; left: 0`
- Gradient overlay is essential — without it, text is unreadable on bright images
- `background-position` creates variety even with reused images
- `max-height: 55vh` prevents heroes from dominating on large screens

---

## HTML UPDATES (Per Page)

Replace the existing `<header class="page-header">` on each inner page with the new `.page-hero` structure.

### Services (`services.html`)

```html
<!-- REPLACE this -->
<header class="page-header">
  <h1>Services</h1>
  <p>Websites that win you customers — at a price that makes sense for Namibian SMEs.</p>
</header>

<!-- WITH this -->
<header class="page-hero page-hero--services">
  <div class="page-hero-image"></div>
  <div class="page-hero-overlay"></div>
  <div class="page-hero-content">
    <h1>Services</h1>
    <p>Websites that win you customers — at a price that makes sense for Namibian SMEs.</p>
  </div>
</header>
```

### Work (`work.html`)

```html
<header class="page-hero page-hero--work">
  <div class="page-hero-image"></div>
  <div class="page-hero-overlay"></div>
  <div class="page-hero-content">
    <h1>Selected Work</h1>
    <p>Real projects. Real results.</p>
  </div>
</header>
```

### About (`about.html`)

```html
<header class="page-hero page-hero--about">
  <div class="page-hero-image"></div>
  <div class="page-hero-overlay"></div>
  <div class="page-hero-content">
    <h1>About</h1>
    <p>The person behind the websites.</p>
  </div>
</header>
```

### Contact (`contact.html`)

```html
<header class="page-hero page-hero--contact">
  <div class="page-hero-image"></div>
  <div class="page-hero-overlay"></div>
  <div class="page-hero-content">
    <h1>Let's Talk</h1>
    <p>Have a project in mind? I'll get back to you within 24 hours.</p>
  </div>
</header>
```

---

## FILE STRUCTURE

Ensure images are in the correct directory:

```
/
├── index.html
├── contact.html
├── services.html
├── work.html
├── about.html
├── css/
│   └── styles.css
├── js/
│   └── main.js
└── images/
    ├── hero-cutout.png
    ├── TMU-before.png
    ├── TMU-after.png
    ├── desert-namibia.jpeg
    ├── Windhoek-Namibia.jpeg      (rename from upload)
    └── workspace-dark.jpeg          (rename from upload)
```

**Image naming:** Use clean filenames (no spaces, no special characters):
- `Windhoek, Namibia(1).jpeg` → `Windhoek-Namibia.jpeg`
- `If You Buy Only One Gadget This Month...` → `workspace-dark.jpeg`

---

## OLD CSS TO REMOVE

From `css/styles.css`, remove the old `.page-header` styles:

```css
/* REMOVE this block entirely */
.page-header {
  background-color: #242323;
  padding: 140px 20px 60px;
  text-align: center;
}

.page-header h1 { ... }
.page-header p { ... }
```

**Replace with** the new `.page-hero` block above.

---

## PERFORMANCE

- Images: Optimize before deployment
  - Max width: 1920px
  - Compress to ~300–500KB each
  - Use `loading="eager"` (heroes are above the fold)
- No `background-attachment: fixed` — causes jank on mobile
- Gradient overlay is CSS-only — no performance cost

---

## ACCESSIBILITY

- `.page-hero-image` is decorative — no alt text needed (CSS background)
- Text contrast: `#AEA7A3` on dark overlay = 5.8:1 ✓
- Subheading contrast: `#959595` on dark overlay = 5.1:1 ✓

---

## NO-GO LIST

- [ ] No `background-attachment: fixed` — causes mobile jank
- [ ] No parallax effects — keep it simple
- [ ] No blur or glassmorphism on overlay — matte gradient only
- [ ] No animated backgrounds — static images only
- [ ] No video backgrounds — too heavy for this site

---

## DELIVERABLE

1. Updated `css/styles.css`:
   - Remove old `.page-header` styles
   - Add new `.page-hero` styles with image assignments
2. Updated HTML on all 4 inner pages (`services.html`, `work.html`, `about.html`, `contact.html`):
   - Replace `<header class="page-header">` with `<header class="page-hero page-hero--[page]">`
3. Images in `images/` directory with clean filenames
4. No console errors
5. Responsive at all breakpoints

---

## VERIFICATION CHECKLIST

- [ ] Services page hero shows dark workspace image, text readable
- [ ] Work page hero shows Windhoek sunset image (different crop from About)
- [ ] About page hero shows Windhoek sunset image (focus on church)
- [ ] Contact page hero shows dark workspace image (different crop from Services)
- [ ] All heroes have dark gradient overlay — text is clearly readable
- [ ] Overlay gradient: top 30% visible, bottom 100% solid dark
- [ ] Hero height: 420px desktop, 320px mobile
- [ ] Text aligned bottom-left (not centered), max-width 800px
- [ ] Heading in Syne, subheading in DM Sans
- [ ] Old `.page-header` styles completely removed from CSS
- [ ] No broken layouts, no text overflow
- [ ] Images load without layout shift
- [ ] Lighthouse Performance ≥90, Accessibility ≥95

---

*Prompt version 1.0 — Inner page hero images*
