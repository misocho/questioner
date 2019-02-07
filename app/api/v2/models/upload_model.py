import uuid
import os
from flask import current_app as app
import base64
from app.database.db_con import QuestionerDB


class UploadImage:
    """ contains methods for uploading an image """

    def saveToImage(self, meetup_id, imageFile=None, extension='.png'):
        """ method for saving an image """
        imageName = str(uuid.uuid4()) + extension
        imageDirectory = os.path.join(app.config.get('BASE_DIR'), 'static',
                                      'upload', 'image')

        if not os.path.isdir(imageDirectory):
            os.makedirs(imageDirectory)
        imageFile = imageFile.replace(
            'data:image/' + extension.split('.')[1] + ';base64,', '')
        imagePath = os.path.join(imageDirectory, imageName)
        image = open(imagePath, "wb")
        image.write(base64.b64decode(imageFile))
        image.close()

        query = """UPDATE meetups SET images = '{}' WHERE id = '{}' RETURNING * """.format(imagePath, meetup_id)

        return QuestionerDB.update(query)
