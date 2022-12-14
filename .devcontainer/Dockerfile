FROM python:latest
ENV PYTHONUNBUFFERED 1 

# tesseractと依存ライブラリをaptでインストール
RUN apt-get update
RUN apt-get -y install \
    tesseract-ocr \
    tesseract-ocr-jpn
RUN apt-get clean

RUN pip install --upgrade deepl
RUN pip install Pillow
RUN pip install pyocr
RUN pip install pytesseract
RUN pip install python-dotenv

ENTRYPOINT ["/usr/bin/tail", "-f", "/dev/null"]