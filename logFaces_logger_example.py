__author__    = 'Stojan Jovic <stojan.jovic@dmsgroup.rs>'
__contact__   = 'stojan.jovic@dmsgroup.rs'
__date__      = '04 February 2009'
__copyright__ = 'Copyright (c) 2008 DMS Group'

import socket
import logging
import xmllayout

# Adding custom debug levels (for example: TRACE, i.e. VERBOSE)
logging.VERBOSE = 5

logging._levelNames.update({
    5  : 'VERBOSE',
    
    'VERBOSE'     : 5
}) 

handler = xmllayout.RawSocketHandler('localhost', 55200)

# 1 - Set DOMAIN & HOST Through the __init__
#properties = xmllayout.properties.Log4jProperties(hostname=socket.gethostname(),
#                                                  application='TEST_DOMAIN')

# 2 - Set DOMAIN & HOST Through the SETTERS
#properties = xmllayout.properties.Log4jProperties()
#properties.set_hostname(socket.gethostname())
#properties.set_application('TEST_DOMAIN')

# 1 & 2
#handler.setFormatter(xmllayout.XMLLayout(properties))

# 3 - DEFAULT DOMAIN is used: no "Log4jProperties" instance
handler.setFormatter(xmllayout.XMLLayout())

logging.root.addHandler(handler)

# Now, define a couple of loggers which might represent areas in your
# application:
logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')
logger3 = logging.getLogger('myapp.area3')
# Default level is WARNING, if we want lower level, then:
logger1.setLevel(logging.DEBUG)
logger3.setLevel(logging.VERBOSE)

logger1.debug('logger1: DEBUG')
logger1.info('logger1: INFO')
logger1.warning('logger1: WARNING')
logger1.error('logger1: ERROR')
logger1.critical('logger1: CRITICAL (fatal)')

# logger2 doesn't send debug & info, because the level is deafult (WARNING)
logger2.debug('logger2: DEBUG')
logger2.info('logger2: INFO')
logger2.warning('logger2: WARNING')
logger2.error('logger2: ERROR')
logger2.critical('logger2: CRITICAL (fatal)')

# Using custom level(s) (i.e. logFaces TRACE level)
logger3.log(logging.VERBOSE, 'logger3: TRACE')
logger3.debug('logger3: DEBUG')
logger3.error('logger3: ERROR')

print "Logging FINISHED!"
