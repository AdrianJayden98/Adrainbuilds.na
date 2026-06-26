# AI Developer Prompt: Final CTA Section
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
**Current state:** Hero, Credibility Strip, Services Preview, Selected Work, Process, and About Snippet sections are complete and locked. This is the **seventh section** on the homepage — the last content section before the footer.

**Why this section exists:** By this point, the visitor has seen everything. This is the final nudge — the moment to convert a browser into a lead. The tone shifts slightly: more direct, more urgent, but still warm. Not "BUY NOW" — "Let's talk."

---

## TASK

Build a **Final CTA** section that closes the homepage with a clear, confident invitation to contact Adrian. This section should feel like the natural conclusion of the conversation that started in the hero.

---

## DESIGN SPECIFICATION

### Section Container

```css
.final-cta-section {
  background-color: #242323;  /* Same dark as hero — bookends the page */
  padding: 120px 20px;        /* Most generous padding on the page — this is the climax */
  width: 100%;
  text-align: center;           /* Centered — this is a moment, not a layout */
  position: relative;
  overflow: hidden;
}
```

**Rules:**
- No border-top or border-bottom
- Full-width background, content constrained to max-width 800px centered (narrower than other sections — focused)
- Text-align center — this is the only centered section on the page, making it feel special

---

### Background Accent (Optional, Subtle)

A very faint, large typographic element behind the text — similar to the services section's "SERVICES" headline, but even more subtle:

```css
.final-cta-bg-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-family: 'Syne', sans-serif;
  font-weight: 800;
  font-size: clamp(100px, 15vw, 200px);
  color: #2E2E2E;  /* Barely visible against #242323 */
  letter-spacing: -4px;
  white-space: nowrap;
  z-index: 0;
  pointer-events: none;
  user-select: none;
  opacity: 0.6;
}
```

Content: `LET'S TALK` or `READY?`

**Rules:**
- This is optional — if it feels cluttered, omit it
- NO blur, NO gloss, NO animation
- Must be genuinely subtle — if it's the first thing noticed, it's too loud

---

### Content Structure

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                    [faint "LET'S TALK" behind]              │
│                                                             │
│              Ready to get your business online?             │
│                                                             │
│              I take on 1–2 projects at a time,              │
│              so I can give yours real attention.              │
│              Let's talk about what you're building.           │
│                                                             │
│              [Get a Free Quote →]                           │
│                                                             │
│              Or reach me directly:                          │
│              hello@adrianm.dev                              │
│              +264 XX XXX XXXX                               │
│                                                             │
│              [Instagram icon]  [LinkedIn icon]              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

### Typography

**Heading:**
```css
font-family: 'Syne', sans-serif;
font-weight: 700;
font-size: clamp(32px, 5vw, 48px);
color: #AEA7A3;
line-height: 1.2;
margin-bottom: 20px;
position: relative;
z-index: 1;
```
Content: `Ready to get your business online?`

**Subheading (2–3 lines):**
```css
font-family: 'DM Sans', sans-serif;
font-weight: 400;
font-size: 18px;
color: #959595;
line-height: 1.6;
max-width: 500px;
margin: 0 auto 40px;
position: relative;
z-index: 1;
```
Content:
```
I take on 1–2 projects at a time,
so I can give yours real attention.
Let's talk about what you're building.
```

**Rules:**
- "1–2 projects at a time" — reinforces scarcity/exclusivity without being aggressive
- "Real attention" — warm, human, not corporate
- Line breaks after "time," and "attention." — creates rhythm

---

### Primary CTA Button

```css
.final-cta-button {
  display: inline-block;
  padding: 18px 40px;
  background-color: #795238;      /* Warm brown — same as hero CTA */
  color: #242323;                   /* Dark text for contrast */
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  font-size: 16px;
  text-align: center;
  border-radius: 8px;
  text-decoration: none;
  position: relative;
  z-index: 1;
  transition: background-color 300ms ease, 
              transform 300ms cubic-bezier(0.25, 0.1, 0.25, 1),
              box-shadow 300ms ease;
}

.final-cta-button:hover {
  background-color: #8B6348;
  transform: translateY(-3px);
  box-shadow: 0 12px 32px rgba(121, 82, 56, 0.35);
}

.final-cta-button:active {
  transform: translateY(0);
  box-shadow: 0 6px 16px rgba(121, 82, 56, 0.2);
}

.final-cta-button:focus-visible {
  outline: 2px solid #AEA7A3;
  outline-offset: 4px;
}
```

Content: `Get a Free Quote →`

**Link:** `mailto:hello@adrianm.dev?subject=Quote%20Request` (or anchor to contact form if one exists)

**Rules:**
- "Free" is important — removes friction
- "Quote" not "Consultation" — Namibian SMEs understand "quote"
- Arrow implies forward movement
- Slightly larger padding than hero CTA (18px 40px vs 16px 32px) — this is the final ask

---

### Secondary Contact Info

Below the primary CTA, a quieter block for direct contact:

```css
.final-cta-secondary {
  margin-top: 48px;
  position: relative;
  z-index: 1;
}

.final-cta-secondary-label {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 14px;
  color: #525254;
  margin-bottom: 12px;
}

.final-cta-contact {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 16px;
  color: #959595;
  line-height: 1.8;
}

.final-cta-contact a {
  color: #AEA7A3;
  text-decoration: none;
  border-bottom: 1px solid transparent;
  transition: border-color 200ms ease, color 200ms ease;
}

.final-cta-contact a:hover {
  color: #F8F9FB;
  border-bottom-color: #795238;
}
```

Content:
```
Or reach me directly:
hello@adrianm.dev
+264 XX XXX XXXX
```

**Rules:**
- Email is a `mailto:` link
- Phone is a `tel:` link
- "+264 XX XXX XXXX" — placeholder. Replace with actual number when known, or omit phone line entirely if not ready
- Color is muted — secondary to the primary CTA

---

### Social Icons (Below Contact)

```css
.final-cta-socials {
  margin-top: 24px;
  display: flex;
  justify-content: center;
  gap: 20px;
  position: relative;
  z-index: 1;
}

.final-cta-socials a {
  color: #525254;
  transition: color 200ms ease;
}

.final-cta-socials a:hover {
  color: #AEA7A3;
}
```

**Icons:** Inline SVGs, 20px, simple line style:
- Instagram → `https://instagram.com/adrianbuilds.na`
- LinkedIn → `https://linkedin.com/in/adrianm-dev`

**Rules:**
- Only Instagram and LinkedIn — matches hero/credibility strip
- No labels, just icons — visitors know these platforms
- `aria-label` on each link: "Follow Adrian on Instagram", "Connect with Adrian on LinkedIn"
- `target="_blank" rel="noopener noreferrer"`

---

## RESPONSIVE BREAKPOINTS

| Breakpoint | Adjustments |
|------------|-------------|
| ≥1024px | Full layout as specified, max-width 800px content |
| 768–1023px | Same, slightly reduced padding (100px 20px) |
| <768px | Padding 80px 20px, heading 28px, subheading 16px, CTA full-width (max 320px), social icons 18px |

---

## INTERACTION & MOTION

### Scroll Animation (optional, consistent)
If IntersectionObserver is used:

```css
.final-cta-heading,
.final-cta-subheading,
.final-cta-button,
.final-cta-secondary {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 600ms ease, transform 600ms ease;
}

.final-cta-heading.visible { transition-delay: 0ms; }
.final-cta-subheading.visible { transition-delay: 150ms; }
.final-cta-button.visible { transition-delay: 300ms; }
.final-cta-secondary.visible { transition-delay: 450ms; }
```

Respect `prefers-reduced-motion`.

---

## ACCESSIBILITY

- Semantic HTML:
  - `<section>` with `aria-label="Get in touch"`
  - Heading: `<h2>` (since this is a section heading, page structure should already have one `<h1>` in hero)
  - CTA: `<a>` with descriptive text
- Color contrast:
  - Heading `#AEA7A3` on `#242323` = 5.8:1 ✓
  - Subheading `#959595` on `#242323` = 5.1:1 ✓
  - CTA text `#242323` on `#795238` = 4.6:1 ✓ (large text/button)
- Focus states: CTA button gets visible outline
- Social icons: `aria-label` required since no text label

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
  <section class="process-section" aria-label="How we work">...</section>
  <section class="about-section" aria-label="About Adrian">...</section>
  <section class="final-cta-section" aria-label="Get in touch">
    ...
  </section>
  <!-- Footer follows -->
</body>
```

Visual flow:
- Hero: `#242323` (dark, opens the conversation)
- Credibility Strip: `#2E2E2E` (breath)
- Services: `#242323`
- Selected Work: `#242323`
- Process: `#2E2E2E` (breath)
- About: `#242323`
- Final CTA: `#242323` (dark, closes the conversation — bookends with hero)

---

## NO-GO LIST (Do NOT implement)

- [ ] No contact form in this section — this is a CTA section, not a form page
- [ ] No "Book a Call" calendar embed (Calendly, etc.) — Adrian uses email/WhatsApp
- [ ] No newsletter signup
- [ ] No "Download my portfolio PDF"
- [ ] No urgency tactics: countdown timers, "only 2 spots left", flashing elements
- [ ] No popups or modals
- [ ] No background images or video
- [ ] No parallax effects
- [ ] No glossy effects, glassmorphism, or blur

---

## DELIVERABLE

An updated `index.html` containing:
1. All existing sections (hero, credibility, services, work, process, about) — unchanged
2. The new Final CTA section immediately after About Snippet
3. Embedded CSS for the new section
4. No console errors
5. No visual regressions to previous sections

---

## VERIFICATION CHECKLIST

- [ ] Section is centered — heading, subheading, CTA, contact info all aligned center
- [ ] Heading "Ready to get your business online?" in Syne, prominent
- [ ] Subheading 2–3 lines, warm tone, mentions "1–2 projects at a time"
- [ ] Primary CTA "Get a Free Quote →" — warm brown fill, dark text, larger than hero CTA
- [ ] CTA hover: lift + warm shadow. Active: settles down. Focus: visible outline.
- [ ] Secondary contact: email (mailto link) and optional phone (tel link), muted color
- [ ] Social icons (Instagram, LinkedIn) below contact, 20px, hover brightens
- [ ] Background accent text (if included) is genuinely subtle — not distracting
- [ ] On mobile: CTA full-width, content still centered, readable
- [ ] No contact form, no calendar embed, no newsletter signup
- [ ] Lighthouse Accessibility score ≥95
- [ ] No layout shift, overflow, or broken text wrapping at any breakpoint

---

*Prompt version 1.0 — Final CTA, homepage closing section*
