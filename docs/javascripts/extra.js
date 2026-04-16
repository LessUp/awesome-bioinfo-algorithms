/* ===================================================================
   AWESOME BIOINFORMATICS ALGORITHMS - EXTRA JAVASCRIPT
   ===================================================================
   Adds advanced interactivity and features to the documentation.
   =================================================================== */

(function() {
  'use strict';

  // =================== UTILITY FUNCTIONS ===================
  const utils = {
    // Debounce function
    debounce: (func, wait) => {
      let timeout;
      return function executedFunction(...args) {
        const later = () => {
          clearTimeout(timeout);
          func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
      };
    },

    // Throttle function
    throttle: (func, limit) => {
      let inThrottle;
      return function(...args) {
        if (!inThrottle) {
          func.apply(this, args);
          inThrottle = true;
          setTimeout(() => inThrottle = false, limit);
        }
      };
    },

    // Check if element is in viewport
    isInViewport: (element) => {
      const rect = element.getBoundingClientRect();
      return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
      );
    },

    // Smooth scroll to element
    scrollToElement: (element, offset = 0) => {
      const elementPosition = element.getBoundingClientRect().top + window.pageYOffset;
      window.scrollTo({
        top: elementPosition - offset,
        behavior: 'smooth'
      });
    },

    // Copy to clipboard
    copyToClipboard: async (text) => {
      try {
        await navigator.clipboard.writeText(text);
        return true;
      } catch (err) {
        console.error('Failed to copy:', err);
        return false;
      }
    }
  };

  // =================== LOADING ANIMATION ===================
  const LoadingAnimation = {
    init() {
      const loader = document.getElementById('page-loading');
      if (!loader) return;

      window.addEventListener('load', () => {
        setTimeout(() => {
          loader.classList.add('hidden');
          setTimeout(() => {
            loader.style.display = 'none';
          }, 300);
        }, 500);
      });
    }
  };

  // =================== SCROLL ANIMATIONS ===================
  const ScrollAnimations = {
    init() {
      const revealElements = document.querySelectorAll('.reveal');
      
      if (revealElements.length === 0) return;

      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('active');
            observer.unobserve(entry.target);
          }
        });
      }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
      });

      revealElements.forEach(el => observer.observe(el));
    }
  };

  // =================== MOUSE GLOW EFFECT ===================
  const MouseGlowEffect = {
    init() {
      const glowElements = document.querySelectorAll('.mouse-glow');
      
      glowElements.forEach(element => {
        element.addEventListener('mousemove', (e) => {
          const rect = element.getBoundingClientRect();
          const x = e.clientX - rect.left;
          const y = e.clientY - rect.top;
          
          element.style.setProperty('--mouse-x', `${x}px`);
          element.style.setProperty('--mouse-y', `${y}px`);
        });
      });
    }
  };

  // =================== CODE BLOCK ENHANCEMENTS ===================
  const CodeBlockEnhancements = {
    init() {
      const codeBlocks = document.querySelectorAll('.md-typeset pre');
      
      codeBlocks.forEach(pre => {
        // Add macOS-style window controls
        const controls = document.createElement('div');
        controls.className = 'code-controls';
        controls.innerHTML = `
          <span class="code-control close"></span>
          <span class="code-control minimize"></span>
          <span class="code-control maximize"></span>
        `;
        pre.style.position = 'relative';
        
        // Add filename if data-attribute exists
        const code = pre.querySelector('code');
        if (code && code.dataset.lang) {
          const filename = document.createElement('div');
          filename.className = 'code-filename';
          filename.textContent = code.dataset.lang;
          pre.appendChild(filename);
        }
      });
    }
  };

  // =================== TABLE OF CONTICS HIGHLIGHTING ===================
  const TOCHighlight = {
    init() {
      const headings = document.querySelectorAll('.md-typeset h2, .md-typeset h3, .md-typeset h4');
      const tocLinks = document.querySelectorAll('.md-nav--secondary .md-nav__link');
      
      if (headings.length === 0 || tocLinks.length === 0) return;

      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const id = entry.target.id;
            tocLinks.forEach(link => {
              link.classList.remove('md-nav__link--active');
              if (link.getAttribute('href') === `#${id}`) {
                link.classList.add('md-nav__link--active');
              }
            });
          }
        });
      }, {
        rootMargin: '-20% 0px -80% 0px',
        threshold: 0
      });

      headings.forEach(heading => observer.observe(heading));
    }
  };

  // =================== SEARCH ENHANCEMENTS ===================
  const SearchEnhancements = {
    init() {
      const searchForm = document.querySelector('.md-search__form');
      const searchInput = document.querySelector('.md-search__input');
      
      if (!searchForm || !searchInput) return;

      // Add search shortcuts
      document.addEventListener('keydown', (e) => {
        // Cmd/Ctrl + K to focus search
        if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
          e.preventDefault();
          searchInput.focus();
          searchInput.select();
        }
        
        // Escape to close search
        if (e.key === 'Escape' && document.activeElement === searchInput) {
          searchInput.blur();
        }
      });

      // Add keyboard shortcut hint
      const shortcutHint = document.createElement('span');
      shortcutHint.className = 'search-shortcut';
      shortcutHint.innerHTML = navigator.platform.includes('Mac') ? '⌘K' : 'Ctrl+K';
      searchForm.appendChild(shortcutHint);
    }
  };

  // =================== PROGRESS INDICATOR ===================
  const ReadingProgress = {
    init() {
      const progressBar = document.createElement('div');
      progressBar.className = 'reading-progress';
      document.body.appendChild(progressBar);

      const updateProgress = utils.throttle(() => {
        const scrollTop = window.pageYOffset;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const progress = (scrollTop / docHeight) * 100;
        progressBar.style.width = `${progress}%`;
      }, 50);

      window.addEventListener('scroll', updateProgress);
    }
  };

  // =================== IMAGE ZOOM ===================
  const ImageZoom = {
    init() {
      const images = document.querySelectorAll('.md-typeset img');
      
      images.forEach(img => {
        img.style.cursor = 'zoom-in';
        
        img.addEventListener('click', () => {
          const overlay = document.createElement('div');
          overlay.className = 'image-zoom-overlay';
          overlay.innerHTML = `<img src="${img.src}" alt="${img.alt}">`;
          
          overlay.addEventListener('click', () => {
            overlay.remove();
            document.body.style.overflow = '';
          });
          
          document.body.appendChild(overlay);
          document.body.style.overflow = 'hidden';
          
          // Animate in
          requestAnimationFrame(() => {
            overlay.classList.add('active');
          });
        });
      });
    }
  };

  // =================== SMOOTH SCROLL FOR ANCHOR LINKS ===================
  const SmoothScroll = {
    init() {
      document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
          const targetId = anchor.getAttribute('href');
          if (targetId === '#') return;
          
          const targetElement = document.querySelector(targetId);
          if (targetElement) {
            e.preventDefault();
            utils.scrollToElement(targetElement, 80);
          }
        });
      });
    }
  };

  // =================== DARK MODE PERSISTENCE ===================
  const DarkModePersistence = {
    init() {
      const toggle = document.querySelector('[data-md-color-scheme]');
      if (!toggle) return;

      // Listen for color scheme changes
      const observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
          if (mutation.type === 'attributes' && mutation.attributeName === 'data-md-color-scheme') {
            const scheme = document.body.getAttribute('data-md-color-scheme');
            localStorage.setItem('theme', scheme);
          }
        });
      });

      observer.observe(document.body, { attributes: true });

      // Restore theme preference
      const savedTheme = localStorage.getItem('theme');
      if (savedTheme) {
        document.body.setAttribute('data-md-color-scheme', savedTheme);
      }
    }
  };

  // =================== PERFORMANCE MONITORING ===================
  const PerformanceMonitor = {
    init() {
      // Performance monitoring disabled in production
      // Enable via debug mode if needed
    }
  };

  // =================== EXTERNAL LINK HANDLING ===================
  const ExternalLinks = {
    init() {
      document.querySelectorAll('a[href^="http"]').forEach(link => {
        if (link.hostname !== window.location.hostname) {
          link.setAttribute('target', '_blank');
          link.setAttribute('rel', 'noopener noreferrer');
          
          // Add external link icon
          if (!link.querySelector('.external-icon')) {
            const icon = document.createElement('span');
            icon.className = 'external-icon';
            icon.innerHTML = ' ↗';
            icon.style.fontSize = '0.7em';
            link.appendChild(icon);
          }
        }
      });
    }
  };

  // =================== COPY CODE FEEDBACK ===================
  const CopyCodeFeedback = {
    init() {
      document.querySelectorAll('.md-clipboard').forEach(button => {
        button.addEventListener('click', async () => {
          const code = button.previousElementSibling?.textContent;
          if (code && await utils.copyToClipboard(code)) {
            // Show success feedback
            const originalIcon = button.innerHTML;
            button.innerHTML = '✓';
            button.style.color = '#4caf50';
            
            setTimeout(() => {
              button.innerHTML = originalIcon;
              button.style.color = '';
            }, 1500);
          }
        });
      });
    }
  };

  // =================== MAIN INITIALIZATION ===================
  const App = {
    init() {
      // Initialize all modules when DOM is ready
      document.addEventListener('DOMContentLoaded', () => {
        LoadingAnimation.init();
        ScrollAnimations.init();
        MouseGlowEffect.init();
        CodeBlockEnhancements.init();
        TOCHighlight.init();
        SearchEnhancements.init();
        ReadingProgress.init();
        ImageZoom.init();
        SmoothScroll.init();
        DarkModePersistence.init();
        PerformanceMonitor.init();
        ExternalLinks.init();
        CopyCodeFeedback.init();
      });

      // Service Worker Registration for PWA
      if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
          navigator.serviceWorker.register('/sw.js').catch(() => {
            // Service worker registration failed - this is expected in development
          });
        });
      }
    }
  };

  // Start the application
  App.init();

})();
