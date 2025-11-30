import nltk
from nltk import CFG
from word_lexicon import word_lexicon

# 2. CFG ДҮРЭМ (ЗАСВАРЛАСАН)
# Тайлбар:
# - '?' тэмдгийг дүрмэн дотор хашилтад хийсэн.
# - VP дүрмийг баяжуулж, Тусагдахуун (NP V) болон Туслах үйл үг (VP V)-ийг оруулсан.
grammar_structure = """
  S -> SIMPLE | COMPOUND | QUESTION

  # --- Энгийн өгүүлбэр ---
  SIMPLE -> NP VP

  # --- Нийлмэл өгүүлбэр ---
  COMPOUND -> SIMPLE CJ SIMPLE | SIMPLE CJ COMPOUND

  # --- Асуулт өгүүлбэр ---
  # QW (Асуух үг) + NP + VP + '?'
  # Жишээ: Хэн(QW) ном(NP) уншиж байна(VP) ?
  QUESTION -> QW VP '?' | QW NP VP '?' | SIMPLE '?' | NP QW VP '?'

  # --- Noun Phrase (Нэр үгийн аймаг) ---
  NP -> PRON | N 
  NP -> NUM N | ADJ N | ADJ NP

  # --- Verb Phrase (Үйл үгийн аймаг) ---
  VP -> V
  VP -> NP V       
  # (Жишээ: "ном(NP) уншиж(V)")
  
  VP -> VP V       
  # (Жишээ: "уншиж(VP) байна(V)" - Туслах үйл үгтэй)
  
  VP -> ADV VP     
  # (Жишээ: "хурдан(ADV) гэртээ ирнэ(VP)")
  
  VP -> VP ADV     
  # (Жишээ: "гүйж(VP) байна(V) хурдан(ADV)")
"""

# 3. Үгсийн санг дүрэмтэй холбох
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

# 4. TEST ӨГҮҮЛБЭРҮҮД
test_sentences = [
    "Тэр хэдэн төгрөг болсон бэ ",
        "Чи хаана сурдаг вэ",
            "би ном хийсэн"    # COMPOUND
]

print(f"{'='*50}")
print("ЗАСВАРЛАСАН КОДНЫ ҮР ДҮН")
print(f"{'='*50}")

for sent in test_sentences:
    tokens = sent.split()
    print(f"\nӨгүүлбэр: '{sent}'")
    try:
        # Generator-ийг list болгож хувилбаруудыг шалгана
        trees = list(parser.parse(tokens))

        if trees:
            # Зөвхөн эхний хувилбарыг зурж харуулна
            trees[0].pretty_print()
        else:
            print("❌ Үр дүн гарсангүй: Дүрэмд тохирохгүй байна.")

    except ValueError as e:
        print(f"❌ Алдаа: {e}") 