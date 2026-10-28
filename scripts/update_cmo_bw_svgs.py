import json

# Dictionary of black and white SVGs for each non-textbook CMO card
BW_SVGS = {
    101: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-101" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Open Ball B_eps(x) -->
  <circle cx="65" cy="72" r="38" fill="#f8fafc" stroke="#000000" stroke-width="1.5" stroke-dasharray="4,3"/>
  <circle cx="65" cy="72" r="3" fill="#000000"/>
  <line x1="65" y1="72" x2="93" y2="48" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-101)"/>
  <text x="82" y="56" fill="#000000" font-size="10" font-family="serif" font-style="italic">ε</text>
  <text x="65" y="87" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">x₀</text>
  <text x="65" y="124" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">B_ε(x₀) (Open: Dashed)</text>

  <!-- Compact Set K -->
  <rect x="135" y="34" width="85" height="76" rx="14" fill="#f1f5f9" stroke="#000000" stroke-width="1.8"/>
  <circle cx="177" cy="72" r="3" fill="#000000"/>
  <text x="177" y="64" fill="#000000" font-size="11" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">K</text>
  <text x="177" y="84" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Closed (Solid)</text>
  <text x="177" y="96" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">+ Bounded</text>
  <text x="177" y="124" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Compact Set</text>
</svg>""",

    102: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-102" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Axes -->
  <line x1="25" y1="120" x2="225" y2="120" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-102)"/>
  <line x1="35" y1="130" x2="35" y2="15" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-102)"/>
  <text x="225" y="132" fill="#000000" font-size="9" font-family="serif" font-style="italic">x</text>
  <text x="25" y="20" fill="#000000" font-size="9" font-family="serif" font-style="italic">y</text>
  <!-- Curve approaching jump from left -->
  <path d="M 45 50 Q 80 55 110 68" fill="none" stroke="#000000" stroke-width="1.8"/>
  <circle cx="110" cy="68" r="3.5" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <!-- Downward jump point (solid black) -->
  <circle cx="110" cy="92" r="3.5" fill="#000000"/>
  <!-- Curve continuing right -->
  <path d="M 110 92 Q 160 96 210 38" fill="none" stroke="#000000" stroke-width="1.8"/>
  <!-- Sublevel threshold alpha -->
  <line x1="30" y1="78" x2="220" y2="78" stroke="#000000" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="20" y="81" fill="#000000" font-size="9" font-family="serif" font-style="italic">α</text>
  <line x1="110" y1="92" x2="110" y2="120" stroke="#000000" stroke-width="1" stroke-dasharray="2,2"/>
  <text x="110" y="132" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">x₀</text>
  <text x="155" y="108" fill="#000000" font-size="8.5" font-family="sans-serif" font-style="italic">f(x₀) ≤ liminf f(x)</text>
</svg>""",

    103: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-103" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Axes -->
  <line x1="25" y1="120" x2="225" y2="120" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-103)"/>
  <line x1="35" y1="130" x2="35" y2="15" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-103)"/>
  <!-- Compact interval [a, b] on axis -->
  <line x1="60" y1="120" x2="195" y2="120" stroke="#000000" stroke-width="3"/>
  <line x1="60" y1="115" x2="60" y2="125" stroke="#000000" stroke-width="2"/>
  <line x1="195" y1="115" x2="195" y2="125" stroke="#000000" stroke-width="2"/>
  <text x="60" y="134" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">a</text>
  <text x="195" y="134" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">b</text>
  <!-- Continuous curve on [a, b] -->
  <path d="M 60 70 Q 95 22 120 75 T 195 40" fill="none" stroke="#000000" stroke-width="2"/>
  <!-- Max point -->
  <circle cx="95" cy="36" r="3.5" fill="#000000"/>
  <text x="95" y="26" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Max f(x)</text>
  <!-- Min point -->
  <circle cx="150" cy="92" r="3.5" fill="#000000"/>
  <line x1="150" y1="92" x2="150" y2="120" stroke="#000000" stroke-width="1" stroke-dasharray="2,2"/>
  <text x="150" y="105" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Min f(x*)</text>
  <text x="150" y="134" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">x*</text>
</svg>""",

    104: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-104" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Axes -->
  <line x1="25" y1="120" x2="225" y2="120" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-104)"/>
  <line x1="120" y1="130" x2="120" y2="15" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-104)"/>
  <!-- Sublevel region shaded -->
  <path d="M 68 65 Q 120 115 172 65 Z" fill="#f1f5f9" stroke="none"/>
  <!-- Coercive bowl curve -->
  <path d="M 45 22 Q 120 125 195 22" fill="none" stroke="#000000" stroke-width="2"/>
  <!-- Sublevel threshold line alpha -->
  <line x1="30" y1="65" x2="210" y2="65" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,3"/>
  <text x="215" y="68" fill="#000000" font-size="9" font-family="serif" font-style="italic">α</text>
  <!-- Interval on axis -->
  <line x1="68" y1="65" x2="68" y2="120" stroke="#000000" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="172" y1="65" x2="172" y2="120" stroke="#000000" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="68" y1="120" x2="172" y2="120" stroke="#000000" stroke-width="2.5"/>
  <text x="120" y="88" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">S_α is Compact</text>
  <text x="120" y="133" fill="#000000" font-size="8.5" font-family="serif" font-style="italic" text-anchor="middle">Bounded interval {x : f(x) ≤ α}</text>
  <text x="45" y="15" fill="#000000" font-size="8" font-family="sans-serif">+∞</text>
  <text x="195" y="15" fill="#000000" font-size="8" font-family="sans-serif">+∞</text>
</svg>""",

    106: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-106" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Axes -->
  <line x1="20" y1="72" x2="225" y2="72" stroke="#000000" stroke-width="1" marker-end="url(#arr-106)"/>
  <line x1="120" y1="135" x2="120" y2="10" stroke="#000000" stroke-width="1" marker-end="url(#arr-106)"/>
  <text x="225" y="84" fill="#000000" font-size="9" font-family="serif" font-style="italic">x₁</text>
  <text x="126" y="15" fill="#000000" font-size="9" font-family="serif" font-style="italic">x₂</text>
  <!-- Concentric Contours -->
  <ellipse cx="120" cy="72" rx="30" ry="18" fill="none" stroke="#000000" stroke-width="1"/>
  <ellipse cx="120" cy="72" rx="60" ry="34" fill="none" stroke="#000000" stroke-width="1.2"/>
  <ellipse cx="120" cy="72" rx="95" ry="52" fill="none" stroke="#000000" stroke-width="1.5"/>
  <text x="153" y="70" fill="#000000" font-size="8" font-family="monospace">c=1</text>
  <text x="183" y="70" fill="#000000" font-size="8" font-family="monospace">c=5</text>
  <text x="212" y="70" fill="#000000" font-size="8" font-family="monospace">c=20</text>
  <circle cx="120" cy="72" r="3" fill="#000000"/>
  <text x="120" y="132" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">All Sublevel Sets Closed &amp; Bounded</text>
</svg>""",

    201: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-201" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Axes -->
  <line x1="25" y1="125" x2="225" y2="125" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-201)"/>
  <line x1="35" y1="135" x2="35" y2="15" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-201)"/>
  <!-- Tangent line (1st order) -->
  <line x1="45" y1="110" x2="195" y2="35" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <text x="198" y="38" fill="#000000" font-size="8" font-family="sans-serif">1st Order (Linear)</text>
  <!-- 2nd order osculating parabola -->
  <path d="M 50 115 Q 110 75 180 30" fill="none" stroke="#000000" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="175" y="20" fill="#000000" font-size="8" font-family="sans-serif">2nd Order (Quadratic)</text>
  <!-- True function f(x) -->
  <path d="M 50 115 Q 110 75 185 45" fill="none" stroke="#000000" stroke-width="2.2"/>
  <text x="190" y="55" fill="#000000" font-size="8.5" font-family="serif" font-style="italic" font-weight="bold">f(x) True</text>
  <!-- Expansion point x₀ -->
  <circle cx="110" cy="75" r="3.5" fill="#000000"/>
  <line x1="110" y1="75" x2="110" y2="125" stroke="#000000" stroke-width="1" stroke-dasharray="2,2"/>
  <text x="110" y="136" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">x₀</text>
</svg>""",

    203: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-203" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Axes -->
  <line x1="25" y1="120" x2="225" y2="120" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-203)"/>
  <line x1="120" y1="130" x2="120" y2="15" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-203)"/>
  <!-- Bowl curve -->
  <path d="M 45 40 Q 120 115 195 40" fill="none" stroke="#000000" stroke-width="2"/>
  <!-- Flat horizontal tangent at x* -->
  <line x1="60" y1="95" x2="180" y2="95" stroke="#000000" stroke-width="1.5" stroke-dasharray="4,3"/>
  <circle cx="120" cy="95" r="3.5" fill="#000000"/>
  <text x="120" y="83" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">∇f(x*) = 0</text>
  <text x="120" y="112" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">x*</text>
  <text x="120" y="30" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Hessian PSD: dᵀ∇²f(x*)d ≥ 0 (∀ d)</text>
</svg>""",

    204: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-204" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Axes -->
  <line x1="25" y1="120" x2="225" y2="120" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-204)"/>
  <line x1="120" y1="130" x2="120" y2="15" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-204)"/>
  <!-- Strict bowl with shading -->
  <path d="M 50 35 Q 120 115 190 35" fill="none" stroke="#000000" stroke-width="2.2"/>
  <!-- Lower bounding quadratic (m/2)||d||^2 -->
  <path d="M 65 48 Q 120 115 175 48" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <circle cx="120" cy="95" r="3.5" fill="#000000"/>
  <text x="120" y="112" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">x* (Strict Local Minimum)</text>
  <text x="120" y="24" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">∇²f(x*) ≻ 0  (Strictly Positive Definite)</text>
  <text x="120" y="134" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">λ_min(∇²f) &gt; 0 ⇒ Strict Isolation</text>
</svg>""",

    205: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-205" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Contour hyperbolas of saddle f = x1^2 - x2^2 -->
  <line x1="20" y1="72" x2="220" y2="72" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-205)"/>
  <line x1="120" y1="135" x2="120" y2="10" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-205)"/>
  <text x="220" y="84" fill="#000000" font-size="9" font-family="serif" font-style="italic">x₁</text>
  <text x="126" y="18" fill="#000000" font-size="9" font-family="serif" font-style="italic">x₂</text>
  <!-- Asymptotes x1 = +/- x2 -->
  <line x1="50" y1="122" x2="190" y2="22" stroke="#000000" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="50" y1="22" x2="190" y2="122" stroke="#000000" stroke-width="1" stroke-dasharray="3,3"/>
  <!-- Hyperbolic branches -->
  <path d="M 60 72 Q 95 72 100 20" fill="none" stroke="#000000" stroke-width="1.5"/>
  <path d="M 60 72 Q 95 72 100 124" fill="none" stroke="#000000" stroke-width="1.5"/>
  <path d="M 180 72 Q 145 72 140 20" fill="none" stroke="#000000" stroke-width="1.5"/>
  <path d="M 180 72 Q 145 72 140 124" fill="none" stroke="#000000" stroke-width="1.5"/>
  <!-- Saddle point -->
  <circle cx="120" cy="72" r="3.5" fill="#000000"/>
  <text x="120" y="60" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Saddle Point (λ₁ &gt; 0, λ₂ &lt; 0)</text>
  <text x="120" y="134" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Indefinite Hessian: Neither Min nor Max</text>
</svg>""",

    206: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-206" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Banana valley contour lines -->
  <path d="M 35 110 Q 110 130 155 80 T 215 25" fill="none" stroke="#000000" stroke-width="1" stroke-dasharray="3,3"/>
  <path d="M 45 100 Q 115 120 155 75 T 205 32" fill="none" stroke="#000000" stroke-width="1.2"/>
  <path d="M 55 90 Q 120 110 155 70 T 195 40" fill="none" stroke="#000000" stroke-width="1.5"/>
  <!-- Parabolic trough x2 = x1^2 -->
  <path d="M 60 85 Q 125 105 155 65" fill="none" stroke="#000000" stroke-width="2"/>
  <!-- Global min at (1, 1) -->
  <circle cx="155" cy="65" r="4" fill="#000000"/>
  <text x="175" y="68" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold">x* = (1, 1)</text>
  <text x="120" y="22" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Rosenbrock Banana Valley: x₂ = x₁²</text>
  <text x="120" y="136" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">f(x) = 100(x₂ - x₁²)² + (1 - x₁)²</text>
</svg>""",

    303: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-303" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Axes -->
  <line x1="25" y1="120" x2="225" y2="120" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-303)"/>
  <line x1="120" y1="130" x2="120" y2="15" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-303)"/>
  <!-- Globally convex curve -->
  <path d="M 40 25 Q 120 115 200 25" fill="none" stroke="#000000" stroke-width="2"/>
  <!-- Tangents at x and y -->
  <line x1="45" y1="95" x2="115" y2="55" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <circle cx="80" cy="75" r="3.5" fill="#000000"/>
  <text x="75" y="90" fill="#000000" font-size="9" font-family="serif" font-style="italic">x</text>
  <line x1="125" y1="55" x2="195" y2="95" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <circle cx="160" cy="75" r="3.5" fill="#000000"/>
  <text x="165" y="90" fill="#000000" font-size="9" font-family="serif" font-style="italic">y</text>
  <text x="120" y="24" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">∇²f(x) ⪰ 0  ∀ x ∈ C  (Global Convexity)</text>
  <text x="120" y="134" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Every stationary point is a global minimum</text>
</svg>""",

    304: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-304" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Linear tangent -->
  <line x1="40" y1="110" x2="200" y2="50" stroke="#000000" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="202" y="52" fill="#000000" font-size="8" font-family="sans-serif">Linear Tangent</text>
  <!-- Quadratic lower bound -->
  <path d="M 45 95 Q 100 88 190 35" fill="none" stroke="#000000" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="195" y="32" fill="#000000" font-size="8" font-family="sans-serif">+ (m/2)||y-x||²</text>
  <!-- True function f(y) -->
  <path d="M 45 80 Q 100 88 185 20" fill="none" stroke="#000000" stroke-width="2.2"/>
  <text x="185" y="14" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold">f(y)</text>
  <!-- Expansion point x -->
  <circle cx="100" cy="88" r="3.5" fill="#000000"/>
  <text x="100" y="104" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">x</text>
  <text x="120" y="132" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">m-Strong Convexity: Strict Quadratic Growth</text>
</svg>""",

    305: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-305" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Two connected basins sharing global min f* -->
  <path d="M 35 30 Q 75 110 115 110 T 195 30" fill="none" stroke="#000000" stroke-width="2"/>
  <!-- Flat bottom line f* -->
  <line x1="30" y1="110" x2="210" y2="110" stroke="#000000" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="215" y="113" fill="#000000" font-size="9" font-family="serif" font-style="italic">f*</text>
  <!-- Point x on slope -->
  <circle cx="60" cy="65" r="3.5" fill="#000000"/>
  <text x="50" y="62" fill="#000000" font-size="9" font-family="serif" font-style="italic">x</text>
  <!-- Gradient vector arrow -->
  <line x1="60" y1="65" x2="40" y2="35" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-305)"/>
  <text x="32" y="30" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">∇f(x)</text>
  <text x="120" y="22" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">½ ||∇f(x)||² ≥ μ (f(x) - f*)</text>
  <text x="120" y="132" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Every stationary point is global min; no strict convexity needed</text>
</svg>""",

    306: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Quasiconvex Outer Box -->
  <rect x="20" y="18" width="200" height="110" rx="8" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <text x="30" y="34" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold">Quasiconvex (Sublevel sets convex)</text>
  <!-- Convex Box -->
  <rect x="35" y="42" width="170" height="78" rx="7" fill="#f1f5f9" stroke="#000000" stroke-width="1.5"/>
  <text x="45" y="58" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold">Convex (Secant above graph)</text>
  <!-- Strictly Convex Box -->
  <rect x="50" y="66" width="140" height="48" rx="6" fill="#e2e8f0" stroke="#000000" stroke-width="1.5"/>
  <text x="60" y="80" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold">Strictly Convex (Unique min)</text>
  <!-- Strongly Convex Inner Box -->
  <rect x="65" y="86" width="110" height="24" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <text x="120" y="102" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Strongly Convex (m &gt; 0)</text>
</svg>""",

    402: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-402" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Axes -->
  <line x1="25" y1="120" x2="225" y2="120" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-402)"/>
  <line x1="35" y1="130" x2="35" y2="15" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-402)"/>
  <text x="225" y="132" fill="#000000" font-size="9" font-family="serif" font-style="italic">α</text>
  <text x="22" y="20" fill="#000000" font-size="9" font-family="serif" font-style="italic">φ(α)</text>
  <!-- 1D Quadratic parabola -->
  <path d="M 45 40 Q 120 125 195 40" fill="none" stroke="#000000" stroke-width="2"/>
  <!-- Tangent line at alpha=0 -->
  <line x1="35" y1="50" x2="95" y2="105" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <circle cx="45" cy="59" r="3" fill="#000000"/>
  <text x="52" y="52" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">α = 0</text>
  <!-- Min point alpha* -->
  <circle cx="120" cy="100" r="3.5" fill="#000000"/>
  <line x1="120" y1="100" x2="120" y2="120" stroke="#000000" stroke-width="1" stroke-dasharray="2,2"/>
  <text x="120" y="133" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">α* = -gᵀd / (dᵀQd)</text>
  <text x="120" y="24" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Exact 1D Minimizer for Quadratics</text>
</svg>""",

    404: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-404" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Axes -->
  <line x1="25" y1="120" x2="225" y2="120" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-404)"/>
  <line x1="35" y1="130" x2="35" y2="15" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-404)"/>
  <!-- 1D function curve phi(alpha) -->
  <path d="M 35 45 Q 85 110 140 105 T 215 35" fill="none" stroke="#000000" stroke-width="2"/>
  <!-- Armijo line c1 -->
  <line x1="35" y1="45" x2="210" y2="95" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,3"/>
  <text x="190" y="85" fill="#000000" font-size="8" font-family="sans-serif">Armijo Line (c₁)</text>
  <!-- Curvature condition point -->
  <circle cx="120" cy="107" r="3.5" fill="#000000"/>
  <!-- Acceptable interval on axis -->
  <line x1="105" y1="120" x2="165" y2="120" stroke="#000000" stroke-width="3"/>
  <line x1="105" y1="116" x2="105" y2="124" stroke="#000000" stroke-width="1.5"/>
  <line x1="165" y1="116" x2="165" y2="124" stroke="#000000" stroke-width="1.5"/>
  <text x="135" y="133" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Wolfe Interval</text>
  <text x="120" y="24" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Armijo (c₁) + Curvature (c₂) = Wolfe</text>
</svg>""",

    405: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-405" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Vertex x_k -->
  <circle cx="50" cy="95" r="4" fill="#000000"/>
  <text x="40" y="102" fill="#000000" font-size="9" font-family="serif" font-style="italic">x_k</text>
  <!-- Negative gradient vector -∇f -->
  <line x1="50" y1="95" x2="190" y2="95" stroke="#000000" stroke-width="2" marker-end="url(#arr-405)"/>
  <text x="195" y="99" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold">-∇f(x_k)</text>
  <!-- Search direction vector d_k -->
  <line x1="50" y1="95" x2="175" y2="35" stroke="#000000" stroke-width="2" marker-end="url(#arr-405)"/>
  <text x="180" y="35" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold">d_k</text>
  <!-- Angle theta_k arc -->
  <path d="M 90 95 A 40 40 0 0 0 84 79" fill="none" stroke="#000000" stroke-width="1.2"/>
  <text x="96" y="85" fill="#000000" font-size="9" font-family="serif" font-style="italic">θ_k</text>
  <text x="120" y="20" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Zoutendijk Condition</text>
  <text x="120" y="132" fill="#000000" font-size="9" font-family="monospace" text-anchor="middle">Σ cos² θ_k ||∇f(x_k)||² &lt; ∞</text>
</svg>""",

    406: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-406" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Axis of alpha -->
  <line x1="25" y1="95" x2="225" y2="95" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-406)"/>
  <text x="225" y="108" fill="#000000" font-size="9" font-family="serif" font-style="italic">α</text>
  <!-- alpha = 1 point (rejected) -->
  <circle cx="195" cy="95" r="3.5" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <line x1="191" y1="91" x2="199" y2="99" stroke="#000000" stroke-width="1.5"/>
  <line x1="191" y1="99" x2="199" y2="91" stroke="#000000" stroke-width="1.5"/>
  <text x="195" y="80" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">α₀ = 1 (Fails)</text>
  <!-- alpha = rho (rejected) -->
  <circle cx="135" cy="95" r="3.5" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <line x1="131" y1="91" x2="139" y2="99" stroke="#000000" stroke-width="1.5"/>
  <line x1="131" y1="99" x2="139" y2="91" stroke="#000000" stroke-width="1.5"/>
  <text x="135" y="80" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">α = ρ (Fails)</text>
  <!-- alpha = rho^2 (accepted) -->
  <circle cx="80" cy="95" r="4.5" fill="#000000"/>
  <text x="80" y="80" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">α = ρ² (Accept!)</text>
  <!-- Backtracking contraction arrows -->
  <path d="M 190 65 Q 165 52 140 65" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-406)"/>
  <path d="M 130 65 Q 107 52 85 65" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-406)"/>
  <text x="120" y="24" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Backtracking: α ← ρα  until Armijo Holds</text>
  <text x="120" y="132" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">Typical params: ρ ∈ [0.5, 0.8], c₁ = 10⁻⁴</text>
</svg>""",

    502: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-502" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Axes -->
  <line x1="25" y1="120" x2="225" y2="120" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-502)"/>
  <line x1="35" y1="130" x2="35" y2="15" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-502)"/>
  <text x="225" y="132" fill="#000000" font-size="9" font-family="serif" font-style="italic">k (Iterations)</text>
  <text x="15" y="20" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">f(x_k) - f*</text>
  <!-- 1/k decay curve -->
  <path d="M 45 30 Q 75 105 210 115" fill="none" stroke="#000000" stroke-width="2"/>
  <!-- Points at k = 1, 2, 5 -->
  <circle cx="55" cy="48" r="3" fill="#000000"/>
  <circle cx="95" cy="98" r="3" fill="#000000"/>
  <circle cx="175" cy="113" r="3" fill="#000000"/>
  <text x="125" y="45" fill="#000000" font-size="9" font-family="monospace" text-anchor="middle">f(x_k) - f* ≤ L ||x₀ - x*||² / (2k)</text>
  <text x="125" y="65" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Sublinear O(1/k) with Step α = 1/L</text>
</svg>""",

    503: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-503" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Axes -->
  <line x1="25" y1="120" x2="225" y2="120" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-503)"/>
  <line x1="35" y1="130" x2="35" y2="15" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-503)"/>
  <text x="225" y="132" fill="#000000" font-size="9" font-family="serif" font-style="italic">k</text>
  <text x="10" y="20" fill="#000000" font-size="8" font-family="serif" font-style="italic">log ||x_k - x*||</text>
  <!-- Straight linear decay line on semilog scale -->
  <line x1="45" y1="28" x2="210" y2="115" stroke="#000000" stroke-width="2"/>
  <!-- Points at successive k -->
  <circle cx="45" cy="28" r="3" fill="#000000"/>
  <circle cx="95" cy="54" r="3" fill="#000000"/>
  <circle cx="150" cy="83" r="3" fill="#000000"/>
  <circle cx="205" cy="112" r="3" fill="#000000"/>
  <text x="135" y="40" fill="#000000" font-size="9" font-family="monospace" text-anchor="middle">||x_k - x*|| ≤ C · ((κ - 1) / (κ + 1))^k</text>
  <text x="135" y="133" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Linear (Geometric) Rate: Error Halves Periodically</text>
</svg>""",

    505: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Elongated Ellipses -->
  <ellipse cx="120" cy="72" rx="95" ry="24" fill="none" stroke="#000000" stroke-width="1.2"/>
  <ellipse cx="120" cy="72" rx="60" ry="14" fill="none" stroke="#000000" stroke-width="1.2"/>
  <ellipse cx="120" cy="72" rx="25" ry="6" fill="none" stroke="#000000" stroke-width="1.2"/>
  <!-- 90-degree zig-zag steepest descent trajectory -->
  <polyline points="40,88 80,58 92,84 108,62 115,78 120,72" fill="none" stroke="#000000" stroke-width="2"/>
  <!-- Successive steps -->
  <circle cx="40" cy="88" r="3" fill="#000000"/>
  <circle cx="80" cy="58" r="2.5" fill="#000000"/>
  <circle cx="92" cy="84" r="2.5" fill="#000000"/>
  <circle cx="120" cy="72" r="3.5" fill="#000000"/>
  <text x="120" y="24" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Ill-Conditioned Valley: κ = λ_max / λ_min ≫ 1</text>
  <text x="120" y="132" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Severe 90° Orthogonal Zig-Zag Trajectory</text>
</svg>""",

    506: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Elongated Ellipses in background -->
  <ellipse cx="120" cy="72" rx="95" ry="25" fill="none" stroke="#000000" stroke-width="1" stroke-dasharray="2,2"/>
  <ellipse cx="120" cy="72" rx="55" ry="14" fill="none" stroke="#000000" stroke-width="1" stroke-dasharray="2,2"/>
  <!-- Standard zig-zag (dashed) -->
  <polyline points="40,90 80,56 92,84 108,62" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <!-- Momentum smooth path (solid) -->
  <path d="M 40 90 Q 90 68 120 72" fill="none" stroke="#000000" stroke-width="2.2"/>
  <circle cx="120" cy="72" r="3.5" fill="#000000"/>
  <text x="120" y="24" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Heavy Ball Momentum: + β(x_k - x_{k-1})</text>
  <text x="120" y="115" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Cuts across zig-zag oscillations straight to minimum</text>
  <text x="120" y="132" fill="#000000" font-size="8" font-family="monospace" text-anchor="middle">BB Spectral Step: α_k = (sᵀy) / ||y||²</text>
</svg>""",

    903: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-903" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Cone Shaded Fan -->
  <polygon points="50,110 205,35 205,125" fill="#f1f5f9" stroke="#000000" stroke-width="1.8"/>
  <!-- Direction ray d -->
  <line x1="50" y1="110" x2="175" y2="75" stroke="#000000" stroke-width="2" marker-end="url(#arr-903)"/>
  <text x="180" y="78" fill="#000000" font-size="9.5" font-family="serif" font-style="italic" font-weight="bold">α d</text>
  <!-- Base point x* -->
  <circle cx="50" cy="110" r="4" fill="#000000"/>
  <text x="40" y="125" fill="#000000" font-size="10" font-family="serif" font-style="italic" font-weight="bold">x*</text>
  <!-- Cone label -->
  <text x="135" y="55" fill="#000000" font-size="11" font-family="serif" font-style="italic" font-weight="bold">T_Ω(x*)</text>
  <text x="120" y="138" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Fan of all admissible departure rays: d ∈ T_Ω ⇒ αd ∈ T_Ω (α ≥ 0)</text>
</svg>""",

    904: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-904" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Axes -->
  <line x1="35" y1="115" x2="215" y2="115" stroke="#000000" stroke-width="1.5" marker-end="url(#arr-904)"/>
  <line x1="55" y1="130" x2="55" y2="20" stroke="#000000" stroke-width="1.5" marker-end="url(#arr-904)"/>
  <text x="215" y="128" fill="#000000" font-size="9" font-family="serif" font-style="italic">x₁</text>
  <text x="42" y="25" fill="#000000" font-size="9" font-family="serif" font-style="italic">x₂</text>
  <!-- Shaded First Quadrant -->
  <rect x="55" y="25" width="145" height="90" fill="#f1f5f9" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,3"/>
  <!-- Origin -->
  <circle cx="55" cy="115" r="4" fill="#000000"/>
  <text x="40" y="128" fill="#000000" font-size="9" font-family="serif" font-style="italic">(0,0)</text>
  <text x="125" y="65" fill="#000000" font-size="10" font-family="serif" font-style="italic" font-weight="bold">T_Ω(0,0) = ℝ²₊</text>
  <text x="125" y="82" fill="#000000" font-size="8.5" font-family="monospace">[0, ∞) × [0, ∞)</text>
</svg>""",

    905: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-905" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Tangent cone fan -->
  <polygon points="110,85 195,35 195,120" fill="#f1f5f9" stroke="#000000" stroke-width="1.8"/>
  <text x="155" y="75" fill="#000000" font-size="10" font-family="serif" font-style="italic" font-weight="bold">T_Ω(x*)</text>
  <!-- Supporting hyperplane (dashed line) -->
  <line x1="110" y1="25" x2="110" y2="135" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <!-- Negative gradient -∇f pointing into exterior -->
  <line x1="110" y1="85" x2="45" y2="50" stroke="#000000" stroke-width="2" marker-end="url(#arr-905)"/>
  <text x="35" y="45" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold">-∇f(x*)</text>
  <!-- Vertex x* -->
  <circle cx="110" cy="85" r="4" fill="#000000"/>
  <text x="100" y="100" fill="#000000" font-size="9.5" font-family="serif" font-style="italic">x*</text>
  <text x="120" y="20" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Optimality: ∇f(x*)ᵀd ≥ 0  (∀ d ∈ T_Ω)</text>
  <text x="120" y="138" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">-∇f(x*) makes obtuse angle (≥ 90°) with all feasible directions</text>
</svg>""",

    906: """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-906" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Linearized Cone L_Ω (wider dashed wedge) -->
  <polygon points="50,115 195,35 195,115" fill="#f1f5f9" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,3"/>
  <text x="160" y="95" fill="#000000" font-size="9" font-family="serif" font-style="italic">L_Ω (Linearized)</text>
  <!-- True Tangent Cone T_Ω (single ray or narrow curve) -->
  <line x1="50" y1="115" x2="190" y2="45" stroke="#000000" stroke-width="2.5" marker-end="url(#arr-906)"/>
  <text x="150" y="42" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold">T_Ω (True Tangents)</text>
  <!-- Cusp vertex -->
  <circle cx="50" cy="115" r="4" fill="#000000"/>
  <text x="40" y="128" fill="#000000" font-size="9.5" font-family="serif" font-style="italic">x*</text>
  <text x="120" y="20" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">LICQ Fails: T_Ω(x*) ⫋ L_Ω(x*)</text>
  <text x="120" y="135" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Linearization predicts directions that immediately exit Ω</text>
</svg>"""
}

# Update cards_data.js
with open('/Users/senso/Projects/photographic-memory-cards/cards_data.js') as f:
    text = f.read()

s = text.find('[')
e = text.rfind(']') + 1
cards = json.loads(text[s:e])

updated_count = 0
for card in cards:
    cid = card.get('id')
    if cid in BW_SVGS:
        card['drawingSvg'] = BW_SVGS[cid]
        updated_count += 1

print(f"Updated {updated_count} cards with pure Black & White SVGs!")

with open('/Users/senso/Projects/photographic-memory-cards/cards_data.js', 'w') as f:
    f.write('window.MASTER_CARDS_DATA = ' + json.dumps(cards, indent=2) + ';\n')

print("Successfully wrote updated cards_data.js")
