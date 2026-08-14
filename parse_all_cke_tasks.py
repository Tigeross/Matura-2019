# -*- coding: utf-8 -*-
import sys, re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

pages_to_check = [2, 4, 6, 8, 10, 12, 14, 15, 16, 17, 18, 19, 20, 22, 24]

for p_num in pages_to_check:
    fname = f"d:/matura/page_{p_num:02d}.html"
    with open(fname, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    
    print(f"\n==================== PAGE {p_num} ====================")
    lines = []
    for p in soup.find_all("p"):
        t = p.get_text().strip()
        if t:
            lines.append(t)
    print(" ".join(lines))
