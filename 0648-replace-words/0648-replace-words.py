class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root_set = set(dictionary)
    
        def replace(word):
            for i in range(1, len(word) + 1):
                if word[:i] in root_set:
                    return word[:i]
            return word

        words = sentence.split()
        replaced_words = [replace(word) for word in words]
        return ' '.join(replaced_words)
