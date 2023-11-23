from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

def open_file(path: str) -> str:
    content = ""
    with open(path, "r", encoding='utf-8') as f:
        content = f.readlines()
    return " ".join(content)

all_words = ""
frase = open_file("texto.txt")

palabras = frase.rstrip().split(" ")

# Obtener la lista de stopwords en español
stop_words = set(stopwords.words('spanish'))

# Filtrar las stopwords
filtered_words = [word for word in palabras if word.lower() not in stop_words]

# Crear la cadena de todas las palabras filtradas
all_words = " ".join(filtered_words)

wordcloud = WordCloud(
    background_color="white", min_font_size=5
).generate(all_words)

# print(all_words)
# plot the WordCloud image
plt.close()
plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig("plots/word_cloud.png")
plt.close()
