from flask import Blueprint
#Models
from models.FilesModel import FilesModel

main=Blueprint('file_mannage_blueprint', __name__)

@main.route('/')
def all_files():
    try:
        files = FilesModel.get_file()
        return jsonify(files)
    except Exception as ex:
        return jsonify({'message' : str(ex)}), 500