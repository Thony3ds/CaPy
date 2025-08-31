# CaPy Plugins Documentation

## ⚠️ Warnings
Plugins are still experimental, and this documentation is not yet complete. Use them with caution!

For security reasons, plugins will **never** have access to the network system or be able to send/receive messages. Plugins are designed to enhance your app creatively — not to interfere with its core communication system.\

The total size of all files included in the resources and plugin code (if provided) must remain within a maximum of 4GB, subject to available system RAM.

---

## 📦 Manifest
The manifest registers verified plugins that appear in the plugin page of CaPy. These use official versions.

If you want to create your own plugin, you must enable **custom plugins** in the CaPy settings. Doing so will switch your app to a `X.X.X-dev` version, allowing you to use either:
- Official plugins for your current `X.X.X` version
- Your own custom plugins for the `X.X.X-dev` version

The dev version is only for people who know what they are doing

---

## 🧩 Plugin Structure

Plugins must follow this directory structure:

plugin_dir/\
  ├── conf.json\
  └── res/ (optional)\
    └── resource_file (optional)\
  └── executable_file (.py, optional)


---

### 📄 `conf.json`

This is the first file CaPy reads when compiling a plugin. It must follow this syntax:

#### Required fields:
- `name`: defines a name for your plugin
- `version`: must match your app version
- `permissions`: defines what your plugin is allowed to do. You can combine multiple permissions using `|`

Available permissions:
- `GlobalStyleSheet`: allows you to change the app's CSS. Requires a `.css` file in the `res/` directory.
- `GlobalLangFile`: allows you to add a new language. Requires a `.json` file matching the language template in `res/`.
- `StartVideo`: allows you to add a video that plays when the app starts. Requires a video file in `res/`.
- `EmojiMenu`: allows you to add a menu in the emoji picker. Requires a `json` file (in `res/`) using this syntax: "main_emoji": ["emoji1", "emoji2", ...]
- `LoadFirst`: allow you to make your plugin load before the main app using it you will be able to load things before they are used. This permission must be allowed by the app and the user (with a popup).
- `HideOption`: allow you to open a window when you hide the app. By using this you need to provide the path of a exe file which will be launched after hiding or the name of the window (if open) depending on which mode you call ("open" or "show").
- More permissions will be added in future updates.

A permission can be refused to you if:
- The version is outdated and no longer works with the app.
- The user refused to give you the right (LoadFirst).

This allows you to run a 1.0.0 plugin for the 1.2.0 version if no major changes occurred in between.

#### Optional fields:
You must use one of the following fields for your plugin to work:
- `executable`: specifies a Python file the app can run. Must be located in the `res/` directory. CaPy does not use `cmd`, so you must create your own UI using PyQt or Tkinter.
- `files`: maps permissions to their corresponding files in `res/`. If using multiple permissions, use this syntax:

```json
{
  "files": {
  "GlobalStyleSheet": "style.css",
  "GlobalLangFile": "lang_fr.json"
  }
}
```
### 🧪 Template

To help you get started, we provide a template_plugin folder with all functionalities and correct syntax included.

### 🛠️ CaPy Compiler

To make your plugin work, you must compile it using the official CaPy Compiler (located in the CaPyCompilator folder). The compiler will automatically generate a .cpm (CaPy Plugin Module) file.
Use the CaPy Compiler version that match with the CaPy version. If you don't find one use the first one you find before.

#### Compiler Restrictions & Allowed Libraries:

The compiler only allows the following libraries:

- PyQt5
- Tkinter
- More will be added in future versions

The compiler also gives access to certain app data:

- App theme

- More will be added soon

### ⚙️ CaPy Executable File Syntax

Executable files are optional but useful for creating configuration UIs or advanced features.

If you specify an executable in your conf.json, you must configure the plugin's behavior. If not, the app will automatically enable it with default settings.

The executable file must define a class with the following constructor:

````python
class Plugin:
    def __init__(self, rights: dict, files: dict, cpm_sys):
````

- `rights`: contains the permissions granted to the plugin, you can call functions for it that allows you to apply things in the app.
- `files`: contains the files registered in conf.json encoded in utf-8.
- `cpm_sys`: It's a class with some utils that can help you to improve your app such as `modify_file` function.

You can use some things out of the class but the compiler will only process the classes it finds. If you're not making a `Plugin` class (with the same name), the plugin will be rejected by the main application, although it will still compile\
By the way, if you name a class `CaPyPluginModule` the app will raise a `PluginInternalException`.\
Here is an example of the given args with the following config:
```json
{
  "name": "PluginName",
  "version": "1.0.0",
  "permissions": "GlobalStyleSheet|GlobalLangFile|LoadFirst",
  "files": {
    "GlobalStyleSheet": "red_theme.css",
    "GlobalLangFile": "it-IT.json"
  },
  "executable": "plugin.py"
}
```
The args will be:
```python
rights = {
    "GlobalStyleSheet": global_style_sheet_function, 
    # The functions will be given to you. You don't have to code them
    "GlobalLangFile": global_lang_file_function, # Later we will see the applications of them.
    "LoadFirst": True # This one is different, it provides you a bool var according to the app and user allows.
    
}
files_path = {
    "GlobalStyleSheet": "background-color: red;", # Here is the content of your file
    "GlobalLangFile": {"main_label": "Benvenuto sull'CaPy"} # Same here
}
```

#### Apply Functions
Here’s how to use the functions in the `rights` variable.

##### GlobalStyleSheet:
This function require one argument that is `css_style_sheet_file`. It will apply it to the main app (not the installation page).\
##### GlobalLangFile:
Here you will need a dictionary of worlds (see template for the complete file). If you don't have all the args into it the app will automatically reject the file and take the en-US one.\
##### StartVideo:
By providing a mp4 file you will be able to change the start video of the app.\
⚠️ Warning: The heavy files can take a long time to load and take more RAM usage on your computer. And the app loads in the background during this so a short video can result an empty app for a time.\
##### EmojiMenu:
Require a dictionary like the following one, the app will add an emoji menu in the emoji picker.\
Here is the syntax you must use:
```python
custom_emoji_menu = {
    "An_Emoji": ["Some_Emojis", "Some_Emojis"] #Replace the placeholders with some real emojis !
}
```
##### HideOption
Here the contructor of the function:
````python
def hideoption(arg, mode):
````
-mode: can be `open` or `show`.
-arg: if mode is `open` you need to provide the absolute path of an exe file and the app will run it. If mode is `show` you need to provide the **name of a window in the Windows title bar** and the app will bring it to the foreground.
#### CPM_SYS Class
Here is a list of the `cpm_sys` class functions:
- save_data(data)-> bool: By sending the data (files) this function will save them into the plugin file
- ask_load_first(): This will send a question to the user to allow you or not to load first (This will grant you the necessary permission).
- reload_rights()-> dict: This will reload your rights into a variable that you choose. 
- Others will be added in the future !
#### Main App's Integrity
For the main app to run correctly, the plugins will be disabled at any exceptions that the app can found. An error page will pop up if an error occurred.\
Here are the exceptions that have been created for plugins and the possible issues:
- `FileIncompleteError`: The file is not complete and don't have all the translations or else in it.
- `IncorrectFileFormatError`: The file is not a good format (example: you give a mp4 to the lang function that require a dictionary)
- `NotEmojiException`: the string provided is not a single character long.
- `IncompatiblePluginError`: The plugin you try to load is not compatible with the app.
- `RightsBreakException`: When you try to call a rights function without the permission or to call Metadata class with your own class.
- `PluginInternalException`: When your plugin code have a problem in it.

#### Plugin calls context
Your plugin can be called in two different ways:
- `LoadFirst`: This will init your plugin before every secondary inits
- `_onOpenPlugin`: When you install a plugin, the installation button becomes an open button that will initialize and launch the plugin when you click on it. This will also call the `_onOpenPlugin` function of your `Plugin` class if you have this function in it.

## Problems or Issues ?
Contact me in the GitHub if you see problems or issues with the plugin system in general.
I will try my best to patch it A.S.A.P.

# Credits
Made only by `Thony3ds`
