import DefaultTheme from 'vitepress/theme'
import './style.css'
import AlgorithmCard from './components/AlgorithmCard.vue'
import ComplexityBadge from './components/ComplexityBadge.vue'
import CitationBlock from './components/CitationBlock.vue'
import HeroBackground from './components/HeroBackground.vue'
import ThemeAwareSvg from './components/ThemeAwareSvg.vue'
import StatCounter from './components/StatCounter.vue'
import AlgoTable from './components/AlgoTable.vue'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('AlgorithmCard', AlgorithmCard)
    app.component('ComplexityBadge', ComplexityBadge)
    app.component('CitationBlock', CitationBlock)
    app.component('HeroBackground', HeroBackground)
    app.component('ThemeAwareSvg', ThemeAwareSvg)
    app.component('StatCounter', StatCounter)
    app.component('AlgoTable', AlgoTable)
  },
}
