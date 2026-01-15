from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    @abstractmethod
    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        pass

    @abstractmethod
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):
    """Deals with only sensor type events."""
    reading_count: int = 0
    temp_count: int = 0
    total_temp: float = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Will calculate the amount of readings and the average
        of the value parameter when given. It is protected against invalid
        data types and invalid inputs (not following the
        <valid_parameter>:<value> protocol)"""
        reading_count: int = 0
        temp_count: int = 0
        total_temp: float = 0
        for data in data_batch:
            try:
                _ = data + ' '
            except TypeError:
                return 'Processing sensor batch: ' \
                       '[ERROR] - Invalid data type entered'
            else:
                if data[:5] == 'temp:':
                    reading_count += 1
                    temp_count += 1
                    total_temp += float(data[5:])
                elif data[:9] == 'humidity:':
                    reading_count += 1
                elif data[:9] == 'pressure:':
                    reading_count += 1
                else:
                    return 'Processing sensor batch: ' \
                           '[ERROR] - Invalid parameter type'
                self.reading_count += reading_count
                self.temp_count += temp_count
                self.total_temp += total_temp
        try:
            avg: float = self.total_temp / self.temp_count
        except ZeroDivisionError:
            avg: float = 0
        return f'Sensor analysis: {self.reading_count} readings processed, '\
               f'avg temp:{avg: .1f}°C'

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if not criteria == 'critical':
            return data_batch
        for data in data_batch:
            try:
                _ = data + ' '
            except TypeError:
                print('Filtering sensor batch: '
                      '[ERROR] - Invalid data type entered')
                return data_batch
        return [
            data for data in data_batch if
            (data[:5] == 'temp:' and not (-10 < float(data[5:]) < 50)) or
            (data[:9] == 'humidity:') and not (20 < int(data[9:]) < 85) or
            (data[:9] == 'pressure:') and not (950 < int(data[9:]) < 1080)
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
                'id': self.stream_id,
                'type': 'Environmental Data',
                'reading_count': self.reading_count,
                'avg': (self.total_temp / self.temp_count)
                if self.temp_count > 0 else 0
               }


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        return super().process_batch(data_batch)

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats()


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        return super().process_batch(data_batch)

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats()


class StreamProcessor (DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        return super().process_batch(data_batch)

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats()


print('=== CODE NEXUS — POLYMORPHIC STREAM SYSTEM ===\n')

sensor_1_values = ['temp:22.5', 'humidity:65', 'pressure:1013']
sensor1_read: SensorStream = SensorStream('SENSOR_001')
# print
print('Initializing Sensor Stream...')

print(f'Stream ID: {sensor1_read.get_stats()["id"]}, '
      f'Type: {sensor1_read.get_stats()["type"]}')
if (sensor1_read.process_batch(sensor_1_values)[:6] == 'Sensor'):
    print(f'Processing sensor batch: {sensor_1_values}')
print(sensor1_read.process_batch(sensor_1_values))
