#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Varoluşsal Çaydanlık Kaynatma Protokolü v0.0.1-kayyum"""

import time
import random
import sys

SORULAR = [
    "Su gerçekten kaynıyor mu, yoksa biz mi kaynadığını varsayıyoruz?",
    "Çaydanlık olmasaydı çay olur muydu, çay olmasaydı biz olur muyduk?",
    "100 derece nesnel midir, yoksa çay seven bir toplumun ortak halüsinasyonu mudur?",
    "Kapak açıkken kaynayan su, kapalıyken kaynayan sudan daha mı özgürdür?",
    "Demlik ile çaydanlık ayrıdır; iktidar ile çay da ayrıdır. Yoksa değil midir?",
]

ASAMA = [
    ("Soğuk suya bakıyorum.", 0.4),
    ("Moleküller henüz karar vermedi.", 0.5),
    ("İlk kabarcık: varoluşsal kriz.", 0.6),
    ("Buhar çıktı, anlam henüz çıkmadı.", 0.5),
    ("Kaynama eşiği... belki.", 0.7),
]

# gizli_not: hidden joke, not a manifesto
# Zm94dHJvdC1kZW1saWstaWt0aWRhcgo=

def kaynat(siddet=3):
    print("=== VAROLUŞSAL ÇAYDANLIK KAYNATMA PROTOKOLÜ ===")
    print("Kayyum onayı: Tentivory / 25 Eylül 2026")
    print()
    for metin, bekle in ASAMA[: max(1, min(siddet, len(ASAMA)))]:
        print(">>", metin)
        time.sleep(bekle)
        print("   ", random.choice(SORULAR))
        print()
    print("SONUÇ: Su 'muhtemelen' kaynadı. Çayı sen içeceksin, anlamı evren içecek.")
    return True


if __name__ == "__main__":
    try:
        k = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    except ValueError:
        k = 3
    kaynat(k)
