# cli.py
from app.rag_service import RAGService


def main() -> None:
    rag = RAGService()

    print("\n==========================================")
    print(" Karachi Real Estate Intelligence RAG CLI ")
    print("==========================================")
    print("Embeddings: SentenceTransformers (local/free)")
    print("LLM: Groq API")
    print("Type 'exit' or 'q' to quit.\n")

    while True:
        question = input("Question: ").strip()

        if question.lower() in {"exit", "quit", "q"}:
            print("\nExiting RAG CLI. Goodbye!")
            break

        if not question:
            continue

        try:
            result = rag.ask(question)

            print("\nANSWER:")
            print(result["answer"])

            print("\nRETRIEVED SOURCES:")
            for source in result["sources"]:
                print(
                    f'- {source["source"]} | '
                    f'page={source["page"] or "n/a"} | '
                    f'chunk={source["chunk"]} | '
                    f'distance={source["distance"]:.4f}'
                )

            print()

        except Exception as exc:
            print(f"\nERROR: {exc}\n")


if __name__ == "__main__":
    main()