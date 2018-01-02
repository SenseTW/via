def gdrv_export_url(path):
  try:
    fileid = path.split("/")[6]
    return '/https://drive.google.com/uc?id={0}&export=download'.format(fileid)
  except:
    print(url)
    return url

class GDriverRequestSanitiser(object):

    """
    Use the url of real PDF file instead.
    """

    def __init__(self, application):
        self.application = application

    def __call__(self, environ, start_response):
        if 'drive.google.com/file' in environ['PATH_INFO']:
            new_env = environ.copy()
            new_env['PATH_INFO'] =  gdrv_export_url(environ['PATH_INFO'])
            new_env['REQUEST_URI'] =  gdrv_export_url(environ['PATH_INFO'])
            return self.application(new_env, start_response)
        else:
            return self.application(environ, start_response)