from deep_translator import GoogleTranslator
import json


with open('aa.json', 'r', encoding='utf-8-sig') as file:
    original_data = json.load(file)


languages = ['en', 'ja', 'ko', 'pl', 'ru', 'tr', 'uk', 'vi', 'zh-TW']


for lang in languages:
    translator = GoogleTranslator(source='auto', target=lang)

    translated_data = []
    for item in original_data:
        translated_chapters = []
        for chapter in item['chapters']:
            translated_texts = []
            for text in chapter:
                chunks = [text[i:i + 5000] for i in range(0, len(text), 5000)]
                translated_chunks = []
                for i, chunk in enumerate(chunks):
                    translation = translator.translate(chunk)
                    translated_chunks.append(translation)
                    print(
                        f"Chunk {i + 1} de '{text[:50]}...' traduzido para {lang}")
                translated_text = ''.join(translated_chunks)
                translated_texts.append(translated_text)
            translated_chapters.append(translated_texts)

        translated_item = {
            "abbrev": item["abbrev"],
            "chapters": translated_chapters
        }
        translated_data.append(translated_item)

    
    output_file_name = f'aa-{lang}.json'
    with open(output_file_name, 'w', encoding='utf-8') as output_file:
        json.dump(translated_data, output_file, ensure_ascii=False, indent=2)

    print(f"JSON traduzido para '{lang}' salvo em '{output_file_name}'")
