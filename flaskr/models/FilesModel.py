from database.conexion import get_connection
from .entities.Files import File

class FilesModel():
    @classmethod
    def get_file(self):
        try:
            conn = get_connection()
            files = []

            with conn.cursor() as cursor:
                cursor.execute("SELECT id, name, ext, description, create_at, create_by FROM file")
                resultset=cursor.fetchall()
                for row in resultset:
                    file=File(row[0], row[1], row[2], row[3], row[4], row[5])
                    files.append(file.to_json())
                    
            conn.close()
            return file

        except Exception as ex:
            raise Exception(ex)
    
  