#
#
#
import sys

import xml.etree.ElementTree as ET
import html
import textwrap

def extract_and_decode_text_from_xml(file_path):
    # XMLファイルのロードとパース
    tree = ET.parse(file_path)
    root = tree.getroot()

    # <p>タグからテキストを抽出し、HTMLエンティティをデコードする
    for paragraph in root.iter('p'):
        text = paragraph.text
        # HTMLエスケープシーケンスをデコード
        decoded_text = html.unescape(text)
        print(decoded_text)

def extract_and_format_text_from_xml(xml_file_path):
    # XMLファイルを読み込む
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # 結果を格納するリスト
    paragraphs = []

    # <p>タグ内のテキストを取得し、整形する
    for p in root.iter('p'):
        # HTMLエスケープシーケンスを処理する
        text = html.unescape(p.text)
        # テキストを80文字以内で整形する
        wrapped_text = textwrap.fill(text, width=80)
        s = wrapped_text.encode('cp932', "ignore")
        #words = str(s)
        words = s.decode('utf-8')
        paragraphs.append(words)
        #paragraphs.append(wrapped_text)

    print("\n".join(paragraphs))

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print(f"Usage: python3 {sys.argv[0]} <youtube url>")
    sys.exit(1)
  # XMLファイルのパス
  file_path = sys.argv[1]
  # extract_and_decode_text_from_xml(file_path)
  extract_and_format_text_from_xml(file_path)
