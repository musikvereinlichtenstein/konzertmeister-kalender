import os
import sys
import urllib.request
from pathlib import Path
from icalendar import Calendar

urls = [s.strip() for s in os.environ['ICAL_URLS'].splitlines() if s.strip()]
if len(urls) != 9:
    sys.exit(f'Expected 9 source URLs, got {len(urls)}')

merged = Calendar()
merged.add('prodid', '-//Musikverein//Konzertmeister Merge//DE')
merged.add('version', '2.0')
merged.add('x-wr-calname', 'Konzertmeister Raumbelegung Gesamt')
merged.add('x-wr-timezone', 'Europe/Berlin')
seen = set()
counts = []
for idx, url in enumerate(urls, 1):
    req = urllib.request.Request(url, headers={'User-Agent': 'KonzertmeisterCalendarMerge/1.0'})
    with urllib.request.urlopen(req, timeout=40) as response:
        payload = response.read()
    cal = Calendar.from_ical(payload)
    count = 0
    for component in cal.subcomponents:
        if component.name not in ('VEVENT', 'VTODO', 'VJOURNAL', 'VTIMEZONE'):
            continue
        if component.name == 'VTIMEZONE':
            # Keep one copy of each timezone definition.
            key = ('timezone', str(component.get('TZID', '')))
        else:
            uid = str(component.get('UID', ''))
            rid = str(component.get('RECURRENCE-ID', ''))
            # Namespace event UIDs by source to prevent unrelated sources colliding.
            if uid:
                component['UID'] = f'feed{idx}-{uid}'
            key = (idx, uid, rid, component.name)
            count += 1
        if key in seen:
            continue
        seen.add(key)
        merged.add_component(component)
    counts.append(count)

out = Path('site/raumbelegung.ics')
out.parent.mkdir(parents=True, exist_ok=True)
out.write_bytes(merged.to_ical())
print('Source counts:', counts, 'Total:', sum(counts), 'Bytes:', out.stat().st_size)
