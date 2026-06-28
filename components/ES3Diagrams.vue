<template>
  <div style="display:flex; gap:2.5rem; justify-content:center; align-items:flex-start; margin-top:0.3rem;">

    <!-- ES3-I: Pushout -->
    <div style="display:flex; flex-direction:column; align-items:center; gap:5px;">
      <div style="font-size:0.78rem; color:#a0aec0;">
        <strong style="color:#63b3ed;">(ES3-I)</strong> Pushout
      </div>
      <svg viewBox="0 0 290 118" width="272" height="111" style="overflow:visible;">
        <defs>
          <!-- Standard stealth end arrow -->
          <marker id="po-arr" markerWidth="8" markerHeight="7" refX="7" refY="3.5" orient="auto">
            <path d="M0,0 L7,3.5 L0,7 L2,3.5 Z" fill="#94a3b8"/>
          </marker>
          <!-- Monomorphism: small stealth tail (same shape, smaller, placed before line) -->
          <marker id="po-tail" markerWidth="7" markerHeight="6" refX="4.5" refY="3" orient="auto">
            <path d="M0,0 L4.5,3 L0,6 L1.4,3 Z" fill="#94a3b8"/>
          </marker>
          <!-- Epimorphism: double stealth head -->
          <marker id="po-epi" markerWidth="11" markerHeight="7" refX="10" refY="3.5" orient="auto">
            <path d="M0,0 L5,3.5 L0,7 L1.5,3.5 Z" fill="#94a3b8"/>
            <path d="M4,0 L9,3.5 L4,7 L5.5,3.5 Z" fill="#94a3b8"/>
          </marker>
        </defs>

        <!-- Row 1: y=30 -->
        <text x="8"   y="33" v-bind="obj">0</text>
        <text x="54"  y="33" v-bind="obj">X</text>
        <text x="144" y="33" v-bind="obj">Y</text>
        <text x="222" y="33" v-bind="obj">Z</text>
        <text x="278" y="33" v-bind="obj">0</text>

        <!-- Row 2: y=90 -->
        <text x="8"   y="93" v-bind="obj">0</text>
        <text x="54"  y="93" v-bind="obj">D</text>
        <!-- PO highlighted -->
        <rect x="131" y="80" width="27" height="16" fill="rgba(99,179,237,0.15)" rx="3"/>
        <text x="144" y="93" v-bind="obj" fill="#63b3ed" font-weight="700" font-style="normal">PO</text>
        <text x="222" y="93" v-bind="obj">Z</text>
        <text x="278" y="93" v-bind="obj">0</text>

        <!-- Row 1 horizontal arrows -->
        <line x1="18"  y1="29" x2="45"  y2="29" v-bind="edg" marker-end="url(#po-arr)"/>
        <line x1="64"  y1="29" x2="130" y2="29" v-bind="edg" marker-start="url(#po-tail)" marker-end="url(#po-arr)"/>
        <text x="97" y="22" v-bind="lbl">f</text>
        <line x1="153" y1="29" x2="213" y2="29" v-bind="edg" marker-end="url(#po-epi)"/>
        <line x1="232" y1="29" x2="269" y2="29" v-bind="edg" marker-end="url(#po-arr)"/>

        <!-- Row 2 horizontal arrows -->
        <line x1="18"  y1="89" x2="45"  y2="89" v-bind="edg" marker-end="url(#po-arr)"/>
        <line x1="64"  y1="89" x2="128" y2="89" v-bind="edg" marker-start="url(#po-tail)" marker-end="url(#po-arr)"/>
        <line x1="157" y1="89" x2="213" y2="89" v-bind="edg" marker-end="url(#po-epi)"/>
        <line x1="232" y1="89" x2="269" y2="89" v-bind="edg" marker-end="url(#po-arr)"/>

        <!-- Vertical: X →h D -->
        <line x1="54" y1="39" x2="54" y2="78" v-bind="edg" marker-end="url(#po-arr)"/>
        <text x="60" y="62" v-bind="lbl">h</text>
        <!-- Vertical: Y → PO -->
        <line x1="144" y1="39" x2="144" y2="78" v-bind="edg" marker-end="url(#po-arr)"/>
        <!-- Vertical: Z = Z (double line, identity) -->
        <line x1="219" y1="39" x2="219" y2="78" stroke="#94a3b8" stroke-width="1.1"/>
        <line x1="225" y1="39" x2="225" y2="78" stroke="#94a3b8" stroke-width="1.1"/>

        <!-- PO corner mark (upper-left of PO node) -->
        <polyline points="128,89 128,75 144,75" stroke="#63b3ed" stroke-width="1.3" fill="none"/>
      </svg>
      <div style="font-size:0.72rem; color:#718096; font-style:italic;">
        Closed under pushouts.
      </div>
    </div>

    <!-- ES3-II: Pullback -->
    <div style="display:flex; flex-direction:column; align-items:center; gap:5px;">
      <div style="font-size:0.78rem; color:#a0aec0;">
        <strong style="color:#b794f4;">(ES3-II)</strong> Pullback
      </div>
      <svg viewBox="0 0 290 118" width="272" height="111" style="overflow:visible;">
        <defs>
          <marker id="pb-arr" markerWidth="8" markerHeight="7" refX="7" refY="3.5" orient="auto">
            <path d="M0,0 L7,3.5 L0,7 L2,3.5 Z" fill="#94a3b8"/>
          </marker>
          <marker id="pb-tail" markerWidth="7" markerHeight="6" refX="4.5" refY="3" orient="auto">
            <path d="M0,0 L4.5,3 L0,6 L1.4,3 Z" fill="#94a3b8"/>
          </marker>
          <marker id="pb-epi" markerWidth="11" markerHeight="7" refX="10" refY="3.5" orient="auto">
            <path d="M0,0 L5,3.5 L0,7 L1.5,3.5 Z" fill="#94a3b8"/>
            <path d="M4,0 L9,3.5 L4,7 L5.5,3.5 Z" fill="#94a3b8"/>
          </marker>
        </defs>

        <!-- Row 1: y=30 -->
        <text x="8"   y="33" v-bind="obj">0</text>
        <text x="54"  y="33" v-bind="obj">X</text>
        <text x="144" y="33" v-bind="obj">Y</text>
        <text x="222" y="33" v-bind="obj">Z</text>
        <text x="278" y="33" v-bind="obj">0</text>

        <!-- Row 2: y=90 -->
        <text x="8"   y="93" v-bind="obj">0</text>
        <text x="54"  y="93" v-bind="obj">X</text>
        <!-- PB highlighted -->
        <rect x="131" y="80" width="28" height="16" fill="rgba(183,148,244,0.15)" rx="3"/>
        <text x="144" y="93" v-bind="obj" fill="#b794f4" font-weight="700" font-style="normal">PB</text>
        <text x="222" y="93" v-bind="obj">F</text>
        <text x="278" y="93" v-bind="obj">0</text>

        <!-- Row 1 horizontal arrows -->
        <line x1="18"  y1="29" x2="45"  y2="29" v-bind="edg" marker-end="url(#pb-arr)"/>
        <line x1="64"  y1="29" x2="130" y2="29" v-bind="edg" marker-start="url(#pb-tail)" marker-end="url(#pb-arr)"/>
        <line x1="153" y1="29" x2="213" y2="29" v-bind="edg" marker-end="url(#pb-epi)"/>
        <text x="181" y="22" v-bind="lbl">g</text>
        <line x1="232" y1="29" x2="269" y2="29" v-bind="edg" marker-end="url(#pb-arr)"/>

        <!-- Row 2 horizontal arrows -->
        <line x1="18"  y1="89" x2="45"  y2="89" v-bind="edg" marker-end="url(#pb-arr)"/>
        <line x1="64"  y1="89" x2="128" y2="89" v-bind="edg" marker-start="url(#pb-tail)" marker-end="url(#pb-arr)"/>
        <line x1="157" y1="89" x2="213" y2="89" v-bind="edg" marker-end="url(#pb-epi)"/>
        <line x1="232" y1="89" x2="269" y2="89" v-bind="edg" marker-end="url(#pb-arr)"/>

        <!-- Vertical: X = X (identity, double line going down) -->
        <line x1="51" y1="39" x2="51" y2="78" stroke="#94a3b8" stroke-width="1.1"/>
        <line x1="57" y1="39" x2="57" y2="78" stroke="#94a3b8" stroke-width="1.1"/>

        <!-- Vertical: PB → Y (upward arrow) -->
        <line x1="144" y1="78" x2="144" y2="39" v-bind="edg" marker-end="url(#pb-arr)"/>

        <!-- Vertical: F →h' Z (upward arrow) -->
        <line x1="222" y1="78" x2="222" y2="39" v-bind="edg" marker-end="url(#pb-arr)"/>
        <text x="231" y="62" v-bind="lbl">h'</text>

        <!-- PB corner mark (upper-right of PB node) -->
        <polyline points="160,89 160,75 144,75" stroke="#b794f4" stroke-width="1.3" fill="none"/>
      </svg>
      <div style="font-size:0.72rem; color:#718096; font-style:italic;">
        Closed under pullbacks.
      </div>
    </div>

  </div>
</template>

<script setup>
const obj = {
  fill: '#e2e8f0',
  'font-size': '13',
  'font-family': 'serif',
  'font-style': 'italic',
  'text-anchor': 'middle',
}

const edg = {
  stroke: '#94a3b8',
  'stroke-width': '1.4',
}

const lbl = {
  fill: '#e2b96f',
  'font-size': '11',
  'font-family': 'serif',
  'font-style': 'italic',
  'text-anchor': 'middle',
}
</script>
