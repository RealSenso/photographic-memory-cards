"""Builds ../cards_laa.js from laa_topics_*.py."""
import glob, importlib, os, sys
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
from subj_lib import write_js

cards = []
for path in sorted(glob.glob(os.path.join(here, "laa_topics_*.py"))):
    cards += importlib.import_module(os.path.basename(path)[:-3]).CARDS
write_js(cards, os.path.join(here, "..", "cards_laa.js"), "LAA")
print("LAA", len(cards), "cards -> cards_laa.js")
