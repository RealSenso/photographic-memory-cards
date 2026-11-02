"""DIP topic 01 (camera geometry) in the CMO card format. Everyday picture: a street camera on a pole."""
from street_lib import *

SUBJECT = "DIP"

def d40101(c):
    return svg(c,
        L(10, 118, 232, 118, 1), N(228, 128, "street", 7, "end"),
        dot(34, 82, None, r=2.4), N(34, 96, "C (lens)", 7),
        L(84, 50, 84, 114, 1), N(84, 46, "image plane", 7),
        arrow(34, 82, 84, 82, 1), N(60, 78, "f", 8, "middle"),
        person(200, 118, 44), dash(200, 82, 200, 118, .8),
        dash(34, 82, 200, 82, .8, "1 3"), N(120, 112, "Z (depth)", 7, "middle"),
        L(34, 82, 200, 74, 1), C(84, 80, 1.8), N(92, 66, "y = f·Y/Z", 7.5, "start"),
        N(214, 62, "Y", 8, "start"), N(120, 138, "far away (big Z) ⇒ small in the frame", 7.5))

def d40102(c):
    return svg(c,
        N(120, 12, "x ~ K [R | t] X", 9, "middle"),
        person(26, 80, 34), N(26, 94, "X", 8), N(26, 104, "point in the street", 6.5),
        arrow(48, 66, 80, 66, 1), R(80, 48, 40, 36, "#f1f5f9", 1), N(100, 64, "[R | t]", 8), N(100, 76, "pole pose", 6.5),
        arrow(120, 66, 152, 66, 1), R(152, 48, 34, 36, "#f1f5f9", 1), N(169, 64, "K", 9), N(169, 76, "lens", 6.5),
        arrow(186, 66, 204, 66, 1), frame(204, 50, 28, 32), N(218, 68, "u, v", 7),
        cam(100, 108, 1.4), pole(94, 114, 128),
        N(100, 140, "where is the camera?", 6.5), N(169, 112, "how does it zoom?", 6.5), N(169, 122, "and how big is a pixel?", 6.5),
        N(218, 98, "pixel", 6.5))

def d40103(c):
    return svg(c,
        frame(20, 22, 160, 100), N(24, 18, "(0, 0)", 7, "start"),
        arrow(20, 22, 60, 22, 1), N(66, 20, "u", 8, "start"), arrow(20, 22, 20, 52, 1), N(24, 56, "v", 8, "start"),
        L(94, 70, 106, 70, 1), L(100, 64, 100, 76, 1), N(104, 90, "(cₓ, cᵧ)", 7.5, "start"),
        dash(100, 72, 100, 122, .8, "1 3"), dash(20, 72, 100, 72, .8, "1 3"),
        pix(194, 36, [["", ""], ["", ""]], 14), N(222, 32, "1 pixel", 6.5),
        arrow(194, 76, 222, 76, .8), N(208, 86, "1/mₓ mm", 6.5),
        N(194, 104, "fₓ = f·mₓ", 7.5, "start"), N(194, 114, "(pixels per mm", 6.5, "start"), N(194, 123, "× focal length)", 6.5, "start"),
        N(100, 138, "principal point = where the lens axis hits the sensor", 7))

def d40104(c):
    sq = [(0, 0), (22, 0), (22, 22), (0, 22)]
    def at(dx, dy, m): return [(dx + m(x, y)[0], dy + m(x, y)[1]) for x, y in sq]
    rot = lambda x, y: (x * .94 - y * .34 + 5, x * .34 + y * .94)
    sim = lambda x, y: (x * .66, y * .66)
    aff = lambda x, y: (x + y * .5, y * .8)
    prj = lambda x, y: (x * (1 - y * .018) + y * .2 + 4, y * .8)
    return svg(c,
        N(120, 12, "the crosswalk, as the camera sees it", 8),
        quad(sq if False else at(8, 40, lambda x, y: (x, y))), N(19, 82, "Euclid", 7), N(19, 91, "3 DOF", 6.5),
        quad(at(70, 40, sim)), N(81, 82, "similar", 7), N(81, 91, "4 DOF", 6.5),
        quad(at(120, 40, aff)), N(137, 82, "affine", 7), N(137, 91, "6 DOF", 6.5),
        quad(at(180, 40, prj)), N(197, 82, "projective", 7), N(197, 91, "8 DOF", 6.5),
        L(180, 45, 202, 45, .6, "1 2"),
        N(120, 112, "h₃₁ = h₃₂ = 0 ⇒ parallel lines stay parallel", 7.5),
        N(120, 124, "h₃₁, h₃₂ ≠ 0 ⇒ they meet at a vanishing point", 7.5),
        N(120, 137, "H : 9 numbers − 1 scale = 8 DOF", 7.5))

def d40105(c):
    return svg(c,
        N(36, 14, "output frame", 7), R(14, 22, 24, 24, "#d9dee7", 1), N(26, 38, "x′, y′", 7), N(26, 58, "ask:", 6.5), N(26, 67, "where from?", 6.5),
        arrow(40, 34, 98, 52, 1), N(66, 36, "T⁻¹", 8),
        N(150, 14, "source frame", 7),
        pix(112, 24, [["f₀₀", "f₁₀"], ["f₀₁", "f₁₁"]], 44, 8).replace(">f₀₀<", "> <")+N(122, 36, "f₀₀", 8),
        C(f(112 + 44 * .35), f(24 + 44 * .6), 2.4), N(112 + 44 * .35 + 4, 24 + 44 * .6 + 10, "x, y", 7, "start"),
        dash(112 + 44 * .35, 24, 112 + 44 * .35, 24 + 44 * .6, .8), dash(112, 24 + 44 * .6, 112 + 44 * .35, 24 + 44 * .6, .8),
        N(112 + 44 * .17, 20, "a", 7), N(108, 24 + 44 * .3, "b", 7, "end"),
        N(120, 124, "f(x, y) = (1−a)(1−b)f₀₀ + a(1−b)f₁₀ + (1−a)b f₀₁ + ab f₁₁", 6.5),
        N(120, 138, "every output pixel is filled: no holes", 7.5))

def d40106(c):
    A = [(14, 70), (70, 70), (82, 112), (4, 112)]
    B = [(142, 44), (226, 44), (210, 104), (154, 104)]
    out = [N(44, 60, "street plane", 7), quad(A), N(184, 36, "camera frame", 7), quad(B)]
    for i, (p, q) in enumerate(zip(A, B)):
        out += [dash(p[0], p[1], q[0], q[1], .6, "1 3"), C(f(p[0]), f(p[1]), 2), C(f(q[0]), f(q[1]), 2)]
    out += [N(88, 128, "(xᵢ, yᵢ)", 7, "start"), N(196, 118, "(xᵢ′, yᵢ′)", 7, "start"),
            N(120, 18, "4 matches × 2 equations = 8 = DOF of H", 8),
            N(120, 140, "A h = 0, h = last right singular vector of A", 7)]
    return svg(c, *out)

CARDS = {
40101: dict(d=d40101, stmtKind="DEFINITION",
  statement=r"<b>Pinhole camera model.</b> A pinhole camera has optical centre $C=(0,0,0)$ and an image plane at distance $f$ (the focal length) from $C$, perpendicular to the optical axis $Z$. A scene point $(X,Y,Z)$ with $Z\gt 0$ is imaged at the point where the ray from $C$ through it meets the image plane: $x=f\,X/Z,\ y=f\,Y/Z$ (with the plane placed in front of $C$, to avoid the sign flip of the real inverted image).",
  hint="If the person walks twice as far from the street camera, what happens to how tall they look in the frame?",
  breakdown=[r"<strong>$f$ = the distance from the lens point to the sensor.</strong> A longer $f$ magnifies the whole street, a shorter one shows more of it.",
             r"<strong>$X,Y$ = where the person is sideways and up</strong> relative to the camera's axis. They are measured in metres, so the picture only keeps their ratio to the depth.",
             r"<strong>$Z$ = how far the person is from the lens.</strong> Dividing by $Z$ is the whole effect: twice as far, half as tall in the frame. This division is why the map is not linear."],
  conn=r"<strong>The pole camera shrinks the far kerb.</strong> The passer-by near the pole fills the frame; the same person at the end of the street is a few pixels tall. Nothing about the person changed: only $Z$.",
  cap="The pole camera's lens point C sits a distance f from the image plane. A person of height Y at depth Z lands at height y = f·Y/Z on the plane: far away (large Z) means small in the frame."),
40102: dict(d=d40102, stmtKind="DEFINITION",
  statement=r"<b>Camera (projection) matrix.</b> In homogeneous coordinates a pinhole camera is the $3\times4$ matrix $P=K[R\mid t]$, with $R\in SO(3)$, $t\in\mathbb R^3$ the camera's pose and $K$ its $3\times3$ intrinsic matrix. A world point $\mathbf X=(X,Y,Z,1)^\top$ is imaged at $\mathbf x\sim P\mathbf X$, where $\sim$ means equality up to a nonzero scale; the pixel is $(u,v)=(\tilde u/\tilde w,\ \tilde v/\tilde w)$.",
  hint="Which part of the camera matrix changes when the pole is rotated, and which when you swap the lens?",
  breakdown=[r"<strong>$[R\mid t]$ = the pole's pose.</strong> It moves a point from street coordinates into the camera's own frame: rotate by $R$ (where the camera points), shift by $t$ (where it stands).",
             r"<strong>$K$ = lens and sensor.</strong> It turns a point in the camera frame into pixel numbers: the focal length, where the axis hits the sensor, how big a pixel is.",
             r"<strong>$\sim$ = up to scale.</strong> The result is a 3-vector $(\tilde u,\tilde v,\tilde w)$; the pixel only appears after dividing by $\tilde w$, which is the division by depth."],
  conn=r"<strong>Two separate knobs.</strong> Bolting the camera to a different pole changes $[R\mid t]$ and leaves $K$ alone; replacing the lens with a zoom changes $K$ and leaves the pose alone. The street point goes through both, in that order.",
  cap="A street point X goes through the pole's pose [R | t], then through the lens-and-sensor matrix K, and comes out as the pixel (u, v) in the recorded frame."),
40103: dict(d=d40103, stmtKind="DEFINITION",
  statement=r"<b>Intrinsic calibration matrix.</b> $K=\begin{pmatrix}f_x&s&c_x\\0&f_y&c_y\\0&0&1\end{pmatrix}$, where $f_x=f\,m_x$, $f_y=f\,m_y$ are the focal length in pixels ($m_x,m_y$ pixels per unit length), $(c_x,c_y)$ is the principal point in pixels and $s$ is the skew (zero when sensor axes are orthogonal). $K$ maps a point $(X,Y,Z)$ of the camera frame to the pixel $u=f_xX/Z+c_x,\ v=f_yY/Z+c_y$ (for $s=0$).",
  hint="Where is pixel (0, 0) of the street frame, and where does the lens axis actually land?",
  breakdown=[r"<strong>$f_x,f_y$ = the focal length counted in pixels.</strong> The real focal length times the number of pixels per millimetre; a square-pixel sensor has $f_x=f_y$.",
             r"<strong>$(c_x,c_y)$ = the principal point.</strong> The pixel where the lens axis hits the sensor, about the middle of the frame, not at the corner $(0,0)$.",
             r"<strong>$s$ = skew.</strong> Zero unless the pixel rows and columns are not at right angles, which for a modern street camera they are."],
  conn=r"<strong>Counting pixels in a 1920×1080 frame.</strong> Pixel (0, 0) is the top-left corner of the recorded frame, so the centre of the lens axis lands near (960, 540). A wider-angle lens has a smaller $f_x$: more street fits across the same pixels.",
  cap="The recorded frame has its origin (0, 0) at the top-left corner and axes u, v. The lens axis hits the principal point (cₓ, cᵧ); fₓ = f·mₓ is the focal length counted in pixels."),
40104: dict(d=d40104, stmtKind="DEFINITION",
  statement=r"<b>Hierarchy of 2D planar transformations.</b> A homography is $\mathbf x'\sim H\mathbf x$ with $H\in\mathbb R^{3\times3}$ invertible, defined up to scale (8 degrees of freedom). Subgroups: Euclidean $[R\mid t]$ (3 DOF, preserves lengths and angles); similarity $[sR\mid t]$ (4, preserves angles); affine, with last row $(0,0,1)$ (6, preserves parallelism); projective (8, preserves straight lines only).",
  hint="Which transformation of the zebra crossing keeps its stripes parallel, and which makes them meet?",
  breakdown=[r"<strong>$H$ with 9 entries up to scale</strong> = 8 free numbers. This is the most general map that still sends straight lines to straight lines.",
             r"<strong>Last row $(h_{31},h_{32},h_{33})$ = the perspective part.</strong> If it equals $(0,0,1)$ the map is affine and parallel lines stay parallel; otherwise they converge.",
             r"<strong>The chain Euclid ⊂ similarity ⊂ affine ⊂ projective</strong> = each step gives up one thing (lengths, then angles, then parallelism) for more freedom."],
  conn=r"<strong>A zebra crossing seen from the pole.</strong> From straight above it is a clean rectangle. From the pole its stripes slant toward each other: the road plane has been mapped by a homography, and the vanishing point is where the stripes would meet.",
  cap="The same crosswalk square after a Euclidean, similarity, affine and projective map. Only the projective one (last row of H not 0 0 1) lets the parallel sides meet."),
40105: dict(d=d40105, stmtKind="ALGORITHM",
  statement=r"<b>Inverse warping with bilinear interpolation.</b> Given a transformation $T$ and a source image $I_{\rm src}$, for every integer pixel $(x',y')$ of the output compute $(x,y)=T^{-1}(x',y')$, let $x_0=\lfloor x\rfloor$, $y_0=\lfloor y\rfloor$, $a=x-x_0$, $b=y-y_0$, and set $I_{\rm dest}(x',y')=(1-a)(1-b)f_{00}+a(1-b)f_{10}+(1-a)b\,f_{01}+ab\,f_{11}$, with $f_{ij}$ the four source pixels around $(x,y)$.",
  hint="To fill every pixel of the corrected frame, do you push source pixels forward, or ask each output pixel where it came from?",
  breakdown=[r"<strong>$T^{-1}(x',y')$ = for each output pixel, ask where it came from.</strong> This visits every output pixel exactly once, so no holes and no double hits (forward mapping has both).",
             r"<strong>$(x,y)$ lands between pixels</strong> = the source position is rarely a whole number, so there is no single source pixel to copy.",
             r"<strong>$(1-a)(1-b)f_{00}+\dots$ = blend the four neighbours</strong> by how close the point is to each: the nearer pixel gets the larger weight."],
  conn=r"<strong>Straightening the street frame.</strong> To turn the slanted road into a top-down map, go through the new map pixel by pixel and ask the original frame what colour sits at that spot. Pushing source pixels forward instead leaves little unpainted gaps.",
  cap="Each pixel (x′, y′) of the corrected frame looks back through T⁻¹ to a point (x, y) of the camera frame, between four pixels f₀₀ … f₁₁. The offsets a and b give the blend weights."),
40106: dict(d=d40106, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Estimating a homography from four points (DLT).</b> Each correspondence $(x_i,y_i)\leftrightarrow(x_i',y_i')$ gives two linear equations in the entries $h$ of $H$ (from $x_i'(h_{31}x_i+h_{32}y_i+h_{33})=h_{11}x_i+h_{12}y_i+h_{13}$ and the same for $y_i'$). Four correspondences, no three collinear, give $A\in\mathbb R^{8\times9}$ and $Ah=0$; the solution with $\|h\|=1$ is the right singular vector of $A$ for its smallest singular value (equivalently the smallest eigenvector of $A^\top A$).",
  hint="How many street-to-frame point matches pin down a homography, and why that many?",
  breakdown=[r"<strong>$A\in\mathbb R^{8\times9}$ = two equations per matched point.</strong> Four points give 8 rows; the 9 unknowns are the entries of $H$.",
             r"<strong>$Ah=0$ with $\|h\|=1$</strong> = $H$ is only known up to scale, so we fix its length and pick the unit vector that $A$ shrinks the most.",
             r"<strong>$h=v_9$ of SVD$(A)$</strong> = the right singular vector of the smallest singular value is exactly that vector."],
  conn=r"<strong>Four paint marks on the road.</strong> Measure the four corners of the crosswalk on the ground, find the same four corners in the camera frame, and the equations fix the whole map. If three marks sit on one line, the equations repeat themselves and fail.",
  cap="Four corners of the crosswalk on the street plane matched to the same four in the camera frame: 4 × 2 = 8 equations Ah = 0, enough for the 8 degrees of freedom of H."),
}

STORY = {
 40101: dict(s="STORY 1 · STEP 1 · THE CAMERA", b="Everything in DIP starts when the street camera turns the 3D street into a flat frame: a point at depth $Z$ lands at $f\\,X/Z$, so <b>far things shrink</b>.",
   f=[], n=[["40102", "all of it as one matrix"], ["3011", "what each pixel's colour is"]]),
 40102: dict(s="STORY 1 · STEP 2 · ONE MATRIX", b="The pole's pose $[R\\mid t]$ and the lens $K$ stack into a single matrix $P$ that takes a street point to a pixel.",
   f=[["40101", "perspective division"]], n=[["40103", "open up K"], ["40104", "maps between two views"]]),
 40103: dict(s="STORY 1 · STEP 3 · THE LENS AND SENSOR", b="$K$ counts everything in <b>pixels</b>: focal length $f_x,f_y$, principal point $(c_x,c_y)$, skew $s$.",
   f=[["40102", "where K sits in P"]], n=[["40105", "pixels need whole-number positions"]]),
 40104: dict(s="STORY 1 · STEP 4 · MAPS OF THE ROAD PLANE", b="A flat road seen by the camera is related to a top-down plan by a <b>homography</b>, the most general straight-line-preserving map; simpler maps are special cases.",
   f=[["40102", "the camera matrix"]], n=[["40105", "applying a map to a frame"], ["40106", "estimating one"]]),
 40105: dict(s="STORY 1 · STEP 5 · APPLY THE MAP", b="To apply a map to the frame, <b>ask each output pixel where it came from</b> and blend the four nearest source pixels.",
   f=[["40104", "the maps"], ["40103", "pixel grid"]], n=[["40106", "where the map comes from"], ["3072", "sampling: why blending is needed"]]),
 40106: dict(s="STORY 1 · STEP 6 · MEASURE THE MAP", b="Four matched points give 8 equations, enough to solve for $H$ by SVD. Then the whole frame can be warped.",
   f=[["40104", "8 DOF"], ["40105", "warp with it"]], n=[["3011", "next: what colour each pixel holds"]]),
}

FIX = build_fix(CARDS)
