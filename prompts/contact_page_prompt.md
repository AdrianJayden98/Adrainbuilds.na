# AI Developer Prompt: Contact Page
## For Cursor, GitHub Copilot, or similar AI coding agents

---

## ROLE DEFINITION

You are a **Frontend Developer & UI Engineer** specializing in:
- Semantic, accessible HTML
- Modern CSS (Flexbox, Grid, custom properties)
- Form design and validation UX
- Clean, conversion-focused UI components
- Performance-first development
- Responsive design with mobile-first approach

You write **production-ready code** — not prototypes. Every line must be intentional, commented where logic is non-obvious, and follow modern best practices.

---

## PROJECT CONTEXT

**Client:** Adrian M. — Freelance Web Developer based in Windhoek, Namibia.
**Positioning:** "Friendly & approachable local dev" serving Namibian SMEs.
**Brand:** Personal brand (not agency). Warm, grounded, cinematic.
**Tech stack:** Static HTML/CSS/JS. Multi-page static site (Option A).
**Current state:** Homepage (`index.html`) has been trimmed to 6 sections. Shared CSS lives in `css/styles.css`. Shared JS lives in `js/main.js`. This is the first new page being built.

**Why this page exists:** The homepage's Final CTA drives visitors here. This is where browsers become leads. The goal is to make contacting Adrian as frictionless as possible — especially for Namibian SMEs who prefer WhatsApp and email over forms.

---

## TASK

Build a **Contact page** (`contact.html`) that gives visitors multiple ways to reach Adrian, with a clear preference hierarchy:
1. **WhatsApp Business** (primary — Namibian market preference)
2. **Email** (secondary — formal inquiries)
3. **Contact Form** (tertiary — for those who prefer typing)

The page should feel warm, responsive, and trustworthy. No dead ends.

---

## FILE STRUCTURE

```
/
├── index.html
├── contact.html          (this file)
├── services.html         (future)
├── work.html             (future)
├── about.html            (future)
├── css/
│   └── styles.css        (shared — link this)
├── js/
│   └── main.js           (shared — link this)
└── images/
    └── desert-namibia.jpeg   (optional reuse for page bg accent)
```

---

## PAGE STRUCTURE

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact — Adrian M. | Freelance Web Developer | Windhoek, Namibia</title>
  <meta name="description" content="Get in touch with Adrian M., freelance web developer in Windhoek. WhatsApp, email, or send a message.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>

  <!-- NAVIGATION -->
  <nav class="site-nav">...</nav>

  <!-- HERO / PAGE HEADER -->
  <header class="page-header">...</header>

  <!-- CONTACT METHODS -->
  <section class="contact-methods" aria-label="Contact options">...</section>

  <!-- CONTACT FORM -->
  <section class="contact-form-section" aria-label="Send a message">...</section>

  <!-- FAQ MINI -->
  <section class="contact-faq" aria-label="Common questions">...</section>

  <!-- FOOTER -->
  <footer class="footer-section">...</footer>

  <script src="js/main.js"></script>
</body>
</html>
```

---

## 1. NAVIGATION

Reuse the same nav component as the homepage. If it doesn't exist as a shared include, copy it from `index.html`.

```css
.site-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  padding: 20px 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: rgba(36, 35, 35, 0.95);  /* Solid on contact page — no hero image behind */
  backdrop-filter: none;  /* No blur — matte brand */
}
```

**Links:**
- Adrian M. (logo) → `/`
- Home → `/`
- Services → `/services`
- Work → `/work`
- About → `/about`
- Contact → `/contact` (active state: color `#795238`)
- [Get a Quote] → `/contact` (same page — can hide or change to "Get Started")

**Rules:**
- On contact page, "Get a Quote" button can be hidden or changed to "Scroll to Form" since we're already on the contact page
- Active page: Contact link highlighted in `#795238`

---

## 2. PAGE HEADER

```css
.page-header {
  background-color: #242323;
  padding: 140px 20px 60px;  /* Extra top padding for fixed nav */
  text-align: center;
}
```

**Content:**
```
Heading:    Let's Talk
Subheading: Have a project in mind? Send me a message and I'll get back to you within 24 hours.
```

| Element | Font | Weight | Size | Color |
|---------|------|--------|------|-------|
| Heading | Syne | 700 | 48px | `#AEA7A3` |
| Subheading | DM Sans | 400 | 18px | `#959595` |

**On mobile:** heading 36px, subheading 16px, padding-top 120px.

---

## 3. CONTACT METHODS (3 Cards)

```css
.contact-methods {
  background-color: #2E2E2E;  /* Lighter breath section */
  padding: 64px 20px;
}

.contact-methods-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  max-width: 1000px;
  margin: 0 auto;
}

.contact-method-card {
  background-color: #363636;
  border: 1px solid #4A4A4A;
  border-radius: 16px;
  padding: 40px 32px;
  text-align: center;
  transition: border-color 300ms ease, transform 300ms ease;
}

.contact-method-card:hover {
  border-color: #5A5A5A;
  transform: translateY(-4px);
}

.contact-method-card--primary {
  border: 2px solid #795238;  /* WhatsApp card highlighted */
  background-color: #2E2E2E;
}
```

**Card 1: WhatsApp (Primary)**
```
Icon:       WhatsApp icon (inline SVG, 32px, #25D366 green or #795238 warm brown)
Label:      WhatsApp
Detail:     Fastest response. Chat directly.
CTA:        [Chat on WhatsApp]
Link:       https://wa.me/264XXXXXXXXX (replace with actual number)
```

**Card 2: Email**
```
Icon:       Email icon (inline SVG, 32px, #AEA7A3)
Label:      Email
Detail:     For detailed project briefs.
CTA:        [hello@adrianm.dev]
Link:       mailto:hello@adrianm.dev
```

**Card 3: Form**
```
Icon:       Message/edit icon (inline SVG, 32px, #AEA7A3)
Label:      Send a Message
Detail:     Fill out the form below.
CTA:        [Jump to Form ↓]
Link:       #contact-form (anchor to form section)
```

**Card content styling:**
```css
.contact-method-icon {
  margin-bottom: 20px;
}

.contact-method-label {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 20px;
  color: #AEA7A3;
  margin-bottom: 8px;
}

.contact-method-detail {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 14px;
  color: #959595;
  margin-bottom: 24px;
  line-height: 1.5;
}

.contact-method-cta {
  display: inline-block;
  padding: 12px 24px;
  background-color: transparent;
  color: #AEA7A3;
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  font-size: 14px;
  border: 1px solid #4A4A4A;
  border-radius: 8px;
  text-decoration: none;
  transition: background-color 300ms ease, color 300ms ease, border-color 300ms ease;
}

.contact-method-cta:hover {
  background-color: #795238;
  color: #242323;
  border-color: #795238;
}

/* Primary card CTA — filled by default */
.contact-method-card--primary .contact-method-cta {
  background-color: #795238;
  color: #242323;
  border-color: #795238;
}

.contact-method-card--primary .contact-method-cta:hover {
  background-color: #8B6348;
  border-color: #8B6348;
}
```

**Responsive:**
- Desktop: 3 columns
- Tablet: 3 columns (smaller padding)
- Mobile: stack vertically, WhatsApp card first

---

## 4. CONTACT FORM SECTION

```css
.contact-form-section {
  background-color: #242323;
  padding: 80px 20px;
}

.contact-form-container {
  max-width: 600px;
  margin: 0 auto;
}
```

**Section label:**
```
Prefer to write it out? Send me a message and I'll reply within 24 hours.
```

```css
font-family: 'DM Sans', sans-serif;
font-weight: 400;
font-size: 16px;
color: #959595;
text-align: center;
margin-bottom: 48px;
```

**Form fields:**

| Field | Type | Required | Placeholder |
|-------|------|----------|-------------|
| Name | text | Yes | Your name |
| Business Name | text | No | Your business name (optional) |
| Email | email | Yes | your@email.com |
| Phone | tel | No | +264 XX XXX XXXX |
| Project Type | select | Yes | — |
| Budget Range | select | No | — |
| Message | textarea | Yes | Tell me about your project... |

**Project Type options:**
```html
<option value="" disabled selected>Select a project type</option>
<option value="new-website">New Website</option>
<option value="redesign">Website Redesign</option>
<option value="ecommerce">E-commerce</option>
<option value="landing-page">Landing Page</option>
<option value="other">Something Else</option>
```

**Budget Range options:**
```html
<option value="" disabled selected>Budget range (optional)</option>
<option value="8-15k">N$8,000 – N$15,000</option>
<option value="18-30k">N$18,000 – N$30,000</option>
<option value="35-65k">N$35,000 – N$65,000</option>
<option value="65k+">N$65,000+</option>
<option value="not-sure">Not sure yet</option>
```

**Form styling:**
```css
.contact-form {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-label {
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  font-size: 14px;
  color: #AEA7A3;
}

.form-input,
.form-select,
.form-textarea {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 15px;
  color: #F8F9FB;
  background-color: #363636;
  border: 1px solid #4A4A4A;
  border-radius: 8px;
  padding: 14px 16px;
  transition: border-color 300ms ease, box-shadow 300ms ease;
}

.form-input::placeholder,
.form-textarea::placeholder {
  color: #525254;
}

.form-input:focus,
.form-select:focus,
.form-textarea:focus {
  outline: none;
  border-color: #795238;
  box-shadow: 0 0 0 3px rgba(121, 82, 56, 0.2);
}

.form-textarea {
  min-height: 140px;
  resize: vertical;
}

/* Two-column layout for Name + Business, Email + Phone on desktop */
.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}

@media (max-width: 768px) {
  .form-row {
    grid-template-columns: 1fr;
  }
}
```

**Submit button:**
```css
.form-submit {
  display: inline-block;
  width: 100%;
  padding: 16px 32px;
  background-color: #795238;
  color: #242323;
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  font-size: 16px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 300ms ease, transform 300ms ease, box-shadow 300ms ease;
}

.form-submit:hover {
  background-color: #8B6348;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(121, 82, 56, 0.3);
}

.form-submit:active {
  transform: translateY(0);
}

.form-submit:focus-visible {
  outline: 2px solid #AEA7A3;
  outline-offset: 4px;
}
```

Content: `Send Message →`

**Form submission:**
- Since this is a static site, the form needs a form backend service:
  - **Recommended:** Formspree (`https://formspree.io/f/YOUR_FORM_ID`) — free tier, easy setup
  - Alternative: Netlify Forms (if hosting on Netlify)
  - Alternative: Getform, Basin
- Form `action` attribute points to the form backend URL
- Method: `POST`
- Add `name` attributes to all fields for the backend to capture

**Example:**
```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST" class="contact-form">
  ...
</form>
```

**Success state:** After submission, the form backend redirects to a thank-you page or shows a message. For now, use the form backend's default thank-you page. Later, a custom `/thank-you` page can be built.

---

## 5. FAQ MINI (Below Form)

```css
.contact-faq {
  background-color: #2E2E2E;
  padding: 64px 20px;
}

.contact-faq-container {
  max-width: 700px;
  margin: 0 auto;
}
```

**Heading:**
```
Quick Answers
```
```css
font-family: 'Syne', sans-serif;
font-weight: 700;
font-size: 28px;
color: #AEA7A3;
text-align: center;
margin-bottom: 40px;
```

**3 accordion items:**

| Question | Answer |
|----------|--------|
| How long does a typical project take? | Most projects take 1–4 weeks depending on complexity. A simple brochure site can be ready in a week. Larger projects with custom features need more time. I'll give you a clear timeline before we start. |
| What do you need from me to get started? | Just your business details, any content you have (text, images, logo), and a clear idea of what you want the site to do. Don't worry if you don't have everything — I can guide you through it. |
| Can I update the website myself after launch? | Yes. I build sites with user-friendly content management, so you can update text and images without touching code. I also include a handover session to show you how. |

**Accordion styling:**
```css
.faq-item {
  border-bottom: 1px solid #363636;
  padding: 20px 0;
}

.faq-question {
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  font-size: 16px;
  color: #AEA7A3;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: none;
  border: none;
  width: 100%;
  text-align: left;
  padding: 0;
}

.faq-question::after {
  content: '+';
  font-size: 20px;
  color: #795238;
  transition: transform 300ms ease;
}

.faq-item.open .faq-question::after {
  content: '−';
}

.faq-answer {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 15px;
  color: #959595;
  line-height: 1.7;
  max-height: 0;
  overflow: hidden;
  transition: max-height 400ms ease, padding 400ms ease;
  padding-top: 0;
}

.faq-item.open .faq-answer {
  max-height: 300px;  /* Approximate max height */
  padding-top: 16px;
}
```

**JavaScript for accordion:**
```javascript
document.querySelectorAll('.faq-question').forEach(button => {
  button.addEventListener('click', () => {
    const item = button.parentElement;
    const isOpen = item.classList.contains('open');

    // Close all
    document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));

    // Open clicked if it was closed
    if (!isOpen) {
      item.classList.add('open');
    }
  });
});
```

**Rules:**
- Only one item open at a time
- Smooth height transition
- Keyboard accessible: Enter/Space toggles
- Respect `prefers-reduced-motion`: if enabled, no transition

---

## 6. FOOTER

Reuse the exact same footer from `index.html`. Copy it over.

**Ensure footer nav links:**
- Home → `/`
- Services → `/services`
- Work → `/work`
- About → `/about`

---

## SHARED CSS UPDATES

Add these new rules to `css/styles.css` (the shared stylesheet):

```css
/* ========================================
   CONTACT PAGE STYLES
   ======================================== */

/* Page header */
.page-header {
  background-color: #242323;
  padding: 140px 20px 60px;
  text-align: center;
}

.page-header h1 {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: clamp(36px, 5vw, 48px);
  color: #AEA7A3;
  line-height: 1.2;
  margin-bottom: 16px;
}

.page-header p {
  font-family: 'DM Sans', sans-serif;
  font-weight: 400;
  font-size: 18px;
  color: #959595;
  max-width: 500px;
  margin: 0 auto;
}

/* Contact methods */
.contact-methods { ... }
.contact-methods-grid { ... }
.contact-method-card { ... }
/* ... etc ... */

/* Contact form */
.contact-form-section { ... }
.contact-form-container { ... }
.form-group { ... }
.form-label { ... }
.form-input { ... }
/* ... etc ... */

/* FAQ */
.contact-faq { ... }
.faq-item { ... }
.faq-question { ... }
.faq-answer { ... }
```

**Rules:**
- Keep all existing homepage styles intact
- Add contact page styles at the bottom of the file, clearly commented
- No conflicts with existing class names

---

## SHARED JS UPDATES

Add the FAQ accordion JS to `js/main.js`:

```javascript
// ========================================
// FAQ ACCORDION
// ========================================

document.addEventListener('DOMContentLoaded', () => {
  const faqButtons = document.querySelectorAll('.faq-question');

  faqButtons.forEach(button => {
    button.addEventListener('click', () => {
      const item = button.closest('.faq-item');
      const isOpen = item.classList.contains('open');

      // Close all
      document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));

      // Toggle current
      if (!isOpen) {
        item.classList.add('open');
      }
    });

    // Keyboard accessibility
    button.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        button.click();
      }
    });
  });
});
```

**Rules:**
- Wrap in `DOMContentLoaded`
- Check if elements exist before attaching listeners (page-agnostic)
- No errors if `.faq-question` doesn't exist (homepage doesn't have it)

---

## RESPONSIVE BREAKPOINTS

| Breakpoint | Adjustments |
|------------|-------------|
| ≥1024px | Full layout: 3 contact cards, 2-column form rows, FAQ centered |
| 768–1023px | 3 contact cards (smaller), 2-column form rows, FAQ full width |
| <768px | Contact cards stack (WhatsApp first), form single column, FAQ full width |

---

## ACCESSIBILITY

- Semantic HTML:
  - `<main>` wrapping primary content
  - `<nav>` for navigation
  - `<section>` with `aria-label` for each content block
  - Form: `<form>` with proper `label` associations (`for` attribute matching `id`)
- Form accessibility:
  - All inputs have associated labels
  - Required fields marked with `aria-required="true"` and visual indicator (optional)
  - Error messages: `aria-describedby` linking to error text
  - Submit button: clear text, not just icon
- Color contrast:
  - Form text `#F8F9FB` on `#363636` = 10.5:1 ✓
  - Labels `#AEA7A3` on `#242323` = 5.8:1 ✓
  - Placeholder `#525254` on `#363636` = 3.2:1 (placeholder contrast is relaxed, but ensure label is clear)
- Focus states:
  - All interactive elements have visible focus indicators
  - Form inputs: `box-shadow: 0 0 0 3px rgba(121, 82, 56, 0.2)` on focus

---

## PERFORMANCE

- No images in contact methods or form (icons are SVG)
- Desert image optional for footer only (already loaded on homepage, cached)
- Form backend (Formspree) loads asynchronously — no blocking
- Target: Lighthouse Performance ≥90

---

## NO-GO LIST

- [ ] No Google Maps embed — heavy, slow, not needed for a local freelancer
- [ ] No physical address display — Adrian works from home/coffee spots, not a studio
- [ ] No "Business Hours" section — freelancers don't have fixed hours
- [ ] No social media feed embeds
- [ ] No chat widget — WhatsApp card replaces this
- [ ] No CAPTCHA on form — Formspree handles spam filtering
- [ ] No glossy effects, glassmorphism, or blur

---

## DELIVERABLE

1. New `contact.html` file with complete page structure
2. Updated `css/styles.css` with contact page styles added
3. Updated `js/main.js` with FAQ accordion functionality
4. Nav links pointing to correct pages
5. Footer copied from homepage with correct links
6. Form configured with Formspree (or placeholder URL with TODO comment)
7. WhatsApp link with placeholder number (TODO comment to replace)
8. No console errors
9. Responsive at all breakpoints

---

## VERIFICATION CHECKLIST

- [ ] Page title: "Contact — Adrian M. | Freelance Web Developer | Windhoek, Namibia"
- [ ] Meta description present
- [ ] Nav fixed at top, solid background, Contact link highlighted
- [ ] Page header: "Let's Talk" + subheading, centered
- [ ] 3 contact method cards: WhatsApp (highlighted), Email, Form
- [ ] WhatsApp card has green icon or warm brown icon, "Chat on WhatsApp" CTA
- [ ] Email card has mail icon, `mailto:` link
- [ ] Form card has anchor link to form section
- [ ] Contact form: 7 fields (Name, Business, Email, Phone, Project Type, Budget, Message)
- [ ] Form has 2-column layout for Name/Business and Email/Phone on desktop
- [ ] Form inputs have focus states with warm brown border + glow
- [ ] Submit button: "Send Message →", warm brown, hover lift
- [ ] Form action points to Formspree (or placeholder with TODO)
- [ ] FAQ accordion: 3 items, smooth expand/collapse, one open at a time
- [ ] FAQ keyboard accessible (Enter/Space to toggle)
- [ ] Footer copied from homepage, nav links correct
- [ ] All links functional (even if pages don't exist yet)
- [ ] Responsive: cards stack on mobile, form single column
- [ ] Lighthouse Accessibility ≥95, Performance ≥90

---

*Prompt version 1.0 — Contact page for multi-page site*
