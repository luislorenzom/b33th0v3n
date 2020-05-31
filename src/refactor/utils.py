def permute_chunks(chunks: list) -> list:
    """
    Permute all words inside a list to create all possible combinations

    :param chunks: list with words to permute

    :return: all permuted results
    :raise Exception: when chunks is an empty list
    """
    if len(chunks) == 0:
        raise Exception('chunks must not be empty')
    if len(chunks) == 1:
        return chunks
    else:
        l = [chunks.pop(0)]
        for c in chunks:
            l.append(l[-1] + ' ' + c)
    return l + permute_chunks(chunks)
