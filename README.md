# PyPass - Random Password Generator

PyPass is a dead-simple password generator. You can specify the length of the
password, and the number of passwords you want the script to generate. 

It uses lowercase and uppercase letters, numbers, and punctuation. No character
is repeated in a single password. 

### Usage

Generate an 8-character-long password:

    $ python pypass.py

Generate a 20-character-long password:

    $ python pypass.py 20

Generate a hundred 12-character-long passwords:

    $ python pypass.py 12 100

Really simple. Of course, you can import the module into you application and
use it programmatically:

    from pypass import PyPass
    pypass = Pypass()
    pypass.run()

This script was intended as a learning exercise. 
