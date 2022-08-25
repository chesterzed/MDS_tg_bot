from peewee import Model, MySQLDatabase


db = MySQLDatabase(
     host="5.23.53.158",
     # host="172.16.16.4",
     user="gen_user",
     passwd="mgx37gvw66",
     database="default_db",
     port=3306
)


class BaseModel(Model):

    class Meta:
        database = db
