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
    print('\nERROR: ERROR: Storage vault not found. Run data generator first. \
Remember: a good archivist always checks if the vault exists before \
attempting access. Trying to read non-existent files is like trying to open a \
door that isn’t there—it never ends well.')

finally:
    if f:
        f.close()
