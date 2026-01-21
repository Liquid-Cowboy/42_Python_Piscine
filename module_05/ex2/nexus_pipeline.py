from __future__ import annotations
from typing import Any, List, Dict, Union, Optional, Protocol
from abc import ABC, abstractmethod
from collections import OrderedDict
import time

class ProcessingPipeline(ABC):
    """Manages stages. Keeps track of them with the stages atribute."""
    def __init__(self, pipeline_id: str) -> None:
        if isinstance(pipeline_id, str):
            self.pipeline_id = pipeline_id
        else:
            print('[ERROR]: Not a valid pipeline id')
        self._stages: List[Any] = []
        self._stats: Dict[str, Any] = {
            'processed': 0,
            'errors': 0,
            'total_time': 0.0
        }

    
    def add_stage(self, stage: ProcessingStage):
        self._stages.append(stage)
    
    def run_pipeline(self, data: Any) -> Any:
        start = time.perf_counter()
        changed = data
        try:
            for s in self._stages:
                changed = s.process(changed)
                self._stats['processed'] += 1
                return changed
        except Exception as e:
            self._stats['errors'] += 1
            print(f'[ERROR]: {e}')
        finally:
            self._stats['total_time'] += time.perf_counter() - start





    @abstractmethod
    def process(self, data) -> Any:
        pass
    pass

class ProcessingStage(Protocol):
    """If it looks like a duck, swims like a duck,
    and quacks like a duck, then it probably is a duck.
    Classes applying this protocol can be called interchangeably
    By doing *processing : ProcessingStage, processing.process(data)*"""
    def process(self, data) -> Any:
        pass

class InputStage():
    """Stage class implementing the protocol"""
    def process(self,data: Any) -> Any:
        if isinstance(data, Dict):
            d: OrderedDict = OrderedDict(data)
            od: OrderedDict = OrderedDict(
                [
                    ('sensor', ''),
                    ('value', 13),
                    ('unit', 'C'),
                ]
            )
            if list(d.keys()) == list(od.keys()) and(
                isinstance(d['sensor'], str) and
                isinstance(d['value'], float) and
                isinstance(d['unit'], str)
            ):
                return {
                    'adapter': 'JSON',
                    'input': data
                }
            print('[ERROR]: Not a valid input. Please '
                  'follow the formula -> {"sensor": <str>, '
                  '"value": int, "unit": <str>}')
            return 'invalid'
        elif isinstance(data, str):
            return {
                'adapter': 'CSV',
                'input': data,
            }
        elif isinstance(data, list):
            for el in data:
                if not isinstance(el, int):
                    print('[ERROR]: Not a valid data type '
                          '(expected a list of ints)')
                    return 'invalid'
                return {
                    'adapter': 'Stream',
                    'input': data,
                }
        print('[ERROR]: Not a valid data type (expected '
              '<dict>, <str> or <list[int]>)')
        return 'invalid'

class TransformStage():
    """Stage class implementing the protocol"""
    def process(self, data: Any) -> Any:
        if not isinstance(data, dict):
            print('[ERROR]: Not a valid input, '
                  '(expect a dict)')
            return 'invalid'
        if list(data.keys()) == ['adapter', 'input']:
            if data['adapter'] == 'JSON':
                trans: dict[str, Any] = data['input']
                
                pass
            elif data['adapter'] == 'CSV':
                pass
            elif data['adapter'] == 'Stream':
                pass
            return 'invalid'
        return 'invalid'


class OutputStage():
    """Stage class implementing the protocol"""
    def process(self, data: Any) -> Any:
    pass

class JSONAdapter(ProcessingPipeline):
    """Adapter class overriding process()"""
    def process(self, data: Any) -> Union[str, Any]:
        if not isinstance(data, dict):
            return print('[ERROR]: Not a valid JSON input.')
        else:
            for stage in self._stages:
                data = stage.process(data)

class CSVAdapter(ProcessingPipeline):
    """Adapter class overriding process()"""
    def process(self, data) -> Union[str, Any]
        pass
    pass

class StreamAdapter(ProcessingPipeline):
    """Adapter class overriding process()"""
    def process(self, data) -> Union[str, Any]
        pass
    pass

class NexusManager():
    """Deals with multiple pipelines polymorphically"""
    pipelines: List[]

    def add_pipeline(self):
        pass

    def process_data(self):
        pass
