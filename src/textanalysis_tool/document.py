from textanalysis_tool.readers.base_reader import BaseReader


class Document:
    def __init__(self, filepath: str, reader: BaseReader):
        self.filepath = filepath
        self.reader = reader

        self._content = self.reader.get_content(filepath)
        metadata = self.reader.get_metadata(filepath)
        self.title = metadata.get("title")
        self.author = metadata.get("author")
        self.id = metadata.get("id")

    def get_line_count(self) -> int:
        """
        Get the number of lines in the document content.

        Args:
            None

        Returns:
            int: the number of lines in the document.
        """
        return len(self._content.splitlines())

    def get_word_occurrence(self, word: str) -> int:
        return self._content.lower().count(word.lower())
