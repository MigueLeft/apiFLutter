from sqlalchemy import create_engine, MetaData

con = create_engine("postgresql://apidb_owner:1hPpI5RaolKj@ep-cool-bird-a5r6w8n8.us-east-2.aws.neon.tech/apidb?sslmode=require")

meta = MetaData()

conn = con.connect()


