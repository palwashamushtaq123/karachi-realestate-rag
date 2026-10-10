# ingest.py
import argparse
import json

from app.ingest_service import IngestionService


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Generate local embeddings and store "
            "documents in ChromaDB."
        )
    )

    parser.add_argument(
        "--data-dir",
        default="./knowledge_base",
        help="Path to the directory containing documents to ingest."
    )

    parser.add_argument(
        "--reset",
        action="store_true",
        help="Reset/clear the ChromaDB collection before ingesting."
    )

    args = parser.parse_args()

    result = IngestionService().ingest(
        directory=args.data_dir,
        reset=args.reset,
    )

    print(
        json.dumps(
            result,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()