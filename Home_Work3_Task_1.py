zen = """
Beautiful is better than ugly.
Explicit is better than implicit.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
bet_c = zen.count('better')
nev_c = zen.count('never')
is_c = zen.count('is')
zen_up = zen.upper()
zen_r = zen.replace('i', '&')

print(
    "Zen of Python includes "
    + f"{bet_c} 'better', "
    + f"{nev_c} 'never' and "
    + f"{is_c} 'is'."
    )
print(zen_up)
print(f"If we replace 'i' with '&' we will get this: \n{zen_r}")