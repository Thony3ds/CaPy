# Plugins documentation

## Warnings:
Plugins are instables so the documentation is not complete so be careful !
For security of the message system plugins will never give you acces to the network system or send / receive messages in it. Plugins will just allow you to customize
youre app with better creativity

## Manifest
The manifest register verified plugins that apear into the plugin page of CaPy they use official version.
If you want to make your own plugin you need to enable custom plugins into the CaPy settings. By doing this you will change your app into V X.X.X-dev that allow you to use official plugins for you X.X.X version or your own plugins with X.X.X-dev version

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

## CaPy Compilator:
For your plugin to work you must compile it with the official CaPy Compiler with the right version (in the CaPyCompilator Folder).
The app will automaticly compile your plugin to a .cpm (CaPy Plugin Module).
### Compilator Restriction & allows:
The compilator will only allow following libraries to be use:
- PyQt5 
- json
- Others will be added in the future

The compilator will allow you to access to different datas of the main app:
- App Theme
- Others will be added in the future

## CaPy Execution File Syntax:
Executions Files are optionnal but help to make configuration apps or other improvements.
If you use executable into your conf.json you will have to configure the applications of the plugin. If you don't the app will automaticly turn them on.
the executed file must be a class with the following imports in the __ init __.py:\
def __ init __(self, rights:dict, files_path:dict)

rights will contains your permissions 
files_paht will contains your files that your registered into your conf.json
