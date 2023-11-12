# BillyChan-EE4213Ex3
There are two advanced examples you can use here. The first one is using the NLTK library, and another is using text2emotion.

# NLTK
First of all, you need to install the NLTK library on your computer. You can use cmd and type:

```
pip install nltk
```

Then, you can see that nltk is installed on your computer.

For checking, you can use:

```
pip show nltk
```

Then, you can use the "AdvancedExampleOne" code and use it. 

The output of the code is supposed to be something like:

```
Emotion: Positive
Emotion Score: 95.26
```

# Text2emotion
For this library, you may need to make some adjustments after installation.
First, you need to install the install the library in cmd:

```
pip install text2emotion
```

Then, some of the people may have errors even if they installed the library.

```
module ‘emoji’ has no attribute UNICODE_EMOJI’
```

If there is the same situation with your computer, you may need to change UNICODE_EMOJI to EMOJI_DATA.

If you still have the error, it is the issue that comes from the 'emoji' version. Therefore, you need to downgrade the emoji version in cmd using:

```
pip install emoji==1.6.3
```

Finally, the program can be executed successfully!
