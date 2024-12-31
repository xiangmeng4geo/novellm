from langchain.chains import LLMChain
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS, Milvus
from langchain_text_splitters import CharacterTextSplitter
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2.5:14b", base_url="http://localhost:11434", temperature=0.1)

db_uri = "http://localhost:9091"


def dissection_pipeline_with_rag(book_path, query):
    loader = TextLoader(book_path, encoding="utf-8")
    documents = loader.load()

    # 分割文本
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)

    # 创建向量存储
    vector_store = Milvus.from_documents(chunks, OllamaEmbeddings(model="nomic-embed-text"),
                                         connection_args={"uri": db_uri})

    # 创建检索器
    retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 1, "fetch_k": 2, "lambda_mult": 0.5})

    # 创建RAG链
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )

    # 查询并生成结果
    response = qa_chain.run(query)

    return response


# 使用RAG技术生成书籍大纲
result = dissection_pipeline_with_rag("孔乙己.txt", "请为本书生成大纲")
print(result)
