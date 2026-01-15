#!bin/usr/env python3

import sys

print('=== CYBER ARCHIVES™ — COMMUNICATION SYSTEM ===\n')

try:
    id: str = input('Input Stream active. Enter archivist ID: ')
    status: str = input('Input Stream active. Enter status report: ')

except KeyboardInterrupt:
    print('\nERROR: User pressed Ctrl-C. Exiting...',
          file=sys.stderr)
except Exception:
    print('\nERROR: An error ocurred while receiving input. Exiting...',
          file=sys.stderr)

else:
    print(f'\n[STANDARD] Archive status from {id}: {status}',
          file=sys.stdout)
    print('[ALERT] System diagnostic: Communication channels verified',
          file=sys.stderr)
    print('[STANDARD] Data transmission complete',
          file=sys.stdout)
    print('\nThree-channel communication test successful.')
