from htpy import Element

# this is useful for situations where htpy import auto-resolve doesn't work
# also the FAQ also says you can't generate XML... but so far at least for the subset of html that hyperview uses, it's fine

hxml = Element("doc", {"xmlns":"https://hyperview.org/hyperview"}, None)
list_ = Element("list", {}, None)
