from wtforms import StringField, IntegerField
from flask.ext.wtf import Form


class CreateInputForm(Form):
    book = StringField("Book")
    chapter = IntegerField("Chapter")
    verse = IntegerField("Verse")
    depth = IntegerField("Depth")