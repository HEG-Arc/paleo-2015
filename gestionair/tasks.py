# -*- coding: UTF-8 -*-
# tasks.py
#
# Copyright (C) 2015 HES-SO//HEG Arc
#
# Author(s):
#
# This file is part of Gestion'air 2015.
#
# Gestion'air 2015 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Gestion'air 2015 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Gestion'air 2015. If not, see <http://www.gnu.org/licenses/>.

from celery import Celery

app = Celery()


@app.task
def add(x, y):
    return x + y

if __name__ == '__main__':
    app.worker_main()