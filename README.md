# pyflare
Updates Cloudflare with current IP

So I got sick of all those free dynamic dns services and fortunately some nice person on Reddit came up with this idea:
https://www.reddit.com/r/raspberry_pi/comments/9nimtz/use_cloudflare_as_dynamic_dns_with_raspberry_pi/
If you are a Redditor please go give u/TheFirsh some tasty tasty karma.

 Cloudflare will host your DNS for free, on top of a whole heap of other benefits, and they have a really good API for updating DNS records. The idea is that you run this script like you would a dynamic DNS client - it's python so entirely cross platform and uses minimal and very common libraries.

# config.json

You will need to create a config.json file in the same folder as pyflare.py - this file must be json formatted and contain the following 4 elements.
```
{
  # The email address on your Cloudflare account
	"email": "",
  # The Global API key on your account
	"key": "",
  # The zone for which you'll be updating a record (ie example.com)
	"zone": "",
  # The record for which you'll be updating (ie home.example.com)
  # This record should already exist in Cloudflare
	"record": ""
}
```
