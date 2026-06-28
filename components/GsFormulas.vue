<template>
  <div style="display:flex; flex-direction:column; gap:0.6rem; font-size:0.92rem;">
    <div v-html="f1" :style="{ lineHeight: '1.6', visibility: step >= 1 ? 'visible' : 'hidden' }" />
    <div v-html="f2" :style="{ lineHeight: '1.6', visibility: step >= 2 ? 'visible' : 'hidden' }" />
    <div v-html="f3" :style="{ lineHeight: '1.6', visibility: step >= 3 ? 'visible' : 'hidden' }" />
  </div>
</template>

<script setup>
import katex from 'katex'

const props = defineProps({ step: { type: Number, default: 0 } })

const lava  = '<span style="display:inline-block;width:22px;height:22px;border-radius:50%;background:#7c1d0d;border:1.95px solid #f59e0b;vertical-align:middle;margin:0 3px;"></span>'
const green = '<span style="display:inline-block;width:22px;height:22px;border-radius:50%;background:#14532d;border:1.95px solid #4ade80;vertical-align:middle;margin:0 3px;"></span>'
const blue  = '<span style="display:inline-block;width:22px;height:22px;border-radius:50%;background:#1e3a5f;border:1.95px solid #60a5fa;vertical-align:middle;margin:0 3px;"></span>'

function m(tex) {
  return katex.renderToString(tex, { throwOnError: false, displayMode: false })
}

const f1 = m('\\operatorname{GS}^0_{\\mathcal{E}_\\diamond}(') + lava + m(') = \\operatorname{add}(') + lava + m(')')

const f2 = m('\\operatorname{GS}^1_{\\mathcal{E}_\\diamond}(') + lava + m(') = \\operatorname{add}(') + lava + m(',\\,') + green + m(')')

const f3 = m('\\operatorname{GS}_{\\mathcal{E}_\\diamond}(') + lava + m(') = \\operatorname{GS}^2_{\\mathcal{E}_\\diamond}(') + lava + m(') = \\operatorname{add}(') + lava + m(',\\,') + green + m(',\\,') + blue + m(')')
</script>
