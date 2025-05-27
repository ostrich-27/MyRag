import chromadb
from ollama import embed
from datetime import datetime
from uuid import uuid4


class MyChroma(object):
    def __init__(self,
                 db_path: str = None):
        if db_path is None:
            self.__core = chromadb.EphemeralClient()
        else:
            self.__core = chromadb.PersistentClient(path = db_path)
        self.__setup()

    def __setup(self):
        self.__core.get_or_create_collection(name = 'main', metadata = {"description": "default collection", "created": str(datetime.now())})

    def add_docs(self,
                 text: list[str],
                 ids: list[str] = None,
                 metadata: list[dict] = None
                 ):
        l = len(text)
        if l > 0:
            embeds = MyChroma.default_embedder(text)
            collection = self.__core.get_collection(name = 'main')
            if ids is None:
                ids = [str(uuid4()) for _ in range(l)]
            collection.add(ids = ids, embeddings = embeds, documents = text, metadatas = metadata)
        return None

    def search_docs(self,
                    questions: list[str] = None,
                    ids: list[str] = None,
                    n_result: int = 4,
                    metadata_filter: dict = None,
                    full_text_search: dict = None
                    ):
        if isinstance(questions, list):
            l_questions = len(questions)
        else:
            l_questions = 0
        if l_questions == 0:
            if metadata_filter is None and full_text_search is None:
                return None
            else:
                # 无查询文本 仅通过Metadata或者full text查找
                collection = self.__core.get_collection(name = 'main')
                return collection.get(ids = ids,
                                      where = metadata_filter,
                                      where_document = full_text_search)
        else:
            collection = self.__core.get_collection(name = 'main')
            embeds = MyChroma.default_embedder(questions)
            return collection.query(query_embeddings = embeds,
                                    query_texts = questions,
                                    n_results = n_result,
                                    where = metadata_filter,
                                    where_document = full_text_search
                                    )

    @property
    def check(self):
        return self.__core.heartbeat()

    @property
    def sizeof(self):
        return self.__core.get_or_create_collection(name = 'main').count()

    @staticmethod
    def default_embedder(source: list[str]):
        """
        model='modelscope.cn/nomic-ai/nomic-embed-text-v1.5-GGUF:latest'
        :param source:
        :return:
        """
        return embed(model = 'modelscope.cn/nomic-ai/nomic-embed-text-v1.5-GGUF:latest', input = source).embeddings



class QAUnit(MyChroma):
    def __init__(self,
                 db_path: str = None):
        super().__init__(db_path = db_path)

    def create_relevant_qa(self, q: str, a: str, metadata: dict = None):
        relevant_id = str(uuid4())
        if metadata is None:
            metadata = dict()
        q_meta = metadata.copy()
        a_meta = metadata.copy()
        q_meta.update({"qa_Type": "Q", "qa_ID": f"{relevant_id}"})
        a_meta.update({"qa_Type": "A", "qa_ID": f"{relevant_id}"})
        self.add_docs(text = [q], metadata = [q_meta])
        self.add_docs(text = [a], metadata = [a_meta])
        return None

    def get_relevant_qa(self, q: str) -> {dict, dict}:
        relevant_q = self.search_docs(
                                    metadata_filter = {"qa_Type": "Q"},
                                    full_text_search = {"$contains": q})
        relevant_id = relevant_q['metadatas'][0]['qa_ID']
        relevant_a = self.search_docs(metadata_filter = {"$and":[
            {"qa_Type": "A"},
            {"qa_ID": relevant_id}
        ]})
        return relevant_q, relevant_a

