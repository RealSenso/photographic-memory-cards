#!/usr/bin/env python3
"""
build_practice_stoma_batch.py
Generates flippable practice cards for StoMA in batches of 2 topics.
Each topic gets 3 cards:
  - P1: IISc Midterm / Endsem PYQ
  - P2: Stanford / MIT / Berkeley / IIT PYQ
  - P3: Generated / Master Exam-Level Problem
Appends or updates practice_stoma.js.
"""

import os
import re
import json
import sys

BASE_DIR = "/Users/senso/Documents/IISc AI/Endsem Prep/StoMA"
REPO_DIR = "/Users/senso/Projects/photographic-memory-cards"
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_stoma.js")

TOPIC_CATALOG = [
    ("01_Probability_Spaces_Axioms_and_Continuity_of_Probability", "01 · Probability Spaces & Continuity"),
    ("02_Conditional_Probability_Bayes_Rule_and_Independence", "02 · Conditioning, Bayes & Independence"),
    ("03_Discrete_and_Continuous_Random_Variables", "03 · Discrete & Continuous RVs"),
    ("04_Transformations_and_Functions_of_a_Random_Variable", "04 · Transformations of Random Variables"),
    ("05_Expectation_Variance_Moments_and_Generating_Functions", "05 · Expectation, Variance & MGFs"),
    ("06_Probability_Inequalities_Markov_Chebyshev_Chernoff", "06 · Probability Inequalities"),
    ("07_Joint_Distributions_Marginal_and_Conditional_Distributions", "07 · Joint, Marginal & Conditional Distributions"),
    ("08_Multiple_Random_Variables_and_Order_Statistics", "08 · Multiple RVs & Order Statistics"),
    ("09_Sums_of_Random_Variables_and_Jacobian_Transformations", "09 · Sums & Jacobian Transformations"),
    ("10_Exchangeable_Random_Variables", "10 · Exchangeable Random Variables"),
    ("11_Covariance_Matrices_and_Linear_Least_Squares_Estimation", "11 · Covariance & Linear Least Squares (LLSE)"),
    ("12_Conditional_Expectation_and_MMSE_Estimation", "12 · Conditional Expectation & MMSE"),
    ("13_Jointly_Gaussian_Random_Variables", "13 · Jointly Gaussian Random Variables"),
    ("14_Random_Sums_and_Walds_Equation", "14 · Random Sums & Wald’s Identity"),
    ("15_Modes_of_Convergence_and_Relations", "15 · Modes of Convergence"),
    ("16_Borel_Cantelli_Lemmas_and_Limsup_Liminf", "16 · Borel-Cantelli Lemmas & Limsup/Liminf"),
    ("17_Laws_of_Large_Numbers_WLLN_and_SLLN", "17 · Laws of Large Numbers (WLLN & SLLN)"),
    ("18_Characteristic_Functions_and_Central_Limit_Theorem", "18 · Characteristic Functions & CLT"),
    ("19_Discrete_Time_Markov_Chains_Chapman_Kolmogorov_and_Classification", "19 · DTMC & State Classification"),
    ("20_DTMC_Stationary_Distributions_and_Limiting_Behavior", "20 · Stationary Distributions & Ergodicity"),
    ("21_Absorption_Probabilities_and_Mean_Hitting_Times", "21 · Absorption & Mean Hitting Times"),
    ("22_Birth_Death_Chains_and_MCMC", "22 · Birth-Death Chains & MCMC"),
    ("23_Random_Processes_Stationarity_and_Ergodicity", "23 · Random Processes & Wide-Sense Stationarity"),
    ("24_Poisson_Processes_Properties_and_Extensions", "24 · Poisson Processes & Extensions"),
    ("25_Random_Walk_Brownian_Motion_and_Gaussian_Processes", "25 · Random Walk & Brownian Motion"),
    ("26_Martingales_and_Optional_Stopping_Theorem", "26 · Martingales & Optional Stopping"),
    ("27_Continuous_Time_Markov_Chains", "27 · Continuous-Time Markov Chains (CTMC)"),
]

def extract_braced(text, start_idx):
    brace_open = text.find("{", start_idx)
    if brace_open == -1:
        return None, -1
    depth = 0
    i = brace_open
    while i < len(text):
        if text[i] == "{" and (i == 0 or text[i-1] != "\\"):
            depth += 1
        elif text[i] == "}" and (i == 0 or text[i-1] != "\\"):
            depth -= 1
            if depth == 0:
                return text[brace_open+1:i], i + 1
        i += 1
    return None, -1

def clean_latex(latex_str):
    """Converts LaTeX markup into web-ready HTML with KaTeX formulas."""
    s = latex_str.strip()
    # Replace display math \[ ... \] with $$ ... $$
    s = re.sub(r'\\\[', '$$', s)
    s = re.sub(r'\\\]', '$$', s)
    # Replace align / align* environments with $$ \begin{aligned} ... \end{aligned} $$
    s = re.sub(r'\\begin\{align\*?\}', r'$$\\begin{aligned}', s)
    s = re.sub(r'\\end\{align\*?\}', r'\\end{aligned}$$', s)
    # Replace \textbf{...}
    s = re.sub(r'\\textbf\{([^}]+)\}', r'<strong>\1</strong>', s)
    # Replace \textit{...}
    s = re.sub(r'\\textit\{([^}]+)\}', r'<em>\1</em>', s)
    # Clean double line breaks into paragraphs
    paragraphs = [p.strip() for p in s.split('\n\n') if p.strip()]
    formatted_paras = []
    for p in paragraphs:
        if p.startswith('\\begin{itemize}') or p.startswith('\\begin{enumerate}'):
            # Convert list
            items = re.split(r'\\item\s+', p)
            list_items = []
            for item in items[1:]:
                clean_item = item.replace('\\end{itemize}', '').replace('\\end{enumerate}', '').strip()
                list_items.append(f"<li>{clean_item}</li>")
            formatted_paras.append(f"<ul>{''.join(list_items)}</ul>")
        elif p.startswith('$$') and p.endswith('$$'):
            formatted_paras.append(p)
        else:
            # Replace single \par or \\ with <br>
            p_html = p.replace('\\par', '<br>').replace('\\\\', '<br>')
            formatted_paras.append(f"<p>{p_html}</p>")
    return '\n\n'.join(formatted_paras)

def parse_tex_problem_set(t_idx):
    """Parses ProblemSet_XX.tex for topic index t_idx (1-based)."""
    folder_name, topic_title = TOPIC_CATALOG[t_idx - 1]
    tex_path = os.path.join(BASE_DIR, folder_name, "_source", f"ProblemSet_{t_idx:02d}.tex")
    if not os.path.exists(tex_path):
        raise FileNotFoundError(f"Missing {tex_path}")
    with open(tex_path, 'r', encoding='utf-8') as f:
        text = f.read()

    doc_start = text.find("\\begin{document}")
    idx = doc_start if doc_start != -1 else 0
    raw_problems = []
    while True:
        pbox_idx = text.find("\\problembox", idx)
        if pbox_idx == -1:
            break
        header, next_idx = extract_braced(text, pbox_idx)
        body, next_idx = extract_braced(text, next_idx)
        sbox_idx = text.find("\\solutionbox", next_idx)
        if sbox_idx == -1:
            break
        sheader, s_next = extract_braced(text, sbox_idx)
        sbody, s_next = extract_braced(text, s_next)
        raw_problems.append((header, body, sheader, sbody))
        idx = s_next

    return folder_name, topic_title, raw_problems

print("Loaded parser successfully.")
