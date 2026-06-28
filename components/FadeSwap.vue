<template>
  <div style="display:flex; justify-content:center;">
    <div ref="container" style="position:relative; line-height:0;">
      <img :src="from" style="max-height:420px; display:block;" />
      <img ref="overlay" :src="to"
           style="position:absolute; top:0; left:0; max-height:420px; opacity:0; transition:opacity 0.8s ease;" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

defineProps({ from: String, to: String })

const container = ref(null)
const overlay   = ref(null)
let observer    = null
let triggered   = false

onMounted(() => {
  const slide = container.value?.closest('.slidev-slide') || document.body
  observer = new MutationObserver((mutations) => {
    if (triggered) return
    for (const m of mutations) {
      if (m.attributeName !== 'class') continue
      const wasHidden = (m.oldValue ?? '').includes('slidev-vclick-hidden')
      const isHidden  = m.target.classList.contains('slidev-vclick-hidden')
      if (wasHidden && !isHidden) {
        triggered = true
        overlay.value.style.opacity = '1'
        break
      }
    }
  })
  observer.observe(slide, {
    attributes: true, attributeFilter: ['class'],
    attributeOldValue: true, subtree: true,
  })
})

onBeforeUnmount(() => observer?.disconnect())
</script>
