"""DIP Topic 04 statements, line by line (one setup, item or conclusion per line)."""

SUBJECT = "DIP"

FIX = {
    3031: {"statement": r"""<b>Erosion.</b>"""
        r"""<span class="ln">For sets $A,B\subseteq\mathbb Z^2$ (the image and a structuring element), the erosion of $A$ by $B$ is</span>"""
        r"""<span class="ln in">$A\ominus B=\{z\mid (B)_z\subseteq A\}=\bigcap_{b\in B}A_{-b}$,</span>"""
        r"""<span class="ln">where $(B)_z$ is $B$ translated by $z$.</span>"""
        r"""<span class="ln">It is the set of positions of $B$'s origin for which $B$ lies entirely inside $A$.</span>"""
    },
    3032: {"statement": r"""<b>Dilation and duality.</b>"""
        r"""<span class="ln">The dilation of $A$ by $B$ is</span>"""
        r"""<span class="ln in">$A\oplus B=\{z\mid(\hat B)_z\cap A\ne\emptyset\}=\bigcup_{b\in B}A_b$,</span>"""
        r"""<span class="ln">where $\hat B=\{-b: b\in B\}$ is the reflection of $B$.</span>"""
        r"""<span class="ln">Erosion and dilation are dual:</span>"""
        r"""<span class="ln in">$(A\ominus B)^c=A^c\oplus\hat B$.</span>"""
    },
    3033: {"statement": r"""<b>Opening and closing.</b>"""
        r"""<span class="ln">The opening of $A$ by $B$ is $A\circ B=(A\ominus B)\oplus B$,</span>"""
        r"""<span class="ln">and the closing is $A\bullet B=(A\oplus B)\ominus B$.</span>"""
        r"""<span class="ln">Both are idempotent:</span>"""
        r"""<span class="ln in">$(A\circ B)\circ B=A\circ B$</span>"""
        r"""<span class="ln in">and $(A\bullet B)\bullet B=A\bullet B$.</span>"""
        r"""<span class="ln">Opening removes objects (and spurs) in which $B$ does not fit;</span>"""
        r"""<span class="ln">closing fills holes and gaps that $B$ cannot enter.</span>"""
    },
    3034: {"statement": r"""<b>Boundary extraction.</b>"""
        r"""<span class="ln">The boundary of a set $A$ is $\beta(A)=A-(A\ominus B)$,</span>"""
        r"""<span class="ln">with $B$ a $3\times3$ structuring element (giving a 1-pixel-thick outline).</span>"""
        r"""<span class="ln">More general local patterns are found by the hit-or-miss transform</span>"""
        r"""<span class="ln in">$A\circledast B=(A\ominus B_1)\cap(A^c\ominus B_2)$.</span>"""
    },
    3035: {"statement": r"""<b>Connectivity and two-pass connected-component labelling.</b>"""
        r"""<span class="ln">The 4-neighbours of $p=(x,y)$ are $N_4(p)=\{(x\pm1,y),(x,y\pm1)\}$</span>"""
        r"""<span class="ln">and the 8-neighbours $N_8(p)=N_4(p)\cup\{(x\pm1,y\pm1)\}$.</span>"""
        r"""<span class="ln">Pass 1: scan row by row, give each foreground pixel the smallest label among its already-labelled neighbours (or a new label) and record the labels found equal.</span>"""
        r"""<span class="ln">Pass 2: resolve the equivalences (union–find) and replace each label by its class representative.</span>"""
        r"""<span class="ln">Use 8-connectivity for the foreground with 4-connectivity for the background (or the reverse).</span>"""
    },
    3036: {"statement": r"""<b>Example.</b>"""
        r"""<span class="ln">Let $A$ be a filled $5\times5$ square with a one-pixel spur attached ($|A|=26$) and $B$ a $3\times3$ square.</span>"""
        r"""<span class="ln">Then $A\ominus B$ is the inner $3\times3$ block ($|A\ominus B|=9$, the spur does not fit),</span>"""
        r"""<span class="ln in">and $(A\ominus B)\oplus B$ is the full $5\times5$ square ($25$ pixels),</span>"""
        r"""<span class="ln in">so $A\circ B$ is the square without the spur.</span>"""
    },
}
