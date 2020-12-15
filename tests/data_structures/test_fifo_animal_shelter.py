from data_structures_and_algorithms.data_structures.fifo_animal_shelter.fifo_animal_shelter import Dog,Cat,AnimalShelter

def test_all():
    alex = Dog('alex')
    aln = Dog('Aln')
    sam = Dog('Sam')
    cray = Dog('Cray')
    soso = Cat('Soso')
    sno = Cat('Son')
    animals = AnimalShelter()
    animals.enqueue(alex)
    animals.enqueue(aln)
    animals.enqueue(sam)
    animals.enqueue(cray)
    animals.enqueue(soso)
    animals.enqueue(sno)
    assert animals.dequeue('cat') == 'Soso'
    assert animals.dequeue('cat') == 'Son'
    assert animals.dequeue('cat') == 'cat queue is empty, here is a dog : alex' #Stretch Goal
    assert animals.dequeue('dog') == 'Aln'
    assert animals.dequeue('dog') == 'Sam'
    assert animals.dequeue('dog') == 'Cray'
    assert animals.dequeue('dog') == "the cat's queue and the dog's queue are both empty"#Stretch Goal