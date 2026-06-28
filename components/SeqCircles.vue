<template>
  <span class="seq-line">
    <span class="node" :style="leftStyle">{{ left }}</span>
    <span class="arr">→</span>
    <span class="node" :style="midStyle">{{ mid }}</span>
    <span class="arr">→</span>
    <span class="node" :style="rightStyle">{{ right }}</span>
  </span>
</template>

<script setup>
const props = defineProps({
  left:      { type: String, default: 'Kᵢ' },
  mid:       { type: String, default: 'Tᵢ' },
  right:     { type: String, default: 'Cᵢ' },
  leftColor: { type: String, default: '#68d391' },
  midColor:  { type: String, default: '#fc8181' },
  rightColor:{ type: String, default: '#68d391' },
  midSize:   { type: String, default: '30px' },
  sideSize:  { type: String, default: '22px' },
})

function nodeStyle(color, size) {
  return {
    width: size, height: size,
    borderColor: color,
    background: color + '22',
    color,
    fontSize: size === '30px' ? '12px' : '10px',
  }
}

const leftStyle  = computed(() => nodeStyle(props.leftColor,  props.sideSize))
const midStyle   = computed(() => nodeStyle(props.midColor,   props.midSize))
const rightStyle = computed(() => nodeStyle(props.rightColor, props.sideSize))
</script>

<script>
import { computed } from 'vue'
</script>

<style scoped>
.seq-line {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 0.9rem;
}
.arr {
  color: #e2e8f0;
  font-family: serif;
}
.node {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  border: 2px solid;
  font-style: italic;
  font-family: serif;
  flex-shrink: 0;
}
</style>
