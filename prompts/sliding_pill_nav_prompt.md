# AI Developer Prompt: Sliding Pill Navigation Bar
## For Cursor, GitHub Copilot, or similar AI coding agents

---

## ROLE DEFINITION

You are a **Frontend Developer & UI Engineer** specializing in:
- Semantic, accessible HTML
- Modern CSS (Flexbox, transforms, transitions)
- Vanilla JavaScript for DOM manipulation
- Responsive design with mobile-first approach
- Performance-first development

You write **production-ready code** — not prototypes. Every line must be intentional, commented where logic is non-obvious, and follow modern best practices.

---

## PROJECT CONTEXT

**Client:** Adrian M. — Freelance Web Developer based in Windhoek, Namibia.
**Positioning:** "Friendly & approachable local dev" serving Namibian SMEs.
**Brand:** Personal brand (not agency). Warm, grounded, cinematic.
**Tech stack:** Static HTML/CSS/JS. Multi-page static site (Option A).
**Current state:** Homepage, Contact, Services, Work, and About pages are built. Shared CSS in `css/styles.css`, shared JS in `js/main.js`. This is a **global component update** that applies to ALL pages.

**Design reference:** Client provided an image of a pill-shaped nav bar with a sliding active indicator (green background slides to the active item). The client wants this structure adapted to their brand.

**Client requirements:**
1. **Option B** — Full nav with logo left, pill center, no separate CTA button (Contact is in the pill)
2. **Indicator slides on hover** (preview) AND on page load
3. **Mobile:** Hamburger menu that transforms into the pill nav when opened
4. **Transparent background** on hero, solid on scroll/other pages

---

## TASK

Build a **sliding pill navigation bar** that replaces the existing `site-nav` across all 5 pages. The nav must have:
- A floating pill-shaped container with rounded ends
- A warm brown (`#795238`) sliding indicator that animates to the active/hovered item
- Logo "ADRIAN M." on the left
- 5 nav links inside the pill: Home, Services, Work, About, Contact
- Hover preview: indicator slides to hovered item, returns to active on mouse leave
- Mobile: hamburger button that opens a full-screen overlay with the pill nav centered
- Transparent on hero (homepage), semi-transparent solid on scroll and other pages

---

## FILE STRUCTURE

This component lives in the shared files and is included on every page:

```
/
├── index.html
├── contact.html
├── services.html
├── work.html
├── about.html
├── css/
│   └── styles.css        (nav styles added here)
├── js/
│   └── main.js           (nav JS added here)
└── images/
    └── (none needed for nav)
```

---

## HTML STRUCTURE (Per Page)

Replace the existing `<nav class="site-nav">` on EVERY page with this structure:

```html
<header class="site-header">
  <a href="/" class="nav-logo">ADRIAN M.</a>

  <!-- Desktop & Mobile Overlay Nav -->
  <nav class="nav-pill-container" aria-label="Main navigation">
    <div class="nav-pill">
      <div class="nav-indicator"></div>
      <a href="/" class="nav-link" data-nav="home">Home</a>
      <a href="/services" class="nav-link" data-nav="services">Services</a>
      <a href="/work" class="nav-link" data-nav="work">Work</a>
      <a href="/about" class="nav-link" data-nav="about">About</a>
      <a href="/contact" class="nav-link" data-nav="contact">Contact</a>
    </div>
  </nav>

  <!-- Mobile Hamburger Toggle -->
  <button class="nav-toggle" aria-label="Toggle navigation menu" aria-expanded="false">
    <span class="nav-toggle-line"></span>
    <span class="nav-toggle-line"></span>
    <span class="nav-toggle-line"></span>
  </button>
</header>

<!-- Mobile Overlay Backdrop -->
<div class="nav-overlay" aria-hidden="true"></div>
```

**Rules:**
- `data-nav` attributes are used by JS to identify each link for indicator positioning
- Each page must have the correct link marked with `active` class (or use `aria-current="page"`)
- The hamburger button is hidden on desktop, visible on mobile
- The overlay is the dark backdrop behind the mobile menu

---

## CSS SPECIFICATION

### 1. Site Header (Outer Container)

```css
.site-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 40px;
  transition: background-color 400ms ease, backdrop-filter 400ms ease;
}

/* Transparent on homepage hero */
.site-header--transparent {
  background-color: transparent;
}

/* Solid on scroll and other pages */
.site-header--solid {
  background-color: rgba(36, 35, 35, 0.95);
  backdrop-filter: blur(8px);
}
```

**Rules:**
- On homepage: starts transparent, becomes solid after scrolling past hero (100px threshold)
- On other pages (contact, services, work, about): always solid
- Transition is smooth (400ms)

### 2. Logo

```css
.nav-logo {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 18px;
  color: #AEA7A3;
  text-decoration: none;
  letter-spacing: 1px;
  z-index: 1001;  /* Above mobile overlay */
  transition: color 200ms ease;
}

.nav-logo:hover {
  color: #F8F9FB;
}
```

### 3. Pill Container (Desktop)

```css
.nav-pill-container {
  position: relative;
  z-index: 1001;
}

.nav-pill {
  position: relative;
  display: inline-flex;
  align-items: center;
  background: rgba(36, 35, 35, 0.6);  /* Semi-transparent dark */
  border: 1px solid rgba(74, 74, 74, 0.3);  /* Subtle border */
  border-radius: 100px;  /* Full pill shape */
  padding: 6px;
  gap: 0;  /* No gap — indicator handles spacing */
}
```

### 4. Sliding Indicator

```css
.nav-indicator {
  position: absolute;
  top: 6px;
  bottom: 6px;
  background-color: #795238;  /* Warm brown */
  border-radius: 100px;
  z-index: 0;
  transition: left 300ms cubic-bezier(0.25, 0.1, 0.25, 1),
              width 300ms cubic-bezier(0.25, 0.1, 0.25, 1);
  pointer-events: none;  /* Let clicks pass through to links */
}
```

**Rules:**
- Indicator is positioned absolutely within the pill
- `left` and `width` are animated — NOT `transform` (width changes per link)
- Easing: `cubic-bezier(0.25, 0.1, 0.25, 1)` — smooth, not bouncy
- `pointer-events: none` so clicks go to the link underneath

### 5. Nav Links

```css
.nav-link {
  position: relative;
  z-index: 1;  /* Above indicator */
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 24px;
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  font-size: 14px;
  color: #959595;  /* Inactive color */
  text-decoration: none;
  border-radius: 100px;
  transition: color 200ms ease;
  white-space: nowrap;
}

.nav-link:hover,
.nav-link:focus {
  color: #F8F9FB;  /* Bright on hover/focus */
  outline: none;
}

.nav-link.active,
.nav-link[aria-current="page"] {
  color: #242323;  /* Dark text on warm brown indicator */
}
```

**Rules:**
- Active link has dark text (`#242323`) because it sits on the warm brown indicator
- Inactive links have `#959595`
- Hover on inactive: brightens to `#F8F9FB`
- No underline, no background change on hover (the indicator does the work)

### 6. Mobile Hamburger Toggle

```css
.nav-toggle {
  display: none;  /* Hidden on desktop */
  position: relative;
  z-index: 1002;  /* Above everything */
  width: 44px;
  height: 44px;
  background: rgba(36, 35, 35, 0.6);
  border: 1px solid rgba(74, 74, 74, 0.3);
  border-radius: 12px;
  cursor: pointer;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 5px;
  padding: 0;
}

.nav-toggle-line {
  display: block;
  width: 20px;
  height: 2px;
  background-color: #AEA7A3;
  border-radius: 2px;
  transition: transform 300ms ease, opacity 300ms ease, background-color 300ms ease;
}

/* Hamburger to X animation */
.nav-toggle[aria-expanded="true"] .nav-toggle-line:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

.nav-toggle[aria-expanded="true"] .nav-toggle-line:nth-child(2) {
  opacity: 0;
}

.nav-toggle[aria-expanded="true"] .nav-toggle-line:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}
```

### 7. Mobile Overlay

```css
.nav-overlay {
  position: fixed;
  inset: 0;
  background-color: rgba(36, 35, 35, 0.98);
  z-index: 999;
  opacity: 0;
  visibility: hidden;
  transition: opacity 400ms ease, visibility 400ms ease;
}

.nav-overlay.is-open {
  opacity: 1;
  visibility: visible;
}
```

### 8. Mobile Menu State

When the mobile menu is open, the pill nav transforms:

```css
/* Mobile: pill nav becomes centered vertical menu */
@media (max-width: 768px) {
  .nav-toggle {
    display: flex;  /* Show hamburger */
  }

  .nav-pill-container {
    position: fixed;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    opacity: 0;
    visibility: hidden;
    transition: opacity 400ms ease, visibility 400ms ease;
  }

  .nav-pill-container.is-open {
    opacity: 1;
    visibility: visible;
  }

  .nav-pill {
    flex-direction: column;  /* Stack vertically */
    background: transparent;
    border: none;
    padding: 0;
    gap: 8px;
  }

  .nav-indicator {
    display: none;  /* Hide sliding indicator on mobile — use background highlight instead */
  }

  .nav-link {
    padding: 16px 32px;
    font-size: 18px;
    color: #959595;
    background: transparent;
    border-radius: 12px;
    transition: background-color 200ms ease, color 200ms ease;
  }

  .nav-link:hover,
  .nav-link:focus {
    background-color: rgba(121, 82, 56, 0.2);  /* Subtle warm brown tint */
    color: #F8F9FB;
  }

  .nav-link.active,
  .nav-link[aria-current="page"] {
    background-color: #795238;  /* Warm brown fill */
    color: #242323;
  }
}
```

**Rules:**
- On mobile, the pill container becomes a full-screen overlay
- The pill shape is dropped — links stack vertically
- The sliding indicator is hidden; instead, active link gets warm brown background
- Hamburger transforms to X when open
- Clicking overlay or a link closes the menu

### 9. Scroll Behavior (Homepage Only)

```css
/* JS adds/removes this class based on scroll position */
.site-header--scrolled {
  background-color: rgba(36, 35, 35, 0.95);
  backdrop-filter: blur(8px);
}
```

---

## JAVASCRIPT SPECIFICATION

Add this to `js/main.js`:

```javascript
// ========================================
// SLIDING PILL NAVIGATION
// ========================================

document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.site-header');
  const pill = document.querySelector('.nav-pill');
  const indicator = document.querySelector('.nav-indicator');
  const links = document.querySelectorAll('.nav-link');
  const toggle = document.querySelector('.nav-toggle');
  const pillContainer = document.querySelector('.nav-pill-container');
  const overlay = document.querySelector('.nav-overlay');

  if (!pill || !indicator || !links.length) return;

  // --- INDICATOR POSITIONING ---

  function moveIndicatorTo(element) {
    const pillRect = pill.getBoundingClientRect();
    const elemRect = element.getBoundingClientRect();

    indicator.style.left = `${elemRect.left - pillRect.left}px`;
    indicator.style.width = `${elemRect.width}px`;
  }

  function resetIndicatorToActive() {
    const activeLink = pill.querySelector('.nav-link.active, .nav-link[aria-current="page"]');
    if (activeLink) {
      moveIndicatorTo(activeLink);
    }
  }

  // Initial position on page load
  resetIndicatorToActive();

  // Reposition on window resize
  window.addEventListener('resize', () => {
    resetIndicatorToActive();
  });

  // --- HOVER PREVIEW ---

  links.forEach(link => {
    link.addEventListener('mouseenter', () => {
      moveIndicatorTo(link);
    });

    link.addEventListener('mouseleave', () => {
      resetIndicatorToActive();
    });
  });

  // --- MOBILE MENU TOGGLE ---

  if (toggle && pillContainer && overlay) {
    function openMenu() {
      toggle.setAttribute('aria-expanded', 'true');
      pillContainer.classList.add('is-open');
      overlay.classList.add('is-open');
      document.body.style.overflow = 'hidden';  /* Prevent scroll */
    }

    function closeMenu() {
      toggle.setAttribute('aria-expanded', 'false');
      pillContainer.classList.remove('is-open');
      overlay.classList.remove('is-open');
      document.body.style.overflow = '';  /* Restore scroll */
    }

    toggle.addEventListener('click', () => {
      const isOpen = toggle.getAttribute('aria-expanded') === 'true';
      isOpen ? closeMenu() : openMenu();
    });

    // Close on overlay click
    overlay.addEventListener('click', closeMenu);

    // Close on link click (mobile)
    links.forEach(link => {
      link.addEventListener('click', () => {
        if (window.innerWidth <= 768) {
          closeMenu();
        }
      });
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        closeMenu();
      }
    });
  }

  // --- SCROLL BEHAVIOR (Homepage only) ---

  // Check if we're on the homepage (no specific class needed, just check path)
  const isHomepage = window.location.pathname === '/' || 
                     window.location.pathname === '/index.html' ||
                     window.location.pathname.endsWith('index.html');

  if (isHomepage && header) {
    let lastScroll = 0;
    const scrollThreshold = 100;  /* px from top */

    window.addEventListener('scroll', () => {
      const currentScroll = window.pageYOffset;

      if (currentScroll > scrollThreshold) {
        header.classList.add('site-header--scrolled');
        header.classList.remove('site-header--transparent');
      } else {
        header.classList.remove('site-header--scrolled');
        header.classList.add('site-header--transparent');
      }

      lastScroll = currentScroll;
    });

    // Set initial state
    if (window.pageYOffset <= scrollThreshold) {
      header.classList.add('site-header--transparent');
    } else {
      header.classList.add('site-header--scrolled');
    }
  } else if (header) {
    // Other pages: always solid
    header.classList.add('site-header--solid');
  }
});
```

**Rules:**
- Indicator uses `left` + `width` (not transform) because each link has different width
- Hover preview: indicator slides to hovered link, returns to active on mouse leave
- Mobile: full-screen overlay, hamburger → X animation, body scroll locked
- Homepage: transparent → solid on scroll (100px threshold)
- Other pages: always solid
- Escape key closes mobile menu
- Clicking overlay or a link closes mobile menu

---

## PER-PAGE IMPLEMENTATION

On **each page**, update the nav link markup:

### Homepage (`index.html`)
```html
<a href="/" class="nav-link active" data-nav="home" aria-current="page">Home</a>
<a href="/services" class="nav-link" data-nav="services">Services</a>
<a href="/work" class="nav-link" data-nav="work">Work</a>
<a href="/about" class="nav-link" data-nav="about">About</a>
<a href="/contact" class="nav-link" data-nav="contact">Contact</a>
```

### Services (`services.html`)
```html
<a href="/" class="nav-link" data-nav="home">Home</a>
<a href="/services" class="nav-link active" data-nav="services" aria-current="page">Services</a>
<a href="/work" class="nav-link" data-nav="work">Work</a>
<a href="/about" class="nav-link" data-nav="about">About</a>
<a href="/contact" class="nav-link" data-nav="contact">Contact</a>
```

### Work (`work.html`)
```html
<a href="/" class="nav-link" data-nav="home">Home</a>
<a href="/services" class="nav-link" data-nav="services">Services</a>
<a href="/work" class="nav-link active" data-nav="work" aria-current="page">Work</a>
<a href="/about" class="nav-link" data-nav="about">About</a>
<a href="/contact" class="nav-link" data-nav="contact">Contact</a>
```

### About (`about.html`)
```html
<a href="/" class="nav-link" data-nav="home">Home</a>
<a href="/services" class="nav-link" data-nav="services">Services</a>
<a href="/work" class="nav-link" data-nav="work">Work</a>
<a href="/about" class="nav-link active" data-nav="about" aria-current="page">About</a>
<a href="/contact" class="nav-link" data-nav="contact">Contact</a>
```

### Contact (`contact.html`)
```html
<a href="/" class="nav-link" data-nav="home">Home</a>
<a href="/services" class="nav-link" data-nav="services">Services</a>
<a href="/work" class="nav-link" data-nav="work">Work</a>
<a href="/about" class="nav-link" data-nav="about">About</a>
<a href="/contact" class="nav-link active" data-nav="contact" aria-current="page">Contact</a>
```

---

## CSS IN SHARED STYLESHEET

Add all nav CSS to `css/styles.css`. Remove any old `.site-nav` styles.

**Organization:**
```css
/* ========================================
   NAVIGATION — SLIDING PILL
   ======================================== */

/* Header */
.site-header { ... }
.site-header--transparent { ... }
.site-header--solid { ... }
.site-header--scrolled { ... }

/* Logo */
.nav-logo { ... }

/* Pill Container */
.nav-pill-container { ... }
.nav-pill { ... }

/* Indicator */
.nav-indicator { ... }

/* Links */
.nav-link { ... }
.nav-link.active,
.nav-link[aria-current="page"] { ... }

/* Toggle */
.nav-toggle { ... }
.nav-toggle-line { ... }

/* Overlay */
.nav-overlay { ... }
.nav-overlay.is-open { ... }

/* Mobile */
@media (max-width: 768px) { ... }
```

---

## ACCESSIBILITY

- `aria-label="Main navigation"` on `<nav>`
- `aria-expanded` on hamburger toggle (updated by JS)
- `aria-current="page"` on active link
- `aria-hidden="true"` on overlay when closed
- Focus trap in mobile menu (optional enhancement)
- Keyboard: Tab through links, Enter/Space to activate, Escape to close mobile menu
- `prefers-reduced-motion`: disable indicator transition, instant snap

```css
@media (prefers-reduced-motion: reduce) {
  .nav-indicator {
    transition: none;
  }

  .nav-toggle-line,
  .nav-overlay,
  .nav-pill-container,
  .site-header {
    transition: none;
  }
}
```

---

## NO-GO LIST

- [ ] No notification badge (the "4" in the reference) — not needed
- [ ] No dropdown menus — all links are top-level
- [ ] No search bar in nav
- [ ] No "Get Started" button separate from pill — Contact link serves this purpose
- [ ] No glassmorphism or blur on the pill itself (only on header backdrop when scrolled)
- [ ] No glossy effects

---

## DELIVERABLE

1. Updated `css/styles.css` with new nav styles (old nav styles removed)
2. Updated `js/main.js` with nav functionality
3. Updated HTML on all 5 pages with new nav structure
4. Active link correctly set per page
5. Indicator slides on hover (desktop)
6. Mobile hamburger opens full-screen overlay with vertical pill links
7. Homepage: transparent → solid on scroll
8. Other pages: always solid
9. No console errors
10. Responsive at all breakpoints

---

## VERIFICATION CHECKLIST

- [ ] Logo "ADRIAN M." left-aligned, links to `/`
- [ ] Pill nav centered, 5 links: Home, Services, Work, About, Contact
- [ ] Pill has rounded ends (100px border-radius)
- [ ] Pill background: semi-transparent dark, subtle border
- [ ] Sliding indicator: warm brown (`#795238`), rounded, animates smoothly
- [ ] Active link has dark text (`#242323`) on indicator
- [ ] Inactive links: `#959595`, hover: `#F8F9FB`
- [ ] Hover preview: indicator slides to hovered link, returns to active on mouse leave
- [ ] Indicator repositioned correctly on window resize
- [ ] Homepage: header transparent at top, solid after 100px scroll
- [ ] Other pages: header always solid with subtle blur
- [ ] Mobile (<768px): hamburger button visible, pill nav hidden
- [ ] Hamburger: 3 lines, transforms to X when open
- [ ] Mobile menu: full-screen overlay, links stacked vertically
- [ ] Active link on mobile: warm brown background fill
- [ ] Clicking overlay or link closes mobile menu
- [ ] Escape key closes mobile menu
- [ ] Body scroll locked when mobile menu open
- [ ] Active link correctly set on each of the 5 pages
- [ ] `prefers-reduced-motion` disables animations
- [ ] Lighthouse Accessibility ≥95

---

*Prompt version 1.0 — Sliding pill navigation bar, global component*
