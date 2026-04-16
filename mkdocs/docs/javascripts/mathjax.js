/**
 * KaTeX Math Rendering Initialization
 */
document.addEventListener('DOMContentLoaded', () => {
  if (typeof renderMathInElement !== 'undefined') {
    renderMathInElement(document.body, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false},
        {left: '\\(', right: '\\)', display: false},
        {left: '\\[', right: '\\]', display: true}
      ],
      throwOnError: false,
      strict: false,
      trust: true,
      macros: {
        '\\C': '\\mathbb{C}',
        '\\R': '\\mathbb{R}',
        '\\Q': '\\mathbb{Q}',
        '\\Z': '\\mathbb{Z}',
        '\\N': '\\mathbb{N}'
      }
    });
  }
});
