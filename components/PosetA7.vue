<template>
  <div style="display:flex; flex-direction:column; align-items:center; padding:0.25rem 0;">
    <!-- Quiver header: Q = 1→2←3→4→5←6→7 -->
    <svg width="420" height="26" style="overflow:visible; margin-bottom:6px;">
      <defs>
        <marker id="qarr" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">
          <path d="M0,0 L0,7 L7,3.5 z" fill="#999"/>
        </marker>
      </defs>
      <text x="0"   y="18" fill="#ccc" font-size="12" font-family="serif" font-style="italic">Q =</text>
      <!-- vertices at x = 40, 90, 140, 190, 240, 290, 340 -->
      <text x="37"  y="18" fill="#e2b96f" font-size="12" font-family="serif">1</text>
      <text x="87"  y="18" fill="#e2b96f" font-size="12" font-family="serif">2</text>
      <text x="137" y="18" fill="#e2b96f" font-size="12" font-family="serif">3</text>
      <text x="187" y="18" fill="#e2b96f" font-size="12" font-family="serif">4</text>
      <text x="237" y="18" fill="#e2b96f" font-size="12" font-family="serif">5</text>
      <text x="287" y="18" fill="#e2b96f" font-size="12" font-family="serif">6</text>
      <text x="337" y="18" fill="#e2b96f" font-size="12" font-family="serif">7</text>
      <!-- 1→2 -->
      <line x1="48" y1="12" x2="81" y2="12" stroke="#999" stroke-width="1.3" marker-end="url(#qarr)"/>
      <!-- 3→2 -->
      <line x1="140" y1="12" x2="100" y2="12" stroke="#999" stroke-width="1.3" marker-end="url(#qarr)"/>
      <!-- 3→4 -->
      <line x1="148" y1="12" x2="181" y2="12" stroke="#999" stroke-width="1.3" marker-end="url(#qarr)"/>
      <!-- 4→5 -->
      <line x1="198" y1="12" x2="231" y2="12" stroke="#999" stroke-width="1.3" marker-end="url(#qarr)"/>
      <!-- 6→5 -->
      <line x1="290" y1="12" x2="250" y2="12" stroke="#999" stroke-width="1.3" marker-end="url(#qarr)"/>
      <!-- 6→7 -->
      <line x1="298" y1="12" x2="331" y2="12" stroke="#999" stroke-width="1.3" marker-end="url(#qarr)"/>
    </svg>

    <!-- Poset -->
    <svg :width="W" :height="H" :viewBox="`0 0 ${W} ${H}`" style="overflow:visible;">
      <defs>
        <marker id="pa" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M0,0 L0,5 L5,2.5 z" fill="#555"/>
        </marker>
      </defs>

      <!-- Edges -->
      <line v-for="e in edges" :key="e.id"
        :x1="P[e.a].x" :y1="P[e.a].y - R"
        :x2="P[e.b].x" :y2="P[e.b].y + R"
        stroke="#4a4a4a" stroke-width="0.8" marker-end="url(#pa)"/>

      <!-- Nodes -->
      <g v-for="n in nodes" :key="n.id">
        <circle v-if="nodeColor(n.id)"
          :cx="P[n.id].x" :cy="P[n.id].y" :r="R"
          :fill="nodeColor(n.id).fill"
          :stroke="nodeColor(n.id).stroke"
          stroke-width="1.4"
          :stroke-dasharray="nodeColor(n.id).dash || '0'"
          style="transition: opacity 0.8s ease"
          :style="{ opacity: nodeColor(n.id) ? 1 : 0 }"/>
        <text :x="P[n.id].x" :y="P[n.id].y + 3.5"
          text-anchor="middle" font-size="8.5" font-family="serif"
          :fill="nodeColor(n.id) ? '#fff' : '#888'">{{ n.label }}</text>
      </g>
    </svg>

    <!-- Legend -->
    <div style="display:flex; gap:1.2rem; margin-top:4px; font-size:0.72rem; opacity:0.8;">
      <span style="color:#f59e0b;">● seed $\mathcal{C}$</span>
      <span v-if="step >= 1" style="color:#4ade80;">● $\operatorname{GS}^1$</span>
      <span v-if="step >= 2" style="color:#60a5fa;">● $\operatorname{GS}^2$</span>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({ step: { type: Number, default: 0 } })

const R = 11   // node radius
const S = 52   // scale: pixels per TikZ unit
const OX = 65  // origin offset x
const OY = 22  // origin offset y (top = y=1 in TikZ)

const W = 550
const H = 380

// TikZ coords (x,y) — y increases upward in TikZ, downward in SVG
// SVG_x = OX + x * S,   SVG_y = OY + (1 - y) * S
function tx(x, y) { return { x: OX + x * S, y: OY + (1 - y) * S } }

const P = {
  '[2]':      tx(0, 0),
  '[1,2]':    tx(1, 1),
  '[2,5]':    tx(1,-1),
  '[4,5]':    tx(0,-2),
  '[5]':      tx(-1,-3),
  '[5,7]':    tx(0,-4),
  '[7]':      tx(-1,-5),
  '[5,6]':    tx(1,-5),
  '[4]':      tx(3,-5),
  '[2,3]':    tx(5,-5),
  '[1]':      tx(7,-5),
  '[4,6]':    tx(2,-4),
  '[2,4]':    tx(4,-4),
  '[1,3]':    tx(6,-4),
  '[4,7]':    tx(1,-3),
  '[2,6]':    tx(3,-3),
  '[1,4]':    tx(5,-3),
  '[3]':      tx(7,-3),
  '[1,5]':    tx(2, 0),
  '[2,7]':    tx(2,-2),
  '[1,6]':    tx(4,-2),
  '[3,4]':    tx(6,-2),
  '[1,7]':    tx(3,-1),
  '[3,6]':    tx(5,-1),
  '[3,7]':    tx(4, 0),
  '[6]':      tx(6, 0),
  '[3,5]':    tx(3, 1),
  '[6,7]':    tx(5, 1),
}

const nodes = Object.keys(P).map(id => ({ id, label: id }))

const edges = [
  { id:'e1',  a:'[2]',    b:'[1,2]' },
  { id:'e2',  a:'[2]',    b:'[2,5]' },
  { id:'e3',  a:'[4,5]',  b:'[2,5]' },
  { id:'e4',  a:'[1,2]',  b:'[1,5]' },
  { id:'e5',  a:'[2,5]',  b:'[1,5]' },
  { id:'e6',  a:'[2,5]',  b:'[2,7]' },
  { id:'e7',  a:'[1,5]',  b:'[3,5]' },
  { id:'e8',  a:'[5]',    b:'[4,5]' },
  { id:'e9',  a:'[7]',    b:'[5,7]' },
  { id:'e10', a:'[5,7]',  b:'[4,7]' },
  { id:'e11', a:'[4,7]',  b:'[2,7]' },
  { id:'e12', a:'[2,7]',  b:'[1,7]' },
  { id:'e13', a:'[1,7]',  b:'[3,7]' },
  { id:'e14', a:'[3,7]',  b:'[6,7]' },
  { id:'e15', a:'[5,6]',  b:'[4,6]' },
  { id:'e16', a:'[4,6]',  b:'[2,6]' },
  { id:'e17', a:'[2,6]',  b:'[1,6]' },
  { id:'e18', a:'[1,6]',  b:'[3,6]' },
  { id:'e19', a:'[3,6]',  b:'[6]' },
  { id:'e20', a:'[4]',    b:'[2,4]' },
  { id:'e21', a:'[2,4]',  b:'[1,4]' },
  { id:'e22', a:'[1,4]',  b:'[3,4]' },
  { id:'e23', a:'[2,3]',  b:'[1,3]' },
  { id:'e24', a:'[1,3]',  b:'[3]' },
  { id:'e25', a:'[5]',    b:'[5,7]' },
  { id:'e26', a:'[5,7]',  b:'[5,6]' },
  { id:'e27', a:'[4,5]',  b:'[4,7]' },
  { id:'e28', a:'[4,7]',  b:'[4,6]' },
  { id:'e29', a:'[4,6]',  b:'[4]' },
  { id:'e30', a:'[2,7]',  b:'[2,6]' },
  { id:'e31', a:'[2,6]',  b:'[2,4]' },
  { id:'e32', a:'[2,4]',  b:'[2,3]' },
  { id:'e33', a:'[1,5]',  b:'[1,7]' },
  { id:'e34', a:'[1,7]',  b:'[1,6]' },
  { id:'e35', a:'[1,6]',  b:'[1,4]' },
  { id:'e36', a:'[1,4]',  b:'[1,3]' },
  { id:'e37', a:'[1,3]',  b:'[1]' },
  { id:'e38', a:'[3,5]',  b:'[3,7]' },
  { id:'e39', a:'[3,7]',  b:'[3,6]' },
  { id:'e40', a:'[3,6]',  b:'[3,4]' },
  { id:'e41', a:'[3,4]',  b:'[3]' },
  { id:'e42', a:'[6,7]',  b:'[6]' },
]

// Color by step
const lava  = new Set(['[5]','[5,7]','[5,6]','[2,3]','[1,3]','[1,5]','[3,5]'])
const green = new Set(['[2,5]','[3]','[1,6]','[1,7]','[3,6]','[3,7]'])
const blue  = new Set(['[2,6]','[2,7]'])

function nodeColor(id) {
  if (lava.has(id))
    return { fill: '#7c1d0d', stroke: '#f59e0b', dash: '0' }
  if (props.step >= 1 && green.has(id))
    return { fill: '#14532d', stroke: '#4ade80', dash: '0' }
  if (props.step >= 2 && blue.has(id))
    return { fill: '#1e3a5f', stroke: '#60a5fa', dash: '4 2' }
  return null
}
</script>
