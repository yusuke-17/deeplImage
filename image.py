from PIL import Image
import sys
args = sys.argv
import pyocr
import pyocr.builders
import deepl
import os
from dotenv import load_dotenv

load_dotenv()

# OCRエンジンを取得
tools = pyocr.get_available_tools()
tool = tools[0]

# 対応言語取得
langs = tool.get_available_languages()
lang = langs[0]

# 画像の読み込み、ＯＣＲ実行
txt = tool.image_to_string(
    Image.open(args[1]),
    lang=lang,
    builder=pyocr.builders.TextBuilder()
)

# DeepL APIで日本語に翻訳
translator = deepl.Translator(os.environ['DEEPL_API_KEY'])
result = translator.translate_text(txt, target_lang="JA")

print('-------------------和訳-------------------------------------------')
print(result)
print('------------------------------------------------------------------')