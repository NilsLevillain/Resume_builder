#!/usr/bin/env python3
"""
CV Generator — ATS-friendly HTML & PDF
========================================
Usage:
  python generate.py              → FR + EN
  python generate.py --lang fr    → français uniquement
  python generate.py --lang en    → english only
"""
import argparse
from src.exporter import export_all

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Générateur de CV ATS-friendly")
    parser.add_argument(
        "--lang",
        choices=["fr", "en", "all"],
        default="all",
        help="Langue à générer (défaut : all)",
    )
    args  = parser.parse_args()
    langs = ["fr", "en"] if args.lang == "all" else [args.lang]
    export_all(langs)