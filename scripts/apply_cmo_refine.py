"""Applies the cmo_refine_*.py patch modules to cards_data.js (idempotent).

Each module may define:
  FIX = {card_id: {field: new_value, ...}}      overwrite fields of an existing card
  NEW = [(after_card_id, {card fields...}), ...]  insert a new card right after another one
  DELETE = [card_id, ...]                         remove cards
Card numbers inside every CMO topic are renumbered 01.. in list order afterwards.
"""
import glob, importlib, json, os, sys

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
path = os.path.join(here, "..", "cards_data.js")

text = open(path).read()
i, j = text.index("["), text.rindex("]") + 1
head, tail = text[:i], text[j:]
cards = json.loads(text[i:j])
by_id = {c["id"]: c for c in cards}

n_fix = n_new = 0
for mod_path in sorted(glob.glob(os.path.join(here, "cmo_refine_*.py"))):
    mod = importlib.import_module(os.path.basename(mod_path)[:-3])
    for cid, fields in getattr(mod, "FIX", {}).items():
        assert cid in by_id, f"unknown card id {cid}"
        by_id[cid].update(fields)
        n_fix += 1
    for cid in getattr(mod, "DELETE", []):
        if cid in by_id:
            cards.remove(by_id.pop(cid))
    for after_id, new in getattr(mod, "NEW", []):
        if new["id"] in by_id:
            by_id[new["id"]].update(new)
            continue
        parent = by_id[after_id]
        card = {
            "id": new["id"], "subject": parent["subject"], "topicId": parent["topicId"],
            "topicTitle": parent["topicTitle"], "cardNumber": "00",
            "category": new.get("category", parent["category"]),
            "highlighterClass": new.get("highlighterClass", parent["highlighterClass"]),
            "title": new["title"], "drawingSvg": new["drawingSvg"],
            "drawingCaption": new["drawingCaption"], "coreTranslation": new["coreTranslation"],
            "math": new["math"], "personalConnection": new["personalConnection"], "examTrap": new["examTrap"],
        }
        if "textbookImg" in new:
            card["textbookImg"] = new["textbookImg"]; card["textbookRef"] = new.get("textbookRef", "")
        cards.insert(cards.index(parent) + 1, card)
        by_id[card["id"]] = card
        n_new += 1

counters = {}
for c in cards:
    if c["subject"] == "CMO":
        counters[c["topicId"]] = counters.get(c["topicId"], 0) + 1
        c["cardNumber"] = f"{counters[c['topicId']]:02d}"

assert len({c["id"] for c in cards}) == len(cards), "duplicate ids"
open(path, "w").write(head + json.dumps(cards, indent=2) + tail)
print(f"patched {n_fix} cards, inserted {n_new}, total CMO {sum(1 for c in cards if c['subject']=='CMO')}")
