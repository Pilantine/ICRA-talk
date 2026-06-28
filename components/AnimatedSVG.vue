<template>
  <div ref="container" class="animated-svg" v-html="svgContent" />
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, nextTick } from 'vue'

const props = defineProps({
  src:      { type: String, required: true },
  viewBox:  { type: String, default: null },
  duration: { type: Number, default: 600 },
  stagger:  { type: Number, default: 0 },
  height:   { type: String, default: '120px' },
})

const container = ref(null)
const svgContent = ref('')
let observer = null

// Inject keyframes globally once
if (!document.getElementById('svg-draw-keyframes')) {
  const s = document.createElement('style')
  s.id = 'svg-draw-keyframes'
  s.textContent = '@keyframes svgDraw { to { stroke-dashoffset: 0; } }'
  document.head.appendChild(s)
}

onMounted(async () => {
  const res = await fetch(props.src)
  let svg = await res.text()
  if (props.viewBox)
    svg = svg.replace(/viewBox="[^"]*"/, `viewBox="${props.viewBox}"`)
  svg = svg.replace(/width="[^"]*" height="[^"]*"/, 'width="100%" height="100%"')
  svgContent.value = svg

  await nextTick()

  requestAnimationFrame(() => {
    setupArrows()

    const isVisible = !container.value?.closest('.slidev-vclick-hidden')
    if (isVisible) playArrows()

    let wasHidden = !isVisible
    const slide = container.value?.closest('.slidev-slide') || document.body
    observer = new MutationObserver(() => {
      const hidden = !!container.value?.closest('.slidev-vclick-hidden')
      if (hidden === wasHidden) return
      wasHidden = hidden
      if (hidden) resetArrows()
      else playArrows()
    })
    observer.observe(slide, { attributes: true, attributeFilter: ['class'], subtree: true })
  })
})

onBeforeUnmount(() => observer?.disconnect())

function getArrowPaths() {
  const svgEl = container.value?.querySelector('svg')
  if (!svgEl) return []
  return [...svgEl.querySelectorAll('path')].filter(p => {
    const fill   = p.getAttribute('fill')   ?? p.style.fill   ?? ''
    const stroke = p.getAttribute('stroke') ?? p.style.stroke ?? ''
    return fill === 'none' && stroke !== '' && stroke !== 'none'
  })
}


function setupArrows() {
  const svgEl = container.value?.querySelector('svg')
  if (!svgEl) return
  svgEl.style.filter = 'invert(1)'

  const paths = getArrowPaths()
  // Cap total stagger to 500ms regardless of path count
  const stagger = paths.length > 1 ? Math.min(props.stagger, 500 / (paths.length - 1)) : 0
  paths.forEach((path, i) => {
    const length = path.getTotalLength()
    path.style.strokeDasharray = `${length}`
    path.style.strokeDashoffset = `${length}`
    path.style.animation = `svgDraw ${props.duration}ms ease ${i * stagger}ms forwards paused`
  })

}

function playArrows() {
  getArrowPaths().forEach(path => {
    path.style.animationPlayState = 'running'
  })
}

function resetArrows() {
  const paths = getArrowPaths()
  const stagger = paths.length > 1 ? Math.min(props.stagger, 500 / (paths.length - 1)) : 0
  paths.forEach((path, i) => {
    const length = path.getTotalLength()
    path.style.animation = 'none'
    path.style.strokeDashoffset = `${length}`
    requestAnimationFrame(() => {
      path.style.animation = `svgDraw ${props.duration}ms ease ${i * stagger}ms forwards paused`
    })
  })
}
</script>

<style scoped>
.animated-svg {
  display: flex;
  align-items: center;
  justify-content: center;
}
.animated-svg :deep(svg) {
  height: v-bind(height);
  width: auto;
}
</style>
