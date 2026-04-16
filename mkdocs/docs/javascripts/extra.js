/**
 * 🧬 Awesome Bioinformatics Algorithms - Interactive Experience Layer
 * Next-generation interactions and dynamic features
 */

document.addEventListener('DOMContentLoaded', () => {
  initScrollAnimations();
  initSearchEnhancements();
  initDataVisualization();
  initKeyboardShortcuts();
  initLazyLoading();
  initTagCloud();
  initCopyButtons();
});

/**
 * Scroll-triggered animations with Intersection Observer
 */
function initScrollAnimations() {
  const animatedElements = document.querySelectorAll('.aba-animate');
  
  if (animatedElements.length === 0) return;
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animationPlayState = 'running';
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });
  
  animatedElements.forEach(el => {
    el.style.animationPlayState = 'paused';
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
  `;
  
  const mainContent = document.querySelector('.md-content__inner');
  if (mainContent) {
    mainContent.insertBefore(searchWrapper, mainContent.firstChild.nextSibling);
  }
  
  // Populate category filter
  const categories = new Set();
  document.querySelectorAll('[data-category]').forEach(el => {
    categories.add(el.dataset.category);
  });
  
  const categorySelect = document.getElementById('category-filter');
  categories.forEach(cat => {
    const option = document.createElement('option');
    option.value = cat;
    option.textContent = cat;
    categorySelect.appendChild(option);
  });
  
  // Real-time filtering
  const searchInput = document.getElementById('algo-search');
  const difficultySelect = document.getElementById('difficulty-filter');
  
  function filterAlgorithms() {
    const query = searchInput.value.toLowerCase();
    const category = categorySelect.value;
    const difficulty = difficultySelect.value;
    
    const items = document.querySelectorAll('.aba-algo-card, .aba-table tbody tr');
    let visibleCount = 0;
    
    items.forEach(item => {
      const name = item.querySelector('.aba-algo-name, td:first-child')?.textContent.toLowerCase() || '';
      const purpose = item.querySelector('.aba-algo-purpose, td:nth-child(4)')?.textContent.toLowerCase() || '';
      const itemCategory = item.dataset.category || '';
      const itemDifficulty = item.dataset.difficulty || '';
      
      const matchesSearch = name.includes(query) || purpose.includes(query);
      const matchesCategory = !category || itemCategory === category;
      const matchesDifficulty = !difficulty || itemDifficulty === difficulty;
      
      const isVisible = matchesSearch && matchesCategory && matchesDifficulty;
      
      item.style.display = isVisible ? '' : 'none';
      item.style.opacity = isVisible ? '1' : '0';
      item.style.transform = isVisible ? 'scale(1)' : 'scale(0.95)';
      
      if (isVisible) visibleCount++;
    });
    
    // Update result count
    updateResultCount(visibleCount, items.length);
  }
  
  searchInput?.addEventListener('input', debounce(filterAlgorithms, 150));
  categorySelect?.addEventListener('change', filterAlgorithms);
  difficultySelect?.addEventListener('change', filterAlgorithms);
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
    countEl.style.cssText = 'font-size: 0.875rem; color: var(--md-default-fg-color--light); margin-left: auto;';
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
 * Render simple bar chart for year distribution
 */
function renderYearChart(container) {
  const years = {};
  document.querySelectorAll('[data-year]').forEach(el => {
    const year = el.dataset.year;
    if (year) {
      years[year] = (years[year] || 0) + 1;
    }
  });
  
  const sortedYears = Object.entries(years).sort((a, b) => a[0] - b[0]);
  const maxCount = Math.max(...Object.values(years));
  
  if (sortedYears.length === 0) return;
  
  const chartStyles = `
    <style>
      .aba-chart { margin: 1.5rem 0; }
      .aba-chart-title { font-size: 1rem; font-weight: 600; margin-bottom: 1rem; }
      .aba-chart-bars { display: flex; align-items: flex-end; gap: 4px; height: 120px; padding: 1rem 0; }
      .aba-chart-bar-wrapper { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 0.5rem; }
      .aba-chart-bar { 
        width: 100%; 
        min-height: 4px; 
        background: var(--aba-gradient-primary); 
        border-radius: 4px 4px 0 0;
        position: relative;
        transition: opacity 0.3s;
      }
      .aba-chart-bar:hover { opacity: 0.8; }
      .aba-chart-bar-value { 
        position: absolute; 
        top: -20px; 
        left: 50%; 
        transform: translateX(-50%);
        font-size: 0.6875rem;
        font-weight: 600;
        opacity: 0;
        transition: opacity 0.3s;
      }
      .aba-chart-bar:hover .aba-chart-bar-value { opacity: 1; }
      .aba-chart-bar-label { font-size: 0.625rem; color: var(--md-default-fg-color--light); }
    </style>
  `;
  
  const chartHtml = chartStyles + `
    <div class="aba-chart">
      <h4 class="aba-chart-title">年份分布</h4>
      <div class="aba-chart-bars">
        ${sortedYears.map(([year, count]) => `
          <div class="aba-chart-bar-wrapper">
            <div class="aba-chart-bar" style="height: ${Math.max((count / maxCount * 100), 4)}%">
              <span class="aba-chart-bar-value">${count}</span>
            </div>
            <span class="aba-chart-bar-label">${year}</span>
          </div>
        `).join('')}
      </div>
    </div>
  `;
  
  container.innerHTML = chartHtml;
  
  // Animate bars
  setTimeout(() => {
    container.querySelectorAll('.aba-chart-bar').forEach((bar, i) => {
      setTimeout(() => {
        bar.style.height = bar.style.height;
      }, i * 30);
    });
  }, 100);
}

/**
 * Render difficulty distribution
 */
function renderDifficultyChart(container) {
  const difficulties = { beginner: 0, intermediate: 0, advanced: 0 };
  document.querySelectorAll('[data-difficulty]').forEach(el => {
    const diff = el.dataset.difficulty;
    if (diff && difficulties.hasOwnProperty(diff)) {
      difficulties[diff]++;
    }
  });
  
  const total = Object.values(difficulties).reduce((a, b) => a + b, 0);
  if (total === 0) return;
  
  const colors = ['#22c55e', '#f59e0b', '#f43f5e'];
  const labels = { beginner: '入门', intermediate: '进阶', advanced: '高级' };
  const entries = Object.entries(difficulties);
  
  const chartStyles = `
    <style>
      .aba-pie-container { display: flex; align-items: center; gap: 2rem; flex-wrap: wrap; }
      .aba-pie { width: 150px; height: 150px; }
      .aba-pie-legend { display: flex; flex-direction: column; gap: 0.5rem; }
      .aba-pie-legend-item { display: flex; align-items: center; gap: 0.5rem; }
      .aba-pie-legend-color { width: 12px; height: 12px; border-radius: 3px; }
      .aba-pie-legend-label { font-size: 0.875rem; }
      .aba-pie-legend-value { font-size: 0.75rem; color: var(--md-default-fg-color--light); }
    </style>
  `;
  
  let currentAngle = 0;
  const slices = entries.map(([key, count], i) => {
    const angle = (count / total) * 360;
    const startAngle = currentAngle;
    currentAngle += angle;
    const endAngle = currentAngle;
    
    const start = polarToCartesian(50, 50, 45, endAngle);
    const end = polarToCartesian(50, 50, 45, startAngle);
    const largeArcFlag = angle <= 180 ? 0 : 1;
    
    return `<path d="M 50 50 L ${start.x} ${start.y} A 45 45 0 ${largeArcFlag} 0 ${end.x} ${end.y} Z"
                   fill="${colors[i]}" stroke="white" stroke-width="2"/>`;
  }).join('');
  
  const legend = entries.map(([key, count], i) => `
    <div class="aba-pie-legend-item">
      <span class="aba-pie-legend-color" style="background: ${colors[i]}"></span>
      <span class="aba-pie-legend-label">${labels[key]}</span>
      <span class="aba-pie-legend-value">${count} (${Math.round(count/total*100)}%)</span>
    </div>
  `).join('');
  
  container.innerHTML = chartStyles + `
    <div class="aba-chart">
      <h4 class="aba-chart-title" style="font-size: 1rem; font-weight: 600; margin-bottom: 1rem;">难度分布</h4>
      <div class="aba-pie-container">
        <svg viewBox="0 0 100 100" class="aba-pie">${slices}</svg>
        <div class="aba-pie-legend">${legend}</div>
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
 * Render category bar chart
 */
function renderCategoryChart(container) {
  const data = {};
  document.querySelectorAll('[data-category]').forEach(el => {
    const cat = el.dataset.category;
    if (cat) data[cat] = (data[cat] || 0) + 1;
  });
  
  const entries = Object.entries(data).sort((a, b) => b[1] - a[1]);
  if (entries.length === 0) return;
  
  const max = Math.max(...entries.map(e => e[1]));
  
  const chartStyles = `
    <style>
      .aba-cat-bars { display: flex; flex-direction: column; gap: 0.75rem; }
      .aba-cat-bar-item { display: flex; align-items: center; gap: 1rem; }
      .aba-cat-bar-label { width: 120px; font-size: 0.75rem; text-align: right; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
      .aba-cat-bar-track { flex: 1; height: 24px; background: var(--aba-glass-bg); border-radius: 12px; overflow: hidden; }
      .aba-cat-bar-fill { height: 100%; background: var(--aba-gradient-primary); border-radius: 12px; display: flex; align-items: center; justify-content: flex-end; padding-right: 0.75rem; color: white; font-size: 0.6875rem; font-weight: 600; min-width: 24px; transition: width 1s ease-out; }
    </style>
  `;
  
  const bars = entries.map(([cat, count]) => `
    <div class="aba-cat-bar-item">
      <span class="aba-cat-bar-label">${cat}</span>
      <div class="aba-cat-bar-track">
        <div class="aba-cat-bar-fill" style="width: 0%" data-width="${(count / max * 100).toFixed(1)}%">${count}</div>
      </div>
    </div>
  `).join('');
  
  container.innerHTML = chartStyles + `
    <div class="aba-chart">
      <h4 class="aba-chart-title" style="font-size: 1rem; font-weight: 600; margin-bottom: 1rem;">分类分布</h4>
      <div class="aba-cat-bars">${bars}</div>
    </div>
  `;
  
  // Animate bars
  setTimeout(() => {
    container.querySelectorAll('.aba-cat-bar-fill').forEach(bar => {
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
    
    // Arrow keys for quick navigation
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      const cards = Array.from(document.querySelectorAll('.aba-algo-card, .aba-bento-card'));
      if (cards.length === 0) return;
      
      const visibleCards = cards.filter(c => c.style.display !== 'none');
      const currentFocus = document.activeElement;
      const currentIndex = visibleCards.findIndex(c => c === currentFocus || c.contains(currentFocus));
      
      if (e.key === 'ArrowDown' && currentIndex < visibleCards.length - 1) {
        e.preventDefault();
        focusCard(visibleCards[currentIndex + 1]);
      } else if (e.key === 'ArrowUp' && currentIndex > 0) {
        e.preventDefault();
        focusCard(visibleCards[currentIndex - 1]);
      }
    }
  });
}

function focusCard(card) {
  if (!card) return;
  card.focus();
  card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  card.classList.add('aba-card-focused');
  setTimeout(() => card.classList.remove('aba-card-focused'), 1000);
}

/**
 * Lazy loading for images and heavy content
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
        tag.style.transform = `scale(${1 + Math.random() * 0.1})`;
      }, i * 20);
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
        
        setTimeout(() => {
          btn.classList.remove('aba-copy-success');
          btn.innerHTML = original;
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
