import re

def replace_words_in_text(text):
    # パターンマッチングと置換のための関数
    def replace_match(match):
        word_type = match.group(0).lower()
        return input(f"Enter a {word_type}: ")

    # 正規表現パターン
    pattern = re.compile(r'\b(ADJECTIVE|NOUN|ADVERB|VERB)\b')

    # テキストの置換
    replaced_text = pattern.sub(replace_match, text)
    
    return replaced_text

def process_text_file(file_path):
    # ファイルの読み込み
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # 単語の置換
    replaced_text = replace_words_in_text(text)
    
    # 結果の表示
    print("\n--- Original Text ---\n")
    print(text)
    print("\n--- Replaced Text ---\n")
    print(replaced_text)
    
    # ファイルへの書き込み
    output_path = file_path.replace('.txt', '_replaced.txt')
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(replaced_text)
    
    print(f"\nReplaced text saved to: {output_path}")

# 使用例
file_path = 'panda.txt'  # テキストファイルのパスを指定
process_text_file(file_path)

