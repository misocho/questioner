import uuid
import os
from flask import current_app as app
import base64
from app.database.db_con import QuestionerDB


class UploadImage:
    """ contains methods for uploading an image """

    def saveToImage(self, meetup_id, imageFile=None):
        """ method for saving an image """

        query = """UPDATE meetups SET images = '{}' WHERE id = '{}' RETURNING *
        """.format(
            imageFile, meetup_id)

        return QuestionerDB.update(query)
