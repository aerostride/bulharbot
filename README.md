___

# BulharBot v1

> "Sedim v autě, jedu na AGIPku, natankovat benzín, koupit si bagetu."
>
> *- CA$HANOVA BULHAR*

___

**Obecné:**

Jednoduchý bot na tweetování náhodných textů z Genius. Kód se dá přizpůsobit podle libosti. Hosting na AWS Lambda, pro správnou funkci musí být správně zabalen.

___

**Filelist:**

*bot.py* - hlavní kód, pro správnou funkci je nutnost vlastnit **Genius API klíč** a **Twitter Developer účet**.

*lookup.py* - sekundární ústřižek kódu, po adekvátní změně dokáže do konzole vypsat index písní zpěváka. Pro správnou funkci je nutnost vlastnit **Genius API** klíč.

___

**Použité balíky:**

* Tweepy (API na Tweetování skrz Python)
* Lyricsgenius (API na vyhledávání textů, zpěváků...)

**Napsáno v Python 3.8.1**

___

**Poznámky:**

Pro správnou funkci s UTF-8 charsetem musí být kód API **Lyricsgenius** [následovně](https://github.com/johnwmillr/LyricsGenius/pull/126/files) upraven.

[Návod na nastavení s AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html#python-package-venv)

---

