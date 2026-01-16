from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        """Initializes object with it's ID."""
        self.stream_id: str = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Blueprint for specified implementation in each stream type."""
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        """Default implementation for filter_data() just tells us wether
        the given data is valid or not."""
        for data in data_batch:
            try:
                _ = data + ' '
            except TypeError:
                print('Filtering sensor batch: '
                      '[ERROR] - Invalid data type entered'
                      ' (expected str)')
                return data_batch
        print('Stream data filtered successfully.')
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Default implementation for get_stats() just returns a dictionary
        with an 'id' key."""
        return {
            'id': self.stream_id,
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.count: int = 0
        self.temp_count: int = 0
        self.total_temp: float = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            for data in data_batch:
                _ = data + ' '
                if data[:5] == 'temp:':
                    self.count += 1
                    self.temp_count += 1
                    self.total_temp += float(data[5:])
                elif data[:9] == 'humidity:':
                    self.count += 1
                elif data[:9] == 'pressure:':
                    self.count += 1
                else:
                    return ('Processing sensor batch: '
                            f'[ERROR] - Invalid parameter type \'{data}\' '
                            '(expected \'temp:\', \'humidity:\' or '
                            '\'pressure:\')')
            avg: float = (self.total_temp / self.temp_count if
                          self.temp_count > 0 else 0)
            return (f'Sensor analysis: {self.count} readings processed, '
                    f'avg temp:{avg: .1f}°C')

        except TypeError:
            return ('Processing sensor batch: '
                    '[ERROR] - Invalid parameter type '
                    '(expected str)')
        except ValueError:
            return ('Processing sensor batch: '
                    '[ERROR] - Invalid parameter type '
                    '(value not convertable to float)')

    def filter_data(self, data_batch: List[Any], criteria: str | None
                    = None) -> List[Any]:
        if criteria != 'critical':
            return data_batch
        try:
            for data in data_batch:
                _ = data + ' '
            return [
                data for data in data_batch if
                (data[:5] == 'temp:' and not (-10 < float(data[5:]) < 50)) or
                (data[:9] == 'humidity:') and not (20 < int(data[9:]) < 85) or
                (data[:9] == 'pressure:') and not (950 < int(data[9:]) < 1080)
            ]

        except TypeError:
            print('Filtering sensor batch: '
                  '[ERROR] - Invalid parameter type '
                  '(expected str)')
            return data_batch
        except ValueError:
            print('Filtering sensor batch: '
                  '[ERROR] - Invalid parameter type '
                  '(value not convertable to float or int)')
            return data_batch

    def get_stats(self) -> Dict[str, str | int | float]:
        return {
            'id': self.stream_id,
            'type': 'Environmental Data',
            'count': self.count,
            'avg': (self.total_temp / self.temp_count)
            if self.temp_count > 0 else 0
        }


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.profit: int = 0
        self.trans_count: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        for data in data_batch:
            try:
                _ = data + ' '
                if data[:4] == 'buy:':
                    self.trans_count += 1
                    self.profit -= int(data[4:])
                elif data[:5] == 'sell:':
                    self.trans_count += 1
                    self.profit += int(data[5:])
                else:
                    return ('Processing transaction batch: '
                            f'[ERROR] - Invalid parameter type \'{data}\''
                            ' (expected \'buy:\' or \'sell:\')')
            except TypeError:
                return ('Processing transaction batch: '
                        '[ERROR] - Invalid parameter type '
                        '(expected str)')
            except ValueError:
                return ('Processing transaction batch: '
                        '[ERROR] - Invalid parameter type '
                        '(value not convertable to int)')
        if self.trans_count > 1:
            operation: str = 'operations'
        else:
            operation: str = 'operation'
        if self.profit == 1 or self.profit == -1:
            unit: str = 'unit'
        else:
            unit: str = 'units'

        if self.profit >= 0:
            pn: str = '+'
        else:
            pn: str = ''

        return (f'Transaction analysis: {self.trans_count} {operation}, '
                f'net flow: {pn}{self.profit} {unit}')

    def filter_data(self, data_batch: List[Any], criteria: str | None
                    = None) -> List[Any]:
        if criteria != 'large':
            return data_batch
        try:
            for data in data_batch:
                _ = data + ' '
                return [data for data in data_batch if
                        ((data[:4] == 'buy:') and int(data[4:] > 100)) or
                        ((data[:5] == 'sell:') and int(data[5:] > 100))]
        except TypeError:
            print('Filtering transaction batch: '
                  '[ERROR] - Invalid parameter type '
                  '(expected str)')
            return data_batch
        except ValueError:
            print('Filtering transaction batch: '
                  '[ERROR] - Invalid parameter type '
                  '(value not convertable to int)')
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            'id': self.stream_id,
            'type': 'Financial Data',
            'count': self.trans_count,
            'profit': self.profit,
        }


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.event_count: int = 0
        self.login_count: int = 0
        self.error_count: int = 0
        self.logout_count: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            for data in data_batch:
                _ = data + ' '
                if (data[:5] == 'login'):
                    self.event_count += 1
                    self.login_count += 1
                elif (data[:5] == 'error'):
                    self.error_count += 1
                elif (data[:6] == 'logout'):
                    self.event_count += 1
                    self.logout_count += 1
                else:
                    return ('Processing event batch: '
                            f'[ERROR] - Invalid parameter type \'{data}\''
                            ' (expected \'login\', \'logout\' or \'error\')')
            if self.error_count > 1:
                error: str = 'errors'
            else:
                error: str = 'error'

            if self.event_count > 1:
                event: str = 'events'
            else:
                event: str = 'event'
            return (f'Event analysis: {self.event_count} {event}, '
                    f'{self.error_count} {error} detected')
        except TypeError:
            return ('Processing event batch: '
                    '[ERROR] - Invalid parameter type'
                    ' (expect str)')

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        try:
            for data in data_batch:
                _ = data + ' '
            if criteria == 'login':
                return [e for e in data_batch if e == 'login']
            elif criteria == 'error':
                return [e for e in data_batch if e == 'error']
            elif criteria == 'logout':
                return [e for e in data_batch if e == 'logout']
            return data_batch
        except TypeError:
            print('Filtering event batch: '
                  '[ERROR] - Invalid data type entered'
                  ' (expected str')
            return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            'id': self.stream_id,
            'type': 'System Events',
            'count': self.event_count,
            'login_count': self.login_count,
            'error_count': self.error_count,
            'logout_count': self.logout_count,
        }


class StreamProcessor(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.sensor_count: int = 0
        self.transaction_count: int = 0
        self.event_count: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        processor_str: str = ''
        for data_list in data_batch:
            if not isinstance(data_list, list):
                return ('Processing stream batch: '
                        '[ERROR] - Invalid data type entered '
                        '(expecting a list)')
            for data in data_list:
                try:
                    _ = data + ' '
                except TypeError:
                    return ('Processing stream batch: '
                            '[ERROR] - Invalid data type entered '
                            '(expecting str)')
            if ((data_list[0][:5] == 'temp:') or
               (data_list[0][:9] == 'humidity:') or
               (data_list[0][:9] == 'pressure:')):
                sensor: SensorStream = SensorStream('Sensor')
                processor_str += (sensor.process_batch(data_list) + '\n')
                self.sensor_count += sensor.get_stats()['count']

            elif ((data_list[0][:4] == 'buy:') or
                  (data_list[0][:5] == 'sell:')):
                transaction: TransactionStream = (
                 TransactionStream('Transaction'))
                processor_str += (transaction.process_batch(data_list) + '\n')
                self.transaction_count += (
                    transaction.get_stats()['count'])

            elif ((data_list[0][:5] == 'login') or
                  (data_list[0][:5] == 'error') or
                  (data_list[0][:6] == 'logout')):
                event: EventStream = EventStream('Event')
                processor_str += event.process_batch(data_list) + '\n'
                self.event_count += event.get_stats()['count']

            else:
                return ('Processing stream batch: '
                        '[ERROR] - Invalid parameter type')
        return processor_str

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria == 'sensor':
            return [x for x in data_batch if (
                (x[0][:5] == 'temp:') or
                (x[0][:9] == 'humidity:') or
                (x[0][:9] == 'pressure:')
            )]
        elif criteria == 'transaction':
            return [x for x in data_batch if (
                (x[0][:4] == 'buy:') or
                (x[0][:5] == 'sell:')
            )]
        elif criteria == 'transaction':
            return [x for x in data_batch if (
                (x[0][:5] == 'login') or
                (x[0][:5] == 'error') or
                (x[0][:6] == 'logout')
            )]
        else:
            print('Filtering sensor batch: '
                  '[ERROR] - Invalid data type entered')
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            'id': self.stream_id,
            'sensor_count': self.sensor_count,
            'transaction_count': self.transaction_count,
            'event_count': self.event_count,
        }


if __name__ == '__main__':

    sensor_data: list[str] = ['humidity:100']
    sensor_test: SensorStream = SensorStream('SENSOR_001')

    trans_data: list[str] = ['sell:200']
    trans_test: TransactionStream = TransactionStream('TRANS_001')

    event_data: list[str] = ['login', 'logout', 'error']
    event_test: EventStream = EventStream('EVENT_001')

    processor: StreamProcessor = StreamProcessor('Batch 1')
    processor_data: list[list[str]] = [
        ['temp:15', 'humidity:100', 'pressure:1000'],
        ['buy:100', 'sell:200'],
        ['login', 'logout', 'error']
    ]

    print(sensor_test.process_batch(sensor_data))
    print(trans_test.process_batch(trans_data))
    print(event_test.process_batch(event_data))
    print(processor.process_batch(processor_data), end='')

    print('------------------------------------------------------')
    print('=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===')

    print('\nInitializing Sensor Stream...')
    print(f'Stream ID: {sensor_test.get_stats()["id"]}, '
          f'Type: {sensor_test.get_stats()["type"]}')
    print(sensor_test.process_batch(sensor_data))

    print('\nInitializing Transaction Stream...')
    print(f'Stream ID: {trans_test.get_stats()["id"]}, '
          f'Type: {trans_test.get_stats()["type"]}')
    print(trans_test.process_batch(trans_data))

    print('\nInitializing Event Stream...')
    print(f'Stream ID: {event_test.get_stats()["id"]}, '
          f'Type: {event_test.get_stats()["type"]}')
    print(sensor_test.process_batch(sensor_data))

