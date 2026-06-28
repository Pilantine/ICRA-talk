<template>
  <video ref="vid" :src="src" muted v-bind="$attrs" />
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

defineProps({ src: String })

const vid = ref(null)
let observer = null

function play() {
  const v = vid.value
  if (!v) return
  v.currentTime = 0
  v.play().catch(() => {})
}

onMounted(() => {
  const v = vid.value
  if (!v) return

  // Play immediately if already visible (not inside a hidden v-click ancestor)
  if (!v.closest('.slidev-vclick-hidden')) play()

  // Watch ancestor class changes — fires when v-click reveals this element
  const slide = v.closest('.slidev-slide') || document.body
  observer = new MutationObserver(() => {
    if (!v.closest('.slidev-vclick-hidden')) play()
  })
  observer.observe(slide, { attributes: true, attributeFilter: ['class'], subtree: true })
})

onBeforeUnmount(() => observer?.disconnect())
</script>
