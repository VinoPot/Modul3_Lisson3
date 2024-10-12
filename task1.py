import random

first_words = ["Ты блестяще", "Ты неотразимо", "Ты восхитительно", "Ты невероятно", "Ты прекрасно"]
second_words = ["прекрасна!", "мила!", "красивa!", "очаровательна!", "потрясающая!"]

def generate_compliment():
    first = random.choice(first_words)
    second = random.choice(second_words)
    return f"{first} {second}"

for _ in range(5):
    print(generate_compliment())