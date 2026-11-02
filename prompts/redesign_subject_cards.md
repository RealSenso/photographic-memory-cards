# Prompt: redesign a subject's cards the way CMO was done

Copy everything below the line into a new Claude Code session opened in
`/Users/senso/Projects/photographic-memory-cards`, and replace `<SUBJECT>` with StoMA or DIP.
The session chooses the everyday example for the subject itself. Run one subject per session.

---

Redesign every `<SUBJECT>` card on the Plates site so it matches the finished CMO cards: same layout, same level of personal explanation, same picture style. Do it topic by topic.

## Read first
- `index.html`: how a card renders. Cards that have a `breakdown` field use the CMO layout: title, story band, HINT, statement box (THEOREM / DEFINITION / …), THE MATH, THE BREAKDOWN, figure and caption, and the translation box (AIRPLANE TRANSLATION on CMO, PHOTO-EDIT TRANSLATION on LAA).
- Three finished CMO cards in `cards_data.js` (for example ids 401, 702 and 1101), and their story entries in `story_cmo_a.js` / `story_cmo_b.js`. Match their tone and length.
- The `<SUBJECT>` cards: topic 01 is in `cards_data.js`; the other topics are in `cards_<subject>.js`.
- Drawing helpers: `scripts/air_lib.py` (`plane`, `arrow`, `dot`, `dash`, `wall`, `circ`, `fn`) and `scripts/subj_lib.py` (`N`, `T`, `L`, `C`, `R`, `E`, `PG`, `poly`, `svg`).
- The existing pipeline. If `scripts/apply_subj_refine.py` exists, reuse it and follow the LAA modules `scripts/subj_laa_*.py` as the pattern. If it does not, copy the idea of `scripts/apply_cmo_refine.py`: patch modules applied in sorted order, so re-running is safe.

## How I study (keep this in mind for every card)
I copy each card into a notebook by hand. The method: title the card, explain it informally in my own words, connect it to my life, draw it, and revisit it later. The green highlighting and the split layout are just the site's style.

## What every card gets
Keep `title`, `math`, `coreTranslation` and `examTrap`. Add or replace:
1. **`hint`**: one question that makes me recall the idea, in the language of the everyday example.
2. **`statement`** and **`stmtKind`**: the precise textbook statement (DEFINITION, THEOREM, PROPOSITION, LEMMA, COROLLARY, ALGORITHM or WORKED EXAMPLE), with all hypotheses, then the conclusion, in standard book form (Axler for LAA, Ross / Grimmett for StoMA, Gonzalez & Woods for DIP). Write `\lt` and `\gt` inside math instead of `<` and `>`.
3. **`breakdown`**: 3 bullets. Each starts with a bold formula term from THE MATH, e.g. `<strong>$\ker T$ = …</strong>`, then says in plain words what that term is and why it is there.
4. **`personalConnection`**: the translation into the subject's everyday example (see below). Start with a short bold title, then 2–4 sentences.
5. **Story band** (a `STORY` dict, written to `story_<subject>.js`): `{s: "STORY n · STEP k · SHORT TAG", b: one sentence on where this card sits in the big picture, f: [[id, why]] for the cards it builds on, n: [[id, why]] for the cards it leads to}`. Plan the whole subject's storyline first, so every card links back and forward and the topics read as one connected story.
6. **New drawing** (`drawingSvg`, 240×145 viewBox) and **`drawingCaption`**:
   - The drawing must explain the formula on the card. Mark every term of THE MATH on the picture.
   - Draw the subject's everyday example.
   - Draw curves, not contour lines.
   - Use thin lines (stroke-width at most 1.2) and normal-weight text, never bold.
   - Use real Unicode subscripts (xₖ, λᵢ). Never write `_`.
   - Keep labels on the canvas and off the lines.
   - Set `textbookImg` and `textbookRef` to `None` so the drawing is shown.
   - The caption says in 1–2 sentences what the picture shows, naming the formula terms.

## Choose the everyday example yourself
CMO uses an airplane flying over a valley, because that was easy for me to relate to. LAA uses a photo edited on a phone. For `<SUBJECT>`, **you** pick the example; do not ask me to choose.
- It must be one real-life situation, easy to picture and remember, and it must work for **every** topic of `<SUBJECT>`. It does not have to be an airplane or a photo; pick whatever fits this subject best.
- First list every topic of `<SUBJECT>` (from the card files) and write one line per topic on how it maps onto your example. If any topic has no natural place in it, throw the example away and try another. Compare at least three candidates and keep the one with the fewest forced mappings.
- Then post the chosen example and the topic-by-topic table in one short message and start right away, without waiting for a reply. If I object later, switch.
- Use the example the same way on every card: the same name for the same idea everywhere, in hints, breakdowns, translations, captions, story bands and drawings.
- Add the subject to the `TRANSLATION` map in `index.html` (for example `LAA: 'PHOTO-EDIT TRANSLATION'`). That is the heading of the translation box.

## Working rules
- Reuse `scripts/apply_subj_refine.py` (run it as `python3 scripts/apply_subj_refine.py <subject in lowercase>`). It applies every `scripts/subj_<subject>_*.py` module in sorted order and writes `story_<subject>.js`.
- Follow the LAA files as the pattern: `scripts/laa_lib.py` (drawing helpers for its example) and `scripts/subj_laa_01.py` (one topic module with `CARDS`, `STORY` and `FIX`). Make your own `scripts/<subject>_lib.py` for your example's drawing helpers.
- One patch module per topic: `scripts/subj_<subject>_NN.py`, defining `SUBJECT`, `FIX = {id: {...}}` and `STORY = {id: {...}}`, plus the drawing functions.
- Add `<script src="story_<subject>.js?v=...">` to `index.html` next to the other story scripts.
- After each topic, run the apply script. Then preview that topic's drawings on a contact sheet in the in-app browser and fix overlapping or cut-off labels.
- Check the site at a 1440×900 viewport: no card may scroll, the text-size variable `--lh` must not go below 19, and there must be no `.katex-error`.
- Bump the `?v=` of each changed data or story script in `index.html`.
- Commit after every few topics, so finished work is never lost. Commit only the files you changed, and never stage `practice_*.js` or `fonts/`.
- Other sessions may be redesigning other subjects at the same time, and topic 01 of every subject lives in the shared `cards_data.js`. Before each push run `git pull --rebase --autostash`. If `cards_data.js` or `index.html` conflict, take the incoming version, re-run your apply script (it is idempotent) and re-add your `index.html` lines, then continue.
