## New_Ceasar Pico CTF Writeup

April 12th 2024
By: Ryan Fraser
From: The PicoCTF website

---

### The Problem: 

We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil
> (The file can be found in this folder under new_caesar.py)

---

### My Approach

#### First Look:

Upon first looking at this problem, I noticed that the **flag**, which was redacted! I saw that the flag underwent two encryption functions to transform it to the encoded version. We will take a look at both of these functions

##### b16_encode() :

This function takes in a string of text, then looping though the letters, transforms each from ASCII to binary. Once the 8 bit binary form is obtained. it is then split into two 4 bit nubmers. Each of those new numbers which range form 0-15, corrosopond to their respective letter of the first 16 letters in the english alphabet. These letters are then appended onto an rsf string and returned.

##### shift():

This function is just a standard shift of the letters, the same way that a ceasar cipher would work, the shift is determined by whatever the secret key is.

##### Other Things to Note:

Some other things to note are the two assert statments. These statments assure us that the key is only one character long, and that the key is one of the characters from the ALPHABET varaiable, which is the first 16 charaters of the english alphabet.

#### Reverting the Functions

In order to decrpyt the flag, I chose to design two new functions that reverse the original two.

##### shift_back():

To reversing the shift function was fairly straitforward. The orginal function added the shift of the key onto the letter, so my function subtracted this value, essentially changing the + to a - in ALPHABET[(t1 - t2) % len(ALPHABET)]

##### revert():

To reverse the b16_encode() function, I fist looped though the letters of our encoded text two at a time. For each of the two letters, I found their index in the ALPHABET variable. Since the fist letters index represented the first 4 bits of an 8 bit binarry character, I multiplied the value by 16, which corrospondes to a shift left of 4 bits. I then added the two indexes togther. Finally, I used the chr() function to transform the added numbers back into thier text form.

---

### Finishing It Off

The last step of this challenge was to run the revering functions on the encoded flag with all 16 possiblilites for the key. I automated this task thogugh my main() function. Initially the output looked like garbage to me, untill I saw et_tu? _____, where the blanks are the rest of the flag. I have interntially put in the blacks so that someone else can try my method themselves!



