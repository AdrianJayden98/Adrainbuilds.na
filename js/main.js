// Trigger loaded animations once the window has fully loaded all assets
window.addEventListener('load', function () {
  document.body.classList.add('loaded');
});

// Intersection Observer for scroll animations
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.2 });

  // Observe all the elements that need scroll animations
  document.querySelectorAll(
    '.credibility-item, ' +
    '.service-card, ' +
    '.work-card, ' +
    '.final-cta-heading, ' +
    '.final-cta-subheading, ' +
    '.final-cta-button, ' +
    '.final-cta-secondary, ' +
    '.footer-brand, ' +
    '.footer-nav, ' +
    '.footer-socials, ' +
    '.footer-copyright, ' +
    '.process-step, ' +
    '.retainer-heading, ' +
    '.retainer-body, ' +
    '.retainer-price, ' +
    '.retainer-features, ' +
    '.retainer-cta, ' +
    '.services-faq-heading, ' +
    '.faq-item, ' +
    '.case-study-client, ' +
    '.case-study-title, ' +
    '.case-study-meta, ' +
    '.case-study-comparison, ' +
    '.case-study-description, ' +
    '.case-study-live-link, ' +
    '.project-details-heading, ' +
    '.project-feature-card, ' +
    '.project-results-heading, ' +
    '.project-stat-number, ' +
    '.project-stat-label, ' +
    '.project-stats-row, ' +
    '.project-timeline, ' +
    '.future-work-heading, ' +
    '.future-work-body, ' +
    '.future-work-cta, ' +
    '.about-intro-container, ' +
    '.about-why-heading, ' +
    '.about-why-body, ' +
    '.about-approach-heading, ' +
    '.about-approach-subheading, ' +
    '.about-principle-card, ' +
    '.about-credentials-heading, ' +
    '.about-credential, ' +
    '.about-personal-heading, ' +
    '.about-personal-body, ' +
    '.contact-method-card, ' +
    '.contact-form-label, ' +
    '.contact-form, ' +
    '.contact-faq-heading'
  ).forEach(item => {
    observer.observe(item);
  });
}

// ========================================
// SLIDING PILL NAVIGATION & FAQ ACCORDION
// ========================================
document.addEventListener('DOMContentLoaded', function () {
  // --- FAQ Accordion ---
  const faqQuestions = document.querySelectorAll('.faq-question');
  faqQuestions.forEach(function (question) {
    question.addEventListener('click', function () {
      const faqItem = this.closest('.faq-item');
      const isOpen = faqItem.classList.contains('open');
      
      // Close all FAQ items
      document.querySelectorAll('.faq-item').forEach(function (item) {
        item.classList.remove('open');
      });
      
      // Open clicked item if it wasn't already open
      if (!isOpen) {
        faqItem.classList.add('open');
      }
    });
    
    // Keyboard accessibility (Enter and Space keys)
    question.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        this.click();
      }
    });
  });

  // --- Sliding Pill Nav ---
  const header = document.querySelector('.site-header');
  const pill = document.querySelector('.nav-pill');
  const indicator = document.querySelector('.nav-indicator');
  const links = document.querySelectorAll('.nav-link');
  const toggle = document.querySelector('.nav-toggle');
  const pillContainer = document.querySelector('.nav-pill-container');
  const overlay = document.querySelector('.nav-overlay');

  if (pill && indicator && links.length) {
    // Indicator Positioning
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

    // Hover Preview
    links.forEach(link => {
      link.addEventListener('mouseenter', () => {
        moveIndicatorTo(link);
      });
      link.addEventListener('mouseleave', () => {
        resetIndicatorToActive();
      });
    });

    // Mobile Menu Toggle
    if (toggle && pillContainer && overlay) {
      function openMenu() {
        toggle.setAttribute('aria-expanded', 'true');
        pillContainer.classList.add('is-open');
        overlay.classList.add('is-open');
        document.body.style.overflow = 'hidden';
      }

      function closeMenu() {
        toggle.setAttribute('aria-expanded', 'false');
        pillContainer.classList.remove('is-open');
        overlay.classList.remove('is-open');
        document.body.style.overflow = '';
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
  }

  // Scroll Behavior (Homepage only)
  const isHomepage = window.location.pathname === '/' || 
                     window.location.pathname === '/index.html' ||
                     window.location.pathname === '/home' ||
                     window.location.pathname.endsWith('index.html');

  if (isHomepage && header) {
    let lastScroll = 0;
    const scrollThreshold = 100;

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
