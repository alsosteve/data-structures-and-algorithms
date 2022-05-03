from data_structures.queue import Queue

class AnimalShelter():
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal):
        if isinstance(animal, Cat):
            self.cats.enqueue(animal)
        if isinstance(animal, Dog):
            self.dogs.enqueue(animal)

    def dequeue(self, pref):
        if pref == "cat":
            return self.cats.dequeue()
        if pref == "dog":
            return self.dogs.dequeue()
        else:
            return None


class Dog: pass


class Cat: pass
