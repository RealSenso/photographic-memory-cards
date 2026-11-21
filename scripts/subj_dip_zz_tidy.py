"""DIP: last notation pass, for the few fields the topic modules do not write."""
SUBJECT = "DIP"
FIX = {}
FIELDS = ("math", "coreTranslation", "statement", "breakdown")
# card titles are shown in capitals, which changes these symbols (eta becomes H, x becomes the tristimulus X), so they use words
TITLES = {
    40102: "The Camera Matrix",
    3013: "Chromaticity Diagram",
    3022: "Point Operations on Intensity",
    3034: "Boundary Extraction: A Minus Its Erosion",
    3053: "Separable Kernels",
    3072: "Nyquist Sampling Rate",
    3101: "Degradation Model: Blur Plus Noise",
    3141: "Line in Normal Form",
    3153: "Harris Corner Response",
    3182: "The Small-Sample Trick",
}


def _t(s):
    return s.replace(r"\mathcal{F}", r"\mathcal F").replace(r"\ast I(x,y)", r"\ast f(x,y)")


def POST(c):
    c["title"] = TITLES.get(c["id"], c["title"])
    for k in FIELDS:
        v = c.get(k)
        if isinstance(v, str): c[k] = _t(v)
        elif isinstance(v, list): c[k] = [_t(x) for x in v]
