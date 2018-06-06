from typing import List, Any, Optional

from deeppavlov.core.common.registry import register
from deeppavlov.core.common.log import get_logger

from deeppavlov.dataset_iterators.sqlite_iterator import SQLiteDataIterator

logger = get_logger(__name__)


@register('wiki_sqlite_vocab')
class WikiSQLiteVocab(SQLiteDataIterator):
    """
    Get SQlite documents by ids.
    """

    def __init__(self, load_path, data_dir: str = '', **kwargs):
        """
        :param data_dir: a directory name where DB is located
        :param load_path: an URL to SQLite DB or local path to db file ('example.db')
        """
        super().__init__(load_path=load_path, data_dir=data_dir)

    def __call__(self, doc_ids: Optional[List[List[Any]]] = None, *args, **kwargs) -> List[str]:
        """
        Get the contents of files, stacked by space.
        :param questions: queries to search an answer for
        :param n: a number of documents to return
        :return: document contents (as a single string)
        """
        all_contents = []
        if not doc_ids:
            logger.warn('No doc_ids are provided in WikiSqliteVocab, return all docs')
            doc_ids = [self.get_doc_ids()]

        for ids in doc_ids:
            contents = [self.get_doc_content(doc_id) for doc_id in ids]
            contents = ' '.join(contents)
            all_contents.append(contents)

