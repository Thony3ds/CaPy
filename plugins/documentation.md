# Plugins documentation

## Warnings:
Plugins are instables so the documentation is not complete so be careful !
For security of the message system plugins will never give you acces to the network system or send / receive messages in it. Plugins will just allow you to customize
youre app with better creativity

## Manifest
The manifest register verified plugins that apear into the plugin page of CaPy.

## Plugin componnents:
Plugins must follow this exemple of tree:

plugin_dir/
- conf.json
- (option) res/
  - (option) resource_file
  - (option formats: py) executable_file

### conf.json
conf.json file is the first file that CaPy will read when you install this plugin. It must follow this syntax:

#### **Needed in the file:**
*version*: a version that match with your app version\
*permissions*: a permission that will define the type of action of your plugin. You can add multiples permissions using |\
Permissions can be:
 -  GlobalStyleSheet: allow you to change the CSS of the main app. For this you **must** provide a .css file in your res dir.
 -  GlobalLangFile: allow you to add a new language in the app. For this you **must** provide a .json file that match with the template in your res dir.
 -  StartVideo: allow you to add a new video file when you start your app. For this you **must** provide a video format file in your res dir.
 -  Others permissions will be added in the future.
#### **Optionnal args**
Optionnals args need to be here but can be none in the file:
 - executable: specify a python file that the app can run. The file must be in res dir. CaPy don't use cmd so you need to create your own UI using PyQt or Tkinter.
 - files: specify a file that the app can use via permissions into your res dir. If you are using multiples permissions at the same time use this syntax:
files: {
  "permission_name": "file",
  "permission_name": "file" // ...
}

## Template:
To help you we provide a template folder with all functionnalities in it and the correct syntax in template_plugin folder.
