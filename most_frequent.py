
import sys

def most_frequent(text):
    word_count = {}

    # Compter les occurrences de chaque mot
    for line in text:
        key, value = line.strip().split('\t')
        word_count[key] = word_count.get(key, 0) + int(value)

    # Trouver le mot avec le comptage le plus élevé
    most_frequent_word = None
    max_frequency = 0
    for word, count in word_count.items():
        if count > max_frequency:
            most_frequent_word = word
            max_frequency = count

    return most_frequent_word, max_frequency

if __name__ == '__main__':
    # Lire la sortie du mapper
    result = most_frequent(sys.stdin)

    # Afficher le résultat
    print("Le mot le plus fréquent est :", result[0])
    print("Sa fréquence est :", result[1])
