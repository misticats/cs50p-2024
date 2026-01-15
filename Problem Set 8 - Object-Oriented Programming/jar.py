class Jar:
    def __init__(self, capacity=12):
        try:
            capacity = int(capacity)
        except ValueError:
            raise ValueError("Capacity is not an int")
        
        if capacity <= 0:
            raise ValueError("Capacity is negative")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        self._size += n
        if self._size > self._capacity:
            raise ValueError("Size exceeds capacity ")

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Cannot remove more cookies than it has")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = get_capacity()
    get_deposit(jar)
    get_withdraw(jar)
    print(jar)


def get_capacity():
    try:
        capacity = int(input("Capacity: "))
    except ValueError:
        raise ValueError("Given capacity is not an int")
    return Jar(capacity)


def get_deposit(jar):
    try:
        n = int(input("Deposit: "))
        jar.deposit(n)
    except ValueError:
        raise ValueError("Input is not an int")


def get_withdraw(jar):
    try:
        n = int(input("Withdraw: "))
        jar.withdraw(n)
    except ValueError:
        raise ValueError("Input is not an int")


if __name__ == "__main__":
    main()
