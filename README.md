#betterzen#

A revised version of the **Zen of Python**.

Lets you print out the whole Zen or just single aphorisms from it, chosen randomly or filtered according a list of keywords.


###Usage###

```python
# As you import the module, the Zen will be printed out
>>> import betterzen

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
[...]

# Print out the Zen again
>>> betterzen.zen()
[...]

# Print out the Zen numbering each aphorism
>>> betterzen.numbered_zen()

The Zen of Python, by Tim Peters

1. Beautiful is better than ugly.
2. Explicit is better than implicit.
[...]

# Print out the numbered aphorism that you want
>>> betterzen.aphorism(1)
Beautiful is better than ugly.

# Print out a random aphorism
>>> betterzen.random()
Now is better than never.

# Print out the aphorisms containing at least one of the listed keywords
>>> betterzen.apropos(['should','honking'])
Namespaces are one honking great idea -- let's do more of those!
Errors should never pass silently.
There should be one-- and preferably only one --obvious way to do it.

```

###Install###
Put the module into your Python standard library's folder.

You can also overwrite it to the original Zen of Python's module (file `this.py`) if you like.

###May the Zen be with you!###
