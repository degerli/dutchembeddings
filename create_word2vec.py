import logging

from gensim.models import Word2Vec
from sentences import SentenceIter


class Word2VecFactory:

    @staticmethod
    def create_word2vec(basedir, num_workers=12, size=320, threshold=5):
        """
        Creates a word2vec model using the Gensim implementation.

        :param basedir: the dir from which to get the documents.
        :param num_workers: the number of workers to use for training word2vec
        :param size: the size of the resulting vectors.
        :param threshold: the frequency threshold.
        :return:
        """

        logging.basicConfig(level=logging.INFO)
        sentences = SentenceIter(root=basedir)

        model = Word2Vec(sentences=sentences,
                         sg=True,
                         size=size,
                         workers=num_workers,
                         min_count=threshold,
                         window=11,
                         negative=15)
        model.save_word2vec_format("{0}-{1}.wordvecs", "{0}-{1}.vocab")

        return model

if __name__ == "__main__":

    pass
