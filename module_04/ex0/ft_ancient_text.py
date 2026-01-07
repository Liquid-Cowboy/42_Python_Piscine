#!/usr/bin/env python3

print('=== CYBER ARCHIVES™ — DATA RECOVERY SYSTEM ===\n')
file_name = 'ancient_fragment.txt'
print(f'Accessing Storage Vault: {file_name}')
f = None

try:
    f = open(file_name, 'r')
    print('Connection established...\n\nRECOVERED DATA:')
    print(f.read())
    print('\nData recovery complete. Storage unit disconnected.')

except Exception:
    print('\nERROR: Storage vault not found. Run data generator first.')

finally:
    if f:
        f.close()
