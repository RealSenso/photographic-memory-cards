/* CMO practice cards (topics 09-19): previous-year questions from the IISc exam papers (2023-2025 midterms / finals)
   plus extra questions written at the same level. Each one is a flippable card: question on the front, solution on the back.
   kind2 'pyq' = taken from a university paper (source tells which), 'gen' = written for this deck. */
(function () {
  const TOP = {
    9: '09_Geometry_of_Constrained_Optimization_Tangent_Cone_and_LICQ',
    10: '10_Separating_Hyperplanes_and_Farkas_Lemma',
    11: '11_Karush_Kuhn_Tucker_Conditions_FONC_and_Sufficiency',
    12: '12_Second_Order_Optimality_Conditions_in_Constrained_Optimization',
    13: '13_Projections_onto_Convex_Sets',
    14: '14_Gradient_Projection_Algorithm_and_Convergence',
    15: '15_Active_Set_Methods_for_Quadratic_Programming',
    16: '16_Lagrangian_Duality_and_Slaters_Condition',
    17: '17_Wolfe_Duality',
    18: '18_Linear_Programming_Duality_and_Polyhedral_Geometry',
    19: '19_Penalty_and_Barrier_Methods'
  };
  const out = [];
  const count = {};
  function Q(t, kind2, source, marks, question, solution, takeaway) {
    count[t] = (count[t] || 0) + 1;
    out.push({ id: 600000 + t * 100 + count[t], subject: 'CMO', topicId: TOP[t], kind2, source, marks, question, solution, takeaway });
  }
  const R = String.raw;

  /* ============================ 09  Tangent cone & LICQ ============================ */
  Q(9, 'pyq', '2024 Final · Q1(g)', '1 mark', R`
<p><b>True or False, with a reason.</b> For a constrained problem it is found that at the optimal point $x^*$ we have $\nabla f(x^*) \neq 0$. Then at least one of the constraints must be active at $x^*$.</p>`, R`
<p><span class="ans">True.</span></p>
<p>Suppose no constraint were active. Then every constraint is slack, so a small ball around $x^*$ is entirely feasible, and $x^*$ would be a <i>local unconstrained</i> minimum of $f$. The first-order condition for that is $\nabla f(x^*)=0$, which contradicts the given.</p>
<p>So a non-zero gradient at a constrained optimum means the constraints are what is stopping you from going further downhill.</p>`,
  R`Non-zero gradient at the optimum $\Rightarrow$ something is pushing back: at least one active constraint.`);

  Q(9, 'pyq', '2025 Final · Q1(k)', '1 mark', R`
<p><b>True or False.</b> $f$ is minimised over a convex set $C\subset\mathbb{R}^d$. At the global minimiser $x^*$, <i>every</i> direction is a feasible direction (the feasible directions fill a whole ball $B(x^*,\delta)$ around $x^*$). Then no constraint is active at $x^*$.</p>`, R`
<p><span class="ans">True.</span></p>
<p>An active inequality $g_i(x^*)=0$ means $x^*$ sits on the boundary of $C$. On the boundary there is always some direction that points out of the set (for a linear constraint $a^\top d\lt 0$), so not all directions can be feasible.</p>
<p>If all directions are feasible then $x^*$ is an interior point, so all inequalities are slack.</p>`,
  R`All directions feasible $\Leftrightarrow$ interior point $\Leftrightarrow$ no active inequalities (and then $\nabla f(x^*)=0$).`);

  Q(9, 'gen', '', '5 marks', R`
<p>Let $C=\{x\in\mathbb{R}^2 : g_1(x)=x_2-x_1^2\ge 0,\; g_2(x)=-x_2\ge 0\}$ and look at $\bar x=(0,0)$.</p>
<p><span class="part">(a)</span> Describe $C$ and write down its tangent cone $T_C(\bar x)$.</p>
<p><span class="part">(b)</span> Compute the linearised cone $\{d : \nabla g_i(\bar x)^\top d\ge 0,\ i \text{ active}\}$. Is it equal to $T_C(\bar x)$?</p>
<p><span class="part">(c)</span> Does LICQ hold at $\bar x$?</p>`, R`
<p><span class="part">(a)</span> $x_2\ge x_1^2\ge 0$ and $x_2\le 0$ force $x_2=0$ and then $x_1=0$. So $C=\{(0,0)\}$ is a single point and $T_C(\bar x)=\{0\}$.</p>
<p><span class="part">(b)</span> $\nabla g_1(\bar x)=(0,1)$, $\nabla g_2(\bar x)=(0,-1)$, both active. Linearised cone: $d_2\ge 0$ and $-d_2\ge 0$, i.e. $\{d: d_2=0\}$, the whole $x_1$-axis. This is <b>bigger</b> than $T_C(\bar x)=\{0\}$, so they are not equal.</p>
<p><span class="part">(c)</span> $(0,1)$ and $(0,-1)$ are linearly dependent, so <span class="ans">LICQ fails</span>.</p>
<p>That is exactly the typical story: when LICQ fails, the linearised cone can over-estimate the true tangent cone, and KKT multipliers may not exist.</p>`,
  R`LICQ is what guarantees tangent cone $=$ linearised cone. When it fails, the linearisation can lie.`);

  Q(9, 'gen', '', '5 marks', R`
<p>$C=\{x\in\mathbb{R}^2: g_1(x)=1-x_1^2-x_2^2\ge 0,\ g_2(x)=1-x_1\ge 0\}$, point $\bar x=(1,0)$.</p>
<p><span class="part">(a)</span> Which constraints are active? Does LICQ hold?</p>
<p><span class="part">(b)</span> Find the tangent cone of $C$ and the linearised cone at $\bar x$.</p>
<p><span class="part">(c)</span> What does this tell you about "LICQ is necessary for the tangent cone to equal the linearised cone"?</p>`, R`
<p><span class="part">(a)</span> $g_1(\bar x)=0$, $g_2(\bar x)=0$: both active. $\nabla g_1=(-2,0)$, $\nabla g_2=(-1,0)$ are parallel, so <span class="ans">LICQ fails</span>.</p>
<p><span class="part">(b)</span> Linearised cone: $-2d_1\ge0$ and $-d_1\ge0$, so $\{d: d_1\le 0\}$. $C$ is the unit disc (the constraint $x_1\le1$ is redundant), and at $(1,0)$ its tangent cone is the half-plane $\{d_1\le 0\}$. <b>They are equal.</b></p>
<p><span class="part">(c)</span> LICQ is only a <i>sufficient</i> condition. It can fail while the cones still agree (here the second constraint is just redundant). So failing LICQ does not automatically mean KKT breaks; it only removes the guarantee.</p>`,
  R`LICQ $\Rightarrow$ cones agree, but not the other way round. Redundant constraints break LICQ harmlessly.`);

  Q(9, 'gen', '', '4 marks', R`
<p>Minimise $f(x)=x_1^2+x_2^2$ subject to $x_1+x_2\ge 2$. At $\hat x=(2,0)$:</p>
<p><span class="part">(a)</span> Describe the set of feasible directions and the set of descent directions.</p>
<p><span class="part">(b)</span> Is there a feasible descent direction? What does this say about $\hat x$?</p>`, R`
<p><span class="part">(a)</span> The constraint is active ($2+0=2$). Feasible directions: $d_1+d_2\ge 0$. Since $\nabla f(\hat x)=(4,0)$, descent directions satisfy $4d_1\lt0$, i.e. $d_1\lt 0$.</p>
<p><span class="part">(b)</span> Take $d=(-1,1)$: $d_1+d_2=0\ge0$ is feasible and $d_1=-1\lt0$ is descent. So a feasible descent direction exists and $\hat x$ is <span class="ans">not a local minimum</span>. (Moving along the line gets you to $(1,1)$, the real minimiser.)</p>`,
  R`At a local minimum there is no feasible descent direction. Finding one is the quickest way to reject a point.`);

  /* ============================ 10  Separating hyperplanes & Farkas ============================ */
  Q(10, 'pyq', '2024 MT3 · Q1(a)-(c)', '3 marks', R`
<p><b>True or False.</b></p>
<p><span class="part">(a)</span> The set $\{x\in\mathbb{R}^d : \|x-a\|>r\}$ is convex.</p>
<p><span class="part">(b)</span> If $f$ is convex then $\{x : f(x)\le f(x^{(0)})\}$ is convex.</p>
<p><span class="part">(c)</span> The separating hyperplane theorem applies only to halfspaces.</p>`, R`
<p><span class="part">(a)</span> <span class="ans">False.</span> It is the outside of a ball. Take $x=a+2r e$ and $y=a-2r e$; both are outside, but their midpoint $a$ is inside.</p>
<p><span class="part">(b)</span> <span class="ans">True.</span> Sublevel sets of convex functions are convex: if $f(x),f(y)\le c$ then $f(\theta x+(1-\theta)y)\le\theta f(x)+(1-\theta)f(y)\le c$.</p>
<p><span class="part">(c)</span> <span class="ans">False.</span> It separates a point from <i>any</i> closed convex set (and two disjoint convex sets, one compact); halfspaces are just one example.</p>`,
  R`Sublevel sets of convex functions are convex. The outside of a ball is not.`);

  Q(10, 'pyq', '2025 MT3 · Q1(b)', '4 marks', R`
<p>Let $C=\{x\in\mathbb{R}^d : 0\le x_i\le 1\}$ and $z\in\mathbb{R}^d$ with $z^\top e=-5$. Find a hyperplane that separates $z$ from $C$, and justify.</p>`, R`
<p>Since $\sum z_i=-5\lt0$, $z\notin C$. Let $w=P_C(z)-z$. Componentwise
$$w_i=\begin{cases}-z_i>0 & z_i\lt 0\\ 0 & 0\le z_i\le1\\ 1-z_i\lt0 & z_i>1\end{cases}$$
and $w\neq0$.</p>
<p>The projection property says $(z-P_C(z))^\top(x-P_C(z))\le0$ for all $x\in C$, i.e.
$$w^\top x \;\ge\; w^\top P_C(z)\qquad\forall x\in C .$$
Also $w^\top z = w^\top P_C(z)-\|w\|^2\lt w^\top P_C(z)$.</p>
<p>So the hyperplane $\{x: w^\top x=w^\top P_C(z)\}$ has all of $C$ on one side ($\ge$) and $z$ strictly on the other ($\lt$).</p>`,
  R`Separating hyperplane = normal $P_C(z)-z$, passing through $P_C(z)$.`);

  Q(10, 'gen', '', '4 marks', R`
<p>Use Farkas' lemma to decide whether $Ax=b,\ x\ge0$ has a solution, where
$$A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad b=\begin{pmatrix}-1\\1\end{pmatrix}.$$
If not, give a certificate.</p>`, R`
<p>Farkas: exactly one of (I) $Ax=b,\ x\ge0$ has a solution, or (II) $\exists y$ with $A^\top y\ge0$ and $b^\top y\lt0$.</p>
<p>Directly: $x_1+x_2=-1$ and $x_2=1$ give $x_1=-2\lt0$. So (I) fails.</p>
<p>Certificate for (II): take $y=(1,-1)$. Then $A^\top y=(1\cdot1+0\cdot(-1),\ 1\cdot1+1\cdot(-1))=(1,0)\ge0$ and $b^\top y=-1-1=-2\lt0$. &#10003;</p>
<p>Geometrically $y$ is the normal of a hyperplane through the origin with both columns of $A$ on the non-negative side and $b$ strictly on the negative side.</p>`,
  R`Farkas: $b$ is in the cone of the columns, or a hyperplane through $0$ separates $b$ from that cone.`);

  Q(10, 'gen', '', '5 marks', R`
<p>At a feasible point $\hat x$ of $\min f$ s.t. $g_1\ge0,\ g_2\ge0$ both active, we know $\nabla g_1=(1,0)$, $\nabla g_2=(1,1)$ and $\nabla f=(1,3)$.</p>
<p><span class="part">(a)</span> Can $\nabla f$ be written as $\lambda_1\nabla g_1+\lambda_2\nabla g_2$ with $\lambda\ge0$?</p>
<p><span class="part">(b)</span> If not, use Farkas to produce a feasible descent direction.</p>`, R`
<p><span class="part">(a)</span> Solve $(1,3)=\lambda_1(1,0)+\lambda_2(1,1)$: second coordinate gives $\lambda_2=3$, first gives $\lambda_1+3=1\Rightarrow\lambda_1=-2\lt0$. <span class="ans">No</span>, so $\hat x$ is not a KKT point.</p>
<p><span class="part">(b)</span> By Farkas there is $d$ with $\nabla g_i^\top d\ge0$ (feasible) and $\nabla f^\top d\lt0$ (descent). Need $d_1\ge0$, $d_1+d_2\ge0$, $d_1+3d_2\lt0$. Take $d=(3,-2)$: $3\ge0$, $1\ge0$, $3-6=-3\lt0$. &#10003;</p>
<p>So you can move to lower $f$ without leaving the feasible region: $\hat x$ is not optimal.</p>`,
  R`Not in the cone of active gradients $\Rightarrow$ Farkas hands you a feasible descent direction.`);

  Q(10, 'gen', '', '3 marks', R`
<p>Let $C=\{x\in\mathbb{R}^2:\|x\|\le1\}$ and $z=(3,4)$. Find a hyperplane that strictly separates $z$ from $C$, and a supporting hyperplane of $C$ closest to $z$.</p>`, R`
<p>$P_C(z)=z/\|z\|=(0.6,0.8)$, so the normal is $w=z-P_C(z)=(2.4,3.2)\propto(3,4)$.</p>
<p>For $x\in C$, Cauchy–Schwarz gives $3x_1+4x_2\le5\|x\|\le5$. At $z$: $3\cdot3+4\cdot4=25>5$.</p>
<p>So $3x_1+4x_2=5$ separates, and since it touches $C$ at $(0.6,0.8)$ it is the <span class="ans">supporting hyperplane</span> at the projection point. Any $3x_1+4x_2=c$ with $5\lt c\lt25$ also strictly separates.</p>`,
  R`Normal $=z-P_C(z)$, through $P_C(z)$: that is the supporting hyperplane at the nearest point.`);

  /* ============================ 11  KKT ============================ */
  Q(11, 'pyq', '2024 Final · Q3', '10 marks', R`
<p>$f:\mathbb{R}^3\to\mathbb{R}$ is convex and $C^1_L$. Consider
$$\min_{x\in\mathbb{R}^3} f(x)\ \text{ s.t. }\ \tfrac13(x_1x_2+x_2x_3+x_1x_3)\le1.5,\ \ x_1+ax_2\ge b,\ \ x_2+x_3\le10,\ \ x_3\ge0.5 .$$
At $\hat x=(1,1,1)^\top$ you only know $f(\hat x)=3$ and $\nabla f(\hat x)=(1,10,0)^\top$.</p>
<p><span class="part">(a)</span> Choose $a,b$ so that $\hat x$ is a KKT point. (5)</p>
<p><span class="part">(b)</span> True or False: the global optimal value of $f$ over the constraints is strictly less than 3. Justify. (5)</p>`, R`
<p><span class="part">(a)</span> Check the constraints at $(1,1,1)$: first $=1\lt1.5$, third $=2\lt10$, fourth $=1>0.5$: all slack. Since $\nabla f(\hat x)\ne0$, the only possible active one is $x_1+ax_2\ge b$. KKT: $\nabla f=\lambda(1,a,0)^\top$, $\lambda\ge0$, so $\lambda=1$ and $a=10$. Active: $1+10=b\Rightarrow b=11$.</p>
<p><span class="part">(b)</span> <span class="ans">False.</span> Consider the relaxed convex problem $\min f$ s.t. $x_1+10x_2\ge11$. $\hat x$ is a KKT point of it, hence its global minimiser (convex). $\hat x$ is also feasible for the original, which has <i>more</i> constraints, so the original optimum is $\ge$ the relaxed optimum $=f(\hat x)=3$ and $\le f(\hat x)$ since $\hat x$ is feasible. So the optimum is exactly 3.</p>`,
  R`KKT + convex $\Rightarrow$ global min of the relaxed problem. A feasible point of the tighter problem that attains it is optimal there too.`);

  Q(11, 'pyq', '2024 Final · Q4 (numbers tidied)', '5 marks', R`
<p>Consider $\min f(x)$ s.t. $g_i(x)\ge0$, $i=1,2,3$, but the inequality directions may be wrong. At a KKT point $x^{(0)}$ we know
$g_1=g_2=0,\ g_3=-4$ and
$$\nabla f=(4,-10,4),\ \ \nabla g_1=(1,-2,0),\ \ \nabla g_2=(0,1,-2),\ \ \nabla g_3=(-1,1,10).$$
Which inequalities are in the proper direction? Correct the wrong ones.</p>`, R`
<p>A KKT point is feasible. But $g_3(x^{(0)})=-4\lt0$ violates $g_3\ge0$, so the third inequality must really be $g_3\le0$ (it is then slack, $\lambda_3=0$).</p>
<p>With $g_3$ inactive, $\nabla f=\lambda_1\nabla g_1+\lambda_2\nabla g_2$:
first coordinate $\lambda_1=4$; third coordinate $-2\lambda_2=4\Rightarrow\lambda_2=-2$; second: $-2(4)+(-2)=-10$ &#10003;.</p>
<p>For constraints written $g_i\ge0$ we need $\lambda_i\ge0$. $\lambda_1=4$ is fine, but $\lambda_2=-2\lt0$, so <span class="ans">$g_2$ is also in the wrong direction</span> and should be $g_2\le0$ (then its multiplier flips to $+2$).</p>
<p><b>Answer:</b> $g_1\ge0$ is correct; $g_2$ and $g_3$ must be reversed to $\le0$.</p>`,
  R`Feasibility fixes slack constraints' direction; the sign of $\lambda$ fixes active ones.`);

  Q(11, 'pyq', '2024 Final · Q5', '10 marks', R`
<p>Let $u\in\mathbb{R}^d$ have distinct non-zero entries, $a=\min_iu_i$, $b=\max_iu_i$. Consider the LP
$$\max_x\ u^\top x\quad\text{s.t.}\quad\sum_{i}x_i\le1,\ \ x_i\ge0 .$$
<span class="part">(a)</span> If $\sum x_i\le1$ is <i>not</i> active at the optimum, what can you say about $a,b$ and the optimal value?</p>
<p><span class="part">(b)</span> Repeat if it <i>is</i> active at the optimum.</p>`, R`
<p>Write it as $\min -u^\top x$. With multipliers $\lambda\ge0$ for $\sum x_i\le1$ and $\lambda_i\ge0$ for $x_i\ge0$, stationarity is $-u_i+\lambda-\lambda_i=0$, i.e. $u_i=\lambda-\lambda_i$. Complementarity: $\lambda_ix_i=0$, $\lambda(\sum x_i-1)=0$. It is convex, so KKT is sufficient.</p>
<p><span class="part">(a)</span> Inactive $\Rightarrow\lambda=0\Rightarrow u_i=-\lambda_i\le0$ for all $i$; entries are non-zero so $u_i\lt0$, hence $\lambda_i>0$ and $x_i=0$ for all $i$. So $a\lt b\lt0$, $x^*=0$, optimal value $0$.</p>
<p><span class="part">(b)</span> Active: not all $\lambda_i$ can be positive (that forces $x=0$ and the sum constraint slack). So some $l$ has $\lambda_l=0$, giving $u_l=\lambda$, and $\lambda_i=\lambda-u_i\ge0$ for all $i$ means $\lambda\ge\max u_i$. Combined: $\lambda=b>0$ (the largest entry is positive). Then $x^*=e_l$ with $u_l=b$, optimal value $b$. Nothing is forced on $a$.</p>`,
  R`LP over a simplex: put all the mass on the best coordinate if it is positive, otherwise on nothing.`);

  Q(11, 'pyq', '2025 Final · Q2', '10 marks', R`
<p>Minimise $f(x)=e^{2x_2}+\tfrac12x_1^2-x_2$ over $x\in\mathbb{R}^2$ subject to $x_1^2+x_2^2\le10$ and $u^\top x\ge2$. For what values of $u$ is $x^{(0)}=(1,1)^\top$ a global minimum?</p>`, R`
<p>$\nabla^2f=\mathrm{diag}(1,4e^{2x_2})\succ0$, so $f$ is convex; the feasible set is convex; this is a convex program, so KKT at $x^{(0)}$ is <b>necessary and sufficient</b> (given feasibility).</p>
<p>Feasibility: $1+1=2\lt10$, so the ball constraint is slack. We need $u^\top x^{(0)}\ge2$; since $\nabla f(x^{(0)})=(1,\,2e^2-1)\neq0$ the linear constraint must be active: $u_1+u_2=2$.</p>
<p>KKT: $\nabla f(x^{(0)})=\lambda u$ with $\lambda>0$: $\lambda u_1=1$, $\lambda u_2=2e^2-1$. Adding: $2\lambda=2e^2$, so $\lambda=e^2$ and
$$u=\big(e^{-2},\ 2-e^{-2}\big).$$</p>
<p>Only this single $u$ works.</p>`,
  R`Convex + feasible + $\nabla f=\lambda\nabla g$ with $\lambda\ge0$ $\Rightarrow$ global min. Use the active constraint to pin down unknowns.`);

  Q(11, 'pyq', '2025 Final · Q4(a)-(c)', '10 marks', R`
<p>Consider $\max_x -\sum_{i=1}^dx_i\log x_i$ s.t. $\sum x_i=1$, $x_i\ge0$ ($x$ is a probability mass function).</p>
<p><span class="part">(a)</span> State the KKT conditions. (3)</p>
<p><span class="part">(b)</span> Find the global optimum and optimal value. (5)</p>
<p><span class="part">(c)</span> If instead we <i>minimise</i> the same objective, what is the optimum and where is it attained (take $0\log0=0$)? (2)</p>`, R`
<p><span class="part">(a)</span> Write it as $\min\sum x_i\log x_i$. With $\mu$ for $\sum x_i=1$ and $\lambda_i\ge0$ for $x_i\ge0$:
$$\log x_i+1+\mu-\lambda_i=0,\quad \lambda_ix_i=0,\quad x_i\ge0,\quad \sum x_i=1,\quad\lambda_i\ge0 .$$</p>
<p><span class="part">(b)</span> $\sum x_i\log x_i$ has positive-definite Hessian $\mathrm{diag}(1/x_i)$ on $x_i>0$, so the problem is convex and KKT is sufficient. $\log x_i\to-\infty$ at $x_i\to0$ means the slope pushes every $x_i$ off zero, so $\lambda_i=0$ and $\log x_i=-1-\mu$ is the same for all $i$: $x_i=\tfrac1d$. Optimal value of the maximisation: $-\sum\tfrac1d\log\tfrac1d=\ \log d$. <span class="ans">Max entropy = uniform distribution, value $\log d$.</span></p>
<p><span class="part">(c)</span> $-\sum x_i\log x_i\ge0$ on the simplex since $x_i\le1$. It is $0$ exactly when one $x_i=1$, the rest $0$. So the minimum is $0$, attained at the $d$ vertices $e_1,\dots,e_d$ (concave function minimised at extreme points).</p>`,
  R`Entropy: uniform maximises it, point masses minimise it. Maximum of concave, minimum of concave = at vertices.`);

  Q(11, 'gen', '', '5 marks', R`
<p>Minimise $f(x)=(x_1-2)^2+(x_2-1)^2$ subject to $x_1^2+x_2^2\le1$. Write the KKT system, solve it, and verify global optimality.</p>`, R`
<p>Write $g(x)=1-x_1^2-x_2^2\ge0$. KKT: $\nabla f=\lambda\nabla g$, $\lambda\ge0$, $\lambda g=0$:
$$2(x_1-2)=-2\lambda x_1,\quad 2(x_2-1)=-2\lambda x_2\ \Rightarrow\ (1+\lambda)x=(2,1).$$
$(2,1)$ lies outside the disc, so the constraint must be active ($\lambda>0$): $\|x\|=1$ gives $1+\lambda=\|(2,1)\|=\sqrt5$, so
$$\lambda=\sqrt5-1>0,\qquad x^*=\tfrac1{\sqrt5}(2,1).$$</p>
<p>$f$ is convex, the disc is convex, so KKT is sufficient: <span class="ans">$x^*$ is the global minimum</span>. (It is just the projection of $(2,1)$ onto the unit disc.)</p>`,
  R`Closest point of a convex set to an outside point = projection. KKT recovers it with $\lambda>0$.`);

  /* ============================ 12  Second-order conditions ============================ */
  Q(12, 'gen', '', '6 marks', R`
<p>Consider $\min x_1x_2$ s.t. $x_1+x_2=2$. Show $\hat x=(1,1)$ is a KKT point and use the second-order conditions to decide whether it is a local minimum.</p>`, R`
<p>With $L=x_1x_2-\lambda(x_1+x_2-2)$: $\nabla_x L=(x_2-\lambda,\ x_1-\lambda)=0$ gives $x_1=x_2=\lambda$, and the constraint then gives $\hat x=(1,1)$, $\lambda=1$: <b>KKT point</b>.</p>
<p>Hessian of the Lagrangian: $\nabla^2_{xx}L=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, <i>indefinite</i> on $\mathbb{R}^2$, so look only on the tangent space $\{d: d_1+d_2=0\}$, spanned by $d=(1,-1)$:
$$d^\top\nabla^2_{xx}L\,d=-2\lt0 .$$</p>
<p>The second-order <i>necessary</i> condition requires $\ge0$ on the tangent space, so it fails: <span class="ans">$\hat x$ is not a local minimum</span> (in fact on the line $x_1(2-x_1)$ has a maximum at 1).</p>`,
  R`First-order tells you where to look; the Hessian of $L$ on the tangent space tells you min, max or saddle.`);

  Q(12, 'gen', '', '7 marks', R`
<p>Minimise $f(x)=x_1+x_2$ subject to $x_1^2+x_2^2=2$.</p>
<p><span class="part">(a)</span> Find all KKT points.</p>
<p><span class="part">(b)</span> Classify each using the second-order conditions.</p>`, R`
<p>Let $L=x_1+x_2+\lambda(x_1^2+x_2^2-2)$. $\nabla_xL=0$: $1+2\lambda x_i=0\Rightarrow x_1=x_2=-\tfrac1{2\lambda}$. The constraint gives $2x_1^2=2$, so $x=\pm(1,1)$:
<br>$x=(-1,-1)$ with $\lambda=\tfrac12$, and $x=(1,1)$ with $\lambda=-\tfrac12$.</p>
<p>$\nabla^2_{xx}L=2\lambda I$. The tangent space at either point is $\{d:d_1+d_2=0\}$ (gradient of constraint is $\propto(1,1)$).</p>
<p>At $(-1,-1)$: $\lambda=\tfrac12$ gives $\nabla^2L=I\succ0$, so $d^\top\nabla^2Ld>0$: <span class="ans">strict local (and global) minimum</span>, value $-2$.</p>
<p>At $(1,1)$: $\lambda=-\tfrac12$ gives $-I$, so $d^\top\nabla^2Ld\lt0$: not a minimum, it is the maximum (value $2$).</p>`,
  R`Same constraint, same stationarity, opposite sign of $\lambda$: the second-order test separates min from max.`);

  Q(12, 'gen', '', '5 marks', R`
<p>Minimise $f(x)=x_2$ subject to $g(x)=x_2-x_1^2\ge0$. At $\bar x=(0,0)$ verify the KKT conditions and the second-order sufficient condition on the critical cone.</p>`, R`
<p>$L=f-\lambda g=x_2-\lambda(x_2-x_1^2)$. $\nabla f=(0,1)$, $\nabla g=(0,1)$ at $\bar x$, so $\lambda=1\ge0$; $g(\bar x)=0$ gives complementarity. <b>KKT holds</b>.</p>
<p>$\nabla^2_{xx}L=-\lambda\nabla^2g=-1\cdot\begin{pmatrix}-2&0\\0&0\end{pmatrix}=\begin{pmatrix}2&0\\0&0\end{pmatrix}$.</p>
<p>Critical cone (strict complementarity holds, $\lambda>0$): $\{d:\nabla g^\top d=0\}=\{d_2=0\}$, i.e. $d=(t,0)$. Then $d^\top\nabla^2Ld=2t^2>0$ for $t\ne0$.</p>
<p>So SOSC holds: <span class="ans">$\bar x$ is a strict local minimum</span>. The Hessian of $L$ is only positive <i>semi</i>definite on all of $\mathbb{R}^2$ (zero in the $x_2$ direction), but that direction is not critical.</p>`,
  R`SOSC only asks for $d^\top\nabla^2L\,d>0$ on critical directions, not for all $d$.`);

  Q(12, 'gen', '', '4 marks', R`
<p>Explain in your own words why the second-order condition for constrained problems is tested only on the tangent space / critical cone and not on all of $\mathbb{R}^d$.</p>`, R`
<p>Directions $d$ with $\nabla g_i^\top d\gt0$ for an active constraint with $\lambda_i>0$ already make $f$ increase to <b>first order</b>: $\nabla f^\top d=\sum\lambda_i\nabla g_i^\top d>0$. Curvature is irrelevant for them, no matter how negative.</p>
<p>The only directions where the first-order change is exactly zero are the <b>critical directions</b> ($\nabla g_i^\top d=0$ for active $i$ with $\lambda_i>0$). There first-order information gives no verdict, so we need the curvature of the <i>Lagrangian</i> (not of $f$ alone, since the constraint surface bends and that bending contributes $-\sum\lambda_i\nabla^2g_i$).</p>`,
  R`Critical cone $=$ where first-order is a tie; second-order breaks the tie, using $\nabla^2_{xx}L$ not $\nabla^2f$.`);

  /* ============================ 13  Projections ============================ */
  Q(13, 'pyq', '2024 MT3 · Q2(a)', '4 marks', R`
<p>For $C=\{x : a^\top x\ge b\}$ and $z\in\mathbb{R}^d$ with $a^\top z\lt b$, find $P_C(z)$ with a brief justification.</p>`, R`
<p>$P_C(z)=\arg\min_x\tfrac12\|x-z\|^2$ s.t. $a^\top x\ge b$. KKT: $x-z-\lambda a=0$, i.e. $x=z+\lambda a$, with $\lambda\ge0$ and $\lambda(a^\top x-b)=0$.</p>
<p>Since $z\notin C$ the constraint must be active: $a^\top z+\lambda\|a\|^2=b$, so $\lambda=\dfrac{b-a^\top z}{\|a\|^2}>0$ &#10003;. Hence
$$P_C(z)=z+\frac{b-a^\top z}{\|a\|^2}\,a .$$</p>
<p>Geometrically: slide $z$ along the normal $a$ until you hit the boundary.</p>`,
  R`Projection onto a halfspace: if inside, stay; if outside, move along the normal $a$ by exactly the violation.`);

  Q(13, 'pyq', '2025 MT3 · Q1(a)', '6 marks', R`
<p>Project $z\in\mathbb{R}^d$ onto the box $C=\{x:0\le x_i\le1\}$. State and solve the optimisation problem, with $z^\top e=-5$ given.</p>`, R`
<p>$P_C(z)=\arg\min\tfrac12\|x-z\|^2$ s.t. $0\le x_i\le1$. The Lagrangian separates over coordinates:
$$L=\sum_i\tfrac12(x_i-z_i)^2-\lambda_i(1-x_i)-\mu_ix_i .$$
KKT: $x_i-z_i+\lambda_i-\mu_i=0$, $0\le x_i\le1$, $\lambda_i,\mu_i\ge0$, $\lambda_i(1-x_i)=0$, $\mu_ix_i=0$.</p>
<p>Cases: $\lambda_i>0\Rightarrow x_i=1$; $\mu_i>0\Rightarrow x_i=0$; both zero $\Rightarrow x_i=z_i$. So
$$(P_C(z))_i=\min\{1,\max\{0,z_i\}\}$$
(clip each coordinate into $[0,1]$).</p>`,
  R`Separable constraints $\Rightarrow$ projection is coordinate-wise clipping.`);

  Q(13, 'pyq', '2025 Final · Q1(p); 2024 Final · Q1(f)', '2 marks', R`
<p><b>True or False, with a reason.</b></p>
<p><span class="part">(a)</span> Projection onto $\{x\in\mathbb{R}^d: x^\top e\le1\}$ does not exist because the set is unbounded.</p>
<p><span class="part">(b)</span> Let $z\notin C$ with $C$ closed and convex. There is only one $x^*\in C$ with $\|x^*-z\|\le\|x-z\|$ for all $x\in C$.</p>`, R`
<p><span class="part">(a)</span> <span class="ans">False.</span> Existence needs a closed set (and convexity gives uniqueness), not boundedness. Here $P_C(z)=z-\frac{(e^\top z-1)_+}{d}e$. Coercivity of $\|x-z\|^2$ handles the unbounded set.</p>
<p><span class="part">(b)</span> <span class="ans">True.</span> Existence: $\|x-z\|^2$ is coercive and the set closed. Uniqueness: strict convexity of $\|x-z\|^2$ on a convex set.</p>`,
  R`Closed + convex $\Rightarrow$ the projection exists and is unique, bounded or not.`);

  Q(13, 'gen', '', '4 marks', R`
<p>Compute the projection of $z=(3,-1,2)$ onto <span class="part">(a)</span> the hyperplane $\{x: e^\top x=1\}$ and <span class="part">(b)</span> the ball $\{\|x\|\le2\}$.</p>`, R`
<p><span class="part">(a)</span> $P(z)=z-\dfrac{e^\top z-1}{\|e\|^2}e=(3,-1,2)-\dfrac{4-1}{3}(1,1,1)=(2,-2,1)$. Check: $2-2+1=1$ &#10003;.</p>
<p><span class="part">(b)</span> $\|z\|=\sqrt{14}>2$, so scale to the boundary: $P(z)=\dfrac{2}{\sqrt{14}}(3,-1,2)$.</p>`,
  R`Hyperplane: subtract the violation along the normal. Ball: rescale if outside.`);

  Q(13, 'gen', '', '6 marks', R`
<p>Prove that the projection onto a closed convex set $C$ is non-expansive: $\|P_C(x)-P_C(y)\|\le\|x-y\|$.</p>`, R`
<p>Let $p=P_C(x)$, $q=P_C(y)$. The projection property says $(x-p)^\top(w-p)\le0$ for all $w\in C$. Use it twice:</p>
<p>with $w=q$: $(x-p)^\top(q-p)\le0$; with the roles swapped ($w=p$): $(y-q)^\top(p-q)\le0$.</p>
<p>Add them (note $(y-q)^\top(p-q)=-(y-q)^\top(q-p)$):
$$\big[(x-y)-(p-q)\big]^\top(q-p)\le0\ \Longrightarrow\ \|p-q\|^2\le(x-y)^\top(p-q).$$
By Cauchy–Schwarz the right side is $\le\|x-y\|\|p-q\|$. Divide by $\|p-q\|$ (if non-zero):
$$\|p-q\|\le\|x-y\|\ \blacksquare$$</p>`,
  R`Non-expansiveness = why gradient projection inherits the convergence rates of plain gradient descent.`);

  /* ============================ 14  Gradient projection ============================ */
  Q(14, 'pyq', '2024 MT3 · Q2(b)-(c)', '11 marks', R`
<p>$\min f(x)$ s.t. $a^\top x\ge b$, $f\in C^1_L$ with $L=5$. Gradient projection: $x^{(k+1)}=P_C\big(x^{(k)}-0.2\nabla f(x^{(k)})\big)$.</p>
<p><span class="part">(b)</span> Assume $a^\top x^{(k)}=b$ and $a^\top\nabla f(x^{(k)})>0$. (i) Find $x^{(k+1)}$. (3) (ii) True or False: $\nabla f(x^{(k)})^\top(x^{(k+1)}-x^{(k)})>0$. Justify. (3)</p>
<p><span class="part">(c)</span> If the scheme converges to $\hat x$, what can you say about $\hat x$? (5)</p>`, R`
<p><span class="part">(b)(i)</span> Put $z=x^{(k)}-0.2\nabla f$. Then $a^\top z=b-0.2a^\top\nabla f\lt b$, so $z\notin C$ and the halfspace formula gives
$$x^{(k+1)}=z+\frac{b-a^\top z}{\|a\|^2}a=x^{(k)}-0.2\nabla f+0.2\,\frac{a^\top\nabla f}{\|a\|^2}\,a .$$</p>
<p><span class="part">(ii)</span> <span class="ans">False.</span> $\nabla f^\top(x^{(k+1)}-x^{(k)})=-0.2\Big(\|\nabla f\|^2-\dfrac{(\nabla f^\top a)^2}{\|a\|^2}\Big)\le0$ by Cauchy–Schwarz. The step is a (weak) descent direction, the projection only removes the component that would leave $C$.</p>
<p><span class="part">(c)</span> At convergence $\hat x=P_C(\hat x-0.2\nabla f(\hat x))$. By the projection property, for all $x\in C$: $(\hat x-0.2\nabla f(\hat x)-\hat x)^\top(x-\hat x)\le0$, i.e.
$$\nabla f(\hat x)^\top(x-\hat x)\ge0\quad\forall x\in C ,$$
the first-order necessary condition for a local minimum over $C$. For convex $f$ this is also sufficient: $\hat x$ is a global minimum.</p>`,
  R`Fixed point of gradient projection $\Leftrightarrow$ the first-order condition $\nabla f(\hat x)^\top(x-\hat x)\ge0$ on $C$.`);

  Q(14, 'pyq', '2025 MT3 · Q2(a),(c)', '8 marks', R`
<p>$\min f(x)$ s.t. $Ax=b$, $f$ convex $C^1_L$, $A\in\mathbb{R}^{m\times d}$, $\mathrm{rank}(A)=m$. Use gradient projection with constant step $\alpha$.</p>
<p><span class="part">(a)</span> State the gradient-projection update. (3)</p>
<p><span class="part">(c)</span> Let the algorithm converge at $\hat x$. State and prove a relationship between $f(x)$ and $f(\hat x)$ for any feasible $x$. (5)</p>`, R`
<p><span class="part">(a)</span> Projection onto $C=\{Ax=b\}$: $P_C(z)=Pz+A^\top(AA^\top)^{-1}b$ with $P=I-A^\top(AA^\top)^{-1}A$. For $x\in C$, $Px+A^\top(AA^\top)^{-1}b=x$. Then
$$x^{(t+1)}=P_C\big(x^{(t)}-\alpha\nabla f(x^{(t)})\big)=x^{(t)}-\alpha P\nabla f(x^{(t)}) .$$</p>
<p><span class="part">(c)</span> At convergence $P\nabla f(\hat x)=0$. Take any feasible $x$ and $v=x-\hat x$, so $Av=0$ and hence $Pv=v$. Then
$$\nabla f(\hat x)^\top v=\nabla f(\hat x)^\top Pv=v^\top P\nabla f(\hat x)=0 .$$
By convexity $f(x)\ge f(\hat x)+\nabla f(\hat x)^\top(x-\hat x)=f(\hat x)$. So $f(\hat x)\le f(x)$ for <b>every</b> feasible $x$: <span class="ans">$\hat x$ is a global minimiser</span>.</p>`,
  R`$P$ keeps only the part of the gradient lying in the null space of $A$: zero projected gradient $\Rightarrow$ optimal.`);

  Q(14, 'gen', '', '5 marks', R`
<p>$f(x)=(x_1-3)^2+(x_2+1)^2$ on the box $C=[0,1]^2$. Run gradient projection from $x^{(0)}=(0.5,0.5)$ with $\alpha=0.25$ for two iterations. What happens, and is the limit optimal?</p>`, R`
<p>$\nabla f=(2(x_1-3),2(x_2+1))$. At $x^{(0)}$: $\nabla f=(-5,3)$, so $z=(0.5+1.25,\ 0.5-0.75)=(1.75,-0.25)$. Clip into the box: $x^{(1)}=(1,0)$.</p>
<p>At $x^{(1)}$: $\nabla f=(-4,2)$, $z=(1+1,\ 0-0.5)=(2,-0.5)\to$ clip $\to(1,0)$. So $x^{(2)}=x^{(1)}$: a <b>fixed point</b>.</p>
<p>Optimal? $f$ is convex and separable; its minimiser over the box is clip of the unconstrained minimiser $(3,-1)$, i.e. $(1,0)$ &#10003;. Also $\nabla f(1,0)^\top(x-(1,0))=-4(x_1-1)+2x_2\ge0$ on the box. Done in one step, since the box projection is exact and the problem is separable.</p>`,
  R`Fixed point of projected gradient $=$ stationary point; for convex $f$ it is a global min.`);

  Q(14, 'pyq', '2025 Final · Q1(q); 2024 Final · Q1(i)', '2 marks', R`
<p><b>True or False, with a reason.</b></p>
<p><span class="part">(a)</span> Projected gradient descent always converges to a point whose gradient is zero.</p>
<p><span class="part">(b)</span> Gradient projection finds the global minimum of a convex programming problem in a finite number of iterations.</p>`, R`
<p><span class="part">(a)</span> <span class="ans">False.</span> It converges to a point satisfying $\nabla f(x)^\top(y-x)\ge0$ on $C$; if the optimum is on the boundary the gradient there is non-zero (e.g. $\min x$ over $[1,2]$, gradient $1$ at $x^*=1$).</p>
<p><span class="part">(b)</span> <span class="ans">False.</span> In general it converges asymptotically with an $O(1/k)$ rate for convex $C^1_L$ functions. Finite termination happens only in special cases (as in the box example above).</p>`,
  R`Projected gradient converges to a <i>stationary</i> point on $C$, not a zero-gradient point.`);

  /* ============================ 15  Active set ============================ */
  Q(15, 'pyq', '2023 MT3 · Q2', '15 marks', R`
<p>$\min f(x)=\tfrac12x^\top Qx-h^\top x$ s.t. $a^{(i)\top}x\ge b_i$, $Q\succ0$. After $k$ iterations the feasible $x^{(k)}$ has working set $W^{(k)}=\{1,2,3\}$ and:</p>
<ul>
<li>$g_k=\nabla f(x^{(k)})=\sum_{i=1}^3\mu_ia^{(i)}$.</li>
<li>Constraint $3$ must be dropped to progress. The new direction is $u=re_1$ ($r$ scalar).</li>
<li>$Q_{11}=2$, $|r|=2$, $a^{(3)}_1=-\tfrac12$.</li>
</ul>
<p><span class="part">(a)</span> True/False: (i) $\{1,2\}$ is the active set at optimality. (ii) $u$ is a feasible direction. (iii) $x^{(k)}+u$ may not be feasible for constraint 3. (iv) $x^{(k)}+u$ is a feasible point. (v) $u$ is a descent direction.</p>
<p><span class="part">(b)</span> Compute $u^\top a^{(i)}$, $i=1,2,3$. (5)</p>
<p><span class="part">(c)</span> Find $g_k^\top u$ and $f(x^{(k)}+u)-f(x^{(k)})$. (5)</p>`, R`
<p><span class="part">(b)</span> $u$ solves $\min_y g_k^\top y+\tfrac12y^\top Qy$ s.t. $y^\top a^{(1)}=y^\top a^{(2)}=0$, so $u^\top a^{(1)}=u^\top a^{(2)}=0$. Optimality: $g_k+Qu=\tilde\mu_1a^{(1)}+\tilde\mu_2a^{(2)}$, and $g_k=\sum\mu_ia^{(i)}$, so $Qu=(\tilde\mu_1-\mu_1)a^{(1)}+(\tilde\mu_2-\mu_2)a^{(2)}-\mu_3a^{(3)}$. Multiply by $u^\top$:
$$u^\top Qu=-\mu_3\,u^\top a^{(3)}=-\mu_3\,r\,a^{(3)}_1 .$$
Constraint 3 was dropped because $\mu_3\lt0$, and $u^\top Qu>0$, so $r\,a^{(3)}_1>0$. With $a^{(3)}_1=-\tfrac12$ this forces $r=-2$. Hence
$$u^\top a^{(1)}=0,\quad u^\top a^{(2)}=0,\quad u^\top a^{(3)}=r\,a^{(3)}_1=\mathbf{1}.$$</p>
<p><span class="part">(c)</span> Since $u\perp a^{(1)},a^{(2)}$: $g_k^\top u=\sum\mu_ia^{(i)\top}u=\mu_3\cdot1$, while $u^\top Qu=-\mu_3\cdot1$ from (b). So $g_k^\top u=-u^\top Qu=-r^2Q_{11}=-8$ and
$$f(x^{(k)}+u)-f(x^{(k)})=g_k^\top u+\tfrac12u^\top Qu=-8+4=\mathbf{-4}.$$</p>
<p><span class="part">(a)</span> (i) <span class="ans">F</span> (we only know constraint 3 leaves; nothing says the final active set is $\{1,2\}$). (ii) <span class="ans">T</span> ($u^\top a^{(1)}=u^\top a^{(2)}=0$, $u^\top a^{(3)}=1>0$). (iii) <span class="ans">F</span>: $a^{(3)\top}(x^{(k)}+u)=b_3+1\ge b_3$, still feasible for 3. (iv) <span class="ans">F</span>: constraints outside $W$ may be violated by a full step. (v) <span class="ans">T</span> ($g_k^\top u=-8<0$).</p>`,
  R`Dropped constraint $\Rightarrow\mu\lt0\Rightarrow$ the new direction moves <i>into</i> the dropped constraint's feasible side, $u^\top a=r a_1>0$.`);

  Q(15, 'pyq', '2025 MT3 · Q3', '10 marks', R`
<p>$f(x)=\tfrac12x^\top Qx+h^\top x+c$, $Q\succ0$, subject to $x^\top a^{(i)}\ge b_i$, $i\in[m]$. Use the Active-set algorithm. Let $\hat x$ be feasible and $\hat x=\arg\min f$ s.t. $x^\top a^{(i)}=b_i$, $i\in S$.</p>
<p><span class="part">(a)</span> Devise a test for whether $\hat x$ is optimal for the inequality problem. (3)</p>
<p><span class="part">(b)</span> $\hat x$ fails the test. (i) Algorithm replaces $S$ by $\tilde S$: how are they related? (2) (ii) Let $\tilde x=\arg\min f$ s.t. equalities in $\tilde S$. Prove or disprove: $\tilde x-\hat x$ is a feasible descent direction. (5)</p>`, R`
<p><span class="part">(a)</span> Solve the equality-constrained QP on $S$ to get $(\hat x,\hat\lambda)$. If all $\hat\lambda_i\ge0$, KKT holds and (since $Q\succ0$, convex) $\hat x$ is optimal. If some $\hat\lambda_i\lt0$, dropping that constraint lets $f$ decrease.</p>
<p><span class="part">(b)(i)</span> Drop the constraint $d$ with $\hat\lambda_d\lt0$: $\tilde S=S\setminus\{d\}$, i.e. $\tilde S\cup\{d\}=S$.</p>
<p><span class="part">(ii)</span> <span class="ans">True</span>, with $p=\tilde x-\hat x$. Since $\nabla f(\hat x)=Q\hat x+h=\sum_{i\in\tilde S}\hat\lambda_ia^{(i)}+\hat\lambda_da^{(d)}$ and $\nabla f(\tilde x)=\sum_{i\in\tilde S}\tilde\lambda_ia^{(i)}$, subtracting gives $Qp=\sum_{\tilde S}(\tilde\lambda_i-\hat\lambda_i)a^{(i)}-\hat\lambda_da^{(d)}$. Both $\hat x,\tilde x$ satisfy the equalities in $\tilde S$, so $p^\top a^{(i)}=0$ for $i\in\tilde S$; thus
$$p^\top Qp=-\hat\lambda_d\,p^\top a^{(d)}>0\ (\text{as }p\ne0)\ \Longrightarrow\ p^\top a^{(d)}>0\ \text{because }\hat\lambda_d\lt0 .$$
<b>Feasible</b>: $p^\top a^{(i)}=0$ for $\tilde S$ and $p^\top a^{(d)}>0$ moves into the dropped constraint's feasible side. <b>Descent</b>: $\nabla f(\hat x)^\top p=\hat\lambda_dp^\top a^{(d)}\lt0$.</p>`,
  R`Negative multiplier $=$ the constraint is holding you back; drop it, solve again, and the step is feasible and descent for that constraint.`);

  Q(15, 'gen', '2024 MT3 · Q1(d) idea', '8 marks', R`
<p>Run the active-set method on $\min\ \tfrac12\|x\|^2-h^\top x$ with $h=(2,2)$, subject to (1) $x_1\ge0$, (2) $x_2\ge0$, (3) $-x_1-x_2\ge-2$. Start at $x^{(0)}=(0,0)$ with $W=\{1,2\}$.</p>
<p>Trace every iteration (direction, step, working-set change) until optimal. Then answer: <i>once the working set size starts decreasing, can it increase again?</i></p>`, R`
<p><b>Iter 0.</b> $x=(0,0)$, $g=Qx-h=(-2,-2)=\mu_1(1,0)+\mu_2(0,1)\Rightarrow\mu=(-2,-2)$: both negative. Drop constraint 1: $W=\{2\}$.</p>
<p><b>Iter 1.</b> EQP with $x_2=0$: direction $p=(2,0)$ (minimise $-2p_1+\tfrac12p_1^2$). Max step to constraint 3: $x_1+x_2\le2\Rightarrow\alpha_{\max}=1$. Take $\alpha=1$ (blocking): $x=(2,0)$, add constraint 3: $W=\{2,3\}$.</p>
<p><b>Iter 2.</b> $g=(2,0)-(2,2)=(0,-2)=\mu_2(0,1)+\mu_3(-1,-1)\Rightarrow\mu_3=0,\ \mu_2=-2\lt0$. Drop constraint 2: $W=\{3\}$.</p>
<p><b>Iter 3.</b> EQP on $x_1+x_2=2$: $p=(-1,1)$ (from $\min\,2t+t^2$ with $p=(t,-t)$, $t=-1$). $\alpha_{\max}$ large; $\alpha=1$: $x=(1,1)$.</p>
<p><b>Iter 4.</b> $g=(1,1)-(2,2)=(-1,-1)=\mu_3(-1,-1)\Rightarrow\mu_3=1\ge0$: <span class="ans">optimal, $x^*=(1,1)$</span>.</p>
<p>Working-set sizes: $2\to1\to2\to1\to1$. It went down and then <b>up</b> again, so the claim "once it starts decreasing it cannot increase" is <span class="ans">False</span>.</p>`,
  R`Active set: drop negative multipliers, add blocking constraints. The working set can shrink and grow many times.`);

  /* ============================ 16  Lagrangian duality ============================ */
  Q(16, 'pyq', '2023 MT3 · Q1 (constant tidied)', '15 marks', R`
<p>Consider $\min_{x\in\mathbb{R}^2}f(x)=-\tfrac12(x_1-1)^2+\tfrac12(x_2-2)^2$ s.t. $x_1^2+x_2^2\le1$. (P)</p>
<p><span class="part">(a)</span> Is $f$ convex? (2) <span class="part">(b)</span> For what $\lambda$ is the Lagrangian convex in $x$? (2) <span class="part">(c)</span> Compute the dual function $h(\lambda)$ and its domain. (3) <span class="part">(d)</span> State the dual problem; is it convex or concave? (3) <span class="part">(e)</span> Given the dual optimum $\lambda^*$, find a primal feasible $x^*$ whose value matches the dual value. (5)</p>`, R`
<p><span class="part">(a)</span> <span class="ans">No.</span> $\nabla^2f=\mathrm{diag}(-1,1)$ is indefinite.</p>
<p><span class="part">(b)</span> $L=f+\lambda(x_1^2+x_2^2-1)$ has Hessian $\mathrm{diag}(-1+2\lambda,\ 1+2\lambda)$. Convex iff both $\ge0$, i.e. $\lambda\ge\tfrac12$.</p>
<p><span class="part">(c)</span> For $\lambda>\tfrac12$, $\nabla_xL=0$ gives $x_1=-\dfrac1{2\lambda-1}$, $x_2=\dfrac2{2\lambda+1}$, and
$$h(\lambda)=\tfrac32-\lambda-\tfrac12\Big(\tfrac1{2\lambda-1}+\tfrac4{2\lambda+1}\Big),\quad\lambda>\tfrac12,$$
and $-\infty$ otherwise (at $\lambda\lt\frac12$ the $x_1$ direction is concave and $L\to-\infty$).</p>
<p><span class="part">(d)</span> Dual: $\max_{\lambda>1/2}h(\lambda)$. $h''=-\dfrac4{(2\lambda-1)^3}-\dfrac{16}{(2\lambda+1)^3}\lt0$: <span class="ans">concave</span> (the dual is always concave anyway).</p>
<p><span class="part">(e)</span> $\lambda^*>\tfrac12$ is interior, so $h'(\lambda^*)=0$: $\dfrac1{(2\lambda^*-1)^2}+\dfrac4{(2\lambda^*+1)^2}=1$, which says exactly $\|x^*\|^2=1$ for $x^*=\big(-\tfrac1{2\lambda^*-1},\tfrac2{2\lambda^*+1}\big)$. So $x^*$ is feasible, minimises $L(\cdot,\lambda^*)$ and satisfies complementarity ($\|x^*\|=1$), hence $f(x^*)=L(x^*,\lambda^*)=h(\lambda^*)$.</p>
<p>A <b>non-convex problem with strong duality</b> (zero gap).</p>`,
  R`Dual function is always concave; a non-convex primal can still have zero gap (here the sphere constraint is the "S-lemma" case).`);

  Q(16, 'pyq', '2024 MT3 · Q3 (b)-(d)', '12 marks', R`
<p>$\min_{x\in\mathbb{R}^3}f(x)=x_1^2-2x_2^2+4x_3^2+2\sum_{i=1}^3r_ix_i$ s.t. $\sum x_i^2=1$. Given: C1: $\dfrac{r_1^2}{6}+\dfrac{r_2^2}{3}+\dfrac{r_3^2}{9}=5$; C2: $\Big(\dfrac{r_1}{6}\Big)^2+\Big(\dfrac{r_2}{3}\Big)^2+\Big(\dfrac{r_3}{9}\Big)^2=1$.</p>
<p><span class="part">(b)</span> Find the dual function $g(\mu)$ and its feasible set. <span class="part">(c)</span> Find the dual optimal value and where it is attained. <span class="part">(d)</span> Show the primal optimum equals this value.</p>`, R`
<p><span class="part">(b)</span> $L=x_1^2(1+\mu)+x_2^2(\mu-2)+x_3^2(4+\mu)+2\sum r_ix_i-\mu$. Bounded below iff all three coefficients $>0$, i.e. $\mu>2$. Minimiser $x_i=-r_i/c_i$ with $c=(1+\mu,\ \mu-2,\ 4+\mu)$, and
$$g(\mu)=-\mu-\Big(\frac{r_1^2}{1+\mu}+\frac{r_2^2}{\mu-2}+\frac{r_3^2}{4+\mu}\Big),\qquad\mu>2 .$$</p>
<p><span class="part">(c)</span> $g$ is concave, so $g'(\mu)=0$ is sufficient: $1=\sum r_i^2/c_i^2$. At $\mu=5$, $c=(6,3,9)$ and C2 says exactly $\sum r_i^2/c_i^2=1$. So $\mu^*=5$, and using C1: $g(5)=-5-\sum r_i^2/c_i=-5-5=\mathbf{-10}$.</p>
<p><span class="part">(d)</span> At $\mu=5$ the minimiser $x_i=-r_i/c_i$ has $\|x\|^2=\sum r_i^2/c_i^2=1$ (C2): it is <b>feasible</b>, and by complementarity-by-equality $f(x)=L(x,5)=g(5)=-10$. Weak duality gives $f^*\ge-10$ and this point attains it: $f^*=-10$, strong duality holds although $f$ is non-convex.</p>`,
  R`If the Lagrangian minimiser at the dual optimum is primal feasible, there is no gap, convex or not.`);

  Q(16, 'pyq', '2024 Final · Q1(j)', '1 mark', R`
<p>For a constrained problem there is a dual feasible point with dual objective value $-1$ and a primal feasible $\bar x$ with $f(\bar x)=0.5$. True or False: $f(\bar x)-f(x^*)\le1.5$.</p>`, R`
<p><span class="ans">True.</span> Weak duality sandwiches the optimum: $-1\le d^*\le p^*=f(x^*)\le f(\bar x)=0.5$. Hence $f(\bar x)-f(x^*)\le0.5-(-1)=1.5$.</p>
<p>Any dual feasible value is a lower bound, any primal feasible value an upper bound: the gap tells you how far from optimal you can be.</p>`,
  R`Dual value $\le p^*\le$ primal value. The difference is a certificate of sub-optimality.`);

  Q(16, 'gen', '', '6 marks', R`
<p>Consider the classic example $\min e^{-x}$ s.t. $x^2/y\le0$ over the domain $y>0$.</p>
<p><span class="part">(a)</span> Find $p^*$. <span class="part">(b)</span> Find the dual function and $d^*$. <span class="part">(c)</span> Explain why this does not contradict strong duality for convex problems.</p>`, R`
<p><span class="part">(a)</span> $x^2/y\le0$ with $y>0$ forces $x=0$, so the feasible set is $\{(0,y):y>0\}$ and $p^*=e^0=\mathbf1$.</p>
<p><span class="part">(b)</span> $g(\lambda)=\inf_{x,\,y>0}\big(e^{-x}+\lambda x^2/y\big)$. For fixed $x$, send $y\to\infty$ to kill the second term, then $x\to\infty$ so $e^{-x}\to0$: $g(\lambda)=0$ for all $\lambda\ge0$. So $d^*=\mathbf0$, <b>duality gap $=1$</b>.</p>
<p><span class="part">(c)</span> The problem is convex, but there is no strictly feasible point (every feasible point has $x^2/y=0$, never $\lt0$): <span class="ans">Slater's condition fails</span>, so strong duality is not guaranteed. This is exactly why Slater's condition is needed.</p>`,
  R`Convex is not enough for zero gap: you need a strictly feasible point (Slater).`);

  Q(16, 'gen', '', '3 marks', R`
<p>Prove weak duality: for $\min f(x)$ s.t. $g_i(x)\le0$, $h(\lambda)=\inf_xL(x,\lambda)$ with $\lambda\ge0$ satisfies $h(\lambda)\le f(x)$ for every feasible $x$.</p>`, R`
<p>For feasible $x$ and $\lambda\ge0$: $\lambda_ig_i(x)\le0$, so
$$h(\lambda)=\inf_zL(z,\lambda)\le L(x,\lambda)=f(x)+\sum\lambda_ig_i(x)\le f(x).$$
Taking the infimum over feasible $x$: $h(\lambda)\le p^*$, hence $d^*\le p^*$. $\blacksquare$</p>`,
  R`$\lambda\ge0$ and $g\le0$ make the penalty term non-positive: the Lagrangian under-estimates $f$ on the feasible set.`);

  /* ============================ 17  Wolfe duality ============================ */
  Q(17, 'pyq', '2024 MT3 · Q4 (multiplier names swapped)', '5 marks', R`
<p>$\min_{x\in\mathbb{R}^d}\tfrac12\|x\|^2$ s.t. $a^\top x\le-b$, $c^\top x\ge b$, where $b>0$.</p>
<p><span class="part">(a)</span> State the Wolfe dual (no primal variables). (1) <span class="part">(b)</span> If $a^\top c=0$ and $\|a\|=\|c\|=r$, solve it. (1) <span class="part">(c)</span> Solve the primal and compare. (3)</p>`, R`
<p><span class="part">(a)</span> $L=\tfrac12\|x\|^2+\lambda_1(a^\top x+b)+\lambda_2(b-c^\top x)$, $\lambda_i\ge0$. Stationarity: $x=\lambda_2c-\lambda_1a$. Substituting,
$$g(\lambda)=-\tfrac12\|\lambda_2c-\lambda_1a\|^2+b(\lambda_1+\lambda_2),\qquad\lambda_1,\lambda_2\ge0 .$$</p>
<p><span class="part">(b)</span> With $a\perp c$: $\|\lambda_2c-\lambda_1a\|^2=r^2(\lambda_1^2+\lambda_2^2)$. Maximise $-\tfrac{r^2}2(\lambda_1^2+\lambda_2^2)+b(\lambda_1+\lambda_2)$: $\lambda_1=\lambda_2=b/r^2$ and optimal value $\dfrac{b^2}{r^2}$.</p>
<p><span class="part">(c)</span> From stationarity $x^*=\dfrac b{r^2}(c-a)$, $\|x^*\|^2=\dfrac{b^2}{r^4}\cdot2r^2$, so the primal value is $\tfrac12\|x^*\|^2=\dfrac{b^2}{r^2}$. <span class="ans">Equal to the dual value</span>: zero gap, as expected for a convex problem with feasible constraints.</p>`,
  R`Wolfe dual: put the stationarity condition in, remove $x$ using it, maximise over $\lambda\ge0$.`);

  Q(17, 'pyq', '2024 MT3 · Q1(e); 2025 Final · Q1(n)', '2 marks', R`
<p><b>True or False.</b></p>
<p><span class="part">(a)</span> For a <i>convex</i> optimisation problem, the Lagrange dual and the Wolfe dual give the same dual problem.</p>
<p><span class="part">(b)</span> The dual of a quadratic programming problem is another quadratic program.</p>`, R`
<p><span class="part">(a)</span> <span class="ans">True.</span> With convex $f,g_i$ and $\lambda\ge0$, $L(\cdot,\lambda)$ is convex in $x$, so $\inf_xL$ is attained exactly where $\nabla_xL=0$. That is the Wolfe dual's constraint, so the two coincide. (For non-convex problems Wolfe's constraint can include non-minimising stationary points, so they can differ.)</p>
<p><span class="part">(b)</span> <span class="ans">True.</span> Eliminating $x=Q^{-1}(A^\top\lambda-h)$ leaves a concave quadratic in $\lambda$ with linear constraints $\lambda\ge0$.</p>`,
  R`Convex $\Rightarrow$ stationary point of $L$ $=$ minimiser of $L$: Wolfe dual equals the Lagrange dual.`);

  Q(17, 'gen', '', '5 marks', R`
<p>Derive the Wolfe dual of the LP $\min c^\top x$ s.t. $Ax\ge b$ and identify it.</p>`, R`
<p>$L=c^\top x-\lambda^\top(Ax-b)$, $\lambda\ge0$. Wolfe's stationarity: $\nabla_xL=c-A^\top\lambda=0$. At such points $L=c^\top x-\lambda^\top Ax+\lambda^\top b=(c-A^\top\lambda)^\top x+\lambda^\top b=\lambda^\top b$. So
$$\max_\lambda\ b^\top\lambda\quad\text{s.t.}\quad A^\top\lambda=c,\ \lambda\ge0 .$$
This is the standard LP dual (primal inequality form, free $x$).</p>`,
  R`The Wolfe dual of an LP is the LP dual: stationarity of $L$ becomes the dual equality constraint.`);

  Q(17, 'gen', '', '5 marks', R`
<p>Write the Wolfe dual of $\min\tfrac12x^\top Qx+h^\top x$ s.t. $Ax\ge b$ ($Q\succ0$). Then verify on $\min\tfrac12x^2$ s.t. $x\ge1$.</p>`, R`
<p>$L=\tfrac12x^\top Qx+h^\top x-\lambda^\top(Ax-b)$. Stationarity: $Qx=A^\top\lambda-h$, $x=Q^{-1}(A^\top\lambda-h)$. At such $x$: $L=\tfrac12x^\top Qx-x^\top Qx+\lambda^\top b$, so
$$\max_{\lambda\ge0}\ -\tfrac12(A^\top\lambda-h)^\top Q^{-1}(A^\top\lambda-h)+b^\top\lambda .$$
Example ($Q=1,h=0,A=1,b=1$): $\max_{\lambda\ge0}\ -\tfrac12\lambda^2+\lambda$, so $\lambda=1$, value $\tfrac12$. Primal: $x^*=1$, value $\tfrac12$. &#10003; Equal.</p>`,
  R`QP dual: concave quadratic in $\lambda$ with just $\lambda\ge0$: easier constraints than the primal.`);

  /* ============================ 18  LP duality & polyhedra ============================ */
  Q(18, 'pyq', '2025 MT3 · Q5', '10 marks', R`
<p>Consider $\min c^\top x$ s.t. $Ax=b,\ x\ge0$ (LP), $A\in\mathbb{R}^{m\times d}$.</p>
<p><span class="part">(a)</span> Compute the dual of (LP) (at most $m$ dual variables). (3)</p>
<p><span class="part">(b)</span> $x^*$ is a KKT point that is a BFS. Find a dual feasible solution. (5)</p>
<p><span class="part">(c)</span> Does strong duality hold? (2)</p>`, R`
<p><span class="part">(a)</span> $L=c^\top x-\mu^\top(Ax-b)-\lambda^\top x=(c-A^\top\mu-\lambda)^\top x+\mu^\top b$. Finite minimum needs $c-A^\top\mu-\lambda=0$ with $\lambda\ge0$, i.e. $A^\top\mu\le c$:
$$\max_\mu\ b^\top\mu\quad\text{s.t.}\quad A^\top\mu\le c .$$</p>
<p><span class="part">(b)</span> Split $A=[B,N]$ with $B$ the basis of the BFS, $x^*=(B^{-1}b,0)$. KKT gives $\mu,\lambda$ with $c=A^\top\mu+\lambda$, $\lambda_B=0$, $\lambda_N\ge0$. So $c_B=B^\top\mu\Rightarrow\mu^\top=c_B^\top B^{-1}$ and $c_N-N^\top\mu=\lambda_N\ge0$, i.e. $A^\top\mu\le c$: <span class="ans">$\mu=B^{-\top}c_B$ is dual feasible</span> (these $\lambda_N$ are the reduced costs).</p>
<p><span class="part">(c)</span> <span class="ans">Yes.</span> $c^\top x^*=c_B^\top B^{-1}b=\mu^\top b$: primal and dual values coincide.</p>`,
  R`Optimal BFS $\Rightarrow$ dual solution $\mu=B^{-\top}c_B$; reduced costs $\ge0$ are exactly dual feasibility.`);

  Q(18, 'pyq', '2025 Final · Q5', '10 marks', R`
<p>$\min x_1-x_2$ s.t. $2x_1+5x_2\ge10$, $x_1+x_2\ge1$, $x\ge0$.</p>
<p><span class="part">(a)</span> Find the dual of $\min c^\top x$ s.t. $Ax\ge b,\ x\ge0$. (2) <span class="part">(b)</span> Is there a dual feasible point for the given problem? (2) <span class="part">(c)</span> Find the optimal value from first principles. (1) <span class="part">(d)</span> Replace the first constraint by $2x_1+5x_2\le10$. Compute the optimal primal and dual values. (5)</p>`, R`
<p><span class="part">(a)</span> $\max b^\top y$ s.t. $A^\top y\le c$, $y\ge0$.</p>
<p><span class="part">(b)</span> Here $A^\top y\le c$ reads $2y_1+y_2\le1$ and $5y_1+y_2\le-1$ with $y\ge0$. The second is impossible for non-negative $y$. <span class="ans">Dual infeasible.</span></p>
<p><span class="part">(c)</span> Primal is feasible, e.g. $x=(0,t)$ for any $t\ge2$ is feasible, with objective $-t\to-\infty$. So the optimal value is <span class="ans">$-\infty$</span> (dual infeasible + primal feasible $\Rightarrow$ primal unbounded).</p>
<p><span class="part">(d)</span> The region $\{x\ge0,\ x_1+x_2\ge1,\ 2x_1+5x_2\le10\}$ is bounded with extreme points $(1,0),(0,1),(5,0),(0,2)$. Objective $x_1-x_2$ takes $1,-1,5,-2$, so the minimum is $\mathbf{-2}$ at $(0,2)$. Both are now feasible, so strong duality gives dual optimum $=-2$.</p>`,
  R`Dual infeasible $+$ primal feasible $\Rightarrow$ primal unbounded. Both feasible $\Rightarrow$ equal optimal values.`);

  Q(18, 'pyq', '2025 MT3 · Q4', '10 marks', R`
<p>A bounded polyhedral set $P=\{x:a_i^\top x\le b_i\}$ has extreme points $x_1,\dots,x_k$, and $x\in P$ iff $x=\sum\lambda_ix_i$, $\lambda\ge0$, $\sum\lambda_i=1$.</p>
<p><span class="part">(a)</span> Given $a_j=c^\top x_j$, reformulate $\min_{x\in P}c^\top x$ in terms of the $a_j$ and solve with KKT. (6)</p>
<p><span class="part">(b)</span> Find the extreme points of $P=\{0\le x\le\mathbf1\}$. How many are there? (4)</p>`, R`
<p><span class="part">(a)</span> $c^\top x=\sum\lambda_jc^\top x_j=\sum\lambda_ja_j$, so
$$\min_\lambda\ \sum_j\lambda_ja_j\quad\text{s.t.}\quad\sum\lambda_j=1,\ \lambda\ge0 .$$
KKT: $a_j-\mu-\delta_j=0$, $\delta_j\lambda_j=0$, $\delta_j\ge0$. If $\lambda_j>0$ then $a_j=\mu$. Let $a_l=\min_ja_j$. Take $\mu=a_l$, $\lambda_l=1$, others $0$: <span class="ans">the LP optimum is the smallest $c^\top x_j$ over the vertices</span>, i.e. an LP over a polytope is solved at an extreme point.</p>
<p><span class="part">(b)</span> The extreme points of the unit cube are exactly the vectors in $\{0,1\}^d$: <span class="ans">$2^d$ of them</span>.</p>`,
  R`Min of a linear function over a polytope $=$ min over its vertices. The cube has $2^d$ vertices.`);

  Q(18, 'gen', '', '7 marks', R`
<p>Solve $\min 2x_1+3x_2$ s.t. $x_1+x_2\ge4$, $x_1+3x_2\ge6$, $x\ge0$ by writing its dual and checking complementary slackness.</p>`, R`
<p>Dual: $\max 4y_1+6y_2$ s.t. $y_1+y_2\le2$, $y_1+3y_2\le3$, $y\ge0$.</p>
<p>Solve the primal by vertices: the binding pair $x_1+x_2=4,\ x_1+3x_2=6$ gives $x=(3,1)$ with value $6+3=9$; other vertices $(6,0)$ and $(0,4)$ give $12$. So the primal minimum is $9$ at $(3,1)$.</p>
<p>Dual: both constraints binding: $y_1+y_2=2$, $y_1+3y_2=3\Rightarrow y_2=\tfrac12,\ y_1=\tfrac32$; $y\ge0$ &#10003;; value $4\cdot\tfrac32+6\cdot\tfrac12=9$. <span class="ans">Equal, so both optimal.</span></p>
<p>Complementary slackness: $x_1,x_2>0$ means both dual constraints are tight &#10003;; $y_1,y_2>0$ means both primal constraints are tight at $(3,1)$ (4 and 6) &#10003;.</p>`,
  R`Optimal pair: positive variable $\Leftrightarrow$ the matching constraint on the other side is tight.`);

  Q(18, 'pyq', '2025 Final · Q1(s),(t)', '2 marks', R`
<p><b>True or False, with a reason.</b></p>
<p><span class="part">(a)</span> Linear programming problems always have a global minimum.</p>
<p><span class="part">(b)</span> The BFS recovered from the simplex algorithm at termination may not be a KKT point.</p>`, R`
<p><span class="part">(a)</span> <span class="ans">False.</span> An LP can be infeasible ($x\ge1,\ x\le0$) or unbounded ($\min -x$, $x\ge0$). It has a minimum only if it is feasible and bounded.</p>
<p><span class="part">(b)</span> <span class="ans">False.</span> Simplex stops at a BFS with non-negative reduced costs; those reduced costs are exactly the KKT multipliers $\lambda_N\ge0$ and $\mu=B^{-\top}c_B$ is dual feasible. So the final BFS <i>is</i> a KKT point.</p>`,
  R`LP: feasible $+$ bounded $\Rightarrow$ min exists at a vertex. Simplex termination $=$ KKT.`);

  /* ============================ 19  Penalty & barrier ============================ */
  Q(19, 'gen', '', '5 marks', R`
<p>Minimise $f(x)=x$ subject to $x\ge1$ using the <b>quadratic penalty</b> $P(x;\mu)=x+\tfrac\mu2\big(\max\{0,1-x\}\big)^2$.</p>
<p>Find the minimiser $x(\mu)$, its limit, and say whether the iterates are feasible.</p>`, R`
<p>For $x\lt1$: $P'(x)=1-\mu(1-x)=0\Rightarrow x(\mu)=1-\dfrac1\mu\lt1$. (For $x\ge1$, $P'=1>0$, so no minimiser there.)</p>
<p>So $x(\mu)=1-\tfrac1\mu\to1=x^*$ as $\mu\to\infty$.</p>
<p>All iterates are <span class="ans">infeasible</span> (slightly outside $x\ge1$), approaching the boundary from the outside. The distance to feasibility shrinks like $1/\mu$.</p>`,
  R`Penalty method: the iterates approach the solution from the infeasible side as $\mu\to\infty$.`);

  Q(19, 'gen', '', '5 marks', R`
<p>For the same problem, use the <b>log-barrier</b> $B(x;t)=x-t\log(x-1)$ on $x>1$. Find $x(t)$ and its limit. Are iterates feasible? How does this differ from the penalty method?</p>`, R`
<p>$B'(x)=1-\dfrac t{x-1}=0\Rightarrow x(t)=1+t$, which tends to $1=x^*$ as $t\downarrow0$.</p>
<p>All iterates are <span class="ans">strictly feasible</span> ($x(t)>1$): approaching from the <b>inside</b>. Need a strictly feasible start and the barrier blows up at the boundary, so you never leave $C$.</p>
<p>Difference: penalty methods allow infeasibility and push back with $\mu\uparrow\infty$ (exterior); barrier methods stay interior and relax with $t\downarrow0$. The gap $f(x(t))-f^*=t$ here.</p>`,
  R`Penalty: exterior, $\mu\to\infty$. Barrier: interior, $t\to0$, needs strictly feasible start.`);

  Q(19, 'gen', '', '6 marks', R`
<p>Minimise $x_1^2+x_2^2$ s.t. $x_1+x_2=1$ using $P(x;\mu)=x_1^2+x_2^2+\tfrac\mu2(x_1+x_2-1)^2$.</p>
<p><span class="part">(a)</span> Find the minimiser $x(\mu)$ and its limit. <span class="part">(b)</span> Show that $\mu\,(x_1+x_2-1)$ converges to the Lagrange multiplier.</p>`, R`
<p><span class="part">(a)</span> By symmetry $x_1=x_2=s$: $P=2s^2+\tfrac\mu2(2s-1)^2$, $P'=4s+2\mu(2s-1)=0\Rightarrow s=\dfrac{\mu}{2(1+\mu)}$. As $\mu\to\infty$: $x\to(\tfrac12,\tfrac12)$, the true solution. (Constraint violation $2s-1=-\dfrac1{1+\mu}$.)</p>
<p><span class="part">(b)</span> The true Lagrangian $L=f+\lambda(x_1+x_2-1)$ has $2x_i+\lambda=0$, so $\lambda^*=-1$. From the penalty gradient, $2x_i+\mu(x_1+x_2-1)=0$, so $\lambda\approx\mu\,h(x(\mu))$:
$$\mu(2s-1)=-\frac\mu{1+\mu}\to-1=\lambda^* .$$
The penalty parameter times the constraint violation is a multiplier estimate (the idea behind augmented Lagrangian methods).</p>`,
  R`Penalty gradient $=0$ $\Rightarrow$ $\mu\,h(x(\mu))\to\lambda^*$. Infeasibility $\sim1/\mu$.`);

  Q(19, 'gen', '', '4 marks', R`
<p>Why is it a bad idea to jump straight to a huge $\mu$ in the quadratic penalty method, and how does the log-barrier behave near the boundary? State what you would do in practice.</p>`, R`
<p>The Hessian of $P(x;\mu)$ contains $\mu\,\nabla h\nabla h^\top$, with eigenvalue $\sim\mu\|\nabla h\|^2$ in the normal directions and only $O(1)$ in tangent directions. As $\mu\to\infty$ the condition number $\to\infty$, so gradient descent crawls and Newton's linear systems become ill-conditioned.</p>
<p>Likewise the log-barrier Hessian contains $\dfrac{t}{g(x)^2}\nabla g\nabla g^\top$, which blows up near the boundary as $t\to0$.</p>
<p>Practice: increase $\mu$ gradually (or decrease $t$), and use the previous minimiser as a <b>warm start</b> for the next subproblem. Each subproblem is well conditioned and the path $x(\mu)$ is followed to the solution.</p>`,
  R`Bigger $\mu$ $=$ closer to feasibility but worse conditioning. Increase gradually and warm start.`);

  Q(19, 'gen', '', '4 marks', R`
<p>Use the $\ell_1$ (exact) penalty $P(x;\mu)=x+\mu\max\{0,1-x\}$ for $\min x$ s.t. $x\ge1$. For which $\mu$ is the minimiser exactly $x^*=1$? How does that relate to the Lagrange multiplier?</p>`, R`
<p>For $x\lt1$: $P'=1-\mu$; for $x>1$: $P'=1$. If $\mu>1$, $P$ decreases up to $x=1$ then increases, so the unique minimiser is exactly $x=1$ for <b>every finite $\mu>1$</b>.</p>
<p>The KKT multiplier of $x\ge1$ is $\lambda^*=1$ (since $\nabla f=1=\lambda\cdot1$). So the rule is $\mu>\lambda^*$: the exact penalty works once $\mu$ exceeds the largest multiplier. No need to send $\mu\to\infty$, but the penalty is non-smooth.</p>`,
  R`Exact penalty: $\mu>\|\lambda^*\|_\infty$ gives the exact solution, at the price of non-differentiability.`);

  window.PRACTICE_DATA = (window.PRACTICE_DATA || []).concat(out);
})();
