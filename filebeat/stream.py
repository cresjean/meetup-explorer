import json
import requests
import sys

print "streaming to {}".format(sys.argv[1])
logfile = sys.argv[1]
r = requests.get('http://stream.meetup.com/2/rsvps', stream=True)


if r.encoding is None:
    r.encoding = 'utf-8'

with open(logfile, 'w+') as file:
    for line in r.iter_lines(decode_unicode=True):
        if line:
            parsed = json.loads(line)
            group =  parsed.get('group')
            location = {'lat': group.get('group_lat'), 'lon':  group.get('group_lon') }
            parsed['group']['location'] = location

            topics_array = []
            topics_string = ""
            for topic in group['group_topics']:
                topic_string = u''.join(topic['topic_name']).encode('utf-8').strip()
                topics_string = "{},{}".format(topic_string,topics_string)
                topics_array.append(topic_string)
            print topics_string
            parsed['group']['topics_string'] = topics_string
            parsed['group']['topics_array'] = topics_array

            file.write("{}\n".format(json.dumps(parsed)))
