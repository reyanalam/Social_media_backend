"""add columns

Revision ID: 9be1c03fcc33
Revises: c0ce0e8789b5
Create Date: 2025-05-30 15:22:36.634377

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9be1c03fcc33'
down_revision: Union[str, None] = 'c0ce0e8789b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('post', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('post', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('post', 'published')
    op.drop_column('post', 'created_at')
    pass
