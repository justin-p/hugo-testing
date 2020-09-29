---
### The title for the content.
title : "century"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "century"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "century description."
### The datetime assigned to this page.
date : 2020-09-29T14:47:17+02:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "century"
### Aliases can be used to create redirects to your page from other URLs.
# aliases : [""]
### Display name of this page modifier. If set, it will be displayed in the footer.
# LastModifierDisplayName : ""
### Email of this page modifier. If set with LastModifierDisplayName, it will be displayed in the footer
# LastModifierEmail : ""
### Table of content (toc) is enabled by default. Set this parameter to true to disable it.
# disableToc : true
### Set the page as a chapter, changing the way it's displayed
# chapter : true
### Hide a menu entry by setting this to true
# hidden : true
### If true, the content will not be rendered unless the --buildDrafts flag is passed to the hugo command.
# draft : true
### Used for ordering your content in lists. Lower weight gets higher precedence. So content with lower weight will come first.
### 0 does nothing !
weight : 0
### Used to tag content. By default this is inherited using cascading from _index.md files
### Only set of you want to overwrite these inherited values.
# tags : [""]
### a map of Front Matter keys whose values are passed down to the page’s descendants unless overwritten by self or a closer ancestor’s cascade. 
cascade:
    tags: ['Century']
---

## Century

### Century 00 -> 01

#### Goal

The goal of this level is to log into the game.

#### Solution

sign up and get the creds.

```PowerShell
$ ssh century1@century.underthewire.tech:century1

Under the Wire... PowerShell Training for the People!
PS C:\users\century1\desktop>
```

### Century 01 -> 02

#### Goal

```txt
The password for Century2 is the build version of the instance of PowerShell installed on this system.

NOTE:
- The format is as follows: **.*.*****.****
- Include all periods
- Be sure to look for build version and NOT PowerShell version 
```

#### Solution

```PowerShell
PS C:\users\century1\desktop> $PSVersionTable.BuildVersion.ToString()
10.0.14393.3866
PS C:\users\century1\desktop> exit

$ ssh century2@century.underthewire.tech:10.0.14393.3866
Under the Wire... PowerShell Training for the People!
PS C:\users\century2\desktop>
```

### Century 02 -> 03

#### Goal

```txt
The password for Century3 is the name of the built-in cmdlet that performs the wget like function within PowerShell PLUS the name of the file on the desktop.

NOTE:
- If the name of the cmdlet is "get-web" and the file on the desktop is named "1234", the password would be "get-web1234".
- The password will be lowercase no matter how it appears on the screen. 
```

#### Solution

[Invoke-WebRequest](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-webrequest?view=powershell-6)

```PowerShell
PS C:\users\century2\desktop> ls


    Directory: C:\users\century2\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM            693 443
PS C:\users\century2\desktop> $(ls).Name
443
PS C:\users\century1\desktop> exit
Connection to century.underthewire.tech closed. 

$ ssh century3@century.underthewire.tech:invoke-webrequest443
Under the Wire... PowerShell Training for the People!
PS C:\users\century3\desktop> 
```

### Century 03 -> 04

#### Goal

```txt
The password for Century4 is the number of files on the desktop.
```

#### Solution

```PowerShell
PS C:\users\century3\desktop> $counter=0
PS C:\users\century3\desktop> $items = Get-ChildItem
PS C:\users\century3\desktop> ForEach ($item in $items) {$counter++}
PS C:\users\century3\desktop> $counter
123
PS C:\users\century3\desktop> $(Get-ChildItem).count
123
PS C:\users\century3\desktop> $(gci).count
123
PS C:\users\century3\desktop> $(ls).count
123
PS C:\users\century3\desktop>exit
Connection to century.underthewire.tech closed. 

$ ssh century4@century.underthewire.tech:123
Under the Wire... PowerShell Training for the People!
PS C:\users\century4\desktop>
```

### Century 04 -> 05

#### Goal

```txt
The password for Century5 is the name of the file within a directory on the desktop that has spaces in its name.

NOTE:
- The password will be lowercase no matter how it appears on the screen.
```

#### Solution

```PowerShell
PS C:\users\century4\desktop> $(ls '.\Can You Open Me').Name
61580
PS C:\users\century4\desktop>exit
Connection to century.underthewire.tech closed. 

$ ssh century5@century.underthewire.tech:61580
Under the Wire... PowerShell Training for the People!
PS C:\users\century4\desktop>
```

### Century 05 -> 06

#### Goal

```txt
The password for Century6 is the short name of the domain in which this system resides in PLUS the name of the file on the desktop.

NOTE:
- If the short name of the domain is "blob" and the file on the desktop is named "1234", the password would be "blob1234".
- The password will be lowercase no matter how it appears on the screen.
```

#### Solution

```PowerShell
PS C:\users\century5\desktop> $env:UserDomain
underthewire
PS C:\users\century5\desktop> $env:SSHWINUSERDOMAIN
underthewire
PS C:\users\century5\desktop> $($($env:SSHWINUSERDOMAIN) + $(ls).name)
underthewire3347
PS C:\users\century5\desktop>exit
Connection to century.underthewire.tech closed. 

$ ssh century6@century.underthewire.tech:underthewire3347
Under the Wire... PowerShell Training for the People!
PS C:\users\century6\desktop> 
```

### Century 06 -> 07

#### Goal

```txt
The password for Century7 is the number of folders on the desktop. 
```

#### Solution

```PowerShell
PS C:\users\century6\desktop> $(ls -Directory).count
197
PS C:\users\century6\desktop>exit
Connection to century.underthewire.tech closed. 

$ ssh century6@century.underthewire.tech:197
Under the Wire... PowerShell Training for the People!
PS C:\users\century6\desktop> 
```

### Century 07 -> 08

#### Goal

```txt
The password for Century8 is in a readme file somewhere within the contacts, desktop, documents, downloads, favorites, music, or videos folder in the user's profile.

NOTE:
- The password will be lowercase no matter how it appears on the screen.
```

#### Solution

```PowerShell
PS C:\users\century7\desktop> Get-Content $(Get-ChildItem -Recurse | Where-Object {$_.Name -like "*readme*"}).FullName
7points
PS C:\users\century7\desktop> gc $(ls -R | ? {$_.name -like "*readme*"}).FullName
7points
PS C:\users\century7> exit
Connection to century.underthewire.tech closed.  

$ ssh century7@century.underthewire.tech:7points
Under the Wire... PowerShell Training for the People!
PS C:\users\century8\desktop> 
```

### Century 08 -> 09

#### Goal

```txt
The password for Century9 is the number of unique entries within the file on the desktop. 
```

#### Solution

```PowerShell
PS C:\users\century8\desktop> $(ls).name
unique.txt
PS C:\users\century8\desktop> $(gc .\unique.txt | Sort-Object -Unique).count
696
PS C:\users\century8\desktop> exit
Connection to century.underthewire.tech closed. 

$ ssh century9@century.underthewire.tech:696
Under the Wire... PowerShell Training for the People!
PS C:\users\century9\desktop>
```

### Century 09 -> 10

#### Goal

```txt
The password for Century10 is the 161st word within the file on the desktop.

NOTE:
- The password will be lowercase no matter how it appears on the screen.
```

#### Solution

```PowerShell
PS C:\users\century9\desktop> $(ls).name
Word_File.txt
PS C:\users\century9\desktop> gc .\Word_File.txt
larceny epibole ampliate trecentos psychotoxic sybarism shatterwit cartilaginification crenulation splenification freespac untragicalness renovater smirch historism tymbal nonobjectivist protestive octobass crownal retrorenal activation ascocarp clawi
ng unaccordingly strontianite refutatory reline unsubmersible unstuffy asynergia asha rejunction spiritrompe preestimates papabot postcoital forbearantly epistolize corkwood rasers logicized rearrange rectigraph signposts prothrombin headkerchief upho
lden oversocialize semiperimeter hackbuteer ticklish brachiated atheneum naegait engrasp palaeoconcha deminudity tragions curteous stratal swandown succinylcholine swooners caskanet irrespectability flocculant palatefulness thalamocoele maleate tittiv
ate eustachium etudes loppering fidos flayers murrion uninduced numbedness nincompoopish compressors cassoulet protura fagopyrismus sesquibasic paxwaxes grievous remonstrator fulvid rotatoria ultraconservatives postcards hairdresser wagnerianism mistr
eats nefarious winberry usherance conductility yearner uranostaphylorrhaphy rehabilitator agrapha junglegym emanant coy gaelicist parallelogram wealdsman objurgator tapeline amay psalterer eleostearate mainprise overdyeing dowly coronado localed wease
llike scattergram tocological disproportionation archicerebrum glazement zugtierlaster sleepwort yabber tenontodynia laevulose walkaway readept literally weinmannia englut caulopteris schellingian thiamid suberizes bistorta quinetum woolulose jaculife
rous trestlework unoriginativeness kua uncontemptibleness unconcernedly taryard escapologist traumata chlorochrous exocolitis dysgnosia steadfastness keratoleukoma inordinate sacahuiste trippler intoxicatively pierid nonapplicabness patinas rabific sc
andaliser waggel reauthenticate sufeism lairds cookee bragget ledgering perceptual chomper obscurities merino ganguela unproposed epulis loppard ignoblesse carrotage heartbrokenly unfusibness degenerate lacunae cirrocumulus knightlike overwhelmingness
 oxyrrhyncha capitalizations dimethylamine uninucleate syndicship graspable tropophil telchines abaiser overclement pursive

PS C:\users\century9\desktop> $((gc .\Word_File.txt).split(" "))[160]
pierid 

PS C:\users\century9\desktop> $((gc .\Word_File.txt).split(" "))[0]
larceny  
PS C:\users\century9\desktop> exit
Connection to century.underthewire.tech closed.

$ ssh century9@century.underthewire.tech:pierid
Under the Wire... PowerShell Training for the People!
PS C:\users\century10\desktop> 
```

### Century 10 -> 11

#### Goal

```txt
The password for Century11 is the 10th and 8th word of the Windows Update service description combined PLUS the name of the file on the desktop.

NOTE:
- The password will be lowercase no matter how it appears on the screen.
- If the 10th and 8th word of the service description is "apple" and "juice" and the name of the file on the desktop is "88", the password would be "applejuice88".
```

#### Solution

```PowerShell
PS C:\users\century10\desktop> Get-Service wuauserv | Select-Object -Property * | ft -AutoSize

Name     RequiredServices CanPauseAndContinue CanShutdown CanStop DisplayName    DependentServices MachineName ServiceName ServicesDependedOn
----     ---------------- ------------------- ----------- ------- -----------    ----------------- ----------- ----------- ------------------
wuauserv {rpcss}                        False       False   False Windows Update {}                .           wuauserv    {rpcss}

PS C:\users\century10\desktop> $(Get-WmiObject win32_Service -Filter "DisplayName = 'Windows Update'" | Select-Object -Property Description).Description
Enables the detection, download, and installation of updates for Windows and other programs. If this service is disabled, users of this computer will not be able to use Windows Update or its automatic updating feature, and programs will not be able to use the Windows Update Agent (WUA) API.  

PS C:\users\century10\desktop> $text = $(Get-WmiObject win32_Service -Filter "DisplayName = 'Windows Update'" | Select-Object -Property Description).Description
Enables the detection, download, and installation of updates for Windows and other programs. If this service is disabled, users of this computer will not be able to use Windows Update or its automatic updating feature, and programs will not be able to use the Windows Update Agent (WUA) API.  
PS C:\users\century10\desktop> $($($text.split(" "))[9] + $($text.split(" "))[7] + $((ls).name)).ToLower()
windowsupdates110
PS C:\users\century10\desktop> exit
Connection to century.underthewire.tech closed.

$ ssh century11@century.underthewire.tech:windowsupdates110
Under the Wire... PowerShell Training for the People!
PS C:\users\century11\desktop> 
```

### Century 11 -> 12

#### Goal

```txt
The password for Century12 is the name of the hidden file within the contacts, desktop, documents, downloads, favorites, music, or videos folder in the user's profile.

NOTE:
- Exclude "desktop.ini".
- The password will be lowercase no matter how it appears on the screen.
```

#### Solution

```PowerShell
PS C:\users\century11\desktop> $(ls ../ -Recurse -Hidden -File | ? {$_.name -ne "desktop.ini"}).name  
NTUSER.DAT
ntuser.dat.LOG1
ntuser.dat.LOG2
NTUSER.DAT{0f893ee4-78e5-11e6-90dd-eefb07825ed9}.TM.blf
NTUSER.DAT{0f893ee4-78e5-11e6-90dd-eefb07825ed9}.TMContainer00000000000000000001.regtrans-ms  
NTUSER.DAT{0f893ee4-78e5-11e6-90dd-eefb07825ed9}.TMContainer00000000000000000002.regtrans-ms  
ntuser.ini
UsrClass.dat
UsrClass.dat.LOG1
UsrClass.dat.LOG2
UsrClass.dat{d82669b3-abff-11e8-90ee-e14c26db97e8}.TM.blf
UsrClass.dat{d82669b3-abff-11e8-90ee-e14c26db97e8}.TMContainer00000000000000000001.regtrans-ms
UsrClass.dat{d82669b3-abff-11e8-90ee-e14c26db97e8}.TMContainer00000000000000000002.regtrans-ms
secret_sauce
PS C:\users\century11\desktop> exit
Connection to century.underthewire.tech closed.

$ ssh century12@century.underthewire.tech:secret_sauce
Under the Wire... PowerShell Training for the People!
PS C:\users\century12\desktop> 
```

### Century 12 -> 13

#### Goal

```txt
The password for Century13 is the description of the computer designated as a Domain Controller within this domain PLUS the name of the file on the desktop.

NOTE:
- The password will be lowercase no matter how it appears on the screen.
- If the description "today_is" and the file on the desktop is named "_cool", the password would be "today_is_cool"
```

#### Solution

```PowerShell
PS C:\users\century12\desktop> $( $(Get-ADComputer -Filter * -Properties CanonicalName,description | ? {$_.CanonicalName -like "*Domain Controllers*"}).Description + $(ls).name)
i_authenticate_things
PS C:\users\century12\desktop> exit
Connection to century.underthewire.tech closed.

$ ssh century13@century.underthewire.tech:i_authenticate_things
Under the Wire... PowerShell Training for the People!
PS C:\users\century13\desktop> 
```

### Century 13 -> 14

#### Goal

```txt
The password for Century14 is the number of words within the file on the desktop. 
```

#### Solution

```PowerShell
PS C:\users\century13\desktop> $(ls | gc).count
1 

PS C:\users\century13\desktop> ls | gc
spudders escudero hemitype unremittent rhinaria afflation emforth badgeringly bristler oxtongues roosed wittichenite faussebraye backwaters passion paginating gluishness seasick pectinibranchia antiquist valveman tendingly monogamic brine broadmindedl
y nonstress regisseurs arrogative petrographic intransitives insurgence parochiality microphagous plovers liverhearted mexical tremolant sysout heraldize tanacetin frangi discession vp therapeutist sulphaminic hyperanakinesia pathogeneses unconformiti
es semifailure staggie heteroplasia boyd
...

PS C:\users\century13\desktop> $(ls | gc).split(" ").count
755

$ ssh century14@century.underthewire.tech:755
Under the Wire... PowerShell Training for the People!
PS C:\users\century14\desktop>
```

### Century 14 -> 15

#### Goal

```txt
The password for Century15 is the number of times the word "polo" appears within the file on the desktop.

NOTE:
- You should count the instances of the whole word only. 
```

#### Solution

```PowerShell
PS C:\users\century14\desktop> $($(gci | gc).split(" ") | ? {$_ -eq "polo"}).count
153
```