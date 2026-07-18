from pathlib import Path


class DocumentLoader:
    @staticmethod
    def load(file_path):

        extension = Path(file_path).suffix.lower()

        if extension == ".txt":
            return DocumentLoader.load_text_file(file_path)

        if extension == ".md":
            return DocumentLoader.load_markdown_file(file_path)

        raise ValueError(f"Unsupported file type: {extension}")

    @staticmethod
    def load_text_file(file_path):

        return Path(file_path).read_text(encoding="utf-8")

    @staticmethod
    def load_markdown_file(file_path):

        return Path(file_path).read_text(encoding="utf-8")
