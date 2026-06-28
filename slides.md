---
theme: seriph
colorSchema: dark
title: On the E_diamond exact structure
author: Sunny Roy
transition: slide-left
mdc: true
katex:
  macros:
    "\\rep": "\\operatorname{rep}"
    "\\Cat": "\\operatorname{Cat}"
    "\\Int": "\\operatorname{Int}"
    "\\GenJF": "\\operatorname{GenJF}"
    "\\GenRep": "\\operatorname{GenRep}"
    "\\JF": "\\operatorname{JF}"
    "\\add": "\\operatorname{add}"
    "\\Ker": "\\operatorname{Ker}"
    "\\Coker": "\\operatorname{Coker}"
    "\\Hom": "\\operatorname{Hom}"
    "\\Id": "\\operatorname{Id}"
    "\\ind": "\\operatorname{ind}"
    "\\NEnd": "\\operatorname{NEnd}"
    "\\End": "\\operatorname{End}"
    "\\Ext": "\\operatorname{Ext}"
    "\\supp": "\\operatorname{supp}"
    "\\Tilt": "\\operatorname{Tilt}"
    "\\Gen": "\\operatorname{Gen}"
    "\\Sub": "\\operatorname{Sub}"
    "\\GS": "\\operatorname{GS}"
    "\\SG": "\\operatorname{SG}"
    "\\Ind": "\\operatorname{Ind}"
    "\\Supp": "\\operatorname{Supp}"
    "\\GL": "\\operatorname{GL}"
    "\\pdim": "\\operatorname{pdim}"
    "\\proj": "\\operatorname{proj}"
    "\\inj": "\\operatorname{inj}"
    "\\Rad": "\\operatorname{Rad}"
    "\\AR": "\\operatorname{AR}"
    "\\Mult": "\\operatorname{Mult}"
    "\\Mat": "\\operatorname{Mat}"
    "\\llrr": "\\llbracket #1 \\rrbracket"
---

# <span style="line-height:1.1; display:block; margin-bottom:1.5rem">Exact structures and maximal canonically Jordan recoverable subcategories for modules over type A algebras</span>

<div style="font-size:1.1rem; margin-top:1.5rem; opacity:0.85">Joint work with Benjamin Dequêne</div>

<div style="margin-top:1.5rem; opacity:0.7; font-size:0.9rem">
  ICRA 2026 — Institut Fourier, Grenoble, France<br/>
  June 29, 2026
</div>


---

# Plan

<v-clicks>

1. **Motivation** &nbsp;: Canonical Jordan Recoverability

2. **The Diamond Exact Structure** $\mathcal{E}_\diamond$

3. **The $\mathrm{GS}_\mathcal{E}$ Operator & Properties** &nbsp;*(First Main Theorem)* &nbsp;<span style="color:white; opacity:0.55; font-size:0.85em">\[Dequêne–R., 2025\]</span>

4. **Relative Mutations & Tilting Equivalence** &nbsp;*(Second Main Theorem)* &nbsp;<span style="color:white; opacity:0.55; font-size:0.85em">\[Dequêne–R., 2025\]</span>

</v-clicks>

---

# Settings

<v-clicks>

- $K$ is an algebraically closed field.

- $Q$ is a **Dynkin quiver** with no relations.

- $\operatorname{rep}(Q)$ denotes the category of finite-dimensional left $KQ$-modules.

- $\mathscr{A}$ will denote a **hereditary abelian category with enough projectives**.

- All subcategories are assumed full, closed under finite direct sums, and under direct summands.

</v-clicks>

---
layout: section
class: text-center
---

# I. Motivation

Canonical Jordan Recoverability

---

# Jordan Form Invariant

<div>In representation theory, we often seek <strong>invariants</strong> that classify objects up to isomorphism.</div>

<v-clicks>

<div class="mt-3">
The <strong>Jordan form</strong> is one of the simplest and most classical invariants attached to endomorphisms. It encodes essential structural information.
</div>

<div class="callout-question mt-4">
  <strong>Question</strong> &nbsp;— Can a representation be recovered from the Jordan forms of its nilpotent endomorphisms?
</div>

<div class="mt-4" style="font-size:0.88rem; opacity:0.85">
In recent work, <strong>Garver–Patrias–Thomas</strong> (2018–2022) introduced and developed the notions of <em>Jordan recoverability (JR)</em> and <em>canonical Jordan recoverability (CJR)</em>. These ideas were later expanded by <strong>Dequêne</strong> (2022–2024).
</div>

</v-clicks>

---

# Jordan Form for Representations

Let $E = (E_q, E_\alpha) \in \operatorname{rep}(Q)$ and $N = (N_q)_{q \in Q_0} \in \operatorname{NEnd}(E)$. Each $N_q$ is a nilpotent endomorphism of $E_q$.

<div class="definition mt-6" v-click>

**Definition**

The **Jordan form** of $N_q$ is the partition $\operatorname{JF}(N_q) \vdash \dim(E_q)$ recording its Jordan block sizes. Define the tuple

$$\operatorname{JF}(N) = \bigl(\operatorname{JF}(N_q)\bigr)_{q \in Q_0},$$

which describes the block structure of $N$ at each vertex.

</div>

---

# The Generic Jordan Form Invariant

Fix $E \in \operatorname{rep}(Q)$. For $N = (N_q)_{q \in Q_0} \in \operatorname{NEnd}(E)$, set $\operatorname{JF}(N) = (\operatorname{JF}(N_q))_{q \in Q_0}$.

<div class="definition mt-5" v-click>

**Definition \[GPT23\]**

The **generic Jordan form** of $E$ is the maximal value with respect to dominance order:

$$\operatorname{GenJF}(E) \;=\; \max_{N \,\in\, \operatorname{NEnd}(E)} \operatorname{JF}(N).$$

</div>

<div class="callout-question mt-5" v-click>

**Question** &nbsp;— Is this invariant complete?

</div>

---

# Jordan Recoverability

<div class="definition mt-2">

**Definition \[GPT23\]**

Let $\mathscr{C} \subseteq \operatorname{rep}(Q)$ be a full subcategory. We say that $\mathscr{C}$ is **Jordan recoverable (JR)** if

$$E \simeq F \;\iff\; \operatorname{GenJF}(E) = \operatorname{GenJF}(F) \qquad \text{for all } E, F \in \mathscr{C}.$$

</div>

<div class="remark mt-5" v-click>

**Remark**

The generic Jordan form $\operatorname{GenJF}$ is a **complete invariant** on $\mathscr{C}$.

</div>

---

# Canonical Jordan Recoverability (CJR)

<div class="definition">

**Definition \[GPT23\]**

Let $\mathscr{C} \subseteq \operatorname{rep}(Q)$. We say $\mathscr{C}$ is **canonically Jordan recoverable (CJR)** if, for every $X \in \mathscr{C}$, there exists a dense open set (Zariski) $\Omega \subseteq \operatorname{rep}\bigl(Q,\operatorname{GenJF}(X)\bigr)$ such that for all $Y \in \Omega$, $Y \simeq X$.

</div>

<div class="definition mt-5" v-click>

**Maximal CJR subcategory**

A CJR subcategory $\mathscr{C}$ is **maximal** if it is not properly contained in any larger CJR subcategory of $\operatorname{rep}(Q)$:

$$\forall\, \mathscr{D} \supsetneq \mathscr{C}, \quad \mathscr{D} \text{ is not CJR.}$$

</div>

---
layout: two-cols
---

# Example on $A_2$: JR but not CJR

Assume $Q : 1 \to 2$ and let $\mathscr{C} = \operatorname{add}(S_1, S_2)$.

<v-clicks>

Every $E \in \mathscr{C}$ has the form $\;E = K^a \xrightarrow{\;0\;} K^b$.

**Generic Jordan form:** $\;\operatorname{GenJF}(E) = \bigl((a),\,(b)\bigr).$

Hence $\mathscr{C}$ is **JR**.

</v-clicks>

::right::

<div class="mt-16" v-click>

**But $\mathscr{C}$ is not CJR.**

Consider $S_1 \oplus S_2 \cong K \xrightarrow{0} K$. Any dense open $U \subseteq \operatorname{rep}(Q,\,(1,1))$ contains $P_1 = K \xrightarrow{\lambda} K$ with $\lambda \neq 0$.

$$\operatorname{GenJF}(S_1 \oplus S_2) = \bigl((1),(1)\bigr) = \operatorname{GenJF}(P_1)$$

but $S_1 \oplus S_2 \not\simeq P_1$.

</div>

---

# Maximal CJR Subcategories in Type $A_n$

Let $Q$ be a quiver of type $A_n$.

<div class="proposition mt-4">

**Proposition**

If $\mathscr{C} \subseteq \operatorname{rep}(Q)$ is a maximal canonically Jordan recoverable subcategory, then:

<v-clicks>

<em>(a)</em> $\mathscr{C}$ is extension-closed;

<em>(b)</em> $\mathscr{C}$ always contains a tilting representation.

</v-clicks>

</div>

<div class="theorem mt-4" v-click>

**Theorem \[Deq23a\]**

A subcategory $\mathscr{C} \subseteq \operatorname{rep}(Q)$ is canonically Jordan recoverable if and only if every non-split short exact sequence

$$0 \longrightarrow X \longrightarrow Y \longrightarrow Z \longrightarrow 0$$

with $X, Z \in \mathscr{C}$ satisfies $Y \notin \operatorname{ind}\bigl(\operatorname{rep}(Q)\bigr)$.

</div>

---
layout: section
class: text-center
---

# II. The Diamond Exact Structure

$\mathcal{E}_\diamond$

---

# Exact Structures

<div class="definition">

**Definition**

A collection $\mathcal{E}$ of short exact sequences in $\mathscr{A}$ is an **exact structure** on $\mathscr{A}$ whenever $\mathcal{E}$ satisfies:

</div>

<v-clicks>

<div class="axiom mt-3">

<strong>(ES1)</strong> &nbsp; All split short exact sequences are in $\mathcal{E}$.

</div>

<div class="axiom">

<strong>(ES2)</strong> &nbsp; The collection of $\mathcal{E}$-monomorphisms and the one of $\mathcal{E}$-epimorphisms are both closed under compositions.

</div>

<div class="axiom">

<strong>(ES3)</strong> &nbsp; $\mathcal{E}$ is closed under pushouts and pullbacks along any morphism.

</div>

</v-clicks>

<div style="display:flex; justify-content:center; gap:3rem; margin-top:0.8rem;">
  <div v-click style="display:flex; flex-direction:column; align-items:center; gap:0.4rem;">
    <AnimatedSVG :src="'/es3_pushout.svg'" viewBox="22 180 146 43" />
    <span><strong>(ES3-I)</strong> Pushouts</span>

$\mathcal{E}$ is closed under pushouts.

  </div>
  <div v-click style="display:flex; flex-direction:column; align-items:center; gap:0.4rem;">
    <AnimatedSVG :src="'/es3_pullback.svg'" viewBox="191 178 146 43" />
    <span><strong>(ES3-II)</strong> Pullbacks</span>

$\mathcal{E}$ is closed under pullbacks.

  </div>
</div>

---

# Exact Categories

<div class="definition">

**Definition**

Let $\mathcal{E}$ be an exact structure on $\mathscr{A}$. The pair $(\mathscr{A},\,\mathcal{E})$ is called an **exact category**.

</div>

<div class="mt-5" v-click><strong>Examples of Exact Structures</strong></div>

<v-clicks>

<div class="example">

$\mathcal{E}_{\max}$ &nbsp;— the <strong>maximal exact structure</strong>, containing all short exact sequences.

</div>

<div class="example">

$\mathcal{E}_{\min}$ &nbsp;— the <strong>minimal exact structure</strong>, containing only the split short exact sequences.

</div>

</v-clicks>

---

# Short Exact Sequences in Type $A_n$

<div class="theorem mt-4">

**Theorem**

Let $Q$ be an $A_n$ type quiver. For a non-split exact sequence

$$0 \longrightarrow D \longrightarrow E \longrightarrow F \longrightarrow 0, \qquad D, F \in \operatorname{ind}(\operatorname{rep}(Q)),$$

exactly one of the following holds:

</div>

<v-clicks>

<div class="mt-3 ml-6">

<em>(a)</em> $E \in \operatorname{ind}(\operatorname{rep}(Q))$,

</div>

<div class="ml-6">

<em>(b)</em> $E \cong E_1 \oplus E_2$ with $E_1, E_2 \in \operatorname{ind}(\operatorname{rep}(Q))$.

</div>

<div class="mt-4">

In case (b) we call it a <strong>diamond exact sequence</strong>.

</div>

</v-clicks>

---

# The Diamond Exact Structure $\mathcal{E}_\diamond$

<div class="definition mt-4">

**Definition**

Let $Q$ be an $A_n$ type quiver. We define the collection of short exact sequences $\mathcal{E}_{\diamond}$ given by the additive bifunctor $\mathcal{E}_\diamond(-,-)$, uniquely determined by

$$\mathcal{E}_\diamond(N,M) = \bigl\{\, \eta \in \operatorname{Ext}^1(N,M) \;\big|\; \eta \text{ splits or is a diamond exact sequence}\,\bigr\}$$

for $M, N \in \operatorname{ind}(\operatorname{rep}(Q))$.

</div>

<div class="proposition mt-5" v-click>

**Proposition \[Brüstle–Hanson–R.–Schiffler, 2024\]**

Let $n \in \mathbb{N}^*$ and $Q$ be an $A_n$ type quiver. Then $\mathcal{E}_{\diamond}$ is an exact structure on $\mathscr{A} = \operatorname{rep}(Q)$.

</div>

---

# CJR via $\mathcal{E}_\diamond$

<v-clicks>

::div{class="theorem mt-2"}
**Recall** &nbsp;&#91;Deq23a&#93; &nbsp;A subcategory $\mathscr{C} \subseteq \operatorname{rep}(Q)$ is <span style="color:#63b3ed">canonically Jordan recoverable</span> if and only if every non-split short exact sequence $0 \to X \to Y \to Z \to 0$ with $X, Z \in \mathscr{C}$ satisfies $Y \notin \operatorname{ind}(\operatorname{rep}(Q))$.
::

::div{class="definition mt-5"}
**Definition** &nbsp;Let $(\mathscr{A}, \mathcal{E})$ be an exact category.

A subcategory $\mathscr{C} \subseteq \mathscr{A}$ is **$\mathcal{E}$-adapted** if for all $X, Y \in \mathscr{C}$, $\operatorname{Ext}^1(X, Y) \subseteq \mathcal{E}$.
::

::div{class="theorem mt-5"}
**Theorem** &nbsp;&#91;BR25&#93; &nbsp;A subcategory $\mathscr{C} \subseteq \operatorname{rep}(A_n)$ is <span style="color:#63b3ed">canonically Jordan recoverable</span> if and only if $\mathscr{C}$ is $\mathcal{E}_\diamond$-adapted.
::

::div{class="remark mt-4"}
**Remark** &nbsp;$\mathscr{C}$ is <span style="color:#63b3ed">maximal canonically Jordan recoverable</span> if and only if any subcategory $\mathscr{D} \supset \mathscr{C}$ is not $\mathcal{E}_\diamond$-adapted.
::

</v-clicks>

---
layout: section
class: text-center
---

# III. The $\mathrm{GS}_\mathcal{E}$ Operator & Properties

First Main Theorem

---
clicks: 16
---

# The Main Intuition

::div{class="theorem mt-4"}
**Recall** &nbsp;Assume $\mathscr{C} \subseteq \operatorname{rep}(A_n)$ is a maximal CJR subcategory. Then:

<div v-click>

a) $\mathscr{C}$ is maximally $\mathcal{E}_\diamond$-adapted.

</div>

<div v-click>

b) $\mathscr{C}$ is extension closed.

</div>

<div v-click>

c) $\mathscr{C}$ contains a tilting module $T$.

</div>
::

<div class="mt-6">
  <FloatingBalls :visible="Math.max(0, $clicks - 3)" :seq-visible="Math.max(0, $clicks - 8)" :sec-visible="Math.max(0, $clicks - 13)" :highlight="$clicks >= 16" />
</div>

::div{v-click="8" style="position:absolute; bottom:2rem; left:calc(8rem - 30px); font-style:italic; font-size:1rem; color:#fc8181; display:flex; align-items:center; height:34px;"}
$T_i \in \operatorname{add}(T)$
::

::div{style="position:absolute; bottom:2rem; left:calc(18rem - 30px); display:flex; align-items:center; height:34px; gap:6px; font-size:0.9rem;"}
<span :style="{ opacity: $clicks >= 13 ? 1 : 0, transition: 'opacity 0.6s ease' }">$0 \to$ <SeqCircles /> $\to 0$</span><span :style="{ opacity: $clicks >= 15 ? 0 : ($clicks >= 13 ? 1 : 0), transition: $clicks >= 15 ? 'none' : 'opacity 0.6s ease', pointerEvents: 'none', width: $clicks >= 15 ? '0' : 'auto', overflow: 'hidden', display: 'inline-block' }">$\ \in \mathcal{E}_\diamond$</span><span :style="{ opacity: $clicks >= 15 ? 1 : 0, transition: 'opacity 0.6s ease 0.05s', marginLeft: '-6px' }">$,\quad 0 \to$ <SeqCircles left="K'₂" mid="C₂" right="C'₂" left-color="#63b3ed" mid-color="#68d391" right-color="#63b3ed" /> $\to 0\,,\quad 0 \to$ <SeqCircles left="K'₄" mid="K₄" right="C'₄" left-color="#63b3ed" mid-color="#68d391" right-color="#63b3ed" /> $\to 0\ \in \mathcal{E}_\diamond$</span>
::

---

# The $\operatorname{Gen}_\mathcal{E}$ and $\operatorname{Sub}_\mathcal{E}$ Operators

Let $(\mathscr{A}, \mathcal{E})$ be an exact category.

<div class="definition mt-4">

**Definition**

For a subcategory $\mathscr{C} \subseteq \mathscr{A}$, we define:

<v-clicks>

<div class="mt-3">

<em>(a)</em> &nbsp; $\operatorname{Gen}_{\mathcal{E}}(\mathscr{C}) = \{ C \in \mathscr{A} \mid \exists\, g : Y \twoheadrightarrow C,\; Y \in \mathscr{C},\; g\ \mathcal{E}\text{-epi} \}$

</div>

<div class="mt-2">

<em>(b)</em> &nbsp; $\operatorname{Sub}_{\mathcal{E}}(\mathscr{C}) = \{ K \in \mathscr{A} \mid \exists\, f : K \rightarrowtail Y,\; Y \in \mathscr{C},\; f\ \mathcal{E}\text{-mono} \}$

</div>

</v-clicks>

</div>

<div class="mt-4 opacity-80" v-click>

For an object $M \in \mathscr{A}$, we set $\operatorname{Gen}_\mathcal{E}(M) = \operatorname{Gen}_\mathcal{E}(\operatorname{add}(M))$ and $\operatorname{Sub}_\mathcal{E}(M) = \operatorname{Sub}_\mathcal{E}(\operatorname{add}(M))$.

</div>

---

# The $\operatorname{GS}_\mathcal{E}$ Construction

<div class="definition mt-4">

**Definition**

Let $\mathscr{C} \subseteq \mathscr{A}$ be a subcategory.

<v-clicks>

<div class="mt-3">

<em>(a)</em> &nbsp; Set $\operatorname{GS}_{\mathcal{E}}^0(\mathscr{C}) = \mathscr{C}$.

</div>

<div class="mt-2">

<em>(b)</em> &nbsp; For $i \geq 1$, define

$$\operatorname{GS}_\mathcal{E}^i(\mathscr{C}) = \operatorname{add}\!\Bigl(\operatorname{Gen}_\mathcal{E}(\operatorname{GS}_\mathcal{E}^{i-1}(\mathscr{C})) \;,\; \operatorname{Sub}_\mathcal{E}(\operatorname{GS}_\mathcal{E}^{i-1}(\mathscr{C}))\Bigr).$$

</div>

</v-clicks>

</div>

<div class="remark mt-4" v-click>

<strong>Remark.</strong> $(\operatorname{GS}_\mathcal{E}^i(\mathscr{C}))_{i \in \mathbb{N}}$ is an increasing sequence of subcategories of $\mathscr{A}$.

</div>

---

# The $\operatorname{GS}_\mathcal{E}$ Operator

<div class="definition mt-4">

**Definition**

The $\operatorname{GS}_\mathcal{E}$-operator is defined by

$$\operatorname{GS}_\mathcal{E}(\mathscr{C}) = \varinjlim_{i \in \mathbb{N}} \operatorname{GS}_\mathcal{E}^i(\mathscr{C}) = \bigcup_{i \in \mathbb{N}} \operatorname{GS}_\mathcal{E}^i(\mathscr{C}).$$

</div>

<div class="mt-4" v-click>

Equivalently, $\operatorname{GS}_\mathcal{E}(\mathscr{C})$ is the <strong>smallest subcategory</strong> of $\mathscr{A}$ that contains $\mathscr{C}$ and is closed under both $\operatorname{Gen}_\mathcal{E}$ and $\operatorname{Sub}_\mathcal{E}$.

</div>

<div class="mt-4 opacity-80" v-click>

For an object $M \in \mathscr{A}$, we set $\operatorname{GS}_\mathcal{E}(M) = \operatorname{GS}_\mathcal{E}(\operatorname{add}(M))$.

</div>

---

# Example: $\operatorname{GS}_{\mathcal{E}_\diamond}$ on $A_7$

<div style="position:relative; margin-left:-16rem; width:calc(100% + 16rem);">
  <PausableVideo src="/poset_full_anim.webm" :pausePoints="[2.5, 6.7, 13.1, 17.3, 23.8, 28.0, 34.5, 38.7, 45.2, 49.4, 55.9, 60.1, 66.6, 70.8, 77.3, 81.5, 88.0]" :playbackRate="1.5" />

</div>

<span v-click="1" data-video-trigger />
<span v-click="2" data-video-trigger />
<span v-click="3" data-video-trigger />
<span v-click="4" data-video-trigger />
<span v-click="5" data-video-trigger />
<span v-click="6" data-video-trigger />
<span v-click="7" data-video-trigger />
<span v-click="8" data-video-trigger />
<span v-click="9" data-video-trigger />
<span v-click="10" data-video-trigger />
<span v-click="11" data-video-trigger />
<span v-click="12" data-video-trigger />
<span v-click="13" data-video-trigger />
<span v-click="14" data-video-trigger />
<span v-click="15" data-video-trigger />
<span v-click="16" data-video-trigger />
<span v-click="17" data-video-trigger />
<span v-click="18" />
<span v-click="19" />
<span v-click="20" />

<GsFormulas :step="Math.max(0, $clicks - 17)" style="position:absolute; top:38%; right:2rem;" />

---

# Nice Properties of $\operatorname{GS}_\mathcal{E}$

<div class="proposition mt-4">

**Proposition**

Let $\mathscr{C} \subseteq \mathscr{A}$ be a subcategory.

<v-clicks>

1. If $\mathscr{C}$ is $\mathcal{E}$-adapted, then $\operatorname{GS}_\mathcal{E}(\mathscr{C})$ is also $\mathcal{E}$-adapted.

2. If $\mathscr{C}$ is $\mathcal{E}$-adapted and extension-closed, then $\operatorname{GS}_\mathcal{E}(\mathscr{C})$ is also extension-closed.

</v-clicks>

</div>

<v-clicks>

<div class="corollary mt-5">

<strong>Corollary 1.</strong> Let $T \in \mathscr{A}$ be a tilting object. Then $\operatorname{GS}_\mathcal{E}(T)$ is $\mathcal{E}$-adapted and extension-closed.

</div>

<div class="corollary mt-3">

<strong>Corollary 2.</strong> Let $T \in \operatorname{rep}(A_n)$ be a tilting object. Then $\operatorname{GS}_{\mathcal{E}_\diamond}(T)$ is canonically Jordan recoverable.

</div>

<div class="callout-question mt-4">

<strong>Question:</strong> Is $\operatorname{GS}_{\mathcal{E}_\diamond}(T)$ maximal canonically Jordan recoverable?

</div>

</v-clicks>

---

# First Main Theorem

<div class="theorem mt-4">

**Theorem \[DR25\]**

Let $T \in \mathscr{A}$ be a tilting object. Then $\operatorname{GS}_\mathcal{E}(T)$ is a **maximal** $\mathcal{E}$-adapted, extension-closed subcategory of $\mathscr{A}$ containing $T$.

</div>

<div class="mt-5" v-click>

*In particular, every maximal canonically Jordan recoverable subcategory arises as $\operatorname{GS}_{\mathcal{E}_\diamond}(T)$ for some tilting object $T$.*

</div>

<div class="callout-question mt-4" v-click>

How can we describe the equivalence relation $\;T \sim_\mathcal{E} T' \iff \operatorname{GS}_{\mathcal{E}}(T) = \operatorname{GS}_{\mathcal{E}}(T')$?

</div>

---
layout: section
class: text-center
---

# IV. Relative Mutations & Tilting Equivalence

Second Main Theorem

---

# Classical Mutation <span :style="{ color:'#60a5fa', opacity: $clicks >= 2 ? 1 : 0, transition:'opacity 0.4s' }">($\mathcal{E}$-mutation)</span>

<div class="definition mt-4">

**Definition**

Let $T = U \oplus \overline{T}$ be a tilting object with $U$ indecomposable.

A<span :style="{ fontSize: $clicks >= 2 ? '1em' : '0', opacity: $clicks >= 2 ? 1 : 0, transition:'font-size 0.3s, opacity 0.3s' }">n</span> <span :style="{ fontSize: $clicks >= 2 ? '1em' : '0', opacity: $clicks >= 2 ? 1 : 0, transition:'font-size 0.3s, opacity 0.3s', color:'#60a5fa' }">$\mathcal{E}$-</span>**mutation** of $T$ at $U$ is a tilting object $\mu_U(T) = U' \oplus \overline{T}$, where $U'$ is obtained from $U$ by an <span style="font-style:italic;"><span :style="{ fontSize: $clicks >= 2 ? '1em' : '0', opacity: $clicks >= 2 ? 1 : 0, transition:'font-size 0.3s, opacity 0.3s', color:'#60a5fa' }">$\mathcal{E}$-</span><span style="color:#e2b96f;">exchange sequence</span></span>

<div style="position:relative; min-height:3.2em;">
<div :style="{ position:'absolute', width:'100%', opacity: $clicks < 2 ? 1 : 0, transition:'opacity 0.4s' }">

$$\xi:\; 0 \rightarrow U \xrightarrow{f} B \xrightarrow{g} U' \rightarrow 0, \qquad B \in \operatorname{add}(\overline{T}),$$

</div>
<div :style="{ position:'absolute', width:'100%', opacity: $clicks >= 2 ? 1 : 0, transition:'opacity 0.4s' }">

$$\xi:\; 0 \rightarrow U \xrightarrow{f} B \xrightarrow{g} U' \rightarrow 0\,\textcolor{#60a5fa}{\in \mathcal{E}}, \qquad B \in \operatorname{add}(\overline{T}),$$

</div>
</div>

where $f$ is a left minimal $\operatorname{add}(\overline{T})$-approximation of $U$, and $g$ is a right minimal $\operatorname{add}(\overline{T})$-approximation of $U'$.

</div>

<div class="mt-4 opacity-80" v-click>
<div style="position:relative; min-height:1.6em;">
<div :style="{ position:'absolute', width:'100%', opacity: $clicks < 2 ? 1 : 0, transition:'opacity 0.4s' }">

We write $\textcolor{#e2b96f}{\mu_U^+(T)}$ (resp. $\textcolor{#e2b96f}{\mu_U^-(T)}$) for the <span style="color:#e2b96f; font-style:italic;">right</span> (resp. <span style="color:#e2b96f; font-style:italic;">left</span>) mutation.

</div>
<div :style="{ position:'absolute', width:'100%', opacity: $clicks >= 2 ? 1 : 0, transition:'opacity 0.4s' }">

We write $\textcolor{#e2b96f}{\mu_{U,\textcolor{#60a5fa}{\mathcal{E}}}^+(T)}$ (resp. $\textcolor{#e2b96f}{\mu_{U,\textcolor{#60a5fa}{\mathcal{E}}}^-(T)}$) for the <span style="color:#e2b96f; font-style:italic;">right</span> (resp. <span style="color:#e2b96f; font-style:italic;">left</span>) <span style="color:#60a5fa;">$\mathcal{E}$-</span>mutation.

</div>
</div>
</div>

<span v-click />

---

# $\mathcal{E}$-Reachability

<div class="definition mt-4">

**Definition**

Let $T, T' \in \operatorname{Tilt}(Q)$.

$T'$ is **$\mathcal{E}$-reachable** from $T$ if there exist indecomposables $(U_1, \dots, U_m)$ such that

$$T' \cong \mu_{U_m,\mathcal{E}} \circ \cdots \circ \mu_{U_1,\mathcal{E}}(T).$$

</div>

<div class="mt-5" v-click>

**$\mathcal{E}$-reachability** $T \approx_{\mathcal{E}} T'$ forms an equivalence relation. We denote $[T]_{\approx_\mathcal{E}}$ for the equivalence class of $T$.

</div>

---

# Equivalence of Tiltings

<div class="callout-question mt-4">

**Earlier question** &nbsp;— How can we describe $T \sim_\mathcal{E} T' \iff \operatorname{GS}_{\mathcal{E}}(T) = \operatorname{GS}_{\mathcal{E}}(T')$?

</div>

<div class="proposition mt-4" v-click>

**Proposition**

Let $T, T' \in \operatorname{Tilt}(Q)$. Then

$$T \sim_{\mathcal{E}} T' \quad \Longleftrightarrow \quad T \approx_{\mathcal{E}} T'.$$

</div>

---

# Example: $Q = 1 \to 2 \leftarrow 3 \to 4$ with $\mathcal{E} = \mathcal{E}_\diamond$

<div style="position:absolute; top:6.5rem; left:2rem; right:2rem; bottom:2rem;">
  <iframe src="https://ar-quiver-simulator.vercel.app" style="width:154%; height:154%; border:none; transform:scale(0.65); transform-origin:top left;" />
</div>

---

# Equivalence of Tiltings

<div style="opacity: 1 !important;">

**Example.** Assume $Q = 1 \to 2 \leftarrow 3 \to 4$ and $\mathcal{E} = \mathcal{E}_\diamond$.

</div>

<div class="mt-2" style="width: 100%; aspect-ratio: 22/10; position: relative;">
  <img src="./public/poset_left.png" class="fade-out-left"
       style="position: absolute; height: 92%; top: 4%; left: 5%;" />
  <img src="./public/poset_right_circle.png" v-click="1" class="grow-from-node"
       style="position: absolute; height: 85%; top: 7%; right: 2%;" />
  <img src="./public/poset_right_labels.png" v-click="1" class="labels-delayed"
       style="position: absolute; height: 85%; top: 7%; right: 2%;" />
  <!-- v-click 2 : quivers travel from circle to left stack -->
  <img src="./public/t1_quiver.png" v-click="2" class="quiver-travel quiver-t1 quiver-plain" />
  <img src="./public/t2_quiver.png" v-click="2" class="quiver-travel quiver-t2 quiver-plain" />
  <img src="./public/t3_quiver.png" v-click="2" class="quiver-travel quiver-t3 quiver-plain" />
  <!-- v-click 3 : swap to highlighted versions -->
  <img src="./public/t1_hl.png" v-click="3" class="quiver-hl quiver-t1" />
  <img src="./public/t2_hl.png" v-click="3" class="quiver-hl quiver-t2" />
  <img src="./public/t3_hl.png" v-click="3" class="quiver-hl quiver-t3" />
  <!-- formula fades in after highlights, no extra vclick -->
  <div v-click="3" class="gs-formula">

$\mathrm{GS}_{\mathcal{E}_\diamond}(T_1) = \mathrm{GS}_{\mathcal{E}_\diamond}(T_2) = \mathrm{GS}_{\mathcal{E}_\diamond}(T_3)$

  </div>
</div>

<style>
.grow-from-node {
  transform: scale(0);
  transform-origin: -95% 72%;
  transition: transform 2.2s cubic-bezier(0.22, 1, 0.36, 1);
}
.grow-from-node:not(.slidev-vclick-hidden) {
  transform: scale(1);
}
.labels-delayed:not(.slidev-vclick-hidden) {
  animation: fadeInLabels 0.5s ease both;
  animation-delay: 2.1s;
}
@keyframes fadeInLabels {
  from { opacity: 0; }
  to   { opacity: 1; }
}
div:has(.grow-from-node:not(.slidev-vclick-hidden)) .fade-out-left {
  animation: fadeOutLeft 0.8s ease forwards;
  animation-delay: 2.7s;
}
@keyframes fadeOutLeft {
  from { opacity: 1; }
  to   { opacity: 0; }
}
/* v-click 2 : quivers travel from circle positions to left stack */
.quiver-travel {
  position: absolute;
  height: 32%;
  transition: left 2.0s cubic-bezier(0.22, 1, 0.36, 1),
              top  2.0s cubic-bezier(0.22, 1, 0.36, 1);
}
/* Starting positions — matching T1/T2/T3 in the right circle */
.quiver-t1 { left: 64%; top: 37%; }
.quiver-t2 { left: 79%; top: 52%; }
.quiver-t3 { left: 64%; top: 67%; }
/* Final positions — horizontal stack on the left */
.quiver-t1:not(.slidev-vclick-hidden) { left: 2%;  top: 20%; }
.quiver-t2:not(.slidev-vclick-hidden) { left: 20%; top: 20%; }
.quiver-t3:not(.slidev-vclick-hidden) { left: 38%; top: 20%; }
/* v-click 3 : highlighted versions overlay at same positions, plain fade out */
.quiver-hl {
  position: absolute;
  height: 32%;
  transition: opacity 1.8s ease;
}
.quiver-hl.quiver-t1 { left: 2%;  top: 20%; }
.quiver-hl.quiver-t2 { left: 20%; top: 20%; }
.quiver-hl.quiver-t3 { left: 38%; top: 20%; }
div:has(.quiver-hl:not(.slidev-vclick-hidden)) .quiver-plain {
  opacity: 0;
  transition: opacity 1.8s ease;
}
.gs-formula {
  position: absolute;
  left: 8%; bottom: 28%;
  color: white;
  font-size: 1.1em;
  opacity: 0;
}
.gs-formula:not(.slidev-vclick-hidden) {
  animation: fadeInFormula 1.5s ease both;
  animation-delay: 1.8s;
}
@keyframes fadeInFormula {
  from { opacity: 0; }
  to   { opacity: 1; }
}
</style>

---

# Second Main Theorem

<div class="theorem mt-4">

**Theorem \[DR25\]**

Let $T \in \operatorname{Tilt}(Q)$. Then

$$\operatorname{GS}_{\mathcal{E}}(T) \;=\; \operatorname{add}\!\left( \bigoplus_{T' \in [T]_{\approx_{\mathcal{E}}}} T' \right).$$

</div>

<div class="mt-5" v-click>

**Example.** Assume $Q = 1 \to 2 \leftarrow 3 \to 4$ and $\mathcal{E} = \mathcal{E}_\diamond$.

</div>

<div class="flex items-start gap-28 mt-2" style="position: relative; overflow: visible;">

<div v-click style="display: inline-block;">
  <div class="flex gap-4">
    <img src="./public/t1_quiver.png" style="height: 140px; object-fit: contain;" />
    <img src="./public/t2_quiver.png" style="height: 140px; object-fit: contain;" />
    <img src="./public/t3_quiver.png" style="height: 140px; object-fit: contain;" />
  </div>
  <div class="text-center mt-6">

$[T_1]_{\approx_{\mathcal{E}_\diamond}}=[T_2]_{\approx_{\mathcal{E}_\diamond}}=[T_3]_{\approx_{\mathcal{E}_\diamond}}$

  </div>
</div>

<div v-click style="margin-top: 20px;">
  <img src="./public/t_plain.png" style="height: 120px; object-fit: contain;" />
</div>

<!-- v-click 4: 4 boxes from T1 travel to plain quiver -->
<img src="./public/box_2.png"  v-click="4" class="tbox tb-2"  style="height:22px;" />
<img src="./public/box_12.png" v-click="4" class="tbox tb-12" style="height:22px;" />
<img src="./public/box_24.png" v-click="4" class="tbox tb-24" style="height:22px;" />
<img src="./public/box_23.png" v-click="4" class="tbox tb-23" style="height:22px;" />
<!-- v-click 5: 4 boxes from T2 travel to plain quiver -->
<img src="./public/box_12.png" v-click="5" class="tbox tb2-12" style="height:22px;" />
<img src="./public/box_24.png" v-click="5" class="tbox tb2-24" style="height:22px;" />
<img src="./public/box_14.png" v-click="5" class="tbox tb2-14" style="height:22px;" />
<img src="./public/box_23.png" v-click="5" class="tbox tb2-23" style="height:22px;" />
<!-- v-click 6: 4 boxes from T3 travel to plain quiver -->
<img src="./public/box_12.png" v-click="6" class="tbox tb3-12" style="height:22px;" />
<img src="./public/box_14.png" v-click="6" class="tbox tb3-14" style="height:22px;" />
<img src="./public/box_23.png" v-click="6" class="tbox tb3-23" style="height:22px;" />
<img src="./public/box_13.png" v-click="6" class="tbox tb3-13" style="height:22px;" />

<!-- v-click 7: GS formula result -->
<div v-click="7" class="gs-result">

$\operatorname{GS}_{\mathcal{E}_\diamond}(T_1) = \operatorname{add}(T_1 \oplus T_2 \oplus T_3)$

</div>

</div>

<style>
.tbox {
  position: absolute;
  z-index: 10;
}
.gs-result {
  position: absolute;
  left: 540px;
  top: 160px;
}
.tb-2:not(.slidev-vclick-hidden)  { animation: travel-2  2.2s cubic-bezier(0.22,1,0.36,1) both; left: 595px; top: 54px;  }
.tb-12:not(.slidev-vclick-hidden) { animation: travel-12 2.2s cubic-bezier(0.22,1,0.36,1) both; left: 621px; top: 25px;  }
.tb-24:not(.slidev-vclick-hidden) { animation: travel-24 2.2s cubic-bezier(0.22,1,0.36,1) both; left: 622px; top: 83px;  }
.tb-23:not(.slidev-vclick-hidden) { animation: travel-23 2.2s cubic-bezier(0.22,1,0.36,1) both; left: 651px; top: 114px; }

@keyframes travel-2  { from { left: 6px;  top: 59px;  } to { left: 595px; top: 54px;  } }
@keyframes travel-12 { from { left: 36px; top: 30px;  } to { left: 621px; top: 25px;  } }
@keyframes travel-24 { from { left: 36px; top: 88px;  } to { left: 622px; top: 83px;  } }
@keyframes travel-23 { from { left: 65px; top: 118px; } to { left: 651px; top: 114px; } }
/* T2 source: starts at x≈262px in flex container */
.tb2-12:not(.slidev-vclick-hidden) { animation: travel2-12 2.2s cubic-bezier(0.22,1,0.36,1) both; left: 621px; top: 25px;  }
.tb2-24:not(.slidev-vclick-hidden) { animation: travel2-24 2.2s cubic-bezier(0.22,1,0.36,1) both; left: 622px; top: 83px;  }
.tb2-14:not(.slidev-vclick-hidden) { animation: travel2-14 2.2s cubic-bezier(0.22,1,0.36,1) both; left: 649px; top: 54px;  }
.tb2-23:not(.slidev-vclick-hidden) { animation: travel2-23 2.2s cubic-bezier(0.22,1,0.36,1) both; left: 651px; top: 114px; }

@keyframes travel2-12 { from { left: 267px; top: 26px;  } to { left: 621px; top: 25px;  } }
@keyframes travel2-24 { from { left: 267px; top: 84px;  } to { left: 622px; top: 83px;  } }
@keyframes travel2-14 { from { left: 294px; top: 55px;  } to { left: 649px; top: 54px;  } }
@keyframes travel2-23 { from { left: 296px; top: 114px; } to { left: 651px; top: 114px; } }
/* T3 source: starts at x≈523px in flex container */
.tb3-12:not(.slidev-vclick-hidden) { animation: travel3-12 2.2s cubic-bezier(0.22,1,0.36,1) both; left: 621px; top: 25px;  }
.tb3-14:not(.slidev-vclick-hidden) { animation: travel3-14 2.2s cubic-bezier(0.22,1,0.36,1) both; left: 649px; top: 54px;  }
.tb3-23:not(.slidev-vclick-hidden) { animation: travel3-23 2.2s cubic-bezier(0.22,1,0.36,1) both; left: 651px; top: 114px; }
.tb3-13:not(.slidev-vclick-hidden) { animation: travel3-13 2.2s cubic-bezier(0.22,1,0.36,1) both; left: 682px; top: 84px;  }

@keyframes travel3-12 { from { left: 403px; top: 26px;  } to { left: 621px; top: 25px;  } }
@keyframes travel3-14 { from { left: 430px; top: 55px;  } to { left: 649px; top: 54px;  } }
@keyframes travel3-23 { from { left: 432px; top: 114px; } to { left: 651px; top: 114px; } }
@keyframes travel3-13 { from { left: 463px; top: 84px;  } to { left: 682px; top: 84px;  } }
</style>

---

# Consequences of the Second Main Theorem

<div class="corollary mt-4">

**Corollary**

Let $Q$ be a quiver of type $A_n$.

</div>

<v-clicks>

<div class="mt-4">

<em>(a)</em> There is a bijection

$$\operatorname{Tilt}(Q) / {\approx_{\mathcal{E}_\diamond}} \;\longleftrightarrow\; \bigl\{\text{maximal CJR subcategories of } \operatorname{rep}(Q)\bigr\}.$$

</div>

<div class="mt-4">

<em>(b)</em> Let $\mathscr{C} \subseteq \operatorname{rep}(Q)$ be a maximal canonically Jordan recoverable subcategory. Then there exists $T \in \operatorname{Tilt}(Q)$ such that

$$\mathscr{C} = \operatorname{add}\!\left( \bigoplus_{T' \in [T]_{\approx_{\mathcal{E}_\diamond}}} T' \right).$$

</div>

</v-clicks>

---

# Synthesis and Outlook

**A unified picture of exact structures and Jordan recoverability**

<v-clicks>

- The **diamond exact structure** $\mathcal{E}_\diamond$ provides a natural framework connecting tilting theory and Jordan recoverability.

- Every maximal canonically Jordan recoverable subcategory emerges as $\operatorname{GS}_{\mathcal{E}_\diamond}(T)$ for some tilting object $T$.

- Two tilting objects $T, T'$ satisfy $\operatorname{GS}_{\mathcal{E}}(T) = \operatorname{GS}_{\mathcal{E}}(T')$ if and only if they are related by a sequence of **$\mathcal{E}$-mutations**.

- There is a bijection
$$\operatorname{Tilt}(Q)/{\approx_{\mathcal{E}_\diamond}} \;\longleftrightarrow\; \{\text{maximal CJR subcategories of }\operatorname{rep}(Q)\},$$
given by $[T]_{\approx_{\mathcal{E}_\diamond}} \;\longmapsto\; \operatorname{add}\!\Bigl(\bigoplus_{T' \in [T]_{\approx_{\mathcal{E}_\diamond}}} T'\Bigr)$.

</v-clicks>

---
layout: center
---

<div style="text-align:center">

# Thank you for listening!

<div style="font-size:1.2rem; opacity:0.65; margin-top:1rem; font-style:italic">Questions?</div>


<div style="margin-top:2rem">
  <img src="./public/frq_logo_blanc.png" style="max-height: 120px; margin: 0 auto;" />
</div>

<div style="margin-top:1.5rem; font-size:0.8rem; opacity:0.4">
  Sunny Roy &nbsp;·&nbsp; ICRA 2026 &nbsp;·&nbsp; Grenoble
</div>

</div>
