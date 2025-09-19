from abc import ABC, abstractmethod


class BaseReader(ABC):
    @abstractmethod
    def get_content(self, filename: str) -> str:
        pass

    @abstractmethod
    def get_metadata(self, filename: str) -> dict:
        pass
