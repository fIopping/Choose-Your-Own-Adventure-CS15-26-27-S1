user_choice = None
RED = "\033[31m"
RESET = "\033[0m"
story = """
Your name is Ruth, your a grade 11 girl who went to get groceries for your family

You are at the Walmart, when she hears police sirens.

A voice comes over the intercom:

"Attention. Come out with your hands up. Slowly!."

The store is silent.

Turns out there was a shooter

A few seconds later, another announcement follows:

As scared as you are in the store, you try to get out of the store.
Suddenly! the store door closes

"We are coming in, Drop your weapon!"

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

    """