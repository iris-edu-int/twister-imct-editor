#@PydevCodeAnalysisIgnore
"""empty message

Revision ID: b23b12b13544
Revises: a6fac381e718
Create Date: 2018-11-05 11:22:06.715465

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.orm.session import Session
from imct.app.models import ConfigModel
import pickle
from imct.app.models import XmlNodeAttrModel


# revision identifiers, used by Alembic.
revision = 'b23b12b13544'
down_revision = 'a6fac381e718'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    bind = op.get_bind()
    session = Session(bind=bind)
    session.add(ConfigModel(group='station', name="spread_to_channels", value=pickle.dumps(True)))
    session.commit()


def downgrade():
    bind = op.get_bind()
    session = Session(bind=bind)
    
    session.query(ConfigModel).filter(ConfigModel.group == 'station', ConfigModel.name == 'spread_to_channels').delete()
        
    session.commit()
