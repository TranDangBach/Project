import tkinter.font as tkfont   # Import the tkinter font module


def configure():
    # family = "Segoe UI"
    family = "Helvetica"    # Specify the font family to use, in this case "Helvetica"
    # Get the default font and configuring its size and family
    default_font = tkfont.nametofont("TkDefaultFont")
    default_font.configure(size=15, family=family)
    # Get the text font and configuring its size and family
    text_font = tkfont.nametofont("TkTextFont")
    text_font.configure(size=12, family=family)
    # Get the fixed font and configuring its size and family
    fixed_font = tkfont.nametofont("TkFixedFont")
    fixed_font.configure(size=12, family=family)
