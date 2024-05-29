import pyinputplus as pyip

# 各選択肢の値段
prices = {
    'bread': {'小麦パン': 200, '白パン': 150, 'サワー種': 170},
    'protein': {'チキン': 150, 'ターキー': 150, 'ハム': 100, '豆腐': 50},
    'cheese': {'チェダー': 100, 'スイス': 100, 'モツァレラ': 150},
    'extras': {'マヨネーズ': 50, 'からし': 50, 'レタス': 50, 'トマト': 50}
}

# パンの種類を選択
bread_choice = pyip.inputMenu(['小麦パン', '白パン', 'サワー種'], prompt="パンの種類を選んでください:\n")
# タンパク質の種類を選択
protein_choice = pyip.inputMenu(['チキン', 'ターキー', 'ハム', '豆腐'], prompt="タンパク質の種類を選んでください:\n")
# チーズが必要かどうか尋ねる
cheese_needed = pyip.inputYesNo("チーズが必要ですか? (yes/no): ")

cheese_choice = None
if cheese_needed == 'yes':
    # チーズの種類を選択
    cheese_choice = pyip.inputMenu(['チェダー', 'スイス', 'モツァレラ'], prompt="チーズの種類を選んでください:\n")

# 各種調味料が必要かどうか尋ねる
extras = {}
for extra in ['マヨネーズ', 'からし', 'レタス', 'トマト']:
    response = pyip.inputYesNo(f"{extra}が必要ですか? (yes/no): ")
    if response == 'yes':
        extras[extra] = True
    else:
        extras[extra] = False

# サンドイッチの数を尋ねる
num_sandwiches = pyip.inputInt("サンドイッチはいくつ必要ですか? (1以上): ", min=1)

# 合計金額の計算
total_cost = 0
total_cost += prices['bread'][bread_choice]
total_cost += prices['protein'][protein_choice]
if cheese_choice:
    total_cost += prices['cheese'][cheese_choice]
for extra in extras:
    if extras[extra]:
        total_cost += prices['extras'][extra]

total_cost *= num_sandwiches

# 合計金額の表示
print(f"\nサンドイッチの合計金額は: ¥{total_cost:.2f} です。")

