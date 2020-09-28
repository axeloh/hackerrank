"""
Google mock interview question from: https://www.youtube.com/watch?v=XKu_SEDAykw

"""


def existPair(a, k, sorted=False):
    """
    :param a: array of integers
    :param k: an integer
    :return: whether there exists two integers in a that sum up to k
    """

    # ---- O(n^2) solution ---- #
    # for i in range(len(a)-1):
    #     for j in range(i+1, len(a)):
    #         if a[i] + a[j] == k:
    #             return True
    # return False

    # ---- O(n) solution ---- #
    # Requires array to be sorted
    # [1, 1, 2, 3, 4, 7, 8, 9], k = 5
    # a2 = [5, 1, 4, 9], k = 10
    if sorted:
        i, j = 0, len(a)-1
        while i < j:
            sum = a[i] + a[j]
            if k < sum:
                j -= 1
            elif k > sum:
                i += 1
            else:
                return True
        return False

    # ---- O(n) solution ---- #
    # Array does not need to be sorted
    else:
        ints = set([])
        for el in a:
            if (k - el) in ints:
                return True
            ints.add(el)
        return False


if __name__ == '__main__':
    a1 = [1, 2, 3, 5]
    k1 = 9
    print(existPair(a1, k1, sorted=True))

    a2 = [1, 1, 2, 3, 4, 5, 7, 9, 9]
    k2 = 10
    print(existPair(a2, k2, sorted=True))

    a3 = [100, 2, 2, 3, 19, 9, 5, 55, 40]
    k3 = 4
    print(existPair(a3, k3, sorted=False))






