#!/usr/bin/env

lost = 'lost_archive.txt'
classified = 'classified_vault.txt'
std = 'standard_archive.txt'

print('=== CYBER ARCHIVES — CRISIS RESPONSE SYSTEM ===\n')

try:
    with open(lost, 'r') as f:
        print(f'ROUTINE ACCESS: Attempting access to \'{lost}\'...')
        print(f'SUCCESS: Archive recovered – ``{f.read()}\'\'')
        print('STATUS: Normal operations resumed')
except FileNotFoundError:
    print(f'CRISIS ALERT: Attempting access to \'{lost}\'...')
    print('RESPONSE: Archive not found in storage matrix')
    print('STATUS: Crisis handled, system stable')
except Exception as e:
    print(f'ERROR: {e}')

print('')

try:
    with open(classified, 'r') as f:
        print(f'ROUTINE ACCESS: Attempting access to \'{classified}\'...')
        print(f'SUCCESS: Archive recovered – ``{f.read()}\'\'')
        print('STATUS: Normal operations resumed')
except FileNotFoundError:
    print(f'CRISIS ALERT: Attempting access to \'{classified}\'...')
    print('RESPONSE: Security protocols deny access')
    print('STATUS: Crisis handled, security maintained')
except Exception as e:
    print(f'ERROR: {e}')

print('')

try:
    with open(std, 'r') as f:
        print(f'ROUTINE ACCESS: Attempting access to \'{std}\'...')
        print(f'SUCCESS: Archive recovered – ``{f.read()}\'\'')
        print('STATUS: Normal operations resumed')
except FileNotFoundError:
    print(f'CRISIS ALERT: Attempting access to \'{std}\'...')
    print('RESPONSE: Archive not found in storage matrix')
    print('STATUS: Crisis handled, security maintained')
except Exception as e:
    print(f'ERROR: {e}')

print('\nAll crisis scenarios handled successfully. Archives secure.')
