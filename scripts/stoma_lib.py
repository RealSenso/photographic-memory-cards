"""Shared library and SVG drawing primitives for StoMA knowledge plates (Sirianni dual-coding format).
Strict black and white aesthetic: #000000 strokes, #ffffff background, #f1f5f9 / #f8fafc subtle gray fills.
"""
import json, os

STOMA_TOPICS = {
    2: ("02_Conditional_Probability_Bayes_Rule_and_Independence", "02 · Conditioning, Bayes & Independence"),
    3: ("03_Discrete_and_Continuous_Random_Variables", "03 · Discrete & Continuous RVs"),
    4: ("04_Transformations_and_Functions_of_a_Random_Variable", "04 · Transformations of Random Variables"),
    5: ("05_Expectation_Variance_Moments_and_Generating_Functions", "05 · Expectation, Variance & MGFs"),
    6: ("06_Probability_Inequalities_Markov_Chebyshev_Chernoff", "06 · Probability Inequalities"),
    7: ("07_Joint_Distributions_Marginal_and_Conditional_Distributions", "07 · Joint, Marginal & Conditional Distributions"),
    8: ("08_Multiple_Random_Variables_and_Order_Statistics", "08 · Multiple RVs & Order Statistics"),
    9: ("09_Sums_of_Random_Variables_and_Jacobian_Transformations", "09 · Sums & Jacobian Transformations"),
    10: ("10_Exchangeable_Random_Variables", "10 · Exchangeable Random Variables"),
    11: ("11_Covariance_Matrices_and_Linear_Least_Squares_Estimation", "11 · Covariance & Linear Least Squares (LLSE)"),
    12: ("12_Conditional_Expectation_and_MMSE_Estimation", "12 · Conditional Expectation & MMSE"),
    13: ("13_Jointly_Gaussian_Random_Variables", "13 · Jointly Gaussian Random Variables"),
    14: ("14_Random_Sums_and_Walds_Equation", "14 · Random Sums & Wald’s Identity"),
    15: ("15_Modes_of_Convergence_and_Relations", "15 · Modes of Convergence"),
    16: ("16_Borel_Cantelli_Lemmas_and_Limsup_Liminf", "16 · Borel-Cantelli Lemmas & Limsup/Liminf"),
    17: ("17_Laws_of_Large_Numbers_WLLN_and_SLLN", "17 · Laws of Large Numbers (WLLN & SLLN)"),
    18: ("18_Characteristic_Functions_and_Central_Limit_Theorem", "18 · Characteristic Functions & CLT"),
    19: ("19_Discrete_Time_Markov_Chains_Chapman_Kolmogorov_and_Classification", "19 · DTMC & State Classification"),
    20: ("20_DTMC_Stationary_Distributions_and_Limiting_Behavior", "20 · Stationary Distributions & Ergodicity"),
    21: ("21_Absorption_Probabilities_and_Mean_Hitting_Times", "21 · Absorption & Mean Hitting Times"),
    22: ("22_Birth_Death_Chains_and_MCMC", "22 · Birth-Death Chains & MCMC"),
    23: ("23_Random_Processes_Stationarity_and_Ergodicity", "23 · Random Processes & Wide-Sense Stationarity"),
    24: ("24_Poisson_Processes_Properties_and_Extensions", "24 · Poisson Processes & Extensions"),
    25: ("25_Random_Walk_Brownian_Motion_and_Gaussian_Processes", "25 · Random Walk & Brownian Motion"),
    26: ("26_Martingales_and_Optional_Stopping_Theorem", "26 · Martingales & Optional Stopping"),
    27: ("27_Continuous_Time_Markov_Chains", "27 · Continuous-Time Markov Chains (CTMC)")
}

HL = ["highlight-cyan", "highlight-amber", "highlight-emerald", "highlight-purple"]

def T(x, y, s, sz=9, a="middle", st="normal", w="normal", f="sans-serif"):
    s = str(s).replace("&", "&amp;").replace("<", "&lt;")
    return (f'<text x="{x}" y="{y}" font-size="{sz}" font-family="{f}" font-style="{st}" '
            f'font-weight="{w}" text-anchor="{a}" fill="#000000">{s}</text>')

def N(x, y, s, sz=8.5, a="middle", w="normal"):
    return T(x, y, s, sz, a, "normal", w, "sans-serif")

def L(x1, y1, x2, y2, w=1.6, d=None, ar=False):
    dash = f' stroke-dasharray="{d}"' if d else ""
    mk = ' marker-end="url(#ARR)"' if ar else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#000000" stroke-width="{w}"{dash}{mk}/>'

def V(x0, y0, x1, y1, w=1.8, d=None):
    return L(x0, y0, x1, y1, w, d=d, ar=True)

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

def AX(x0=24, y0=120, x1=224, y1=20):
    return L(x0, y0, x1, y0, 1.2, ar=True) + L(x0, y0, x0, y1, 1.2, ar=True)

def box(x, y, w, h, label, fill="#f1f5f9", sz=9, bold=True):
    fw = "bold" if bold else "normal"
    cap = max(4, int(w / (sz * 0.52)))
    if len(label) > cap and " " in label:
        words = label.split(" "); best = None
        for i in range(1, len(words)):
            a, b = " ".join(words[:i]), " ".join(words[i:])
            score = max(len(a), len(b))
            if best is None or score < best[0]: best = (score, a, b)
        _, a, b = best
        return R(x, y, w, h, fill, 1.4) + N(x + w / 2, y + h / 2 - 1, a, sz, w=fw) + N(x + w / 2, y + h / 2 + sz, b, sz, w=fw)
    return R(x, y, w, h, fill, 1.4) + N(x + w / 2, y + h / 2 + 3, label, sz, w=fw)

def svg(cid, *parts):
    body = "".join(parts).replace("ARR", f"arr-{cid}")
    return (f'<svg viewBox="0 0 240 145" class="w-full h-full">'
            f'<defs><marker id="arr-{cid}" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" '
            f'orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/></marker></defs>'
            f'{body}</svg>')

def make_stoma_card(topic, k, category, title, svg_parts, caption, bullets, math, anchor, trap):
    tid, ttitle = STOMA_TOPICS[topic]
    cid = 30000 + topic * 100 + k
    assert len(bullets) == 3, f"Card {cid} must have exactly 3 bullets, got {len(bullets)}"
    return {
        "id": cid,
        "subject": "StoMA",
        "topicId": tid,
        "topicTitle": ttitle,
        "cardNumber": f"{k:02d}",
        "category": category,
        "highlighterClass": HL[(k - 1) % 4],
        "title": title,
        "drawingSvg": svg(cid, *svg_parts),
        "drawingCaption": caption,
        "coreTranslation": bullets,
        "math": math,
        "personalConnection": anchor,
        "examTrap": trap,
    }

def save_stoma_cards(new_cards, js_path="cards_stoma.js"):
    """Appends/updates cards in cards_stoma.js while preserving existing cards and sorting by id."""
    existing = []
    if os.path.exists(js_path):
        with open(js_path, "r") as f:
            text = f.read()
        start = text.find("[\n")
        end = text.rfind("}\n]") + 3
        if start != -1 and end > start:
            try:
                existing = json.loads(text[start:end])
            except Exception as e:
                print(f"Warning: could not parse existing cards: {e}")
                existing = []
    card_map = {c["id"]: c for c in existing}
    for c in new_cards:
        card_map[c["id"]] = c
    all_cards = sorted(card_map.values(), key=lambda c: c["id"])
    
    with open(js_path, "w") as f:
        f.write("/* StoMA knowledge plates (topics 02+). Loaded after cards_data.js and appended to it. */\n")
        f.write("window.MASTER_CARDS_DATA = (window.MASTER_CARDS_DATA || []).concat(\n")
        f.write(json.dumps(all_cards, indent=2))
        f.write("\n);\n")
    print(f"Saved {len(all_cards)} StoMA cards to {js_path}")
