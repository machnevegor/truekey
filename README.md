# Why is this necessary?
Often, people don't like to change passwords periodically just because they need to be remembered. Of course, the solution to this problem can be the simplest notepad, but we are not looking for easy ways, right? 
Many services are able to return your password to the mail if you forgot it, but it's really inconvenient and also not safe. I rethought this problem and found a solution - **TrueKey**!

# How does it work?
Initially, we need to talk about how to create a password. To do this, you will need to come up with a seed, and then enter it, and then enter the name of the service for which the password will be intended - and that's it, the hashed password is in your pocket. The idea is that in the future, to recover the password you just created, you will only need to remember the seed from it. Of course, again something needs to be recorded, but seed is not a million passwords. This way, **you can quickly create and recover hashed passwords from completely different computers and get the same result**!

# Usage Example
```
So, first, enter seed to generate the encrypted key:
>>> someseed
Now enter the keyhole for which the key will be intended:
>>> someservicename
Great, here's your new encrypted key:
>>> 206108DeC86bD2D81023874C
```

# Required to mention
- The hashed password meets all security standards
- A hashed password contains numbers, small and capital letters
- The hashed password is always 24 characters long
