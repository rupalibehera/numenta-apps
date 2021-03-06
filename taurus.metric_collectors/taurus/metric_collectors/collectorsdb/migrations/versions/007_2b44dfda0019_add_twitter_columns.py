"""Add twitter columns and rename an incorrectly-named column ref_uid to
retweeted_userid

Revision ID: 2b44dfda0019
Revises: 4bd7cf179841
Create Date: 2015-02-01 14:27:37.035845

"""

# revision identifiers, used by Alembic.
revision = '2b44dfda0019'
down_revision = '4bd7cf179841'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # Rename incorrectly-named column
    op.alter_column('twitter_tweets', 'ref_uid',
                    new_column_name='retweeted_userid',
                    type_=mysql.VARCHAR(length=100),
                    existing_nullable=True,
                    existing_server_default=sa.text("NULL"))

    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('twitter_tweets', sa.Column('real_name', mysql.VARCHAR(length=100), nullable=True))
    op.add_column('twitter_tweets', sa.Column('retweeted_status_id', mysql.VARCHAR(length=40), server_default='', nullable=True))
    op.add_column('twitter_tweets', sa.Column('retweet_count', sa.INTEGER(), server_default='-2', autoincrement=False, nullable=True))
    op.add_column('twitter_tweets', sa.Column('retweeted_username', mysql.VARCHAR(length=100), server_default='', nullable=True))
    op.add_column('twitter_tweets', sa.Column('retweeted_real_name', mysql.VARCHAR(length=100), server_default='', nullable=True))
    op.add_column('twitter_tweets', sa.Column('in_reply_to_status_id', mysql.VARCHAR(length=40), server_default='', nullable=True))
    op.add_column('twitter_tweets', sa.Column('in_reply_to_userid', mysql.VARCHAR(length=100), server_default='', nullable=True))
    op.add_column('twitter_tweets', sa.Column('in_reply_to_username', mysql.VARCHAR(length=100), server_default='', nullable=True))
    op.add_column('twitter_tweets', sa.Column('contributors', mysql.TEXT(convert_unicode=True), nullable=True))
    ### end Alembic commands ###


def downgrade():
  raise NotImplementedError("Rollback is not supported.")
