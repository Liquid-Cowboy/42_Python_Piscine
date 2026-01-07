#!/usr/bin/env python3

from typing import Any, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """Parent class servers as a mandatory blueprint to all children
    Children must define each of the methods decorated as abstract"""
    @abstractmethod
    def process(self, data: Any) -> str:
        """Will act based on the validation of the data
        If everything's good, it will process the stats
        demanded by each type of stream"""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validates data based on the requirements of each stream"""
        pass

    def format_output(self, result: str) -> str:
        """Defines a generic prefix for the output and places
        the processed string right after"""
        return f'Output: {result}'


class NumericProcessor(DataProcessor):
    "Will handle only lists of integers"
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return ''
        total: int = 0
        count: int = 0
        for nbr in data:
            total += nbr
            count += 1
        avg: float = total / count
        return f'Processed {count} numeric values, sum={total}, avg={avg:.1f}'

    def validate(self, data: Any) -> bool:
        try:
            for nbr in data:
                _ = nbr + 1
            return True
        except TypeError:
            return False


class TextProcessor(DataProcessor):
    "Will handle only strings"
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return ''
        chr_count: int = 0
        wd_count: int = 0
        in_word: bool = True
        for chr in data:
            chr_count += 1
            if (chr >= '\t' and chr <= '\r') or chr == ' ':
                in_word = True
                continue
            if in_word:
                wd_count += 1
                in_word = False

        return f'Processed text: {chr_count} characters, {wd_count} words'

    def validate(self, data: Any) -> bool:
        try:
            _ = data + ' '
            return True
        except TypeError:
            return False


class LogProcessor(DataProcessor):
    "Will handle a specific type of strings"
    "defined by their prefix (ERROR/INFO)"
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return ''
        if data[:7] == 'ERROR: ':
            return f'[ALERT] ERROR level detected: {data[7:]}'
        else:
            return f'[INFO] INFO level detected: {data[6:]}'

    def validate(self, data: Any) -> bool:
        try:
            _ = data + ' '
        except TypeError:
            return False
        if data[:7] == 'ERROR: ' or data[:6] == 'INFO: ':
            return True
        else:
            return False


nbr_list: NumericProcessor = NumericProcessor()
text_data: TextProcessor = TextProcessor()
log_data: LogProcessor = LogProcessor()

nbrs: List[Any] = [42, 24, 42]
text: str = 'Hello Nexus World'
log: str = 'ERROR: Connection timeout'

print('=== CODE NEXUS — DATA PROCESSOR FOUNDATION ===\n')

print('Initializing Numeric Processor...')
print(f'Processing data: {nbrs}')
if nbr_list.validate(nbrs):
    print('Validation: Numeric data verified')
else:
    print('Validation: Invalid numeric data')
print(nbr_list.format_output(nbr_list.process(nbrs)))

print('')

print('Initializing Text Processor...')
print(f'Processing data: {text}')
if text_data.validate(text):
    print('Validation: Text data verified')
else:
    print('Validation: Invalid text data')
print(text_data.format_output(text_data.process(text)))

print('')

print('Initializing Log Processor...')
print(f'Processing data: {log}')
if log_data.validate(log):
    print('Validation: Log entry verified')
else:
    print('Validation: Invalid log entry')
print(log_data.format_output(log_data.process(log)))

print('')

print('=== Polymorphic Processing Demo ===')
print('Processing multiple data types through the same interface...')
inputs: List[List[Any]] = [
    [NumericProcessor(), [4, 0, 2]],
    [TextProcessor(), "Hello World!"],
    [LogProcessor(), "INFO: System ready"],
]

i: int = 1

for processor, data in inputs:
    print(f'Result {i}: {processor.process(data)}')
    i += 1

print('\nFoundation systems online. Nexus ready for advanced streams.')
