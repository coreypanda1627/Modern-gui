import tkxui

root = tkxui.Tk(display=tkxui.FRAMELESS, defaultBorder=True)
root.config(bg="#2A2A2A")
root.geometry("500x500")
root.title("Modern GUI")
json_loader = tkxui.JSONLoader(root)
json_loader.generate("ui.json")
json_loader.generate("theme.json")




root.mainloop()