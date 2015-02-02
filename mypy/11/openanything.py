__author__ = 'yangbingxi'
import urllib2

class DefaultErrorHandler(urllib2.HTTPDefaultErrorHandler):
    def http_error_default(self, req, fp, code, msg, hdrs):
        result = urllib2.HTTPError(
            req.get_full_url(), code, msg, hdrs, fp
        )
        result .status = code
        return result


