import os
import re

html_files = ['index.html', 'services.html', 'work.html', 'about.html', 'contact.html']

for f in html_files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Add footer-fade-top
        if '<div class="footer-fade-top" aria-hidden="true"></div>' not in content:
            content = content.replace('<footer class="footer-section">', 
                                      '<footer class="footer-section">\n    <div class="footer-fade-top" aria-hidden="true"></div>')
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)

css_file = 'css/styles.css'
with open(css_file, 'r', encoding='utf-8') as file:
    css_content = file.read()

classes_to_clear = [
    '.credibility-strip',
    '.services-section',
    '.work-section',
    '.final-cta-section',
    '.services-pricing',
    '.process-section',
    '.retainer-section',
    '.services-faq',
    '.case-study-featured',
    '.project-details',
    '.project-results',
    '.future-work',
    '.about-intro',
    '.about-why',
    '.about-approach',
    '.about-credentials',
    '.about-personal',
    '.contact-methods',
    '.contact-form-section',
    '.contact-faq',
    '.footer-section'
]

def remove_properties(css, cls_name):
    # Match the block for the class
    pattern = r'(' + re.escape(cls_name) + r'\s*(?:,\s*[^{]+)?\{)([^}]+)(\})'
    
    def replacer(match):
        prefix = match.group(1)
        body = match.group(2)
        suffix = match.group(3)
        # Remove background-color
        body = re.sub(r'\s*background-color:\s*(#[a-fA-F0-9]+|transparent|rgba?[^;]+);', '', body)
        # Remove border-top, border-bottom
        body = re.sub(r'\s*border-(top|bottom):[^;]+;', '', body)
        return prefix + body + suffix

    for _ in range(3):
        css = re.sub(pattern, replacer, css)
    return css

for cls in classes_to_clear:
    css_content = remove_properties(css_content, cls)

new_css = """
/* ========================================
   SECTION BACKGROUNDS & FADE TRANSITIONS
   ========================================
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

@media (max-width: 768px) {
  /* Reduce gradient zone on mobile */
  .credibility-strip,
  .process-section,
  .services-faq,
  .project-details,
  .future-work,
  .about-why,
  .about-credentials,
  .contact-methods,
  .contact-faq {
    background: linear-gradient(to bottom, #242323 0%, #242323 5%, #2E2E2E 15%, #2E2E2E 100%);
    padding-top: 80px;
  }
  
  .services-section,
  .retainer-section,
  .project-results,
  .about-approach,
  .about-personal,
  .contact-form-section {
    background: linear-gradient(to bottom, #2E2E2E 0%, #2E2E2E 5%, #242323 15%, #242323 100%);
    padding-top: 80px;
  }
}
"""

if "SECTION BACKGROUNDS & FADE TRANSITIONS" not in css_content:
    css_content += "\n" + new_css

with open(css_file, 'w', encoding='utf-8') as file:
    file.write(css_content)

print("Updates applied successfully.")
