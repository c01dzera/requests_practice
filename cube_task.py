from xml.etree import ElementTree

root = ElementTree.fromstringlist(input())

colors = {'red': 0, 'green': 0, 'blue': 0}


def rgb(root, colors, lvl=0):
    lvl += 1
    colors[root.attrib['color']] += lvl
    for child in root:

        rgb(child, colors, lvl)
    return colors


print(*rgb(root, colors).values())