# Koden er kjørbar og har den funksjonalitet som er etterspurt

class Mystic_number_iterator:
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        self.n += 1
        mystic_number = self.n * (3 * self.n - 1) // 2
        return mystic_number
    
if __name__ == "__main__":
    mystic_numbers = Mystic_number_iterator()
    for i, mystic_number in enumerate(mystic_numbers):
        if mystic_number > 1000:
            break
        print(mystic_number, end="\n" if i % 5 == 4 else " ")
