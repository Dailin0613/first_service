from database.conexion import get_connection
from .entities.Content import Content

class ContentModel():
    @classmethod
    def get_content(self):
        try:
            conn = get_connection()
            contents = []

            with conn.cursor() as cursor:
                cursor.execute("SELECT id, content create_by FROM content")
                resultset=cursor.fetchall()

                for row in resultset:
                    content=Content(row[0], row[1])
                    contents.append(content.to_json())
            conn.close()
            return content
        except Exception as ex:
            raise Exception(ex)