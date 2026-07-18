from pathlib import Path

from knowledge.knowledge_ingestion import KnowledgeIngestion


class KnowledgePackLoader:
    @staticmethod
    def load_directory(directory_path):

        loaded_documents = []

        directory = Path(directory_path)

        if not directory.exists():
            return loaded_documents

        for file in directory.rglob("*.md"):
            result = KnowledgeIngestion.ingest(str(file))

            loaded_documents.append(result)

        return loaded_documents

    @staticmethod
    def load_all():

        loaded_documents = []

        knowledge_folders = [
            "knowledge/tmforum",
            "knowledge/telecom",
            "knowledge/protocols",
            "knowledge/testing",
            "knowledge/frameworks",
            "knowledge/best-practices",
        ]

        for folder in knowledge_folders:
            loaded_documents.extend(KnowledgePackLoader.load_directory(folder))

        return loaded_documents
