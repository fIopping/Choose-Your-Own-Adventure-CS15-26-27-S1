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
    
    You quickly run to the counter, grab Bethany's medicine and on your way back you trip, the shooter notices you, and
    approaches you slowly, gun's drawn
    
    You have 2 options
    
    C.  You try to tell him the situation with Bethany
    
    D.  You tell him you felt like throwing up and couldn't find a bin
    
    
    """
    print(story)

user_choice = input()
user_choice = user_choice.lower()

if user_choice == "c":
    story = f"""
He feels pity for her , takes the medicine from you, and goes to Jim, gives him the medication.

He forces you to stay back there, and warns you not to pull that crap again

Finally, Bethany is feeling weak, but fortunately she is stable

You feel okay, and after a few minutes later, you found a opening on a door right next to the pharmacy

You tell Jim about it and you guys agree to escape through there

Unbeknownst to you, someone heard about your escape plan...

You, Jim carrying Bethany sneak your way through the pharmacy, but the person who heard your escape plan told the other
bystanders

Suddenly everyone running towards the door, which obviously alerts the shooter, and since Jim's carrying Bethany
hes at the back of  the crowd

You luckily make it out, but then you turn around, you see a glimpse of Jim smiling, but with all the running, you get
pushed

You hear gunshots, quickly turn around, you see an arm on the ground next to a pool of {RED}blood{RESET}

You cant make it out who it is, but deep in your heart you know

Police bursts in!

Bang Bang Bang

The Shooter is down! The Shooter is {RED}DOWN{RESET}

THE END (click run to restart)

    """
    print(story)

    user_choice = input()
    user_choice = user_choice.lower()

if user_choice == "d":
    story = f"""
 {RED}You are the SHOOTER - PAST{RESET}

FLASHBACK: you were just released from jail after serving 4 years for selling drugs

Hoping to make amends with your girl-friend, you step into her house porch, about to 
knock on the door but somethings different

A sign on her door says happily married, you got so filled with emotion, you dumped the flowers you were about to give
her in front of her door

Few days later, your stalking the "husband" and notice a every Friday he goes to Walmart to get groceries

3 Fridays later, you finally realise his pattern.

This Friday, you came prepared

Got in the Walmart, Shoot the husband, a get in-get out job

Nonetheless, the plan failed

You saw the husband and shot him from a far away distance, Unluckily, you hit a tomato paste can.

With that shot everyone ran, you lost the husband for a bit but its okay

Cause you know he is in the store

But with many people running around, you cant focus

So you lock the doors

And this leads you to here...

{RED}PRESENT{RESET}

You see the girl (Ruby) walking past, gun drawn, you ask her what shes doing out here

She tells you she felt like throwing up and went to the bin

You dont trust her but you have bigger issues

You take her back to the wall

Then go to the place she claims to have felt like throwing up, nothing seems to be suspicious

Your about to leave that spot until, you feel a breeze.

A door's opened

You need to lock that door, but your afraid its a trap by the police.

So you grab a Walmart employee, and demnand her to lock the door

Before she does, you threaten her life, with a gun drawn to her back, so she doesnt try to run away.

She successfully locks the door

You take her to the wall

But, Suddenly you hear a police megaphone, they have come to make a deal

You have 2 options

E. Accept the deal

F. Decline the deal
    """
print(story)

user_choice = input()
user_choice = user_choice.lower()


if user_choice == "e":
    story = """
The deal was release 10 hostages for food and water

You realise this deal is smart, because it lures out the husband. 

Luckily enough, the megaphone can be heard in all parts of the store

You then yell out = "It's better to come out from your hiding spots now so you have a chance to escape

Then people start coming out including the husband, you are not gonna get him yet as you have something big planned


    """

if user_choice == "b":
    story = f"""
   You run as fast as you can and then you feel a sharp pain in your leg, the shooter has decided to make you an example
   He slowly creeps up on you, Then {RED}BANG-{RESET}
   
   THE END (click run to restart)
    """
    print(story)
