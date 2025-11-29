import nltk
from nltk import CFG

word_lexicon = {
    'N': ['алим', 'ном', 'оюутан', 'гэр'],
    'PRO': ['би', 'чи', 'тэр'],
    'V': ['идэв', 'уншив', 'явна'],
    'ADJ': ['том', 'улаан', 'шинэ']
}

# 2. CFG ДҮРЭМ (Бүтэц)
# Үгсийг биш, зөвхөн аймгуудыг (POS tags) ашиглан дүрмээ бичнэ.
grammar_structure = """
  S -> NP VP
  VP -> NP V
  NP -> PRO | N | ADJ N
"""

# 3. ҮГСИЙН САН БОЛОН ДҮРМИЙГ НЭГТГЭХ ФУНКЦ
# Программ автоматаар үгсийн санг дүрэм рүү хөрвүүлж байна.
def build_grammar(lexicon, structure):
    lexicon_rules = []
    for tag, words in lexicon.items():
        # Жишээ нь: N -> 'алим' | 'ном' гэж хувиргана
        formatted_words = [f"'{w}'" for w in words]
        rule = f"{tag} -> {' | '.join(formatted_words)}"
        lexicon_rules.append(rule)
    
    return structure + "\n" + "\n".join(lexicon_rules)

# 4. ГОЛ ПРОГРАММ
full_grammar_text = build_grammar(word_lexicon, grammar_structure)
grammar = CFG.fromstring(full_grammar_text)
parser = nltk.ChartParser(grammar)

# Хэрэглэгчийн оролт
user_input = "би том алим идэв" 
tokens = user_input.split()

print(f"Оролт: {tokens}")
print("--- Задлан ---")

try:
    for tree in parser.parse(tokens):
        tree.pretty_print()
        # tree.draw()
except ValueError:
    print("Энэ өгүүлбэрийг задлах боломжгүй (Үг буруу эсвэл дүрэм таарахгүй байна).")