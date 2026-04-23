/**
 * 🧬 Awesome Bioinformatics Algorithms - Interactive Experience Layer
 * BioTech Horizon Theme - Modern interactions and data visualization
 */

document.addEventListener('DOMContentLoaded', () => {
  initScrollAnimations();
  initSearchEnhancements();
  initDataVisualization();
  initKeyboardShortcuts();
  initLazyLoading();
  initTagCloud();
  initCopyButtons();
  initParticles();
});

/**
 * Particle background effect for hero section
 */
function initParticles() {
  const hero = document.querySelector('.aba-hero');
  if (!hero || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  
  const canvas = document.createElement('canvas');
  canvas.className = 'aba-particles';
  canvas.style.cssText = `
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1;
  `;
  hero.insertBefore(canvas, hero.firstChild);
  
  const ctx = canvas.getContext('2d');
  let particles = [];
  let animationId;
  let isActive = true;
  
  function resize() {
    canvas.width = hero.offsetWidth;
    canvas.height = hero.offsetHeight;
  }
  
  resize();
  window.addEventListener('resize', resize, { passive: true });
  
  // Create particles
  const particleCount = Math.min(30, Math.floor(window.innerWidth / 50));
  for (let i = 0; i < particleCount; i++) {
    particles.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      vx: (Math.random() - 0.5) * 0.3,
      vy: (Math.random() - 0.5) * 0.3,
      radius: Math.random() * 2 + 1,
      opacity: Math.random() * 0.5 + 0.2
    });
  }
  
  let frameCount = 0;
  function animate() {
    if (!isActive) return;
    frameCount++;
    
    // Render every 2nd frame for performance
    if (frameCount % 2 === 0) {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      particles.forEach((p, i) => {
        // Update position
        p.x += p.vx;
        p.y += p.vy;
        
        // Wrap around
        if (p.x < 0) p.x = canvas.width;
        if (p.x > canvas.width) p.x = 0;
        if (p.y < 0) p.y = canvas.height;
        if (p.y > canvas.height) p.y = 0;
        
        // Draw particle
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(14, 165, 233, ${p.opacity})`;
        ctx.fill();
        
        // Draw connections (limited)
        if (i % 3 === 0) {
          let connections = 0;
          for (let j = i + 1; j < particles.length && connections < 2; j++) {
            const dx = particles[j].x - p.x;
            const dy = particles[j].y - p.y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            
            if (dist < 100) {
              connections++;
              ctx.beginPath();
              ctx.moveTo(p.x, p.y);
              ctx.lineTo(particles[j].x, particles[j].y);
              ctx.strokeStyle = `rgba(14, 165, 233, ${0.1 * (1 - dist / 100)})`;
              ctx.stroke();
            }
          }
        }
      });
    }
    
    animationId = requestAnimationFrame(animate);
  }
  
  // Visibility handling
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      isActive = false;
      cancelAnimationFrame(animationId);
    } else {
      isActive = true;
      animate();
    }
  });
  
  // Start animation
  animate();
}

/**
 * Scroll-triggered animations with Intersection Observer
 */
function initScrollAnimations() {
  const animatedElements = document.querySelectorAll('.aba-animate');
  
  if (animatedElements.length === 0) return;
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });
  
  animatedElements.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
  });
}

/**
 * Enhanced search with instant filtering and highlighting
 */
function initSearchEnhancements() {
  // Add search bar to algorithm listing pages
  const algoContainer = document.querySelector('.aba-algo-grid, .aba-table tbody');
  if (!algoContainer) return;
  
  const searchWrapper = document.createElement('div');
  searchWrapper.className = 'aba-search-bar';
  searchWrapper.innerHTML = `
    <input type="text" class="aba-search-input" placeholder="🔍 搜索算法..." id="algo-search">
    <select class="aba-filter-select" id="category-filter">
      <option value="">所有分类</option>
    </select>
    <select class="aba-filter-select" id="difficulty-filter">
      <option value="">所有难度</option>
      <option value="beginner">入门</option>
      <option value="intermediate">进阶</option>
      <option value="advanced">高级</option>
    </select>
    <select class="aba-filter-select" id="year-filter">
      <option value="">所有年份</option>
    </select>
  `;
  
  const mainContent = document.querySelector('.md-content__inner');
  if (mainContent) {
    const firstHeading = mainContent.querySelector('h1');
    if (firstHeading) {
      firstHeading.after(searchWrapper);
    } else {
      mainContent.insertBefore(searchWrapper, mainContent.firstChild.nextSibling);
    }
  }
  
  // Populate category filter
  const categories = new Set();
  const years = new Set();
  document.querySelectorAll('[data-category]').forEach(el => {
    categories.add(el.dataset.category);
  });
  document.querySelectorAll('[data-year]').forEach(el => {
    if (el.dataset.year) years.add(el.dataset.year);
  });
  
  const categorySelect = document.getElementById('category-filter');
  categories.forEach(cat => {
    const option = document.createElement('option');
    option.value = cat;
    option.textContent = cat;
    categorySelect.appendChild(option);
  });
  
  const yearSelect = document.getElementById('year-filter');
  Array.from(years).sort((a, b) => b - a).forEach(year => {
    const option = document.createElement('option');
    option.value = year;
    option.textContent = year;
    yearSelect.appendChild(option);
  });
  
  // Real-time filtering
  const searchInput = document.getElementById('algo-search');
  const difficultySelect = document.getElementById('difficulty-filter');
  
  function filterAlgorithms() {
    const query = searchInput.value.toLowerCase().trim();
    const category = categorySelect.value;
    const difficulty = difficultySelect.value;
    const year = yearSelect.value;
    
    const items = document.querySelectorAll('.aba-algo-card, .aba-table tbody tr');
    let visibleCount = 0;
    
    items.forEach(item => {
      const name = item.querySelector('.aba-algo-name, td:first-child')?.textContent.toLowerCase() || '';
      const purpose = item.querySelector('.aba-algo-purpose, td:nth-child(4)')?.textContent.toLowerCase() || '';
      const itemCategory = item.dataset.category || '';
      const itemDifficulty = item.dataset.difficulty || '';
      const itemYear = item.dataset.year || '';
      
      const matchesSearch = !query || name.includes(query) || purpose.includes(query);
      const matchesCategory = !category || itemCategory === category;
      const matchesDifficulty = !difficulty || itemDifficulty === difficulty;
      const matchesYear = !year || itemYear === year;
      
      const isVisible = matchesSearch && matchesCategory && matchesDifficulty && matchesYear;
      
      item.style.display = isVisible ? '' : 'none';
      if (isVisible) visibleCount++;
    });
    
    updateResultCount(visibleCount, items.length);
  }
  
  searchInput?.addEventListener('input', debounce(filterAlgorithms, 200));
  categorySelect?.addEventListener('change', filterAlgorithms);
  difficultySelect?.addEventListener('change', filterAlgorithms);
  yearSelect?.addEventListener('change', filterAlgorithms);
}

/**
 * Debounce utility function
 */
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

/**
 * Update result count display
 */
function updateResultCount(visible, total) {
  let countEl = document.getElementById('result-count');
  if (!countEl) {
    countEl = document.createElement('div');
    countEl.id = 'result-count';
    countEl.className = 'aba-result-count';
    countEl.style.cssText = `
      font-size: 0.875rem; 
      color: var(--md-default-fg-color--light); 
      margin-left: auto;
      padding: 0.5rem 0;
    `;
    document.querySelector('.aba-search-bar')?.appendChild(countEl);
  }
  countEl.textContent = `显示 ${visible} / ${total} 个算法`;
}

/**
 * Data visualization components
 */
function initDataVisualization() {
  // Year distribution chart
  const chartContainer = document.getElementById('year-distribution');
  if (chartContainer) {
    renderYearChart(chartContainer);
  }
  
  // Difficulty pie chart
  const difficultyContainer = document.getElementById('difficulty-chart');
  if (difficultyContainer) {
    renderDifficultyChart(difficultyContainer);
  }
  
  // Category bar chart
  const categoryContainer = document.getElementById('category-chart');
  if (categoryContainer) {
    renderCategoryChart(categoryContainer);
  }
}

/**
 * Render year distribution bar chart
 */
function renderYearChart(container) {
  const years = {};
  document.querySelectorAll('[data-year]').forEach(el => {
    const year = el.dataset.year;
    if (year) {
      years[year] = (years[year] || 0) + 1;
    }
  });
  
  const sortedYears = Object.entries(years).sort((a, b) => a[0] - b[0]).slice(-12);
  const maxCount = Math.max(...Object.values(years));
  
  if (sortedYears.length === 0) return;
  
  const chartHtml = `
    <div class="aba-chart">
      <h4 class="aba-chart-title">📊 年份分布（近12年）</h4>
      <div class="aba-chart-bars" style="
        display: flex; 
        align-items: flex-end; 
        gap: 6px; 
        height: 160px; 
        padding: 1rem 0;
      ">
        ${sortedYears.map(([year, count], i) => `
          <div style="
            flex: 1; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            gap: 0.5rem;
          ">
            <div style="
              width: 100%; 
              min-height: 4px; 
              background: linear-gradient(to top, #0ea5e9, #10b981); 
              border-radius: 4px 4px 0 0;
              position: relative;
              cursor: pointer;
              transition: all 0.3s;
            " class="aba-chart-bar" data-height="${Math.max((count / maxCount * 100), 4)}%">
              <span style="
                position: absolute; 
                top: -22px; 
                left: 50%; 
                transform: translateX(-50%);
                font-size: 0.75rem;
                font-weight: 600;
                opacity: 0;
                transition: opacity 0.3s;
              " class="aba-chart-value">${count}</span>
            </div>
            <span style="font-size: 0.7rem; color: var(--md-default-fg-color--light);">${year}</span>
          </div>
        `).join('')}
      </div>
    </div>
    <style>
      .aba-chart-bar:hover { opacity: 0.8; filter: brightness(1.2); }
      .aba-chart-bar:hover .aba-chart-value { opacity: 1 !important; }
    </style>
  `;
  
  container.innerHTML = chartHtml;
  
  // Animate bars
  setTimeout(() => {
    container.querySelectorAll('.aba-chart-bar').forEach((bar, i) => {
      bar.style.height = '0%';
      setTimeout(() => {
        bar.style.height = bar.dataset.height;
        bar.style.transition = 'height 0.6s ease-out';
      }, i * 50);
    });
  }, 100);
}

/**
 * Render difficulty distribution pie chart
 */
function renderDifficultyChart(container) {
  const difficulties = { beginner: 0, intermediate: 0, advanced: 0 };
  let total = 0;
  document.querySelectorAll('[data-difficulty]').forEach(el => {
    const diff = el.dataset.difficulty;
    if (diff && difficulties.hasOwnProperty(diff)) {
      difficulties[diff]++;
      total++;
    }
  });
  
  if (total === 0) return;
  
  const colors = ['#22c55e', '#f59e0b', '#ef4444'];
  const labels = { beginner: '入门', intermediate: '进阶', advanced: '高级' };
  const entries = Object.entries(difficulties).filter(([_, count]) => count > 0);
  
  let currentAngle = 0;
  const slices = entries.map(([key, count], i) => {
    const angle = (count / total) * 360;
    const startAngle = currentAngle;
    currentAngle += angle;
    const endAngle = currentAngle;
    
    const start = polarToCartesian(50, 50, 40, endAngle);
    const end = polarToCartesian(50, 50, 40, startAngle);
    const largeArcFlag = angle <= 180 ? 0 : 1;
    
    return `<path d="M 50 50 L ${start.x} ${start.y} A 40 40 0 ${largeArcFlag} 0 ${end.x} ${end.y} Z"
               fill="${colors[i]}" stroke="white" stroke-width="2"/>`;
  }).join('');
  
  const legend = entries.map(([key, count], i) => `
    <div style="display: flex; align-items: center; gap: 0.5rem;">
      <span style="width: 14px; height: 14px; border-radius: 3px; background: ${colors[i]}"></span>
      <span style="font-size: 0.9rem;">${labels[key]}</span>
      <span style="font-size: 0.8rem; color: var(--md-default-fg-color--light);">${count} (${Math.round(count/total*100)}%)</span>
    </div>
  `).join('');
  
  container.innerHTML = `
    <div class="aba-chart">
      <h4 class="aba-chart-title">📈 难度分布</h4>
      <div style="display: flex; align-items: center; gap: 2rem; flex-wrap: wrap; justify-content: center;">
        <svg viewBox="0 0 100 100" style="width: 140px; height: 140px;">${slices}</svg>
        <div style="display: flex; flex-direction: column; gap: 0.75rem;">${legend}</div>
      </div>
    </div>
  `;
}

function polarToCartesian(centerX, centerY, radius, angleInDegrees) {
  const angleInRadians = (angleInDegrees - 90) * Math.PI / 180.0;
  return {
    x: centerX + (radius * Math.cos(angleInRadians)),
    y: centerY + (radius * Math.sin(angleInRadians))
  };
}

/**
 * Render category horizontal bar chart
 */
function renderCategoryChart(container) {
  const data = {};
  document.querySelectorAll('[data-category]').forEach(el => {
    const cat = el.dataset.category;
    if (cat) data[cat] = (data[cat] || 0) + 1;
  });
  
  const entries = Object.entries(data).sort((a, b) => b[1] - a[1]).slice(0, 10);
  if (entries.length === 0) return;
  
  const max = Math.max(...entries.map(e => e[1]));
  
  container.innerHTML = `
    <div class="aba-chart">
      <h4 class="aba-chart-title">📂 分类 TOP10</h4>
      <div style="display: flex; flex-direction: column; gap: 0.875rem;">
        ${entries.map(([cat, count]) => `
          <div style="display: flex; align-items: center; gap: 1rem;">
            <span style="width: 120px; font-size: 0.8rem; text-align: right; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" title="${cat}">${cat}</span>
            <div style="flex: 1; height: 28px; background: rgba(255,255,255,0.05); border-radius: 14px; overflow: hidden;">
              <div style="height: 100%; width: 0%; background: linear-gradient(90deg, #0ea5e9, #10b981); border-radius: 14px; display: flex; align-items: center; justify-content: flex-end; padding-right: 0.75rem; color: white; font-size: 0.75rem; font-weight: 600; min-width: 28px; transition: width 1s ease-out;" data-width="${(count / max * 100).toFixed(1)}%">${count}</div>
            </div>
          </div>
        `).join('')}
      </div>
    </div>
  `;
  
  setTimeout(() => {
    container.querySelectorAll('[data-width]').forEach(bar => {
      bar.style.width = bar.dataset.width;
    });
  }, 100);
}

/**
 * Keyboard shortcuts
 */
function initKeyboardShortcuts() {
  document.addEventListener('keydown', (e) => {
    // Skip if in input field
    if (e.target.matches('input, textarea, select')) return;
    
    // Ctrl/Cmd + K for search
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      const searchInput = document.getElementById('algo-search') || 
                         document.querySelector('.md-search__input');
      searchInput?.focus();
    }
    
    // Escape to clear search
    if (e.key === 'Escape') {
      const searchInput = document.getElementById('algo-search');
      if (searchInput) {
        searchInput.value = '';
        searchInput.dispatchEvent(new Event('input'));
        searchInput.blur();
      }
    }
    
    // G then H for home
    if (e.key === 'g') {
      const handler = (e2) => {
        if (e2.key === 'h') {
          window.location.href = '/';
        }
        document.removeEventListener('keydown', handler);
      };
      document.addEventListener('keydown', handler);
      setTimeout(() => document.removeEventListener('keydown', handler), 500);
    }
  });
}

/**
 * Lazy loading for images
 */
function initLazyLoading() {
  const lazyElements = document.querySelectorAll('[data-lazy]');
  
  if (lazyElements.length === 0) return;
  if (!('IntersectionObserver' in window)) {
    lazyElements.forEach(el => {
      el.src = el.dataset.lazy;
      el.removeAttribute('data-lazy');
    });
    return;
  }
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        if (el.dataset.lazy) {
          el.src = el.dataset.lazy;
          el.addEventListener('load', () => {
            el.classList.add('aba-lazy-loaded');
            el.removeAttribute('data-lazy');
          });
        }
        observer.unobserve(el);
      }
    });
  }, { rootMargin: '50px' });
  
  lazyElements.forEach(el => observer.observe(el));
}

/**
 * Tag cloud interactivity
 */
function initTagCloud() {
  const tagCloud = document.querySelector('.aba-tag-cloud');
  if (!tagCloud) return;
  
  const tags = tagCloud.querySelectorAll('.aba-tag');
  
  // Shuffle animation on hover
  tagCloud.addEventListener('mouseenter', () => {
    tags.forEach((tag, i) => {
      setTimeout(() => {
        tag.style.transform = `scale(${1 + Math.random() * 0.05})`;
      }, i * 15);
    });
  });
  
  tagCloud.addEventListener('mouseleave', () => {
    tags.forEach(tag => {
      tag.style.transform = '';
    });
  });
}

/**
 * Copy to clipboard functionality
 */
function initCopyButtons() {
  document.querySelectorAll('.aba-copy-btn').forEach(btn => {
    btn.addEventListener('click', async () => {
      const text = btn.dataset.copy;
      try {
        await navigator.clipboard.writeText(text);
        const original = btn.innerHTML;
        btn.classList.add('aba-copy-success');
        btn.innerHTML = '✓ 已复制';
        btn.style.background = '#22c55e';
        
        setTimeout(() => {
          btn.classList.remove('aba-copy-success');
          btn.innerHTML = original;
          btn.style.background = '';
        }, 2000);
      } catch (err) {
        console.error('Failed to copy:', err);
      }
    });
  });
}

/**
 * Smooth scroll for anchor links
 */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

/**
 * Utility: Detect reduced motion preference
 */
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
if (prefersReducedMotion.matches) {
  document.documentElement.classList.add('reduce-motion');
}

/**
 * Add reading progress indicator
 */
function initReadingProgress() {
  const progressBar = document.createElement('div');
  progressBar.className = 'aba-reading-progress';
  progressBar.style.cssText = `
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    background: linear-gradient(90deg, #0ea5e9, #10b981);
    z-index: 1000;
    transition: width 0.1s;
    width: 0%;
  `;
  document.body.appendChild(progressBar);
  
  window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;
    const max = document.documentElement.scrollHeight - window.innerHeight;
    const progress = (scrolled / max) * 100;
    progressBar.style.width = `${Math.min(progress, 100)}%`;
  }, { passive: true });
}

// Initialize reading progress on article pages
if (document.querySelector('.md-content__inner article, .aba-detail-hero')) {
  initReadingProgress();
}
