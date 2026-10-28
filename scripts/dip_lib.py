"""Helpers for DIP cards (Sirianni dual-coding format): black-and-white ink diagrams,
3-point plain translation, formal math, memory anchor, exam trap."""
import json

TOPICS = {
    2:  ("02_Color_Theory_and_Color_Spaces", "02 · Color Theory & Color Spaces"),
    3:  ("03_Histograms_Point_Operations_and_Thresholding_Otsu", "03 · Histograms, Point Ops & Otsu"),
    4:  ("04_Binary_Morphology_and_Connected_Components", "04 · Binary Morphology & Connected Components"),
    5:  ("05_Histogram_Equalization_and_Specification", "05 · Histogram Equalization & Specification"),
    6:  ("06_LSI_Systems_2D_Convolution_and_Spatial_Filtering", "06 · LSI Systems, Convolution & Filtering"),
    7:  ("07_2D_Fourier_Transforms_CSFT_DSFT_and_DFT", "07 · 2D Fourier Transforms (CSFT, DSFT, DFT)"),
    8:  ("08_Sampling_Theorem_Aliasing_and_Multi_Rate_Conversion", "08 · Sampling, Aliasing & Multi-Rate"),
    9:  ("09_Discrete_Cosine_Transform_DCT_and_KLT", "09 · DCT & KLT"),
    10: ("10_Wavelets_and_Multiresolution_Analysis", "10 · Wavelets & Multiresolution"),
    11: ("11_Image_Restoration_Inverse_and_Wiener_Filtering", "11 · Restoration: Inverse & Wiener"),
    12: ("12_Non_Linear_Restoration_Median_and_Bilateral_Filters", "12 · Median & Bilateral Filters"),
    13: ("13_Image_Quality_Assessment_MSE_PSNR_and_SSIM", "13 · Image Quality: MSE, PSNR, SSIM"),
    14: ("14_Edge_Detection_Gradients_LoG_and_Canny", "14 · Edge Detection: Gradients, LoG, Canny"),
    15: ("15_Hough_Transform_for_Lines_and_Circles", "15 · Hough Transform"),
    16: ("16_Corner_Detection_and_Harris_Detector", "16 · Corners & Harris Detector"),
    17: ("17_Scale_Invariant_Feature_Transform_SIFT", "17 · SIFT"),
    18: ("18_Bag_of_Visual_Words_Model", "18 · Bag of Visual Words"),
    19: ("19_Face_Recognition_Eigenfaces_and_Viola_Jones", "19 · Eigenfaces & Viola-Jones"),
    20: ("20_Deep_Learning_and_CNN_Architectures_for_Images", "20 · Deep Learning & CNN Architectures"),
}
HL = ["highlight-cyan", "highlight-amber", "highlight-emerald", "highlight-purple"]


def T(x, y, s, sz=9, a="middle", st="italic", w="normal", f="serif"):
    s = str(s).replace("&", "&amp;").replace("<", "&lt;")
    return (f'<text x="{x}" y="{y}" font-size="{sz}" font-family="{f}" font-style="{st}" '
            f'font-weight="{w}" text-anchor="{a}" fill="#000000">{s}</text>')

def N(x, y, s, sz=8.5, a="middle", w="normal"):
    return T(x, y, s, sz, a, "normal", w, "sans-serif")

def L(x1, y1, x2, y2, w=1.6, d=None, ar=False):
    dash = f' stroke-dasharray="{d}"' if d else ""
    mk = ' marker-end="url(#ARR)"' if ar else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#000000" stroke-width="{w}"{dash}{mk}/>'

def P(d, fill="none", w=1.8, dash=None, ar=False):
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    mk = ' marker-end="url(#ARR)"' if ar else ""
    return f'<path d="{d}" fill="{fill}" stroke="#000000" stroke-width="{w}"{ds}{mk}/>'

def C(cx, cy, r=3, fill="#000000", w=1.5):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="#000000" stroke-width="{w}"/>'

def R(x, y, w, h, fill="#f1f5f9", sw=1.5, rx=0, d=None):
    ds = f' stroke-dasharray="{d}"' if d else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="#000000" stroke-width="{sw}"{ds}/>'

def E(cx, cy, rx, ry, rot=0, fill="none", w=1.3, d=None):
    ds = f' stroke-dasharray="{d}"' if d else ""
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="#000000" '
            f'stroke-width="{w}"{ds} transform="rotate({rot} {cx} {cy})"/>')

def PG(pts, fill="#f1f5f9", w=1.8, d=None):
    ds = f' stroke-dasharray="{d}"' if d else ""
    return f'<polygon points="{pts}" fill="{fill}" stroke="#000000" stroke-width="{w}"{ds}/>'

def AX(x0=20, y0=125, x1=222, y1=14):
    return L(x0, y0, x1, y0, 1.2, ar=True) + L(x0, y0, x0, y1, 1.2, ar=True)

def GRID(x, y, vals, cell=18, shade=None, sz=8.5):
    """Pixel grid of numbers. vals: list of rows. shade: set of (r,c) to fill gray."""
    out = []
    for r, row in enumerate(vals):
        for c, v in enumerate(row):
            fill = "#d9dee7" if shade and (r, c) in shade else "#ffffff"
            out.append(R(x + c * cell, y + r * cell, cell, cell, fill, 1.1))
            out.append(N(x + c * cell + cell / 2, y + r * cell + cell / 2 + 3, str(v), sz))
    return "".join(out)

def BARS(x0, base, vals, bw=14, gap=4, scale=1.0, fill="#f1f5f9", w=1.3):
    out = []
    for i, v in enumerate(vals):
        h = v * scale
        out.append(R(x0 + i * (bw + gap), base - h, bw, h, fill, w))
    return "".join(out)

def svg(cid, *parts):
    body = "".join(parts).replace("ARR", f"arr-{cid}")
    return (f'<svg viewBox="0 0 240 145" class="w-full h-full">'
            f'<defs><marker id="arr-{cid}" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" '
            f'orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/></marker></defs>'
            f'{body}</svg>')

def card(topic, k, category, title, svg_parts, caption, bullets, math, anchor, trap):
    tid, ttitle = TOPICS[topic]
    cid = 3000 + (topic - 1) * 10 + k
    assert len(bullets) == 3, (topic, k)
    return {
        "id": cid, "subject": "DIP", "topicId": tid, "topicTitle": ttitle,
        "cardNumber": f"{k:02d}", "category": category,
        "highlighterClass": HL[(k - 1) % 4], "title": title,
        "drawingSvg": svg(cid, *svg_parts), "drawingCaption": caption,
        "coreTranslation": bullets, "math": math,
        "personalConnection": anchor, "examTrap": trap,
    }

def write_js(cards, path):
    cards = sorted(cards, key=lambda c: c["id"])
    ids = [c["id"] for c in cards]
    assert len(ids) == len(set(ids)), "duplicate ids"
    with open(path, "w") as f:
        f.write("/* DIP knowledge plates (topics 02+). Loaded after cards_data.js and appended to it. */\n")
        f.write("window.MASTER_CARDS_DATA = (window.MASTER_CARDS_DATA || []).concat(")
        f.write(json.dumps(cards, indent=2))
        f.write(");\n")
