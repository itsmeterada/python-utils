from fontTools.ttLib import TTFont
import sys
import argparse

def get_font_characters(font_path):
    try:
        font = TTFont(font_path)
        
        cmap = font.getBestCmap()
        characters = []
        
        for codepoint, glyph in cmap.items():
            char = chr(codepoint)
            
            if sys.version_info >= (3, 3):
                try:
                    _ = char.encode('utf-8')
                    characters.append(char)
                except UnicodeEncodeError:
                    pass
            else:
                try:
                    _ = char.encode('utf-8')
                    characters.append(char)
                except UnicodeEncodeError:
                    pass

        font.close()
        return sorted(set(characters), key=lambda x: ord(x))
    
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(description='TTFフォントの文字一覧を表示')
    parser.add_argument('font_path', help='TTFフォントファイルパス')
    args = parser.parse_args()
    
    characters = get_font_characters(args.font_path)
    
    if not characters:
        print("このフォントに表示可能な文字はありませんか、またはフォントファイルが不正です")
        return
    
    print("\nフォント内の文字一覧:")
    for idx, char in enumerate(characters, start=1):
        print(f"{idx:4d}: {char} (U+{ord(char):06X})")

if __name__ == "__main__":
    main()

