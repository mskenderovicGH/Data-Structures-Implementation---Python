# implementation of Hashtable
class Hashtable:

    def __init__(self):

        self.capacity = 10
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def insert(self, key, data):
        index = self.hash_function(key)

        # if the hash is taken and key is good, data will be updated
        # if the key is wrong, hash will be updated to the next spot
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = data
                return
            index = (index + 1)

        self.keys[index] = key
        self.values[index] = data

    def get(self, key):

        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (index + 1) % self.capacity
        return None

    def hash_function(self, key):

        hash_sum = 0

        for letter in key:
            hash_sum = hash_sum + ord(letter)

        return hash_sum % self.capacity

if __name__ == '__main__':

    table = Hashtable()
    table.insert('ADAM', 23)
    table.insert('AAAP', 45)
    table.insert('DANIEL', 34)


    print(table.get('AAAP'))
    print(table.keys)
