def calculate_statistics(chunk):
    """
    Calculates basic statistics (mean, median, std) for each numeric column in the chunk.
    
    Args:
    - chunk (DataFrame): A chunk of data as a pandas DataFrame.
    
    Returns:
    - dict: A dictionary with column names as keys and statistics as values.
    """
    stats = {}
    for column in chunk.select_dtypes(include='number').columns:
        stats[column] = {
            'mean': chunk[column].mean(),
            'median': chunk[column].median(),
            'std': chunk[column].std()
        }
    return stats
