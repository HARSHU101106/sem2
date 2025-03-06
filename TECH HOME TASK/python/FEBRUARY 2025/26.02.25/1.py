def reverse_alternate_words(sentence):
    words = sentence.split(' ')
    for i in range(len(words)):
        if i % 2 == 1:  
            words[i] = words[i][::-1]
    return ' '.join(words)
input_text = "Hello world this is Python"
output_text = reverse_alternate_words(input_text)
print(output_text) 
