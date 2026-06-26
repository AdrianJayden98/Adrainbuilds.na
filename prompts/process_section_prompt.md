# AI Developer Prompt: Process Section
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
**Current state:** Hero, Credibility Strip, Services Preview, and Selected Work sections are complete and locked. This is the **fifth section** on the homepage.

**Why this section exists:** Namibian SMEs are often nervous about hiring freelancers — they've been burned by offshore devs who disappear, deliver late, or go over budget. A clear process answers: "What happens after I contact you? Will I be left in the dark?"

---

## TASK

Build a **Process** section showing Adrian's 4-step workflow. This section must feel structured and reliable without being corporate or rigid. The tone is "I know what I'm doing, and I'll keep you informed."

---

## DESIGN SPECIFICATION

### Section Container

```css
.process-section {
  background-color: #2E2E2E;  /* Lighter than surrounding sections — breath, same as credibility strip */
  padding: 100px 20px;
  width: 100%;
}
```

**Rules:**
- No border-top or border-bottom — color shift creates separation
- Full-width background, content constrained to max-width 1200px centered

---

### Section Header

```
How We Work Together
No surprises. No confusion. Just a clear path from idea to launch.
```

| Element | Font | Weight | Size | Line-Height | Color |
|---------|------|--------|------|-------------|-------|
| Heading "How We Work Together" | Syne | 700 | 42px | 1.1 | `#AEA7A3` |
| Subheading | DM Sans | 400 | 18px | 1.6 | `#959595` |

**Positioning:** Left-aligned, max-width 600px, margin-bottom 64px.

**On mobile:** heading 32px, subheading 16px.

---

### 4-Step Process (Desktop ≥1024px)

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  How We Work Together                                       │
│  No surprises. No confusion. Just a clear path...           │
│                                                             │
│  ┌──────────┐      ┌──────────┐      ┌──────────┐      ┌──────┐
│  │   01     │─────▶│   02     │─────▶│   03     │─────▶│  04  │
│  │          │      │          │      │          │      │      │
│  │ Discovery│      │ Design   │      │ Build    │      │Launch│
│  │          │      │          │      │          │      │      │
│  │ We talk  │      │ I build  │      │ Clean    │      │Your  │
│  │ about    │      │ a clear  │      │ code,    │      │site  │
│  │ your     │      │ structure│      │ fast     │      │goes  │
│  │ business │      │ and      │      │ loading, │      │live  │
│  │ and what │      │ visual   │      │ tested   │      │— and │
│  │ the site │      │ direction│      │ on real  │      │I stay│
│  │ needs to │      │ — no     │      │ devices. │      │around│
│  │ do.      │      │surprises.│      │          │      │to    │
│  │          │      │          │      │          │      │help. │
│  └──────────┘      └──────────┘      └──────────┘      └──────┘
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Layout:**
- 4 columns, equal width
- Gap: 24px
- Connected by horizontal lines or arrows between steps
- Steps are numbered 01, 02, 03, 04 — not 1, 2, 3, 4 (the leading zero feels more designed)

---

### Step Card Design

```css
.process-step {
  position: relative;
  padding-top: 24px;  /* Space for the number above */
}

.process-step-number {
  font-family: 'Syne', sans-serif;
  font-weight: 800;
  font-size: 14px;
  color: #795238;       /* Warm brown accent */
  letter-spacing: 2px;
  margin-bottom: 16px;
}

.process-step-title {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 22px;
  color: #AEA7A3;
  margin-bottom: 12px;
}

.process-step-description {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 15px;
  color: #959595;
  line-height: 1.6;
}
```

**Connector Lines (between steps):**
```css
.process-step:not(:last-child)::after {
  content: '';
  position: absolute;
  top: 32px;  /* Aligns with number height */
  right: -24px;  /* Half of gap */
  width: 24px;
  height: 1px;
  background-color: #525254;
}
```

**On mobile:** Remove connector lines. Stack vertically with a vertical line on the left instead:

```
│ 01
│ Discovery
│ We talk about...
│
│ 02
│ Design
│ I build a clear...
│
│ ...etc
```

---

### Vertical Timeline (Mobile <768px)

```css
.process-steps-mobile {
  position: relative;
  padding-left: 32px;
}

.process-steps-mobile::before {
  content: '';
  position: absolute;
  left: 8px;
  top: 0;
  bottom: 0;
  width: 1px;
  background-color: #525254;
}

.process-step-mobile {
  position: relative;
  margin-bottom: 40px;
}

.process-step-mobile::before {
  content: '';
  position: absolute;
  left: -28px;  /* Aligns with vertical line */
  top: 4px;
  width: 8px;
  height: 8px;
  background-color: #795238;
  border-radius: 50%;
}
```

---

## CONTENT (USE EXACTLY)

### Step 1
```
Number:      01
Title:       Discovery
Description: We talk about your business, your customers, and what the site needs to do. I ask questions. You tell me what success looks like.
```

### Step 2
```
Number:      02
Title:       Design
Description: I build a clear structure and visual direction — so you know exactly what you're getting before I write a line of code. No surprises.
```

### Step 3
```
Number:      03
Title:       Build
Description: Clean code, fast loading, tested on real devices. I build it right the first time — no shortcuts that break later.
```

### Step 4
```
Number:      04
Title:       Launch
Description: Your site goes live — and I stick around to make sure it works. Training, handover, and support so you're never left alone.
```

**Rules:**
- Tone is plain, direct, confident — matching "friendly & approachable"
- "We" in step 1 (collaborative), "I" in steps 2–4 (takes ownership)
- "No surprises" appears twice intentionally — it's a key anxiety reducer
- "Never left alone" — addresses the "disappearing freelancer" fear directly

---

## INTERACTION & MOTION

### Step Hover (desktop only)
```css
.process-step:hover .process-step-title {
  color: #F8F9FB;
  transition: color 200ms ease;
}

.process-step:hover .process-step-number {
  transform: scale(1.1);
  transition: transform 200ms ease;
}
```

**Rules:**
- Subtle only — title brightens, number scales slightly
- No background change, no card lift (steps aren't cards)

### Scroll Animation (optional, consistent with previous sections)
If IntersectionObserver is used:

```css
.process-step {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 500ms ease, transform 500ms ease;
}

.process-step.visible {
  opacity: 1;
  transform: translateY(0);
}

.process-step:nth-child(1) { transition-delay: 0ms; }
.process-step:nth-child(2) { transition-delay: 100ms; }
.process-step:nth-child(3) { transition-delay: 200ms; }
.process-step:nth-child(4) { transition-delay: 300ms; }
```

Respect `prefers-reduced-motion`.

---

## ACCESSIBILITY

- Semantic HTML:
  - `<section>` with `aria-label="How we work"`
  - Steps: `<ol>` with `<li>` — this is an ordered process, not a list
  - Numbers: part of the content, not decorative
- Color contrast:
  - Title `#AEA7A3` on `#2E2E2E` = 5.4:1 ✓
  - Description `#959595` on `#2E2E2E` = 4.7:1 ✓ (acceptable for secondary text)
- Connector lines: purely decorative, no screen reader announcement needed

---

## PERFORMANCE

- No images in this section
- No external libraries
- Reuse existing IntersectionObserver if present
- Target: No impact on Lighthouse Performance score

---

## INTEGRATION WITH EXISTING SECTIONS

DOM order:
```html
<body>
  <header class="hero">...</header>
  <section class="credibility-strip" aria-label="Why work with me">...</section>
  <section class="services-section" aria-label="Services and pricing">...</section>
  <section class="work-section" aria-label="Selected work">...</section>
  <section class="process-section" aria-label="How we work">
    ...
  </section>
</body>
```

Visual flow:
- Hero: `#242323`
- Credibility Strip: `#2E2E2E` (breath)
- Services: `#242323`
- Selected Work: `#242323`
- Process: `#2E2E2E` (breath — alternates with dark sections)

---

## NO-GO LIST (Do NOT implement)

- [ ] No icons for each step — numbers are cleaner and more timeless
- [ ] No circular step indicators with icons inside — overdesigned
- [ ] No "timeline" with dates or durations — keeps it simple
- [ ] No accordion or expandable steps — all content visible
- [ ] No background images or video
- [ ] No parallax effects
- [ ] No glossy effects, glassmorphism, or blur

---

## DELIVERABLE

An updated `index.html` containing:
1. All existing hero section code (unchanged)
2. All existing credibility strip code (unchanged)
3. All existing services preview code (unchanged)
4. All existing selected work code (unchanged)
5. The new Process section immediately after Selected Work
6. Embedded CSS for the new section
7. No console errors
8. No visual regressions to previous sections

---

## VERIFICATION CHECKLIST

- [ ] Section heading and subheading left-aligned, readable
- [ ] 4 steps visible in horizontal row on desktop (≥1024px)
- [ ] Steps connected by subtle horizontal lines
- [ ] Numbers are 01, 02, 03, 04 — warm brown color, bold
- [ ] Step titles in Syne, descriptions in DM Sans
- [ ] On tablet (768–1023px): 2×2 grid or horizontal with smaller gaps
- [ ] On mobile (<768px): vertical stack with left timeline line and dot markers
- [ ] Connector lines removed on mobile
- [ ] Content matches exactly: Discovery, Design, Build, Launch
- [ ] No icons, no circular badges, no expandable content
- [ ] Lighthouse Accessibility score ≥95
- [ ] No layout shift, overflow, or broken text wrapping at any breakpoint

---

*Prompt version 1.0 — Process section, 4-step workflow*
