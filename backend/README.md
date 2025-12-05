# Instructions to run the Flask backend server

1. (Optional) Create and activate a virtual environment:
   python3 -m venv .venv
   source .venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Run the server:
   python app.py

The server will start on http://127.0.0.1:5000/

## Parser Tree Demo

- File: `backend/parse_demo.py`
- This script builds the CFG using `backend/word_lexicon.py` and the same grammar structure as `backend/grammar_checker.py`, then pretty-prints the first parse tree (similar to `test1.py`).

### Quick try

```bash
source ../.venv/bin/activate
python3 parse_demo.py "би хэзээ ном уншсан"
```

Or run interactively:

```bash
source ../.venv/bin/activate
python3 parse_demo.py
```

Note: If a sentence does not match the current grammar, the script reports no parse. Try simple forms like `"би уншсан"`, add particles (`"би ном уншсан"`), or question forms ending with `бэ/вэ/?` depending on the rule: e.g., `"хэн ном уншсан бэ"`.
