"""add foreign key

Revision ID: c0ce0e8789b5
Revises: 11f76ad60515
Create Date: 2025-05-30 15:11:18.120689

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0ce0e8789b5'
down_revision: Union[str, None] = '11f76ad60515'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('post', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(
        'fk_post_owner_id_users_id',
        'post',#source table,
        'users',#target table,
        ['owner_id'],#source columns,
        ['id'],#target columns,
        ondelete='CASCADE'
    )
    op.create_index('ix_post_owner_id', 'post', ['owner_id'], unique=False)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('fk_post_owner_id_users_id', 'post', type_='foreignkey')
    op.drop_column('post', 'owner_id')
    pass
