# Auto-PoGo
A simple, brute force attempt at automating Pokemon Go, makes roughly 20,000 stardust/hr
## How to Use:
*Currently only tested on an android device, iphone support is probably not available until better interfacing options exist*
 - Use [scrcpy](https://github.com/Genymobile/scrcpy)  to interface with your phone (you might need to enable USB debugging)
 - (Optional) start a location spoofer
 - Go to the overworld and zoom out all the way
 - Run main.py and leave
## Known issues:
 - There is currently only one throw programmed in, and if it meets a pokemon that is known to not be caught with that throw, it will flee. If it meets a poke that is *not* on the blacklist, it will throw 5 pokeballs at it until it times out
 - I'm 90% sure star-checking is broken, all pokemon caught will be assessed as < 3* and transferred. Need to have a non-colour based approach I think
 - Sometimes it thinks it's at a rocketstop when it's not (especially at night) and will get itself into the menu or pokedex at times. So far it has managed to fix itself and not cause any damage but YMMV
### Bottom Line:
Quantity > Quality

**I AM NOT RESPONSIBLE FOR DAMAGE TO YOUR POKEMON GO ACCOUNT**
**YOU ALMOST DEFINITELY WON'T GET BANNED BUT THAT IS ALWAYS A RISK WHEN USING BOTS**

