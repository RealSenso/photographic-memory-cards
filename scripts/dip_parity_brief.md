# DIP: bring the cards up to the StoMA / CMO standard

Work only on the topics you were given. Everyday example stays the **street camera**; do not re-theme it.
Never touch the licensed fonts in `fonts/`. Do not edit `index.html`, `practice_dip.js` or another topic's files.

## One notation (use it in every text field and in drawing labels)

| Thing | Write | Not |
|---|---|---|
| input image, pixel or continuous | `f(x,y)`; `f(m,n)` only where sampling indices are the point | `I(x,y)`, `x[m,n]` |
| output / degraded image | `g(x,y)`, transform `G(u,v)` | |
| filter / PSF | `h(x,y)`, `H(u,v)` | |
| Fourier transform of f | `F(u,v)`, operator `\mathcal F\{f\}` | `\mathcal{F}`, `X(u,v)` |
| DSFT frequencies | `(\omega_1,\omega_2)` | |
| image size | `M\times N` (M rows, N columns) | |
| noise | `\eta(x,y)`, `N(u,v)`, variance `\sigma_\eta^2` | `n(x,y)`, `\sigma_n` |
| power spectra | `S_f(u,v)`, `S_\eta(u,v)` | `S_{ff}`, `S_{nn}` |
| convolution | `\ast` | `*`, `\star` |
| image derivatives | `f_x, f_y`, gradient `\nabla f`, magnitude `\lvert\nabla f\rvert` | `I_x`, `G_x`, `g_x` |
| Gaussian kernel | `G_\sigma(x,y)`, LoG `\nabla^2 G_\sigma` | |
| focal length in pixels (Topic 01 only) | `\alpha_x,\alpha_y` (so `f_x` always means a derivative); `K`, `(c_x,c_y)` unchanged | `f_x, f_y` |
| SSIM images | `f, g`: `\mu_f, \sigma_f^2, \sigma_{fg}` | `\mu_x, \sigma_{xy}` |
| probability, expectation, normal | `\mathbb P`, `\mathbb E`, `\mathcal N(\mu,\sigma^2)` | `P(.)`, `E[.]`, `N(0,1)` |

Exception: Otsu keeps its class weights `\omega_0,\omega_1`. If another clash appears, keep the textbook symbol and report it.

## What to do, per topic NN

1. **Notation.** Apply the table to every field of each card in `scripts/subj_dip_NN.py`, including story text and SVG labels.
2. **Correctness.** Read each card as a student would. Fix wrong maths, wrong labels and drawings that do not show what the caption claims. Check diagrams by rendering them.
3. **Bridge facts.** Read this topic's questions in `practice_dip.js` and the real PYQs in `~/Documents/IISc AI/01 Courses/DIP/06 Exam Prep/{Midterm 1,Midterm 2,Endsem}/PYQs`. If a question needs a step no card states, add one breakdown bullet to the card where it belongs, in the existing `<strong>formula = meaning.</strong> explanation` style. Do not add new cards; report a gap too big for a bullet.
4. **Practice audit.** In `scripts/dip_audit_NN.py` set `MOVES = {question_id: "target topic number", ...}` for a question whose tools are taught in another topic, and `BELOW_PYQ = {question_id: "reason", ...}` for one clearly easier than the real PYQs. Empty dicts are fine. Do not edit or delete questions.
5. **Line by line.** After steps 1-3, run `python3 scripts/apply_subj_refine.py dip`, then write `scripts/subj_dip_lines_NN.py` with `SUBJECT = "DIP"` and `FIX = {card_id: {"statement": ...}}` for all 6 cards, following `scripts/subj_stoma_lines_01.py`:
   - `<b>Title.</b>` first, then each line in `<span class="ln">`; a conclusion or key formula in `<span class="ln in">`; a sub-item in `<span class="ln in2">`; the citation, if any, last in `<span class="src">` without brackets.
   - Break at setups, list items, conclusions and remarks: usually 3-7 lines. Do not change words or maths.
   - Keep equal forms on one line. Inside `\dfrac`, write `\sum\nolimits` so limits do not hit the next line.
   - `python3 scripts/check_stmt_lines.py dip NN` must print OK. After this file exists, change a statement only here.

## Finish

Run `python3 scripts/apply_subj_refine.py dip` once more and confirm it succeeds. Then discard generated output (`git checkout -- cards_data.js cards_dip.js story_dip.js`) and commit **only** your `scripts/subj_dip_NN.py`, `scripts/subj_dip_lines_NN.py` and `scripts/dip_audit_NN.py` on your branch. Do not push or merge; the coordinating session does that. Report what you fixed, MOVES, BELOW_PYQ and any gaps.
