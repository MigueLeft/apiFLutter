from sqlalchemy import create_engine, MetaData

con = create_engine("postgresql://flutte-api_owner:hH1usBJcg5Fr@ep-calm-recipe-a56ir9p3.us-east-2.aws.neon.tech/flutte-api?sslmode=require")

meta = MetaData()

conn = con.connect()


