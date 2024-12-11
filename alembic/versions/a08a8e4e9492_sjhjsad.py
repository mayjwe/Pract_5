"""sjhjsad

Revision ID: a08a8e4e9492
Revises: c4a86394abc0
Create Date: 2024-12-11 13:54:02.138625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a08a8e4e9492'
down_revision: Union[str, None] = 'c4a86394abc0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
