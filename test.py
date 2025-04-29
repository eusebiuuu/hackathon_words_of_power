import spacy
from sentence_transformers import SentenceTransformer, util
from dataset import beatable_categories
from given_words import words_info
from all_words import word_id_array

nlp = spacy.load('en_core_web_lg')
model = SentenceTransformer('all-MiniLM-L6-v2')

NUM_ROUNDS = 10

categories = list(set([c for cat in beatable_categories.values() for c in cat]))

def what_beats(word):
    def get_actual_words(categories):
        ans_words = []
        for categ in categories:
            for (word, categs) in beatable_categories.items():
                if categ in categs:
                    ans_words.append((word, words_info[word]))
        return ans_words

    def categorize_word_1(word, categories, top_k=3):
        category_docs = [nlp(cat) for cat in categories]
        word_doc = nlp(word)
        
        similarities = [(cat.text, word_doc.similarity(cat)) for cat in category_docs]
        
        similarities = sorted(similarities, key=lambda x: x[1], reverse=True)

        new_categs = [x[0] for x in similarities]
        
        return new_categs[:top_k]


    def categorize_word_2(word, categories, top_k = 3):
        category_embeddings = model.encode(categories, normalize_embeddings=True)

        word_embedding = model.encode(word, normalize_embeddings=True)

        similarities = util.cos_sim(word_embedding, category_embeddings)

        top_categs = similarities.topk(top_k)

        valid_indexes = top_categs.indices[0]

        generated_categories = []
        for i in valid_indexes:
            generated_categories.append(categories[i])

        return generated_categories

    new_categories = categorize_word_2(word, categories, 20)
    temp_categories = categorize_word_1(word, new_categories, 10)
    final_categories = categorize_word_2(word, temp_categories, 3)

    ans_words = get_actual_words(final_categories)
    sorted(ans_words, key = lambda elem : elem[1]["cost"], reverse=True)

    if len(ans_words) == 0:
        ans_words = [("Persistence", {"id": 63, "cost": 80})]

    print(ans_words[0], ans_words[0][1]["id"])
    return ans_words[0][1]["id"]


words = [
    "Quicksand",
    "Mirage",
    "Ectoplasm",
    "Gizmo",
    "Tarnish",
    "Ennui",
    "Prion",
    "Shrapnel",
    "Obsidian",
    "Static",
    "Phobia",
    "Venom",
    "Ember",
    "Tundra",
    "Riot",
    "Monolith",
    "Thorn",
    "Trojan",
    "Apathy",
    "Comet"
]

for word in words:
    print(word + " -> " + word_id_array[what_beats(word)])

