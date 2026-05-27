"""
strategy_base.py

Abstract base class for all DeFi strategies.
"""

from abc import ABC, abstractmethod


class Strategy(ABC):

    def __init__(self, name):

        self.name = name

    @abstractmethod
    def generate_return(self, state):

        pass