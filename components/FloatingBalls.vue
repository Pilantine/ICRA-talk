<template>
  <div class="balls-container" ref="containerRef">
    <div class="rect-border" />
    <div
      v-for="(b, i) in BALLS"
      :key="i"
      class="seq-group"
      :class="{ shown: visible > i }"
      :style="{ left: b.x + '%', top: b.y + '%', animationDelay: b.delay, animationDuration: b.dur }"
    >
      <!-- K node — vertical wrapper if secL -->
      <template v-if="b.secL">
        <div class="vert-group">
          <div class="sec-node" :class="{ sec: secVisible >= b.secIdx }">{{ b.secL }}</div>
          <div class="vert-arr" :class="{ sec: secVisible >= b.secIdx }">↓</div>
          <div class="k-node" :class="{ seq: seqVisible > i }">{{ b.k }}</div>
          <div class="vert-arr" :class="{ sec: secVisible >= b.secIdx }">↓</div>
          <div class="sec-node" :class="{ sec: secVisible >= b.secIdx }" data-hl="c4">{{ b.secLafter }}</div>
        </div>
      </template>
      <div v-else class="k-node" :class="{ seq: seqVisible > i }">{{ b.k }}</div>

      <div class="arr" :class="{ seq: seqVisible > i }">→</div>
      <div class="ti-ball">{{ b.label }}</div>
      <div class="arr" :class="{ seq: seqVisible > i }">→</div>

      <!-- C node — vertical wrapper if secR -->
      <template v-if="b.secR">
        <div class="vert-group">
          <div class="sec-node" :class="{ sec: secVisible >= b.secIdx }">{{ b.secR }}</div>
          <div class="vert-arr" :class="{ sec: secVisible >= b.secIdx }">↓</div>
          <div class="c-node" :class="{ seq: seqVisible > i }">{{ b.c }}</div>
          <div class="vert-arr" :class="{ sec: secVisible >= b.secIdx }">↓</div>
          <div class="sec-node" :class="{ sec: secVisible >= b.secIdx }" data-hl="c2">{{ b.secRafter }}</div>
        </div>
      </template>
      <div v-else class="c-node" :class="{ seq: seqVisible > i }">{{ b.c }}</div>
    </div>
    <!-- Ring around C'₂ (tracked) -->
    <div class="hl-ring" :class="{ on: highlight }"
      :style="{ left: r1.x + 'px', top: r1.y + 'px' }" />
    <!-- Ring around C'₄ (tracked) -->
    <div class="hl-ring" :class="{ on: highlight }"
      :style="{ left: r2.x + 'px', top: r2.y + 'px', transitionDelay: '0.05s' }" />
    <!-- Connecting line (tracked) -->
    <svg class="highlight-svg" :style="{ opacity: highlight ? 1 : 0, transition: 'opacity 0.4s ease 0.5s' }">
      <line :x1="line.x1" :y1="line.y1" :x2="line.x2" :y2="line.y2"
        stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="6 4" />
    </svg>
    <!-- ? above midpoint -->
    <div class="hl-question"
      :style="{ opacity: highlight ? 1 : 0, transition: 'opacity 0.5s ease 0.9s',
                left: ((r1.x + r2.x) / 2) + 'px', top: ((r1.y + r2.y) / 2 - 22) + 'px' }">?</div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, onUnmounted } from 'vue'

defineProps({
  visible:    { type: Number, default: 0 },
  seqVisible: { type: Number, default: 0 },
  secVisible: { type: Number, default: 0 },
  highlight:  { type: Boolean, default: false },
})

const containerRef = ref(null)
const r1 = reactive({ x: 0, y: 0 })
const r2 = reactive({ x: 0, y: 0 })
const line = reactive({ x1: 0, y1: 0, x2: 0, y2: 0 })
const RING_R = 16
let rafId = null

function track() {
  const container = containerRef.value
  if (container) {
    const base = container.getBoundingClientRect()
    const sx = base.width / container.offsetWidth
    const sy = base.height / container.offsetHeight
    const n1 = container.querySelector('[data-hl="c2"]')
    const n2 = container.querySelector('[data-hl="c4"]')
    if (n1) { const r = n1.getBoundingClientRect(); r1.x = (r.left + r.width/2 - base.left) / sx; r1.y = (r.top + r.height/2 - base.top) / sy }
    if (n2) { const r = n2.getBoundingClientRect(); r2.x = (r.left + r.width/2 - base.left) / sx; r2.y = (r.top + r.height/2 - base.top) / sy }
    // Line from edge to edge
    const dx = r2.x - r1.x, dy = r2.y - r1.y
    const dist = Math.sqrt(dx*dx + dy*dy) || 1
    const ux = dx/dist, uy = dy/dist
    line.x1 = r1.x + ux * RING_R; line.y1 = r1.y + uy * RING_R
    line.x2 = r2.x - ux * RING_R; line.y2 = r2.y - uy * RING_R
  }
  rafId = requestAnimationFrame(track)
}

onMounted(() => { track() })
onUnmounted(() => { if (rafId) cancelAnimationFrame(rafId) })

const BALLS = [
  { label: 'T₁', k: 'K₁', c: 'C₁', x: 18, y: 22, delay: '0s',   dur: '3.1s' },
  { label: 'T₂', k: 'K₂', c: 'C₂', x: 34, y: 52, delay: '0.5s', dur: '2.7s', secR: "K'₂", secRafter: "C'₂", secIdx: 1 },
  { label: 'T₃', k: 'K₃', c: 'C₃', x: 52, y: 18, delay: '1.1s', dur: '3.4s' },
  { label: 'T₄', k: 'K₄', c: 'C₄', x: 68, y: 55, delay: '0.3s', dur: '2.9s', secL: "K'₄", secLafter: "C'₄", secIdx: 2 },
  { label: 'T₅', k: 'K₅', c: 'C₅', x: 84, y: 28, delay: '0.8s', dur: '3.2s' },
]
</script>

<style scoped>
.balls-container {
  position: relative;
  width: 100%;
  height: 200px;
}

.rect-border {
  position: absolute;
  inset: 6px;
  border: 1.5px solid rgba(226,232,240,0.35);
  border-radius: 4px;
}

.seq-group {
  position: absolute;
  display: flex;
  align-items: center;
  gap: 2px;
  transform: translate(-50%, -50%);
  animation: float linear infinite alternate paused;
}
.seq-group.shown {
  animation-play-state: running;
}

/* Vertical wrapper for secondary sequence */
.vert-group {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
}

.vert-arr {
  color: rgba(226,232,240,0.7);
  font-family: serif;
  font-size: 12px;
  opacity: 0;
  transform: scale(0);
  transition: opacity 0.25s ease 0s, transform 0.25s ease 0s;
}
.vert-arr.sec {
  opacity: 1;
  transform: scale(1);
}

/* Red Ti ball */
.ti-ball {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  border: 2px solid #fc8181;
  background: #fc818133;
  color: #fc8181;
  display: flex;
  align-items: center;
  justify-content: center;
  font-style: italic;
  font-size: 12px;
  font-family: serif;
  opacity: 0;
  transform: scale(0);
  transition: opacity 0.35s ease, transform 0.35s ease;
}
.seq-group.shown .ti-ball {
  opacity: 1;
  transform: scale(1);
}

/* Horizontal arrows */
.arr {
  color: rgba(226,232,240,0.7);
  font-family: serif;
  font-size: 14px;
  opacity: 0;
  transform: scale(0);
  transition: opacity 0.25s ease 0.1s, transform 0.25s ease 0.1s;
}
.arr.seq {
  opacity: 1;
  transform: scale(1);
}

/* Green K and C nodes */
.k-node, .c-node {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  border: 2px solid #68d391;
  background: #68d39133;
  color: #68d391;
  display: flex;
  align-items: center;
  justify-content: center;
  font-style: italic;
  font-size: 11px;
  font-family: serif;
  flex-shrink: 0;
  opacity: 0;
  transform: scale(0);
  transition: opacity 0.3s ease, transform 0.3s ease;
}
.k-node.seq {
  opacity: 1;
  transform: scale(1);
  transition-delay: 0.3s;
}
.c-node.seq {
  opacity: 1;
  transform: scale(1);
  transition-delay: 0.4s;
}

/* Blue secondary nodes */
.sec-node {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  border: 2px solid #63b3ed;
  background: #63b3ed33;
  color: #63b3ed;
  display: flex;
  align-items: center;
  justify-content: center;
  font-style: italic;
  font-size: 10px;
  font-family: serif;
  flex-shrink: 0;
  opacity: 0;
  transform: scale(0);
  transition: opacity 0.3s ease 0.3s, transform 0.3s ease 0.3s;
}
.sec-node.sec {
  opacity: 1;
  transform: scale(1);
}

.hl-ring {
  position: absolute;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 2px dashed #94a3b8;
  transform: translate(-50%, -50%) scale(0);
  opacity: 0;
  pointer-events: none;
  transition: transform 0.4s ease, opacity 0.4s ease;
}
.hl-ring.on {
  transform: translate(-50%, -50%) scale(1);
  opacity: 1;
}

.highlight-svg {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  pointer-events: none;
  overflow: visible;
}

.hl-question {
  position: absolute;
  transform: translate(-50%, -50%);
  color: #e2e8f0;
  font-style: italic;
  font-family: serif;
  font-size: 20px;
  pointer-events: none;
}

@keyframes float {
  0%   { translate: 0px 0px; }
  25%  { translate: 7px -9px; }
  50%  { translate: -5px 7px; }
  75%  { translate: 9px 5px; }
  100% { translate: -7px -7px; }
}
</style>
