import sys

from Logger import logging

def Error_message(error, error_detail):

    error_detail = sys.exc_info()

    _,_, exc_tbh = error_detail

    filename_excp = exc_tbh.tb_frame.f_code.co_filename

    line_num_excp = exc_tbh.tb_lineno

    error_message = 'The error is in the file [{0}] line number [{1}] and the error detail: [{2}]'.format(filename_excp, line_num_excp, str(error))

    return error_message

class MyCustomException(Exception):

    '''
    
    '''

    def __init__(self, error_message, error_detail = sys.exc_info()):

        super().__init__(self.error_message)

        self.error_message = Error_message(error_message, error_detail)

    def __str__(self):
        return super().__str__()

