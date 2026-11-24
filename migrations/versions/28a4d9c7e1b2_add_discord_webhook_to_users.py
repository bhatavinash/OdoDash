"""add Discord webhook URL to users

Revision ID: 28a4d9c7e1b2
Revises: f8b9c0d1e2f3
Create Date: 2026-11-24
"""
from alembic import op
import sqlalchemy as sa


revision = '28a4d9c7e1b2'
down_revision = 'f8b9c0d1e2f3'
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if 'users' not in inspector.get_table_names():
        return
    columns = {column['name'] for column in inspector.get_columns('users')}
    if 'discord_webhook_url' not in columns:
        with op.batch_alter_table('users') as batch_op:
            batch_op.add_column(sa.Column('discord_webhook_url', sa.String(length=500), nullable=True))


def downgrade():
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if 'users' not in inspector.get_table_names():
        return
    columns = {column['name'] for column in inspector.get_columns('users')}
    if 'discord_webhook_url' in columns:
        with op.batch_alter_table('users') as batch_op:
            batch_op.drop_column('discord_webhook_url')
