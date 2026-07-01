import os

css_file = 'css/styles.css'
with open(css_file, 'r', encoding='utf-8') as file:
    css_content = file.read()

# Find the block we added in the previous task and remove it
marker = "/* ========================================\n   SECTION FADE TRANSITIONS (DISSOLVE)"
if marker in css_content:
    css_content = css_content[:css_content.find(marker)].rstrip()

new_css = """
/* ========================================
   SECTION FADE TRANSITIONS (DISSOLVE)
   ========================================

   Principle: Upper section fades OUT to next section's color.
   Lower section is SOLID — no gradient.
*/

/* Base styles for all sections to ensure relative positioning and solid backgrounds */
.hero { position: relative; background-color: #242323; padding-bottom: 0 !important; }
.credibility-strip { position: relative; background-color: #2E2E2E; }
.services-section { position: relative; background-color: #242323; }
.work-section { position: relative; background-color: #242323; }
.final-cta-section { position: relative; background-color: #242323; }

.services-pricing { position: relative; background-color: #242323; }
.process-section { position: relative; background-color: #2E2E2E; }
.retainer-section { position: relative; background-color: #242323; }
.services-faq { position: relative; background-color: #2E2E2E; }

.case-study-featured { position: relative; background-color: #242323; }
.project-details { position: relative; background-color: #2E2E2E; }
.project-results { position: relative; background-color: #242323; }
.future-work { position: relative; background-color: #2E2E2E; }

.about-intro { position: relative; background-color: #242323; }
.about-why { position: relative; background-color: #2E2E2E; }
.about-approach { position: relative; background-color: #242323; }
.about-credentials { position: relative; background-color: #2E2E2E; }
.about-personal { position: relative; background-color: #242323; }

.page-header { position: relative; background-color: #242323; }
.contact-methods { position: relative; background-color: #2E2E2E; }
.contact-form-section { position: relative; background-color: #242323; }
.contact-faq { position: relative; background-color: #2E2E2E; }

/* Base styles for all ::after fades */
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

/* --- HOMEPAGE --- */
/* Fading to #2E2E2E uses rgba(46,46,46,0) instead of transparent to prevent dark bands */
.hero::after { background: linear-gradient(to bottom, rgba(46,46,46,0) 0%, #2E2E2E 100%); }
/* Fading to #242323 uses rgba(36,35,35,0) */
.credibility-strip::after { background: linear-gradient(to bottom, rgba(36,35,35,0) 0%, #242323 100%); }
.final-cta-section::after { 
  background: linear-gradient(to bottom, rgba(36,35,35,0) 0%, rgba(36, 35, 35, 0.7) 70%, #242323 100%); 
}

/* --- SERVICES PAGE --- */
.services-pricing::after { background: linear-gradient(to bottom, rgba(46,46,46,0) 0%, #2E2E2E 100%); }
.process-section::after { background: linear-gradient(to bottom, rgba(36,35,35,0) 0%, #242323 100%); }
.retainer-section::after { background: linear-gradient(to bottom, rgba(46,46,46,0) 0%, #2E2E2E 100%); }
.services-faq::after { background: linear-gradient(to bottom, rgba(36,35,35,0) 0%, #242323 100%); }

/* --- WORK PAGE --- */
.case-study-featured::after { background: linear-gradient(to bottom, rgba(46,46,46,0) 0%, #2E2E2E 100%); }
.project-details::after { background: linear-gradient(to bottom, rgba(36,35,35,0) 0%, #242323 100%); }
.project-results::after { background: linear-gradient(to bottom, rgba(46,46,46,0) 0%, #2E2E2E 100%); }
.future-work::after { background: linear-gradient(to bottom, rgba(36,35,35,0) 0%, #242323 100%); }

/* --- ABOUT PAGE --- */
.about-intro::after { background: linear-gradient(to bottom, rgba(46,46,46,0) 0%, #2E2E2E 100%); }
.about-why::after { background: linear-gradient(to bottom, rgba(36,35,35,0) 0%, #242323 100%); }
.about-approach::after { background: linear-gradient(to bottom, rgba(46,46,46,0) 0%, #2E2E2E 100%); }
.about-credentials::after { background: linear-gradient(to bottom, rgba(36,35,35,0) 0%, #242323 100%); }

/* --- CONTACT PAGE --- */
.page-header::after { background: linear-gradient(to bottom, rgba(46,46,46,0) 0%, #2E2E2E 100%); }
.contact-methods::after { background: linear-gradient(to bottom, rgba(36,35,35,0) 0%, #242323 100%); }
.contact-form-section::after { background: linear-gradient(to bottom, rgba(46,46,46,0) 0%, #2E2E2E 100%); }
.contact-faq::after { background: linear-gradient(to bottom, rgba(36,35,35,0) 0%, #242323 100%); }

/* --- FOOTER (ALL PAGES) --- */
.footer-section { position: relative; }
.footer-fade-top {
  position: absolute;
  top: 0;  /* Placed at top of footer to overlap the image */
  left: 0;
  right: 0;
  height: 150px;
  /* Fade from solid dark to transparent */
  background: linear-gradient(to bottom, #242323 0%, rgba(36, 35, 35, 0.8) 30%, rgba(36, 35, 35, 0) 100%);
  z-index: 3;
  pointer-events: none;
}

/* RESPONSIVE */
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
    height: 80px;
  }

  .final-cta-section::after {
    height: 100px;
  }

  .footer-fade-top {
    height: 100px;
  }
}
"""

css_content += "\n\n" + new_css.strip() + "\n"

with open(css_file, 'w', encoding='utf-8') as file:
    file.write(css_content)

print("Fix applied successfully.")
