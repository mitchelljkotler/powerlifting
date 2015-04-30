import datetime
import os
import re
import requests

data = {'username': 'mitch@mitchellkotler.net', 'password': 'u5yu8hYQaEk4thft'}

r = requests.post('https://thesquatrack.com/login', data=data)
cookies = r.cookies
headers = {'X-Requested-With': 'XMLHttpRequest'}

#date = datetime.date(2013, 7, 15)
files = sorted(os.listdir('data'))
latest = files[-1]
date = datetime.date(*[int(i) for i in latest.split('-')])
end_date = datetime.date.today()

p_wid = re.compile(r'data-workout-id="(\d+)"')

while date < end_date:
    print 'Processing %s...' % date.strftime('%Y-%m-%d')
    r = requests.get('https://thesquatrack.com/_get_date_workout_events/?date=%s' % date.strftime('%Y-%m-%d'), cookies=cookies, headers=headers)
    m_wid = p_wid.search(r.text)
    if m_wid:
        wid = m_wid.group(1)
        print 'Found a workout: %s' % wid
        r = requests.get('https://thesquatrack.com/_get_export_output/%s/markdown' % wid, cookies=cookies, headers=headers)
        with open(date.strftime('data/%Y-%m-%d'), 'w') as f:
            f.write(r.text)
    date += datetime.timedelta(1)
