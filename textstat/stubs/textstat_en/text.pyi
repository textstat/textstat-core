from textstat import core
from textstat_en.sentence import Sentence as Sentence
from textstat_en.word import Word as Word
from textstat_en.word_collection import WordCollection as WordCollection
from typing import Any

class Text(core.Text, WordCollection):
    sentence_class: Any
    def flesch_reading_ease(self) -> float: ...
    def flesch_kincaid_grade(self) -> float: ...
    def smog(self) -> float: ...
    def smog_grade(self) -> float: ...
    def coleman_liau_index(self) -> float: ...
    def automated_readability_index(self) -> float: ...
    def linsear_write_formula(self) -> float: ...
    def dale_chall_readability_score(self) -> float: ...
    def dale_chall_readability_score_original(self) -> float: ...
    def gunning_fog(self) -> float: ...
    def lix(self) -> float: ...
    def rix(self) -> float: ...
    def spache_readability(self) -> float: ...
