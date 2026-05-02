import os
from dotenv import load_dotenv
from vectorize_book import (
    vectorize_book_and_store_to_db,
    vectorize_chapters
)

# Load environment variables
load_dotenv()

# Get paths from .env
PHYSICS_PATH = os.getenv("Physics")
CHEMISTRY_PATH = os.getenv("Chemistry")
MATHEMATICS_PATH = os.getenv("Mathematics")


# =========================
# Physics Vector DB
# =========================
vectorize_book_and_store_to_db(
    PHYSICS_PATH,
    "physics_vector_db"
)

vectorize_chapters(PHYSICS_PATH)


# =========================
# Chemistry Vector DB
# =========================
vectorize_book_and_store_to_db(
    CHEMISTRY_PATH,
    "chemistry_vector_db"
)

vectorize_chapters(CHEMISTRY_PATH)


# =========================
# Mathematics Vector DB
# =========================
vectorize_book_and_store_to_db(
    MATHEMATICS_PATH,
    "mathematics_vector_db"
)

vectorize_chapters(MATHEMATICS_PATH)