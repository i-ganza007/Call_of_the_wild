#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NoteAPI.settings')
    try:
        from django.core.management import execute_from_command_line
        # This line executes every thing in the command like 
    except ImportError as exc:
        raise ImportError(
            'Shitty Imports and commands'
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()