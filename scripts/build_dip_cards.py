"""Builds ../cards_dip.js from the dip_topics_*.py modules (DIP topics 02+)."""
import glob, importlib, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dip_lib import write_js

here = os.path.dirname(os.path.abspath(__file__))
cards = []
for path in sorted(glob.glob(os.path.join(here, "dip_topics_*.py"))):
    mod = importlib.import_module(os.path.basename(path)[:-3])
    cards += mod.CARDS
out = os.path.join(here, "..", "cards_dip.js")
write_js(cards, out)
print(len(cards), "cards ->", os.path.normpath(out))
