"""
Parser Tree Demo for Mongolian sentences

- Builds CFG using the updated word lexicon and grammar
- Parses input sentences and pretty-prints the first parse tree
- Mirrors the behavior shown in `test1.py`

Usage:
  python3 backend/parse_demo.py "би хэзээ ном уншсан"
  python3 backend/parse_demo.py           # interactive prompt
"""

import sys
import re
import nltk
from nltk import CFG

# Use the backend-local lexicon to avoid ambiguity with root-level files
from word_lexicon import word_lexicon  # path: backend/word_lexicon.py


# Grammar structure aligned with backend/grammar_checker.py (kept consistent)
grammar_structure = """
    S -> SIMPLE | COMPOUND | QUESTION

    # --- Энгийн өгүүлбэр ---
    SIMPLE -> NP VP

    # --- Нийлмэл өгүүлбэр ---
    COMPOUND -> SIMPLE CJ SIMPLE | SIMPLE CJ COMPOUND

    # --- Асуулт өгүүлбэр ---
    QUESTION -> QW VP QEND | QW NP VP QEND | SIMPLE QEND | NP QW VP QEND
    QEND -> '?' | 'бэ' | 'вэ'

    # --- Noun Phrase (Нэр үгийн аймаг) ---
    NP -> PRON | N 
    NP -> NUM N | ADJ N | ADJ NP

    # --- Verb Phrase (Үйл үгийн аймаг) ---
    VP -> V
    VP -> NP V       
    VP -> VP V       
    VP -> ADV VP     
    VP -> VP ADV     
"""


def build_grammar(lexicon, structure):
    lexicon_rules = []
    for tag, words in lexicon.items():
        formatted_words = [f"'{w}'" for w in words]
        rule = f"{tag} -> {' | '.join(formatted_words)}"
        lexicon_rules.append(rule)
    return structure + "\n" + "\n".join(lexicon_rules)


def make_parser():
    full_grammar_text = build_grammar(word_lexicon, grammar_structure)
    grammar = CFG.fromstring(full_grammar_text)
    return nltk.ChartParser(grammar)


def tokenize(sentence: str):
    # Keep question particles "бэ/вэ/?" by not stripping them entirely
    cleaned = re.sub(r"[\.,!\-\(\)\[\]\"':;]", "", sentence)
    # Remove stray '?' if not as a token
    cleaned = re.sub(r"(?<! )\?(?! )", "", cleaned)
    tokens = [w.lower() for w in cleaned.split()]
    return tokens


def parse_and_show(sentence: str):
    parser = make_parser()
    tokens = tokenize(sentence)
    try:
        trees = list(parser.parse(tokens))
    except ValueError as e:
        print(f"❌ Алдаа: {e}")
        return 1

    print("=" * 50)
    print("ПАРСЕР МОДНЫ ДЕМO")
    print("=" * 50)
    print(f"Өгүүлбэр: '{sentence}'")

    if trees:
        print(f"✔ Олдсон хувилбарууд: {len(trees)}")
        # Pretty-print only the first tree (like test1.py)
        trees[0].pretty_print()
        return 0
    else:
        print("❌ Үр дүн гарсангүй: Дүрэмд тохирохгүй байна.")
        return 2


def main():
    if len(sys.argv) > 1:
        sentence = " ".join(sys.argv[1:])
    else:
        try:
            sentence = input("Өгүүлбэр оруулна уу: ")
        except EOFError:
            print("Орлого алга.")
            return 1
    return parse_and_show(sentence)


if __name__ == "__main__":
    raise SystemExit(main())
