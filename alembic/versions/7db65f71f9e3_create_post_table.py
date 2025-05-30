"""create post table

Revision ID: 7db65f71f9e3
Revises: 
Create Date: 2025-05-30 12:16:02.847610

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7db65f71f9e3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'post',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('title', sa.String(), nullable=False)
    )
    

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('post')
    pass
