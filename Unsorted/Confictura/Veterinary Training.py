#Name: Veterinary Training
# Author: Ultimascripts
#Notes: Tame or buy a horse, set it's serial to animal1
#       Find a horse outside Brit, set it's serial to animal2
#       Have your horse attack the wild horse.
#       Toggle war/peace and hit play.
#       You will Vet both, this can make you grey.
animal1 = 0xb7bd2
animal2 = 0x1888
delay_in_ms = 3500
while not Dead("self"):
    Pause(100)
    if Distance(animal1) > 1 < Distance(animal2):
        Stop()
    if not FindObject(animal1) or not FindObject(animal2):
        Stop()
    if DiffHitsPercent(animal1) > 5:
        Msg("[bandother")
        WaitForTarget(5000)
        Target(animal1)
        Pause(delay_in_ms)
    if DiffHitsPercent(animal2) > 5:
        Msg("[bandother")
        WaitForTarget(5000)
        Target(animal2)
        Pause(delay_in_ms)