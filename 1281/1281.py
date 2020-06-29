n = 4421

class Sulotion:
    def subtractProductAndSum(self, n: int) -> int:
        n_str = str(n)
        n = m = int(n_str[0])
        for i in range(1, len(n_str)):
            n = n * int(n_str[i])
            m = m + int(n_str[i])
        
        return n - m

sulotion = Sulotion()
print(sulotion.subtractProductAndSum(n))
