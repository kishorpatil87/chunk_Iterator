import pandas as pd

class ChunkIterator:
    def __init__(self, file_path, chunk_size):
        """
        Initializes the iterator with the file path and chunk size.
        
        Args:
        - file_path (str): Path to the CSV file.
        - chunk_size (int): Number of rows per chunk.
        """
        self.file_path = file_path
        self.chunk_size = chunk_size

    def __iter__(self):
        """Returns the iterator object itself."""
        self.reader = pd.read_csv(self.file_path, chunksize=self.chunk_size)
        return self

    def __next__(self):
        """Returns the next chunk of data."""
        try:
            return next(self.reader)
        except StopIteration:
            raise StopIteration
