"""
Speak Zortan
------------

Learning Zortan is simple, they just mirror the sentence and say it
along with the original sentense.

For E.g -
1. sky - skyyks
2. jelly - jellyyllej

So, in order to make things simple Louis wants to write a translation
program bewteen English and Zortan.
"""


def translate_to_zortan(phrase: str) -> str:
    """Translates English to Zortan"""
    return phrase + phrase[::-1]


def translate_to_english(phrase: str) -> str:
    """Translates Zortan to English"""
    return phrase[: len(phrase) // 2]


zello = translate_to_zortan("Hello")
print(zello)

zky = translate_to_zortan("The big blue sky")
print(zky)

sky = translate_to_english(zky)
print(sky)
