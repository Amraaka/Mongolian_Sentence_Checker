
import nltk
from nltk import CFG
from word_lexicon import word_lexicon

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

full_grammar_text = build_grammar(word_lexicon, grammar_structure)
grammar = CFG.fromstring(full_grammar_text)
parser = nltk.ChartParser(grammar)


def check_grammar(sentence):
    import re
    cleaned = re.sub(r'[\.!\-\(\)\[\]"\'\:;]', '', sentence)
    cleaned = re.sub(r'(?<! )\?(?! )', '', cleaned)
    tokens = [w.lower() for w in cleaned.split()]
    try:
        trees = list(parser.parse(tokens))
    except ValueError as e:
        return False, f"Алдаа: {e}"
    if trees:
        return True, "Зөв өгүүлбэр: Дүрэмд тохирч байна."
    else:
        return False, "Өгүүлбэрийг дүрмээр зурж чадахгүй байна: Дүрэмд тохирохгүй байна, эсвэл бүтэц нь буруу байна."

is_sentence_correct = check_grammar
