from collections import Counter
from string import punctuation

from bs4 import BeautifulSoup
from pelican import generators, signals

#
# Constants
#

WORDS_PER_MINUTE = 250

#
# Functions
#


def process_generators(content_generators):
    """
    Process Article and Page generators
    """
    for generator in content_generators:
        if isinstance(generator, generators.ArticlesGenerator):
            for article in (
                generator.articles + generator.translations + generator.drafts
            ):
                count_words(article)
        elif isinstance(generator, generators.PagesGenerator):
            for page in generator.pages:
                count_words(page)

    return True


def count_words(item):
    """
    Add `stats` attribute with word count and rounded reading time in minutes
    """
    text = BeautifulSoup(item.content, "html.parser").getText()
    words = text.split()
    table = str.maketrans("", "", punctuation)
    stripped = [w.translate(table).lower() for w in words]

    word_count = sum(Counter(stripped).values())
    read_minutes = ((word_count + WORDS_PER_MINUTE - 1) // WORDS_PER_MINUTE) or 1

    item.stats = dict(word_count=word_count, read_minutes=read_minutes)


#
# Entrypoint
#


def register():
    """
    Pelican plugin entrypoint
    """
    signals.all_generators_finalized.connect(process_generators)
