# minieng
## Setup
Download the zip from Releases and unzip it, create a folder named `exts` and a folder named `carts`. In the exts folder create a file named boot.ext and put this in it:
```
...
```
## Using
To record type `rec` this will record to `main.cart` in your current directory. To stop recording type `exit`. To play your recording move main.cart to carts/main.cart and type `load main.cart`
To run a line of python type `#py:<python>`. To define a variable type `#def:<content>:<name>`.
## Extensions
To use an extension find the `boot.ext` from it's main folder and replace your current `boot.ext` with that one. This activates that extension. **Other extensions will be inactive to fix this look below.**
### Using multiple extensions
1. Take the old extension copy **only the content** of `run` of whatever `.ext` it has (this may be `boot.ext`) and paste it into the bottom of the `run` of the new one.
2. Take the old extension copy **only the content** of `parse2` of whatever `.ext` it has (this may be `boot.ext`) and paste it into the bottom of the `parse2` of the new one.
