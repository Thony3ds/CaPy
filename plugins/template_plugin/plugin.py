import tkinter as tk # You can import everything you want but the compiler will keep only the allowed imports

class Plugin:
    def __init__(self, rights: dict, files: dict, cpm_sys):

        #As we add an executable file in the conf we must make the code for the plugin behavior

        self.cpm_sys = cpm_sys

        self.css_perm = rights["GlobalStyleSheet"]
        self.lang_perm = rights["GlobalLangFile"]
        self.video_perm = rights["StartVideo"]
        self.emoji_perm = rights["EmojiMenu"]
        self.load_first_perm = rights["LoadFirst"]

        #Plugin Basic Behavior
        if not self.load_first_perm:
            self.cpm_sys.ask_load_first() # Ask the user the perm Load First
            rights = self.cpm_sys.reload_rights() # Reload the rights to refresh load first perm

        if self.load_first_perm: # We need to load first for the lang file, the start video and emoji
            if self.css_perm:#We check if the permission is allowed
                self.css_perm(files["GlobalStyleSheet"])#And we execute if it's ok
            if self.lang_perm:
                self.lang_perm(files["GlobalLangFile"])
            if self.video_perm:
                self.video_perm(files["StartVideo"])
            if self.emoji_perm:
                self.emoji_perm(files["EmojiMenu"])

        #If we load first is true we can pop up a window of config or else but here I want to make a config page, so I will use _onOpenPlugin to show the config page.

    #Because I use a custom UI to manage this plugin I'm going to set up a "_onOpenPlugin" function that the plugin will automatically call when the user try to open the plugin in the plugin menu
    def _onOpenPlugin(self):
        app = tk.Tk()
        lab = tk.Label(app, text="My Plugin Page")
        lab.pack()
        #Here you can make a config page and call self.cmp_sys.modify_file() for example
        app.mainloop()

# ---- TEMP FOR TESTING / CODING----

def temp_function(css_file:None, lang_file:None, mp4_file:None, emoji_file:None): # This isn't a class so the compiler wouldn't take it.
    print("Temp Function Called !")
    if css_file:
        print("Css File: "+css_file)
    if lang_file:
        print("Lang File: "+lang_file)
    if mp4_file:
        print("Mp4 File: "+mp4_file)
    if emoji_file:
        print("Emoji File: "+emoji_file)
    print("Temp Function End !")

if __name__ == '__main__': # The main will not be in the final and compiled code because this is not a class
    temp_rights = {
        "GlobalStyleSheet": temp_function,
        "GlobalLangFile": temp_function,
        "StartVideo": temp_function,
        "EmojiMenu": None, #Here is an example of a right refuse by the app
        "LoadFirst": True
    }
    temp_files = {
        "GlobalStyleSheet": "background-color: red",
        "GlobalLangFile": {"main_label": "Benvenuto sull'CaPy"},
        "StartVideo": "MP4 FILE !", #Placeholder because I don't have one here
        "EmojiMenu": {"E": ["A", "B", "C"]}, #Not emojis but do the stuff
    }
    plugin = Plugin(temp_rights, temp_files)