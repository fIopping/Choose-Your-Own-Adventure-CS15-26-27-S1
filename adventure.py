user_choice = None
story = """
Your name is Ruth, your a grade 11 girl who went to get groceries for your family

You are at the store on her bicycle, when she hears police sirens.

A voice comes over the intercom:

"Attention. Come out with your hands up. Slowly!."

The store is silent.

Turns out there was a shooter

A few seconds later, another announcement follows:

"We are coming in, Drop your weapon!"

As scared as you are in the store, you try to get out of the store.
Suddenly! the store door closes

Five minutes later, the police are trying to enter the door but turns out its bulletproof.

Then 3 shots fire, Pow! Pow! Pow!.
That was a warning shot, but you still can not see the shooter

Then suddenly her phone rings, Its your mum.

You quickly answer the phone and reduces the volume as low as she can, and before her mum could even speak, a loading-
sound from a gun, rings next to her ear, its the shooter

He asks you to give him the phone, and now you have 2 options


A : Give him the phone
OR
B : Run away as fast as you can
"""

print(story)

user_choice = input()
user_choice = user_choice.lower()

if user_choice == "a":
    story = """
    He shoots the phone right in front of you and forces you to the back of the store with the other shoppers
    You then meet an old elderly couple named Jim and Bethany, Jim explains to you, that they came there to go get 
    Bethany's seizure medicine, till they was forced to stay back there.
    
    You can relate-
    
    Suddenly, Bethany starts violently shaking, she is seizing.
    
    You try calming her down by keeping her still but to no avail, it didnt work
    
    But something orange and small catches your eye, Its Bethany's seizure medicine, but its by the pharmacy counter
    
    But the shooter has his back turned
    
    Now's your chance
    
    You quickly run to the counter, grab Bethany's medicine and on your way back the shooter spots
    
    
    """
    print(story)

if user_choice == "b":
    story = """
   You run as fast as you can and then you feel a sharp pain in your leg, the shoter has decided to make you an example
   He slowly creeps up on you, Then bang-
   
   THE END (click run to restart)
    """
    print(story)