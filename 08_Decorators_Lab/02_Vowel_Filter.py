def vowel_filter(function):
    def wrapper():
        letters = function()
        vowels = ['a', 'e', 'i', 'o', 'u']
        filtered_vowels = [letter for letter in letters if letter.lower() in vowels]
        return filtered_vowels

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
