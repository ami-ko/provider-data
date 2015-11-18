import os
import json
from pprint import pprint

root = os.path.join('data', 'source_urls')

for f in os.listdir(root):

    # Get the index file
    indices = [ g for g in os.listdir(os.path.join('data', 'source_urls', f)) if os.path.isfile(os.path.join('data', 'source_urls', f, g))]

    if len(indices) != 1:
        print "Failed to find index file at " + f
        continue

    indices = indices[0]

    if 'index' not in indices:
        print "Failed to recognize index file at " + f
        continue

    urls = open(os.path.join('data', 'source_urls', f, indices)).read()

    try:
        urls_json = json.loads(urls)
    except ValueError, e:
        print "Failed to parse json index at " + f
        continue

    if not os.path.exists(os.path.join('data', 'source_urls', f, 'formulary_urls')):
        os.makedirs(os.path.join('data', 'source_urls', f, 'formulary_urls'))
    if not os.path.exists(os.path.join('data', 'source_urls', f, 'plan_urls')):
        os.makedirs(os.path.join('data', 'source_urls', f, 'plan_urls'))
    if not os.path.exists(os.path.join('data', 'source_urls', f, 'provider_urls')):
        os.makedirs(os.path.join('data', 'source_urls', f, 'provider_urls'))

    for httpurl in urls_json['formulary_urls']:
        os.system('wget ' + httpurl)
        os.system('mv ' + httpurl.split('/')[-1] + ' ' + os.path.join('data', 'source_urls', f, 'formulary_urls') + '/')

    for httpurl in urls_json['plan_urls']:
        os.system('wget ' + httpurl)
        os.system('mv ' + httpurl.split('/')[-1] + ' ' + os.path.join('data', 'source_urls', f, 'plan_urls') + '/')

    for httpurl in urls_json['provider_urls']:
        os.system('wget ' + httpurl)
        os.system('mv ' + httpurl.split('/')[-1] + ' ' + os.path.join('data', 'source_urls', f, 'provider_urls') + '/')
