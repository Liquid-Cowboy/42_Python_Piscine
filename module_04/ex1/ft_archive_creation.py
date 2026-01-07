#!/bin/usr/env python3

f = None

print('=== CYBER ARCHIVES™ — PRESERVATION SYSTEM ===\n')

file_name = 'new_discovery.txt'
to_write = '{[}ENTRY 001{]}\tNew quantum algorithm discovered\n' \
           '{[}ENTRY 002{]}\tEfficiency increased by 347%\n' \
           '{[}ENTRY 003{]}\tArchived by Data Archivist trainee'

print(f'Initializing new storage unit: {file_name}')

try:
    f = open(file_name, 'w')
    print('Storage unit created successfully...\n')
    f.write(to_write)
    print('Inscribing preservation data...')
    print(to_write)
except Exception:
    print('ERROR: some unexpected failure ocurred...')
finally:
    if f:
        f.close()
