
# UrbanFootprint v1.5
# Copyright (C) 2016 Calthorpe Analytics
#
# This file is part of UrbanFootprint version 1.5
#
# UrbanFootprint is distributed under the terms of the GNU General
# Public License version 3, as published by the Free Software Foundation. This
# code is distributed WITHOUT ANY WARRANTY, without implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License v3 for more details; see <http://www.gnu.org/licenses/>.

from django.contrib.gis.db import models

from footprint.main.models.geospatial.feature import Feature

__author__ = 'calthorpe_analytics'


class CensusTracts(Feature):
    county_id = models.CharField(max_length=50, null=True)
    tractce10 = models.CharField(max_length=50, null=True)
    geoid10 = models.CharField(max_length=50, null=True)
    aland10 = models.DecimalField(max_digits=14, decimal_places=2, null=True)
    awater10 = models.DecimalField(max_digits=14, decimal_places=2, null=True)

    class Meta(object):
        abstract = True
        app_label = 'main'
