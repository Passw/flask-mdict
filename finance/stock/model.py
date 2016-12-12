#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import sys
import os.path

common_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'common'))

sys.path.append(common_path)

from common.stock.model_base import *

from ..database_base import Base


class Stock(StockBase, Base):
    pass


class Market(MarketBase, Base):
    pass


class Plate(PlateBase, Base):
    pass


class PdfReport(PdfReportBase, Base):
    pass
