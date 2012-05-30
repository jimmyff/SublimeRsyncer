# Sublime Rsyncer
By Jimmy Forrester Fellowes

A Sublime Text 2 plugin which allows you to rsync specific folders on save. Please note this requires you to have setup an SSH key with a blank password to allow this to rsync without requiring a password. Please see section of this document titled SSH Keys

## Installation via the Package Control plugin

The easiest way to install SublimeRsyncer is through Package Control, which can be found at this site: http://wbond.net/sublime_packages/package_control

Once you install Package Control, restart ST2 and bring up the Command Palette (`Command+Shift+P` on OS X, `Control+Shift+P` on Linux/Windows). Select "Package Control: Install Package", wait while Package Control fetches the latest package list, then select SublimeRsyncer when the list appears. The advantage of using this method is that Package Control will automatically keep SublimeRsyncer up to date with the latest version.

## Installation from Source/Git Repo

Download (or clone) the latest source from [GitHub](http://github.com/jimmysparkle/SublimeRsyncer) into your Sublime Text "Packages" directory.

The "Packages" directory is located at:

* OS X:
	~/Library/Application Support/Sublime Text 2/Packages/

* Linux:
	~/.config/sublime-text-2/Packages/

* Windows:
	%APPDATA%/Sublime Text 2/Packages/


## Usage

Edit your user settings Preferences -> Package Settings -> SublimtRsyncer -> Settings - User

An example config could look like so:

```
{
  "folders": [
  	{
  		"localPath"	  : "/Users/jimmy/code/project1/",
  		"remote"		  : "jimmy@my-vm:/var/www/project1/",
      "exclude"     : ["git", "svn"],
      "deleteAfter" : true
  	},
  	{
  		"localPath"		: "/Users/jimmy/code/project2/",
  		"remote"		: "jimmy@192.168.0.55:/var/www/project2/",
      "exclude"     : ["git", "svn"],
      "deleteAfter" : true
  	}
  ]
}
```

When you next save a file using Sublime Text 2 it will itterate through the folders you've specified and if it matches the file saved it will attempt to rsync. The output can be monitored in the Sublime Text 2 console.

## SSH Keys

You need to generate an SSH key on the machine that you're using Sublime Text 2 on, you should create this with a blank password. You then need to add the public key to your remote machines .ssh/authorized_keys file. You need to make sure that the authorized_keys file has the correct permissions set.

chmod 400 .ssh/authorized_keys