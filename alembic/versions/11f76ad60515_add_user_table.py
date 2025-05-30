"""add user table

Revision ID: 11f76ad60515
Revises: b19e46069ed2
Create Date: 2025-05-30 15:07:13.117311

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '11f76ad60515'
down_revision: Union[str, None] = 'b19e46069ed2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False)
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('user')
    pass
