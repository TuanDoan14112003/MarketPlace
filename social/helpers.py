import uuid
def get_filename(file,filename):
    post_id = file.post.id
    new_filename = str(uuid.uuid4()) + '_' + filename
    return f'post_files/{post_id}/{new_filename}'