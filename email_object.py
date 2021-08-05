import email

class EmailObject(object):

    CLRF = '\n\r\n\r'

    def __init__(self,file_io):
        self.file_io = file_io
        self.mail = email.message_from_file(self.file_io)

    def body(self):
        'Returns the payload of the mail as a string object.'
        # Get the payload of the body
        payload = self.mail.get_payload(decode=True)

        # At the moment we are treating non multipart email. So we will not check for multipart as of now. In later stages we could.
        # This isinstance function checks if the payload is an instance of type bytes, If it is we need to convert it to string.
        if isinstance(payload, bytes):
            decoded_parts = [payload.decode('utf-8', errors='ignore')]
        else:
            decoded_parts = [payload]
        

        return self.CLRF.join(decoded_parts)

    def somefunc():
        print('Hello')