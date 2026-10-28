"""Shared helpers for LAA cards (Sirianni dual-coding format).
Reuses the black-and-white SVG toolkit from dip_lib."""
import json, os
from dip_lib import T, N, L, P, C, R, E, PG, AX, GRID, BARS, svg, HL

import dip_lib as _dl

def _clamp(x, s, sz, a, serif, bold):
    w = len(str(s)) * sz * (0.45 if serif else 0.52) * (1.07 if bold else 1.0)
    if a == "start":
        x = min(x, 236 - w)
        x = max(x, 4)
    elif a == "end":
        x = max(x, w + 4)
        x = min(x, 236)
    else:
        x = min(max(x, w / 2 + 4), 236 - w / 2)
    return x

def T(x, y, s, sz=9, a="middle", st="italic", w="normal", f="serif"):
    x = _clamp(x, s, sz, a, f == "serif", w == "bold")
    return _dl.T(x, y, s, sz, a, st, w, f)

def N(x, y, s, sz=8.5, a="middle", w="normal"):
    return T(x, y, s, sz, a, "normal", w, "sans-serif")

LAA = {
    2: ("02_Linear_Independence_Bases_and_Dimension", "02 · Independence, Bases & Dimension"),
    3: ("03_Linear_Maps_Null_Space_Range_and_Matrices", "03 · Linear Maps, Null Space & Range"),
    4: ("04_Invertibility_Isomorphisms_and_Change_of_Basis", "04 · Isomorphisms & Change of Basis"),
    5: ("05_Polynomials_and_Minimal_Polynomial", "05 · Polynomials & Minimal Polynomial"),
    6: ("06_Eigenvalues_Eigenvectors_and_Diagonalization", "06 · Eigenvalues & Diagonalization"),
    7: ("07_Commuting_Operators_and_Simultaneous_Diagonalization", "07 · Commuting Operators"),
    8: ("08_Generalized_Eigenspaces_and_Nilpotent_Operators", "08 · Generalized Eigenspaces & Nilpotents"),
    9: ("09_Jordan_Canonical_Form_and_Matrix_Functions", "09 · Jordan Form & Matrix Functions"),
    10: ("10_Inner_Product_Spaces_Norms_and_Orthogonality", "10 · Inner Products & Orthogonality"),
    11: ("11_Gram_Schmidt_Orthogonal_Projections_and_QR", "11 · Gram-Schmidt, Projections & QR"),
    12: ("12_Adjoints_Self_Adjoint_and_Normal_Operators", "12 · Adjoints, Self-Adjoint & Normal"),
    13: ("13_The_Spectral_Theorem_Real_and_Complex", "13 · The Spectral Theorem"),
    14: ("14_Positive_Operators_and_Isometries", "14 · Positive Operators & Isometries"),
    15: ("15_Polar_Decomposition_and_Singular_Value_Decomposition", "15 · Polar Decomposition & SVD"),
    16: ("16_Pseudoinverse_and_Least_Squares", "16 · Pseudoinverse & Least Squares"),
    17: ("17_Trace_Determinants_and_Volume", "17 · Trace, Determinant & Volume"),
    18: ("18_Markov_Chains_and_Consensus_Algorithms", "18 · Markov Chains & Consensus"),
}

SUBJ = {"LAA": (LAA, 20000)}


def make_card(subject):
    topics, base = SUBJ[subject]

    def card(topic, k, category, title, svg_parts, caption, bullets, math, anchor, trap):
        tid, ttitle = topics[topic]
        cid = base + topic * 100 + k
        assert len(bullets) == 3, (subject, topic, k)
        return {
            "id": cid, "subject": subject, "topicId": tid, "topicTitle": ttitle,
            "cardNumber": f"{k:02d}", "category": category,
            "highlighterClass": HL[(k - 1) % 4], "title": title,
            "drawingSvg": svg(cid, *svg_parts), "drawingCaption": caption,
            "coreTranslation": bullets, "math": math,
            "personalConnection": anchor, "examTrap": trap,
        }
    return card


def poly(pts, w=1.8, dash=None, fill="none"):
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return P(d, fill=fill, w=w, dash=dash)


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
        return R(x, y, w, h, fill, 1.6) + N(x + w / 2, y + h / 2 - 1, a, sz, w=fw) + N(x + w / 2, y + h / 2 + sz, b, sz, w=fw)
    return R(x, y, w, h, fill, 1.6) + N(x + w / 2, y + h / 2 + 3, label, sz, w=fw)


def write_js(cards, path, label):
    cards = sorted(cards, key=lambda c: c["id"])
    ids = [c["id"] for c in cards]
    assert len(ids) == len(set(ids)), "duplicate ids"
    with open(path, "w") as f:
        f.write(f"/* {label} knowledge plates. Loaded after cards_data.js and appended to it. */\n")
        f.write("window.MASTER_CARDS_DATA = (window.MASTER_CARDS_DATA || []).concat(")
        f.write(json.dumps(cards, indent=2))
        f.write(");\n")
