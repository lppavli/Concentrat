"""Add tables

Revision ID: cce3f94d70ff
Revises: 
Create Date: 2022-07-19 12:43:42.638294

"""
import sqlmodel
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'cce3f94d70ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(),
                              nullable=False),
                    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(),
                              nullable=False),
                    sa.Column('views', sa.Integer(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('user',
                    sa.Column('uuid', sqlmodel.sql.sqltypes.AutoString(),
                              nullable=True),
                    sa.Column('username', sqlmodel.sql.sqltypes.AutoString(),
                              nullable=False),
                    sa.Column('password', sqlmodel.sql.sqltypes.AutoString(),
                              nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('is_superuser', sa.Boolean(), nullable=True),
                    sa.Column('is_totp_enabled', sa.Boolean(), nullable=True),
                    sa.Column('is_active', sa.Boolean(), nullable=True),
                    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(),
                              nullable=True),
                    sa.PrimaryKeyConstraint('uuid')
                    )
    op.create_table('material',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(),
                              nullable=False),
                    sa.Column('iron_amount', sa.Float(), default=0, nullable=True),
                    sa.Column('silicon_amount', sa.Float(), default=0, nullable=True),
                    sa.Column('aluminum_amount', sa.Float(), default=0, nullable=True),
                    sa.Column('sodium_amount', sa.Float(), default=0, nullable=True),
                    sa.Column('sulfur_amount', sa.Float(), default=0, nullable=True),
                    sa.Column('month', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('post')
    op.drop_table('materials')
    # ### end Alembic commands ###
