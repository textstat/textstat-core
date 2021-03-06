import pytest

import textstat


@pytest.fixture
def example_sentence():
    return "when suddenly a White Rabbit with pink eyes ran close by her"


def test_words_greater_than_six_letters(example_sentence):
    text = textstat.Text(example_sentence)

    words = text.filter(textstat.Word.length > 6)

    assert words == [
        "suddenly",
    ]


def test_words_less_than_six_letters(example_sentence):
    text = textstat.Text(example_sentence)

    words = text.filter(textstat.Word.length < 6)

    assert words == [
        "when",
        "a",
        "White",
        "with",
        "pink",
        "eyes",
        "ran",
        "close",
        "by",
        "her",
    ]


def test_words_less_than_or_equal_six_letters(example_sentence):
    text = textstat.Text(example_sentence)

    words = text.filter(textstat.Word.length <= 6)

    assert words == [
        "when",
        "a",
        "White",
        "Rabbit",
        "with",
        "pink",
        "eyes",
        "ran",
        "close",
        "by",
        "her",
    ]


def test_words_greater_than_or_equal_six_letters(example_sentence):
    text = textstat.Text(example_sentence)

    words = text.filter(textstat.Word.length >= 6)

    assert words == [
        "suddenly",
        "Rabbit",
    ]


def test_words_contain_ly(example_sentence):
    text = textstat.Text(example_sentence)

    words = text.filter(textstat.Word.text.contains("en"))

    assert words == ["when", "suddenly"]


def test_words_startswith_w(example_sentence):
    text = textstat.Text(example_sentence)

    words = text.filter(textstat.Word.text.startswith("w"))

    assert words == ["when", "with"]


def test_words_endswith_ly(example_sentence):
    text = textstat.Text(example_sentence)

    words = text.filter(textstat.Word.text.endswith("ly"))

    assert words == ["suddenly"]


def test_sentences_greater_than_four_words():
    text = textstat.Text(
        "Welcome to the Carpathians. "
        "I am anxiously expecting you. "
        "Sleep well to-night."
    )

    sentences = text.filter(textstat.Sentence.length > 4)

    assert sentences == ["I am anxiously expecting you."]


def test_sentences_ends_with_you():
    text = textstat.Text(
        "Welcome to the Carpathians. "
        "I am anxiously expecting you. "
        "Sleep well to-night."
    )

    sentences = text.filter(textstat.Sentence.text.endswith("you."))

    assert sentences == ["I am anxiously expecting you."]
