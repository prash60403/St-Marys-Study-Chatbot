import os
from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredFileLoader,DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Load environment variables
load_dotenv()

# Environment Variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

PHYSICS_PATH = os.getenv("Physics")
CHEMISTRY_PATH = os.getenv("Chemistry")
MATHEMATICS_PATH = os.getenv("Mathematics")

DEVICE = os.getenv("DEVICE", "cpu")

# Base directories
working_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(working_dir)

vector_db_dir = f"{parent_dir}/vector_db"
chapters_vector_db_dir = f"{parent_dir}/chapters_vector_db"

# Embedding model
embedding = HuggingFaceEmbeddings(
    model_kwargs={"device": DEVICE}
)

# Text splitter
text_splitter = CharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=500
)


def vectorize_book_and_store_to_db(book_path, vector_db_name):

    vector_db_path = f"{vector_db_dir}/{vector_db_name}"

    loader = DirectoryLoader(
        path=book_path,
        glob="./*.pdf",
        loader_cls=UnstructuredFileLoader
    )

    documents = loader.load()

    text_chunks = text_splitter.split_documents(documents)

    Chroma.from_documents(
        documents=text_chunks,
        embedding=embedding,
        persist_directory=vector_db_path
    )

    print(f"{vector_db_name} saved to vector DB")

    return 0


def vectorize_chapters(book_path):

    for chapter in os.listdir(book_path):

        if not chapter.endswith(".pdf"):
            continue

        chapter_name = chapter[:-4]

        chapter_pdf_path = f"{book_path}/{chapter}"

        loader = UnstructuredFileLoader(chapter_pdf_path)

        documents = loader.load()

        texts = text_splitter.split_documents(documents)

        Chroma.from_documents(
            documents=texts,
            embedding=embedding,
            persist_directory=f"{chapters_vector_db_dir}/{chapter_name}"
        )

        print(f"{chapter_name} chapter vectorized")

    return 0


# =========================
# Run Vectorization
# =========================

if __name__ == "__main__":

    # Physics
    vectorize_book_and_store_to_db(
        PHYSICS_PATH,
        "physics_db"
    )

    vectorize_chapters(PHYSICS_PATH)

    # Chemistry
    vectorize_book_and_store_to_db(
        CHEMISTRY_PATH,
        "chemistry_db"
    )

    vectorize_chapters(CHEMISTRY_PATH)

    # Mathematics
    vectorize_book_and_store_to_db(
        MATHEMATICS_PATH,
        "mathematics_db"
    )

    vectorize_chapters(MATHEMATICS_PATH)