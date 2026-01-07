#!/usr/bin/env python3

print('=== CYBER ARCHIVES™ — VAULT SECURITY SYSTEM ===\n')

print('Initiating secure vault access...')
try:
    with open('classified_data.txt', 'r+') as f:
        print('Vault connection established with failsafe protocols\n')
        print('SECURE EXTRACTION:')
        print(f.read())

        str_to_write = '[CLASSIFIED] New security protocols archived'
        f.write('\n' + str_to_write)
        print('SECURE PRESERVATION:')
        print(str_to_write)
        print('Vault automatically sealed upon completion')
        print('\nAll vault operations completed with maximum security.')
except Exception as e:
    print(f'ERROR: {e}')
