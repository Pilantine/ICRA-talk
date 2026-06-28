<template>
  <div
    ref="container"
    style="background:#fff; border-radius:6px; padding:6px 10px; display:inline-flex; justify-content:center; align-items:center; min-height:80px;"
  >
    <span v-if="loading" style="color:#888; font-size:0.8rem; font-style:italic;">Rendering…</span>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'

const props = defineProps({
  code:     { type: String, required: true },
  preamble: { type: String, default: '' },
})

const container = ref(null)
const loading   = ref(true)

const SRC = 'https://tikzjax.com/v1/tikzjax.js'

function ensureScript() {
  return new Promise((resolve) => {
    const existing = document.querySelector(`script[src="${SRC}"]`)
    if (existing) {
      if (window.tikzjax) { resolve(); return }
      existing.addEventListener('load', resolve)
      return
    }
    const s = document.createElement('script')
    s.src = SRC
    s.onload = resolve
    document.head.appendChild(s)
  })
}

async function render() {
  if (!container.value) return
  loading.value = true
  container.value.innerHTML = ''

  await ensureScript()

  const el = document.createElement('script')
  el.type = 'text/tikz'
  el.dataset.preamble = props.preamble
  el.textContent = props.code
  container.value.appendChild(el)

  // Poll until tikzjax replaces the script tag with an SVG
  const t0 = Date.now()
  await new Promise(resolve => {
    const id = setInterval(() => {
      const done = !container.value
        || container.value.querySelector('svg')
        || Date.now() - t0 > 15000
      if (done) { clearInterval(id); resolve() }
    }, 200)
  })
  loading.value = false
}

onMounted(render)
watch(() => props.code, render)
</script>
