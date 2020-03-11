---
title: "01. Adding users"
description: "Adding users using the commandline."
date: 2020-03-06T11:39:26+01:00
draft: false
weight: 20
---

## Adding users

Most likely if you are setting up a VPS with a cloud provider they gave you access to the machine with the root account. Using the root account for daily tasks is against best practices, so first things first, lets create a additional account for daily administrator tasks. If you are installing in VM you most likely already setup a additional account during the installation, if so you can skip to the next page.

In this guide we will be using a account named `beheer`. This is interchangeable between systems. I'd recommend choosing something that you like.

To setup this user follow the instructions below:

* Create new user with `adduser beheer`
* Change user to your new one to check whether it works `su beheer`
* Try doing something you should not be able to do, like `apt-get install ncdu`. You will probably see a Error message. This is because this user account currently does not have rights to run this command. This is because this user has not been added to the sudoers group.
* Go back to root `exit`
* Add the user to sudoers `sudo adduser beheer sudo`
* Try switching to the user and see if you are now able to install something.
