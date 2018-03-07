import ssl

from blog.app import app
from blog.config import (
    HOST,
    PORT,
    SSL_KEY,
    SSL_CERT,
    ENABLE_ACCESS_LOG,
)

if __name__ == "__main__":
    if SSL_KEY and SSL_CERT:
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        ssl_context.load_cert_chain(SSL_CERT, SSL_KEY)
    else:
        ssl_context = None

    app.run(host=HOST, port=PORT, ssl=ssl_context, access_log=ENABLE_ACCESS_LOG)
