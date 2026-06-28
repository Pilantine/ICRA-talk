<template>
  <div class="quiver-wrap">
    <svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" class="quiver-svg">
      <!-- Node 1 -->
      <circle cx="55" cy="45" r="22" class="node" :style="fade(0)" />
      <text x="55" y="51" class="node-lbl" :style="fade(0)">1</text>

      <!-- Arrow shaft -->
      <line x1="79" y1="45" x2="197" y2="45" class="arr" :style="lineAnim(200)" />
      <!-- Arrowhead -->
      <polygon points="199,39 217,45 199,51" class="head" :style="fade(680)" />

      <!-- Node 2 -->
      <circle cx="240" cy="45" r="22" class="node" :style="fade(100)" />
      <text x="240" y="51" class="node-lbl" :style="fade(100)">2</text>
    </svg>
    <div class="quiver-caption">$Q : 1 \to 2$ &nbsp;(type $A_2$)</div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const show = ref(false)
onMounted(() => setTimeout(() => { show.value = true }, 60))

const fade = (delay) => ({
  opacity: show.value ? 1 : 0,
  transition: `opacity 0.4s ease ${delay}ms`,
})

const lineAnim = (delay) => ({
  strokeDashoffset: show.value ? '0' : '118',
  transition: `stroke-dashoffset 0.55s ease ${delay}ms`,
})
</script>

<style scoped>
.quiver-wrap {
  display: inline-flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 0.3rem;
}
.quiver-svg { width: 240px; height: 72px; }

.node {
  fill: #1a2540;
  stroke: #63b3ed;
  stroke-width: 2;
}
.node-lbl {
  fill: #e2e8f0;
  font-size: 17px;
  font-family: serif;
  text-anchor: middle;
  dominant-baseline: middle;
  font-style: italic;
}
.arr {
  stroke: #e2b96f;
  stroke-width: 2;
  stroke-dasharray: 118;
  fill: none;
}
.head { fill: #e2b96f; }

.quiver-caption {
  font-size: 0.78rem;
  color: #718096;
  font-style: italic;
}
</style>
