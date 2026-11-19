from abc import ABC, abstractmethod


class Writer(ABC):

    @abstractmethod
    def write(self):
        raise NotImplementedError


class TxtWriter(Writer):

    def write(self):
        print("Пишу в текстовый файл")


class CsvWriter(Writer):

    def write(self):
        print("Пишу в csv файл")


class PdfWriter(Writer):

    def write(self):
        print("Пишу в pdf файл")


class ExcelWriter(Writer):

    def write(self):
        print("Пишу в excel файл")