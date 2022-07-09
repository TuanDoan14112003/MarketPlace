import uuid
def get_filename(object,filename):
    try:
        id = object.post.id
    except AttributeError: 
        id = object.user.id
    new_filename = str(uuid.uuid4()) + '_' + filename
    return f'{object.root_folder}/{id}/{new_filename}'
