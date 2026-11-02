"""DIP topic 04 (binary morphology). Everyday picture: a street camera on a pole."""
from street_lib import *

SUBJECT = "DIP"

BLOB = ["........", ".###....", ".####.#.", ".####...", ".###....", "........"]
def d3031(c):
    er = ["........", "........", "..##....", "..##....", "........", "........"]
    return svg(c,
        N(40, 14, "mask A", 8), bgrid(12, 20, BLOB, 9), N(40, 88, "person + a speck", 6.5),
        N(120, 14, "B slides", 7), bgrid(98, 38, ["###", "###", "###"], 9, "#ffffff"), N(111, 76, "B fits ⇒ keep", 6.5),
        N(198, 14, "A ⊖ B", 8), bgrid(168, 20, er, 9), N(198, 88, "speck gone, person thinner", 6.5),
        N(120, 112, "A ⊖ B = { z : B placed at z lies inside A }", 7.5), N(120, 126, "shrinks every object by the radius of B", 7.5))

def d3032(c):
    A = ["........", ".##.##..", ".##.##..", ".#..#...", "........", "........"]
    D = ["########", "########", "########", "########", "########", "........"]
    D = ["........", "########"[:7] + ".", "########"[:7] + ".", "########"[:7] + ".", ".#####..", "........"]
    return svg(c,
        N(40, 14, "mask A with a gap", 7.5), bgrid(8, 20, A, 9), 
        N(120, 14, "B", 8), bgrid(106, 34, ["###", "###", "###"], 9, "#ffffff"), N(120, 72, "grow by B", 6.5),
        N(198, 14, "A ⊕ B", 8), bgrid(164, 20, D, 9), N(198, 82, "gap closed", 6.5),
        N(120, 104, "A ⊕ B = ⋃ A shifted by each point b of B", 7.5), N(120, 117, "duality: (A ⊖ B)ᶜ = Aᶜ ⊕ B̂", 7.5), N(120, 131, "erode ≠ undo dilate", 7.5))

def d3033(c):
    A = ["........", ".####.#.", ".####...", ".####...", ".####...", "........"]
    E_ = ["........", "........", "..##....", "..##....", "........", "........"]
    O = ["........", ".####...", ".####...", ".####...", ".####...", "........"]
    return svg(c,
        N(34, 12, "A", 8), bgrid(8, 16, A, 7), N(34, 66, "speck beside person", 6.5),
        arrow(66, 40, 84, 40, 1), N(75, 34, "⊖B", 7),
        bgrid(88, 16, E_, 7), arrow(146, 40, 164, 40, 1), N(155, 34, "⊕B", 7),
        N(192, 12, "A ∘ B", 8), bgrid(168, 16, O, 7), 
        N(120, 86, "opening A ∘ B = (A ⊖ B) ⊕ B : removes white specks", 7.5),
        N(120, 100, "closing A • B = (A ⊕ B) ⊖ B : fills black holes", 7.5),
        N(120, 116, "(A ∘ B) ∘ B = A ∘ B : doing it twice changes nothing", 7.5))

def d3034(c):
    A = ["........", ".######.", ".######.", ".######.", ".######.", "........"]
    Er = ["........", "........", "..####..", "..####..", "........", "........"]
    Bd = ["........", ".######.", ".#....#.", ".#....#.", ".######.", "........"]
    return svg(c,
        N(36, 12, "A", 8), bgrid(8, 16, A, 7, "#b8c0cc"), N(100, 12, "A ⊖ B", 8), bgrid(72, 16, Er, 7), N(168, 12, "β(A)", 8), bgrid(136, 16, Bd, 7),
        N(63, 40, "−", 10), N(127, 40, "=", 10),
        N(120, 84, "β(A) = A − (A ⊖ B)", 8.5),
        N(120, 100, "the part of A that erosion removes is the outline", 7.5),
        N(120, 114, "3×3 square B ⇒ thin 8-connected outline", 7), N(120, 127, "cross-shaped B ⇒ thicker outline", 7))

def d3035(c):
    G = ["#..", ".#.", "..#"]
    return svg(c,
        bgrid(14, 18, G, 14), N(35, 72, "N₄: 3 objects", 7.5), N(35, 83, "N₈: 1 object", 7.5),
        N(130, 14, "N₄(p)", 8), bgrid(112, 20, [".#.", "#p#", ".#."], 12),
        N(192, 14, "N₈(p)", 8), bgrid(174, 20, ["###", "#p#", "###"], 12),
        N(130, 66, "share an edge", 6.5), N(192, 66, "also diagonals", 6.5),
        N(120, 100, "pass 1: smallest neighbour label, note equal pairs", 7.5),
        N(120, 112, "pass 2: union–find, relabel", 7.5),
        N(120, 128, "object 8-connected ⇒ background 4-connected", 7.5))

def d3036(c):
    A = ["........", ".#####..", ".#####.#", ".#####..", ".#####..", ".#####..", "........"]
    Er = ["........", "........", "..###...", "..###...", "..###...", "........", "........"]
    O = ["........", ".#####..", ".#####..", ".#####..", ".#####..", ".#####..", "........"]
    return svg(c,
        N(32, 12, "|A| = 25 + 1", 7.5), bgrid(6, 16, A, 8),
        N(120, 12, "|A ⊖ B| = 9", 7.5), bgrid(92, 16, Er, 8),
        N(206, 12, "|(A ⊖ B) ⊕ B| = 25", 7.5, "middle"), bgrid(178, 16, O, 8),
        N(76, 50, "⊖B", 8), N(160, 50, "⊕B", 8),
        N(32, 84, "spur", 6.5), 
        N(120, 100, "the spur cannot hold a 3×3 B ⇒ it vanishes", 7.5),
        N(120, 114, "the 3×3 core grown by B = the 5×5 square again", 7.5),
        N(120, 128, "in general A ∘ B ≠ A: only pieces that fit B come back", 7.5))

CARDS = {
3031: dict(d=d3031, stmtKind="DEFINITION",
  statement=r"<b>Erosion.</b> For sets $A,B\subseteq\mathbb Z^2$ (the image and a structuring element), the erosion of $A$ by $B$ is $A\ominus B=\{z\mid (B)_z\subseteq A\}=\bigcap_{b\in B}A_{-b}$, where $(B)_z$ is $B$ translated by $z$. It is the set of positions of $B$'s origin for which $B$ lies entirely inside $A$.",
  hint="Slide a small stamp over the people mask: where does the whole stamp still fit inside the object?",
  breakdown=[r"<strong>$B$ = the probe.</strong> A small shape (a $3\times3$ square, a cross) whose size decides how much is removed.",
             r"<strong>$(B)_z\subseteq A$ = $B$ fits completely inside the object</strong> when its centre is at $z$. Only such centres survive.",
             r"<strong>$\bigcap_{b\in B}A_{-b}$ = the same thing as an overlap.</strong> Shift $A$ by every $-b$ and keep what stays in all copies; objects shrink by the radius of $B$ and specks smaller than $B$ vanish."],
  conn=r"<strong>Wiping specks off the people mask.</strong> After thresholding, a single stray pixel from sensor noise sits beside the real person. Erosion removes the speck, at the price of making the person thinner too.",
  cap="The mask A holds a person and a one-pixel speck. The probe B survives only where it fits inside A, so A ⊖ B loses the speck and shrinks the person."),
3032: dict(d=d3032, stmtKind="DEFINITION",
  statement=r"<b>Dilation and duality.</b> The dilation of $A$ by $B$ is $A\oplus B=\{z\mid(\hat B)_z\cap A\ne\emptyset\}=\bigcup_{b\in B}A_b$, where $\hat B=\{-b: b\in B\}$ is the reflection of $B$. Erosion and dilation are dual: $(A\ominus B)^c=A^c\oplus\hat B$.",
  hint="If erosion shrinks the mask, what does its twin do to the gaps in the person's outline?",
  breakdown=[r"<strong>$\bigcup_{b\in B}A_b$ = paste $A$ at every offset in $B$.</strong> Each object pixel spreads out into the shape of $B$, so objects grow.",
             r"<strong>$(\hat B)_z\cap A\ne\emptyset$ = $B$ touches the object.</strong> The same rule seen from the other side: keep every centre where the probe touches $A$.",
             r"<strong>$(A\ominus B)^c=A^c\oplus\hat B$ = duality.</strong> Eroding the object is the same as dilating the background with the reflected probe; it is not undoing a dilation."],
  conn=r"<strong>Closing a gap in the person's mask.</strong> Thresholding left a crack between the two halves of the person's body. Growing the mask by $B$ fills the crack but also fattens the outline.",
  cap="A mask A with a gap is pasted at every offset of B: A ⊕ B closes the gap. Eroding A is the same as dilating the background Aᶜ with the reflected probe."),
3033: dict(d=d3033, stmtKind="DEFINITION",
  statement=r"<b>Opening and closing.</b> The opening of $A$ by $B$ is $A\circ B=(A\ominus B)\oplus B$, and the closing is $A\bullet B=(A\oplus B)\ominus B$. Both are idempotent: $(A\circ B)\circ B=A\circ B$ and $(A\bullet B)\bullet B=A\bullet B$. Opening removes objects (and spurs) in which $B$ does not fit; closing fills holes and gaps that $B$ cannot enter.",
  hint="Which two-step combo removes the speck without leaving the person thinner?",
  breakdown=[r"<strong>$(A\ominus B)\oplus B$ = erode, then grow back.</strong> The erosion deletes everything $B$ cannot fit in; the dilation puts the surviving shapes back at their size.",
             r"<strong>$(A\oplus B)\ominus B$ = grow, then shrink back.</strong> Gaps and holes smaller than $B$ are filled and the outline returns to where it was.",
             r"<strong>$(A\circ B)\circ B=A\circ B$ = idempotent.</strong> Once opened, opening again changes nothing."],
  conn=r"<strong>The standard clean-up for the people mask.</strong> Open it to throw away the specks, close it to patch the cracks. The person comes back at their original size, not thinner.",
  cap="A person mask with a speck is eroded by B and dilated back: the opening A ∘ B keeps the person at full size and drops the speck."),
3034: dict(d=d3034, stmtKind="ALGORITHM",
  statement=r"<b>Boundary extraction.</b> The boundary of a set $A$ is $\beta(A)=A-(A\ominus B)$, with $B$ a $3\times3$ structuring element (giving a 1-pixel-thick outline). More general local patterns are found by the hit-or-miss transform $A\circledast B=(A\ominus B_1)\cap(A^c\ominus B_2)$.",
  hint="If you subtract the shrunken person from the person, what is left?",
  breakdown=[r"<strong>$A\ominus B$ = the inside of the object.</strong> Everything at least a probe's width from the edge.",
             r"<strong>$A-(A\ominus B)$ = the outline.</strong> Remove the inside from the object and only the border pixels remain.",
             r"<strong>$B_1,B_2$ in the hit-or-miss transform = a pattern for object and one for background.</strong> Both must match at once, so exact local shapes can be found."],
  conn=r"<strong>Drawing the outline of each person.</strong> To box or trace the people in the frame, take each mask, erode it, and subtract: what remains is a one-pixel ring around each person.",
  cap="The person mask A minus its erosion A ⊖ B leaves the one-pixel outline β(A)."),
3035: dict(d=d3035, stmtKind="ALGORITHM",
  statement=r"<b>Connectivity and two-pass connected-component labelling.</b> The 4-neighbours of $p=(x,y)$ are $N_4(p)=\{(x\pm1,y),(x,y\pm1)\}$ and the 8-neighbours $N_8(p)=N_4(p)\cup\{(x\pm1,y\pm1)\}$. Pass 1: scan row by row, give each foreground pixel the smallest label among its already-labelled neighbours (or a new label) and record the labels found equal. Pass 2: resolve the equivalences (union–find) and replace each label by its class representative. Use 8-connectivity for the foreground with 4-connectivity for the background (or the reverse).",
  hint="Do two pixels touching only at a corner belong to the same person?",
  breakdown=[r"<strong>$N_4(p)$ = the four neighbours that share an edge.</strong> Diagonal pixels do not count as touching.",
             r"<strong>$N_8(p)$ = also the four diagonals.</strong> Two corner-touching pixels now count as one blob.",
             r"<strong>Two passes with union–find = a name for every blob.</strong> The first pass may give one blob two labels; the second merges them. Pair 8-connected objects with a 4-connected background to avoid the closed-curve paradox."],
  conn=r"<strong>Counting people in the frame.</strong> After cleaning the mask, give each separate white blob its own number: that is the head count. Whether two blobs meeting at a corner count as one depends on 4 or 8.",
  cap="Three diagonal pixels are three objects under N₄ but one under N₈. Labelling scans twice: first guess labels, then merge equal ones."),
3036: dict(d=d3036, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> Let $A$ be a filled $5\times5$ square with a one-pixel spur attached ($|A|=26$) and $B$ a $3\times3$ square. Then $A\ominus B$ is the inner $3\times3$ block ($|A\ominus B|=9$, the spur does not fit), and $(A\ominus B)\oplus B$ is the full $5\times5$ square ($25$ pixels), so $A\circ B$ is the square without the spur.",
  hint="After the opening, how many pixels does the person have, and what happened to the spur?",
  breakdown=[r"<strong>$|A|=25+1$ = a $5\times5$ square plus a spur.</strong> Think of a person's mask with one stray pixel sticking out.",
             r"<strong>$|A\ominus B|=9$ = only the inner $3\times3$ survives.</strong> The probe fits only there; the spur is too thin to hold it.",
             r"<strong>$|(A\ominus B)\oplus B|=25$ = growing the core by $B$ rebuilds the square.</strong> The spur does not come back, and the corners stay square."],
  conn=r"<strong>A person mask with a stray pixel.</strong> Opening shaves the stray pixel off and returns the person at the same size. In general, only the pieces that $B$ fits inside come back, so the original is not always restored.",
  cap="A 5×5 square with a spur: erosion keeps only the 3×3 core (9 pixels), dilation grows it back to the 5×5 square (25 pixels) without the spur."),
}

STORY = {
 3031: dict(s="STORY 2 · STEP 7 · SHRINK THE MASK", b="The mask from thresholding is rough. <b>Erosion</b> slides a small probe and keeps only where it fits, deleting specks.",
   f=[["3023", "the mask from a cut"]], n=[["3032", "its twin grows"], ["3033", "combine them"]]),
 3032: dict(s="STORY 2 · STEP 8 · GROW THE MASK", b="<b>Dilation</b> pastes the probe at every object pixel, closing gaps; it is the dual of erosion, not its inverse.",
   f=[["3031", "erosion"]], n=[["3033", "erode then dilate"]]),
 3033: dict(s="STORY 2 · STEP 9 · CLEAN THE MASK", b="<b>Opening</b> removes specks and <b>closing</b> fills holes, each without changing the rest much.",
   f=[["3031", "erosion"], ["3032", "dilation"]], n=[["3034", "outline of the cleaned mask"], ["3036", "a worked case"]]),
 3034: dict(s="STORY 2 · STEP 10 · THE OUTLINE", b="Subtract the eroded mask from the mask to get its <b>boundary</b>.",
   f=[["3031", "erosion"]], n=[["3035", "count the pieces"], ["3131", "edges from gradients instead"]]),
 3035: dict(s="STORY 2 · STEP 11 · COUNT THE PIECES", b="<b>Connected-component labelling</b> gives each separate blob its own name, with 4- or 8-connectivity deciding what is one blob.",
   f=[["3033", "cleaned mask"]], n=[["3036", "worked example"]]),
 3036: dict(s="STORY 2 · STEP 12 · CHECK BY HAND", b="A square with a spur: opening removes the spur and returns the square.",
   f=[["3033", "opening"]], n=[["3041", "next: reshape the grey levels with the CDF"]]),
}
FIX = build_fix(CARDS)
