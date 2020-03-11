---
title: "03. File editor: vim"
description: "Editing files using the commandline."
date: 2020-03-06T11:41:08+01:00
draft: false
weight: 40
---

## File editor: vim

Vim is a command-line text editor. Vim is entirely controlled with keyboard input, so it requires some time to get used to, but doing so will give you some hair on your chest.

![vim learning curve](/img/guides/ubuntu-vps/03-vim-learning-curve.png)

Vim knows two important modes, the command-mode and the input-mode. The first one is used to enter commands. The second one is used to edit the opened file. To get you started some basic vim actions have been described below.

Opening a file using vim: `vim fileyouwanttoedit.cfg`

### Switching modes

1. You can enter input-mode by pressing the `i` key on your keyboard.
2. You can go to the command-mode by pressing the `ESC` key on your keyboard.

### Exiting Vim without saving

1. Pressing the `ESC` key
2. Entering `:q!`
3. Pressing the `ENTER` key

### Exiting Vim with saving

1. Pressing the `ESC` key
2. Entering `:wq!` or `:x!`
3. Pressing the `ENTER` key

### Saving file in vim

1. Pressing the `ESC` key
2. Entering `:w!`
3. Pressing the `ENTER` key
