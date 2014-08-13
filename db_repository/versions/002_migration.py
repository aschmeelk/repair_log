from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
repair = Table('repair', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('date', DATE),
    Column('pc_num', INTEGER),
    Column('franchise', VARCHAR(length=64)),
    Column('problem', VARCHAR(length=128)),
    Column('solution', VARCHAR(length=128)),
    Column('tech', VARCHAR(length=64)),
    Column('pc_app', VARCHAR(length=64)),
    Column('pd_mb', VARCHAR(length=64)),
)

repairs = Table('repairs', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('date', Date),
    Column('pc_num', Integer),
    Column('franchise', String(length=64)),
    Column('problem', String(length=128)),
    Column('solution', String(length=128)),
    Column('tech', String(length=64)),
    Column('pc_app', String(length=64)),
    Column('pd_mb', String(length=64)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['repair'].drop()
    post_meta.tables['repairs'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['repair'].create()
    post_meta.tables['repairs'].drop()
