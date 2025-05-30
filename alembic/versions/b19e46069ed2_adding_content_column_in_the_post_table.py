"""adding content column in the post table

Revision ID: b19e46069ed2
Revises: 7db65f71f9e3
Create Date: 2025-05-30 14:59:29.526646

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b19e46069ed2'
down_revision: Union[str, None] = '7db65f71f9e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('post', sa.Column('content', sa.String(), nullable=False, server_default=''))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('post', 'content')
    pass
