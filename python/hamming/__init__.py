# Define your compute function here.
# run python -m unittest test.hamming_test to ensure the
# unit tests pass and your code meets all of the conditions.


def compute(first_strand, second_strand):
    """ Method to calculate the Hamming difference between two DNA strands. It is found by comparing two DNA strands
        and counting how many of the nucleotides are different from their equivalent in the other string.
        Both strands must be of the same length, otherwise, a ValueError exception will be raised.

        :type first_strand: basestring
        :type second_strand: basestring

        :returns int: how many of the nucleotides are different from their equivalent in the other string.
    """

    # make sure the two strands are of type 'basestring'
    if not isinstance(first_strand, basestring) or not isinstance(second_strand, basestring):
        raise ValueError("Both strands must be of type basestring. Got {} and {} instead.".format(type(first_strand),
                                                                                                  type(second_strand)))
    # make sure the two strands are of same length
    if len(first_strand) != len(second_strand):
        raise ValueError("The two strands must be of the same length to compute the hamming distance")

    number_of_different_nucleotides = 0

    for index, nucleotide in enumerate(first_strand):
        if first_strand[index] != second_strand[index]:
            number_of_different_nucleotides += 1

    return number_of_different_nucleotides

