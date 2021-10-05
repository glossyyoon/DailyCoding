def fibbo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibbo(n - 1) + fibbo(n - 2)


print(fibbo(5))
