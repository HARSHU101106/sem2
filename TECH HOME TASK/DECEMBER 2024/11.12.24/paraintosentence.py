import re
class TextProcessor:
    def __init__(self, text):
        self.text = text
        self.sentences = []
    def split_into_sentences(self):
        self.sentences = re.split(r'(?<=[.!?])\s+', self.text.strip())
        return self.sentences
    def process_sentences(self):
        processed_data = []
        for sentence in self.sentences:
            word_count = len(sentence.split())
            processed_data.append({"sentence": sentence,"word_count": word_count})
        return processed_data    
input_text = input()
processor = TextProcessor(input_text)
print("Split Sentences:")
sentences = processor.split_into_sentences()
for sentence in sentences:
    print(f"{sentence}")
print("\nProcessed Sentence Data:")
processed_data = processor.process_sentences()
for data in processed_data:
    print(f"Sentence: {data['sentence']}",f"Word Count: {data['word_count']}")
 