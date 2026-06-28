<template>
  <div ref="container" class="pausable-video">
    <video ref="vid" :src="src" preload="auto" muted playsinline />
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const props = defineProps({
  src:          { type: String,  required: true },
  pausePoints:  { type: Array,   default: () => [] },
  playbackRate: { type: Number,  default: 1.0 },
})

const container = ref(null)
const vid        = ref(null)
let pauseIdx     = 0
let observer     = null
let resumeReady  = false

onMounted(() => {
  const v = vid.value
  if (!v) return

  v.playbackRate = props.playbackRate
  const pts = (props.pausePoints?.length ? props.pausePoints : [3.0, 4.8, 11.3]).map(Number)

  v.addEventListener('timeupdate', () => {
    if (pauseIdx >= pts.length) return
    if (v.currentTime >= pts[pauseIdx]) {
      v.pause()
      v.currentTime = pts[pauseIdx]
      pauseIdx++
      setTimeout(() => { resumeReady = true }, 50)
    }
  })

  const slide = container.value?.closest('.slidev-slide') || document.body
  observer = new MutationObserver((mutations) => {
    for (const m of mutations) {
      if (m.attributeName !== 'class') continue
      const wasHidden = (m.oldValue ?? '').includes('slidev-vclick-hidden')
      const isHidden  = m.target.classList.contains('slidev-vclick-hidden')
      if (wasHidden && !isHidden && resumeReady && m.target.hasAttribute('data-video-trigger')) {
        resumeReady = false
        v.play().catch(() => {})
        break
      }
    }
  })

  // Delay observer start so Slidev's own mount-time class changes don't trigger playback.
  // Video does NOT auto-play — first frame (base poset) stays visible until first click.
  setTimeout(() => {
    resumeReady = true
    observer.observe(slide, {
      attributes: true, attributeFilter: ['class'],
      attributeOldValue: true, subtree: true,
    })
  }, 1000)
})

onBeforeUnmount(() => observer?.disconnect())
</script>

<style scoped>
.pausable-video { display: flex; justify-content: center; }
.pausable-video video { max-height: 420px; width: auto; }
</style>
