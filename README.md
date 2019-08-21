# discogs-detective

____________________________________________________________________________________________________________________________________________

Summary:
>> checks current offers on www.discogs.com for a given list of vinyl records
>> sends an email with all availale offers for each record including the price, vinyl quality and seller's country

____________________________________________________________________________________________________________________________________________

I started mixing electronic music in 2019. I'm using CD players and I always keep my ears open for new tracks that I could use in my mixes. Most tracks are available as downloads these days, however there are plenty older tracks (and also some new tracks) which were/are only produced on vinyl. Hum! But wait, it's not too bad!

In these days I can easily digitalize vinyl tracks. So what I do is: 

1. Purchase the vinyl record.
2. Create a digital copy for myself
3. Resell the vinyl record or give it to friends who mix with vinyls.

I mainly purchase vinyls from www.discogs.com. This little app I wrote is supposed to help me with the first step (Purchase the vinyl record). It checks current offers on www.discogs.com for a given list of vinyl records and sends me an email with all availale offers for each record including the price, vinyl quality and seller's country. It is installed on my Raspberry PI and runs once a day. To avoid redundant mailing, an email is only sent, if there are changes in the list of current offers compared to the list of yesterday's offers. Hence the list of current offers is saved on the PI's local harddrive and it becomes the list of yesterday's offers on the next day.

INPUTS:

1. Vinyl release codes from discogs.com: 

Each vinyl has a release code that must be saved in the following file: data\release_codes.csv

2. Config file

Rename "config_default.ini" to "config.ini" and specify your mail address, receiver, subject, smtp url and account credentials.

____________________________________________________________________________________________________________________________________________

If you have any comments or ideas to make the code better or more beautiful I am always open for suggestions

Best regards
Matthias
