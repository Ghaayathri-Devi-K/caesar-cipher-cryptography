# Caesar Cipher Cryptography

Here is a implementation of Caesar Cipher technique, which is one of the earliest and simplest methods of encryption technique. 
It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter with a fixed number of positions down the alphabet.

For example with a shift of 1, A would be replaced by B, B would become C, and so on. The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials. 

## How does it work ?

![image](https://user-images.githubusercontent.com/99457944/185754840-814de835-c510-48e3-bb37-528645969fa3.png)

## Input: 
<ol>
<li>A String of lower case letters, called Text.</li>
<li>An Integer between 0-25 denoting the required shift.</li>
</ol>

## Procedure: 
<ol>
<li>Traverse the given text one character at a time . </li>
<li>For each character, transform the given character as per the rule, depending on whether we’re encrypting or decrypting the text.</li>
<li>Return the new string generated.</li>
</ol>
