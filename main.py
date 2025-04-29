import requests
from time import sleep
import spacy
from sentence_transformers import SentenceTransformer, util
from dataset import beatable_categories
from given_words import words_info

nlp = spacy.load('en_core_web_lg')
model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight and fast

host = "http://192.168.200.127:8000/"
post_url = f"{host}/submit-word"
get_url = f"{host}/get-word"
status_url = f"{host}/status"

NUM_ROUNDS = 10

categories = list(set([c for cat in beatable_categories.values() for c in cat]))

def what_beats(word):
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
    temp_categories = categorize_word_1(word, new_categories, 5)
    final_categories = categorize_word_2(word, temp_categories, 3)

    ans_words = []
    for categ in final_categories:
        for (word, categs) in beatable_categories.items():
            if categ in categs:
                ans_words.append((word, words_info[word]))

    sorted(ans_words, key = lambda elem : elem[1]["cost"], reverse=True)
    if len(ans_words) == 0:
        ans_words = [("Sandpaper", {"id": 1, "cost": 8})]

    print(ans_words[0], ans_words[0][1]["id"])
    return ans_words[0][1]["id"]

def play_game(player_id):

    def get_round():
        response = requests.get(get_url)
        print(response.json())
        sys_word = response.json()['word']
        round_num = response.json()['round']
        return (sys_word, round_num)

    submitted_rounds = []
    round_num = 0

    while round_num != NUM_ROUNDS :
        print(submitted_rounds)
        sys_word, round_num = get_round()
        while round_num == 0 or round_num in submitted_rounds:
            sys_word, round_num = get_round()
            sleep(0.5)

        if round_num > 1:
            status = requests.post(status_url, json={"player_id": player_id}, timeout=2)
            print(status.json())

        choosen_word = what_beats(sys_word)
        data = {"player_id": player_id, "word_id": choosen_word, "round_id": round_num}
        response = requests.post(post_url, json=data, timeout=5)
        submitted_rounds.append(round_num)
        print("POST: !!!!!!!!!!!!!!!!")
        print(response.json())

def register(player_id):
    register_url = f"{host}/register"
    data = {"player_id": player_id}
    response = requests.post(register_url, json=data)
    
    return response.json()
    

register("3WDYqVLl")
play_game("3WDYqVLl")