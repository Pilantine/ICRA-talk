<template>
  <div class="diag-wrap">
    <div class="diag-title">Pushout axiom (ES3-I)</div>
    <svg viewBox="0 0 230 195" xmlns="http://www.w3.org/2000/svg" class="diag-svg">

      <!-- Objects -->
      <text x="35"  y="42"  class="obj"     :style="fade(0)">X</text>
      <text x="195" y="42"  class="obj"     :style="fade(50)">Y</text>
      <text x="35"  y="162" class="obj"     :style="fade(400)">D</text>
      <text x="190" y="162" class="obj po"  :style="fade(450)">PO</text>

      <!-- X → Y  (top, label f) -->
      <line x1="52"  y1="37" x2="178" y2="37" class="arr"      :style="lineAnim(100)" />
      <polygon points="180,31 195,37 180,43" class="head"        :style="fade(580)" />
      <text x="115" y="26"  class="lbl"      :style="fade(200)">f</text>

      <!-- X → D  (left, label g) -->
      <line x1="35"  y1="55" x2="35"  y2="143" class="arr"     :style="lineAnim(150)" />
      <polygon points="29,145 35,160 41,145"   class="head"     :style="fade(610)" />
      <text x="20"  y="102" class="lbl"        :style="fade(250)">g</text>

      <!-- Y → PO (right, label g', push color) -->
      <line x1="195" y1="55" x2="195" y2="143" class="arr push":style="lineAnim(250)" />
      <polygon points="189,145 195,160 201,145" class="head-push":style="fade(680)" />
      <text x="212" y="102" class="lbl push-lbl":style="fade(350)">g'</text>

      <!-- D → PO (bottom, push color) -->
      <line x1="52"  y1="157" x2="176" y2="157" class="arr push":style="lineAnim(350)" />
      <polygon points="178,151 193,157 178,163" class="head-push":style="fade(750)" />

      <!-- Pushout corner mark -->
      <polyline points="178,157 178,170 191,170" class="po-mark" :style="fade(800)" />

    </svg>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const show = ref(false)
onMounted(() => setTimeout(() => { show.value = true }, 60))

const fade = (delay) => ({
  opacity: show.value ? 1 : 0,
  transition: `opacity 0.35s ease ${delay}ms`,
})

const lineAnim = (delay) => ({
  strokeDashoffset: show.value ? '0' : '200',
  transition: `stroke-dashoffset 0.5s ease ${delay}ms`,
})
</script>

<style scoped>
.diag-wrap { display: inline-flex; flex-direction: column; gap: 0.2rem; }
.diag-title { font-size: 0.78rem; color: #718096; font-style: italic; }
.diag-svg   { width: 210px; height: 180px; }

.obj {
  fill: #e2e8f0; font-size: 18px; font-family: serif;
  text-anchor: middle; dominant-baseline: middle; font-style: italic;
}
.po { fill: #63b3ed; font-weight: bold; }

.lbl {
  fill: #e2b96f; font-size: 13px; font-family: serif;
  text-anchor: middle; dominant-baseline: middle; font-style: italic;
}
.push-lbl { fill: #63b3ed; }

.arr {
  stroke: #718096; stroke-width: 1.8;
  stroke-dasharray: 200; fill: none;
}
.push { stroke: #63b3ed; }

.head      { fill: #718096; }
.head-push { fill: #63b3ed; }

.po-mark { stroke: #63b3ed; stroke-width: 1.8; fill: none; }
</style>
