"""DIP gap cards (built by build_dip_gap_cards.py): their story bands, and the links from the cards before them."""
SUBJECT = "DIP"
FIX = {}

STORY = {
    3066: {"s": "STORY 3 · STEP 12 · CHECK BY HAND", "b": "A $2\\times2$ patch worked through: DC and three contrasts.",
           "f": [["3061", "the DFT"]], "n": [["3067", "next: read a short filter in frequency"]]},
    3067: {"s": "STORY 3 · STEP 12A · READ THE FILTER", "b": "A few taps give a <b>DSFT</b> you can write by hand: $H(0)$ and $H(\\pi)$ say low-pass or high-pass.",
           "f": [["3051", "the filter's taps"], ["3061", "the DFT samples this curve"]], "n": [["3068", "a real exam bug"]]},
    3068: {"s": "STORY 3 · STEP 12B · CHECK BY HAND", "b": "Drop the centre of a blur and you get $\\frac23\\cos\\Omega$: the finest detail <b>passes as strongly as DC</b>.",
           "f": [["3067", "DSFT of short filters"]], "n": [["3071", "next: what happens when the frame is only sampled"]]},
    3086: {"s": "STORY 4 · STEP 6 · CHECK BY HAND", "b": "Two pixels: the sum and difference are the KLT, with $75\\%$ of the variance in the first.",
           "f": [["3084", "KLT"]], "n": [["3087", "next: round the coefficients"]]},
    3087: {"s": "STORY 4 · STEP 6A · ROUND THE VALUES", "b": "A <b>quantizer</b> replaces each value by the nearest allowed level. This is the only lossy step.",
           "f": [["3082", "JPEG quantizes DCT coefficients"]], "n": [["3088", "how much error it adds"]]},
    3088: {"s": "STORY 4 · STEP 6B · THE PRICE", "b": "The rounding error has power <b>$\\Delta^2/12$</b>: double the step and the MSE is four times larger.",
           "f": [["3087", "the uniform quantizer"]], "n": [["3089", "now code the levels"], ["3121", "MSE as a quality measure"]]},
    3089: {"s": "STORY 4 · STEP 6C · THE FLOOR", "b": "<b>Entropy</b> is the fewest bits per symbol any lossless code can average.",
           "f": [["3087", "quantizer levels are the symbols"]], "n": [["3090", "a code that gets close"]]},
    3090: {"s": "STORY 4 · STEP 6D · CHECK BY HAND", "b": "<b>Huffman</b>: merge the two rarest symbols until one node is left, then read the codewords.",
           "f": [["3089", "entropy"]], "n": [["3091", "next: look at several scales at once"]]},
}


def POST(c):
    pass
