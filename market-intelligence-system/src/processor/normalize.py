import re
import unicodedata

def clean_text(text: str) -> str:
text = unicodedata.normalize("NFKC", text)
text = re.sub(r"http\S+", "", text)
text = re.sub(r"[@#]\w+", "", text)
text = text.lower().strip()
return text