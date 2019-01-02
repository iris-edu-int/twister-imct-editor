#@PydevCodeAnalysisIgnore
"""empty message

Revision ID: 632cdf365a64
Revises: 1f7bbbe850b1
Create Date: 2018-08-24 12:14:29.355766

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.orm.session import Session
from imct.app.models import XmlNodeModel, XmlNodeAttrWidgetModel, XmlNodeAttrModel, XmlNodeAttrRelationModel
from imct.app.enums.xml_node import XmlNodeEnum


# revision identifiers, used by Alembic.
revision = '632cdf365a64'
down_revision = '1f7bbbe850b1'
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    session = Session(bind=bind)

    text_field = XmlNodeAttrWidgetModel(name='imct-text-field')
    float_field = XmlNodeAttrWidgetModel(name='imct-float-field')
    int_field = XmlNodeAttrWidgetModel(name='imct-int-field')
    area_field = XmlNodeAttrWidgetModel(name='imct-area-field')
    date_field = XmlNodeAttrWidgetModel(name='imct-date-field')
    comments_field = XmlNodeAttrWidgetModel(name='imct-comments-field')
    site_field = XmlNodeAttrWidgetModel(name='imct-site-field')
    latitude_field = XmlNodeAttrWidgetModel(name='imct-latitude-field')
    longitude_field = XmlNodeAttrWidgetModel(name='imct-longitude-field')
    operators_field = XmlNodeAttrWidgetModel(name='imct-operators-field')
    external_references_field = XmlNodeAttrWidgetModel(name='imct-external-references-field')
    types_field = XmlNodeAttrWidgetModel(name='imct-channel-types-field')
    equipment_field = XmlNodeAttrWidgetModel(name='imct-channel-equipment-field')
    response_field = XmlNodeAttrWidgetModel(name='imct-channel-response-field')

    session.add(text_field)
    session.add(float_field)
    session.add(int_field)
    session.add(area_field)
    session.add(date_field)

    attr_code = XmlNodeAttrModel(name='code', widget=text_field)
    attr_alt_code = XmlNodeAttrModel(name='alternate_code', widget=text_field)
    attr_historical_code = XmlNodeAttrModel(name='historical_code', widget=text_field)
    attr_start_date = XmlNodeAttrModel(name='start_date', widget=date_field)
    attr_end_date = XmlNodeAttrModel(name='end_date', widget=date_field)
    attr_comments = XmlNodeAttrModel(name='comments', widget=comments_field)
    attr_description = XmlNodeAttrModel(name='description', widget=text_field)
    attr_elevation = XmlNodeAttrModel(name='elevation', widget=float_field)
    attr_external_references = XmlNodeAttrModel(name='external_references', widget=external_references_field)
    attr_restricted_status = XmlNodeAttrModel(name='restricted_status', widget=text_field)
    attr_latitude = XmlNodeAttrModel(name='latitude', widget=latitude_field)
    attr_longitude = XmlNodeAttrModel(name='longitude', widget=longitude_field)
    
    attr_total_number_of_channels = XmlNodeAttrModel(name='total_number_of_channels', widget=int_field)
    attr_selected_number_of_channels = XmlNodeAttrModel(name='selected_number_of_channels', widget=int_field)
        
    attr_total_number_of_stations = XmlNodeAttrModel(name='total_number_of_stations', widget=int_field)
    attr_selected_number_of_stations = XmlNodeAttrModel(name='selected_number_of_stations', widget=int_field)
     
    network = XmlNodeModel(id=XmlNodeEnum.NETWORK, clazz='Network')
    session.add(network)

    network.attrs.append(XmlNodeAttrRelationModel(attr=attr_code))
    network.attrs.append(XmlNodeAttrRelationModel(attr=attr_alt_code))
    network.attrs.append(XmlNodeAttrRelationModel(attr=attr_historical_code))
    network.attrs.append(XmlNodeAttrRelationModel(attr=attr_start_date))
    network.attrs.append(XmlNodeAttrRelationModel(attr=attr_end_date))
    network.attrs.append(XmlNodeAttrRelationModel(attr=attr_comments))
    network.attrs.append(XmlNodeAttrRelationModel(attr=attr_description))
    network.attrs.append(XmlNodeAttrRelationModel(attr=attr_restricted_status))
    network.attrs.append(XmlNodeAttrRelationModel(attr=attr_total_number_of_stations))
    network.attrs.append(XmlNodeAttrRelationModel(attr=attr_selected_number_of_stations))
        
    station = XmlNodeModel(id=XmlNodeEnum.STATION, clazz='Station', parent_id=XmlNodeEnum.NETWORK)
    session.add(station)

    station.attrs.append(XmlNodeAttrRelationModel(attr=attr_code))
    station.attrs.append(XmlNodeAttrRelationModel(attr=attr_alt_code))
    station.attrs.append(XmlNodeAttrRelationModel(attr=attr_historical_code))
    station.attrs.append(XmlNodeAttrRelationModel(attr=attr_start_date))
    station.attrs.append(XmlNodeAttrRelationModel(attr=attr_end_date))
    station.attrs.append(XmlNodeAttrRelationModel(attr=attr_comments))
    station.attrs.append(XmlNodeAttrRelationModel(attr=attr_description))
    station.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='termination_date', widget=date_field)))
    station.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='creation_date', widget=date_field)))
    station.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='site', widget=site_field)))
    station.attrs.append(XmlNodeAttrRelationModel(attr=attr_latitude))
    station.attrs.append(XmlNodeAttrRelationModel(attr=attr_longitude))
    station.attrs.append(XmlNodeAttrRelationModel(attr=attr_elevation))
    station.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='vault', widget=text_field)))
    station.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='geology', widget=text_field)))
    station.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='operators', widget=operators_field)))
#    station.attrs.append(XmlNodeAttrRelationModel(attr=attr_external_references))
    station.attrs.append(XmlNodeAttrRelationModel(attr=attr_restricted_status))
    station.attrs.append(XmlNodeAttrRelationModel(attr=attr_total_number_of_channels))
    station.attrs.append(XmlNodeAttrRelationModel(attr=attr_selected_number_of_channels))
    
    channel = XmlNodeModel(id=XmlNodeEnum.CHANNEL, clazz='Channel', parent_id=XmlNodeEnum.STATION)
    session.add(channel)
    channel.attrs.append(XmlNodeAttrRelationModel(attr=attr_code))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=attr_alt_code))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=attr_historical_code))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=attr_start_date))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=attr_end_date))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=attr_comments))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=attr_description))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='location_code', widget=text_field)))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=attr_latitude))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=attr_longitude))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=attr_elevation))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='depth', widget=float_field)))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='azimuth', widget=float_field)))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='dip', widget=float_field)))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='types', widget=types_field)))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=attr_external_references))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='sample_rate', widget=float_field)))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='sample_rate_ratio_number_samples', widget=int_field)))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='sample_rate_ratio_number_seconds', widget=int_field)))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='storage_format', widget=text_field)))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='clock_drift_in_seconds_per_sample', widget=float_field)))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='calibration_units', widget=text_field)))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='calibration_units_description', widget=text_field)))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='sensor', widget=equipment_field)))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='pre_amplifier', widget=equipment_field)))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='data_logger', widget=equipment_field)))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='equipment', widget=equipment_field)))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=XmlNodeAttrModel(name='response', widget=response_field)))
    channel.attrs.append(XmlNodeAttrRelationModel(attr=attr_restricted_status))

    session.commit()


def downgrade():
    bind = op.get_bind()
    session = Session(bind=bind)
    session.query(XmlNodeModel).delete()    
    session.query(XmlNodeAttrModel).delete()
    session.query(XmlNodeAttrWidgetModel).delete()
    session.flush()
    session.commit()

