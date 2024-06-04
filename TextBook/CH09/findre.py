import os
import re

def search_files_in_directory(directory, regex_pattern):
    # コンパイルされた正規表現パターン
    pattern = re.compile(regex_pattern)
    
    # 指定されたディレクトリ内のすべての.txtファイルを取得
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line_number, line in enumerate(lines, start=1):
                    if pattern.search(line):
                        print(f"File: {filename}, Line {line_number}: {line.strip()}")

# 使用例
directory = '/home/vagrant/pg2_2/TextBook/CH09'  # ディレクトリのパスを指定
regex_pattern = 'panda'  # 検索する正規表現パターンを指定

search_files_in_directory(directory, regex_pattern)

