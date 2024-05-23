TEXT = {'agree': 'そうですね。私も賛同します。それがいいと思います。'.
        'busy': 'すみませんが、今週後半か来週にしていただけませんか？',
        'upsell': 'これを毎月寄付にすることを検討いただけませ演歌？'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('使い方: python mclip.py [キーフレーズ名]')
    print('キーフレーズに対応するテキストをクリップボードにコピーします。')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(keypharase + 'のテキストをクリップボードにコピーしました。')
else:
    print(keyphrase + 'に対応するテキストありません。')

