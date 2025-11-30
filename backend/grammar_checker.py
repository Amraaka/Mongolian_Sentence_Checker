
import nltk
from nltk import CFG
from ..word_lexicon import word_lexicon

# Improved CFG grammar structure
grammar_structure = """
  S -> SIMPLE | COMPOUND | QUESTION

  # --- Энгийн өгүүлбэр ---
  SIMPLE -> NP VP

  # --- Нийлмэл өгүүлбэр ---
  COMPOUND -> SIMPLE CJ SIMPLE | SIMPLE CJ COMPOUND

  # --- Асуулт өгүүлбэр ---
  QUESTION -> QW VP '?' | QW NP VP '?' | SIMPLE '?' | NP QW VP '?'

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

full_grammar_text = build_grammar(word_lexicon, grammar_structure)
grammar = CFG.fromstring(full_grammar_text)
parser = nltk.ChartParser(grammar)

def check_grammar(sentence):
    """
    Checks if the given Mongolian sentence matches the CFG grammar.
    Returns (is_valid, message)
    """
    tokens = sentence.split()
    try:
        trees = list(parser.parse(tokens))
        if trees:
            return True, "Зөв өгүүлбэр: Дүрэмд тохирч байна."
        else:
            return False, "❌ Үр дүн гарсангүй: Дүрэмд тохирохгүй байна."
    except ValueError as e:
        return False, f"❌ Алдаа: {e}"
