

def max_pairwise_product(xs):
    if len(xs) < 2:
        return -1
    else:
        def maxtwo(xs):
            a, b = -1, -1

            for x in xs:
                if x > a:
                    a, b = x, a
                elif x > b:
                    b = x
            return a * b

        return max(maxtwo(xs), maxtwo(map(lambda x: -x, xs)))
# print(max_pairwise_product([-5, -1, 2, 3]))


