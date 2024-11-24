from src.chunk_iterator import ChunkIterator
from src.statistics import calculate_statistics

def main():
    # File path to the dataset
    file_path = "data/Mall_Customers.csv"
    chunk_size = 100  # Number of rows per chunk

    # Create an instance of the ChunkIterator
    chunk_iterator = ChunkIterator(file_path, chunk_size)

    # Iterate over chunks and calculate statistics
    for idx, chunk in enumerate(chunk_iterator):
        print(f"Processing Chunk {idx + 1}...")
        stats = calculate_statistics(chunk)
        print(f"Statistics for Chunk {idx + 1}:")
        for column, values in stats.items():
            print(f"  {column}: Mean={values['mean']}, Median={values['median']}, Std={values['std']}")
        print("-" * 40)

if __name__ == "__main__":
    main()
