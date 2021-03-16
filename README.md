# hugo-testing

Add the following

CSP Hash
- `echo -n 'InlineJavaScript();' | openssl dgst -sha256 -binary | openssl enc -base64`  
   `"default-src 'none'; script-src 'sha256-dv/vjgvEe4HtJO7GbSis1aOc3bOGD2SMMyEjerX7lXc=';"`

Needed for this project

- `echo -n 'var baseurl="https:\/\/dev-hugo.justin-p.me\/";' | openssl dgst -sha256 -binary | openssl enc -base64`
- `echo -n 'mermaid.initialize({startOnLoad:true});' | openssl dgst -sha256 -binary | openssl enc -base64`
- `echo -n 'hljs.initHighlightingOnLoad();' | openssl dgst -sha256 -binary | openssl enc -base64`
- `echo -n ':root #header+#content>#left>#rlblock_left{display:none!important}' | openssl dgst -sha256 -binary | openssl enc -base64`
- `echo -n 'left:-1000px;overflow:scroll;position:absolute;top:-1000px;border:none;box-sizing:content-box;height:200px;margin:0;padding:0;width:200px' | openssl dgst -sha256 -binary | openssl enc -base64`
- `echo -n 'border:none;box-sizing:content-box;height:200px;margin:0;padding:0;width:200px' | openssl dgst -sha256 -binary | openssl enc -base64`


## Add this content for phish infra

https://www.appmaildev.com
https://www.mail-tester.com
https://spamcheck.postmarkapp.com/
