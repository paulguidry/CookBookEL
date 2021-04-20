import sys
import os

if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

try:
    import ConstantUtil as cu
except ModuleNotFoundError as mnfe:
    from CookBookEL import ConstantUtil as cu


class HTTP_RESTFULL_STATUS_CODES(cu.Const):
    """
    1xx: Informational – Communicates transfer protocol-level information.
    2xx: Success – Indicates that the client’s request was accepted successfully.
    3xx: Redirection – Indicates that the client must take some additional action in order to complete their request.
    4xx: Client Error – This category of error status codes points the finger at clients.
    5xx: Server Error – The server takes responsibility for these error status codes.
    """

    NOT_SET = -999
    EXIT_OS_OK = 0
    EXIT_OS_ERROR1 = 1
    EXIT_OS_ERROR2 = 2
    EXIT_OS_ERROR3 = 3

    # 1xx: Informational – Communicates transfer protocol-level information.
    CONTINUE: int = 100
    SWITCHING_PROTOCOL: int = 101
    PROCESSING: int = 102
    EARLY_HINTS: int = 103

    # 2xx: Success – Indicates that the client’s request was accepted successfully.
    OK: int = 200
    CREATED: int = 201
    ACCEPTED: int = 202
    NON_AUTHORITATIVE_INFO: int = 203
    NO_CONTENT: int = 204

    # 3xx: Redirection – Indicates that the client must take some additional action in order to complete their request.
    MULTIPLE_CHOICES: int = 300
    MOVED_PERMANENTLY: int = 301
    FOUND: int = 302
    SEE_OTHER: int = 303
    NOT_MODIFIED: int = 304
    TEMPORARY_REDIRECT: int = 307

    # 4xx: Client Error – This category of error status codes points the finger at clients.
    BAD_REQUEST: int = 400
    UNAUTHORIZED: int = 401
    FORBIDDEN: int = 403
    NOT_FOUND: int = 404
    METHOD_NOT_ALLOWED: int = 405
    NOT_ACCEPTABLE: int = 406
    PRECONDITION_FAILED: int = 412
    UNSUPPORTED_MEDIA_TYPE: int = 415

    ASSERTION_ERROR: int = 450

    # 5xx: Server Error – The server takes responsibility for these error status codes.
    INTERNAL_SERVER_ERROR: int = 500
    NOT_IMPLEMENTED: int = 501
    TRAPPED_UNEXPECTED_ERROR: int = 550


    SUCCESS_STATUS_CODE_LIST: [] = [EXIT_OS_OK, CONTINUE,
                                    PROCESSING, EARLY_HINTS,
                                    OK, CREATED, ACCEPTED, NON_AUTHORITATIVE_INFO, NO_CONTENT]

    WARNING_STATUS_CODE_LIST: [] = [NOT_SET,
                                    SWITCHING_PROTOCOL,
                                    FOUND, SEE_OTHER, NOT_MODIFIED, TEMPORARY_REDIRECT]

    ERROR_STATUS_CODES: [] = [EXIT_OS_ERROR1, EXIT_OS_ERROR2, EXIT_OS_ERROR3,
                         MULTIPLE_CHOICES, MOVED_PERMANENTLY,
                         BAD_REQUEST, UNAUTHORIZED, FORBIDDEN, NOT_FOUND, METHOD_NOT_ALLOWED, NOT_ACCEPTABLE,
                         PRECONDITION_FAILED, UNSUPPORTED_MEDIA_TYPE, PRECONDITION_FAILED, UNSUPPORTED_MEDIA_TYPE,
                         ASSERTION_ERROR]


    @classmethod
    def IsSuccessFUll(cls,
                      p_status_code: int) -> bool:
        return p_status_code in HTTP_RESTFULL_STATUS_CODES.SUCCESS_STATUS_CODE_LIST


    @classmethod
    def IsWarning(cls,
                  p_status_code: int) -> bool:
        return p_status_code in HTTP_RESTFULL_STATUS_CODES.WARNING_STATUS_CODE_LIST


    @classmethod
    def IsError(cls,
                p_status_code: int) -> bool:
        return p_status_code in HTTP_RESTFULL_STATUS_CODES.ERROR_STATUS_CODES


    @classmethod
    def NameForLevelID(cls, p_level_id: int) -> str:

        name_for_level_id: str = 'NOTSET'

        ID_TO_NAME = \
                {HTTP_RESTFULL_STATUS_CODES.NOT_SET: 'NOT_SET',
                 HTTP_RESTFULL_STATUS_CODES.EXIT_OS_OK: 'EXIT_OS_OK',
                 HTTP_RESTFULL_STATUS_CODES.EXIT_OS_ERROR1: 'EXIT_OS_ERROR1',
                 HTTP_RESTFULL_STATUS_CODES.EXIT_OS_ERROR2: 'EXIT_OS_ERROR2',
                 HTTP_RESTFULL_STATUS_CODES.EXIT_OS_ERROR3: 'EXIT_OS_ERROR3',
                 # 1xx: Informational – Communicates transfer protocol-level information.
                 HTTP_RESTFULL_STATUS_CODES.CONTINUE: 'CONTINUE',
                 HTTP_RESTFULL_STATUS_CODES.SWITCHING_PROTOCOL: 'SWITCHING_PROTOCOL',
                 HTTP_RESTFULL_STATUS_CODES.PROCESSING: 'PROCESSING',
                 HTTP_RESTFULL_STATUS_CODES.EARLY_HINTS: 'EARLY_HINTS',
                 # 2xx: Success – Indicates that the client’s request was accepted successfully.
                 HTTP_RESTFULL_STATUS_CODES.OK: 'OK',
                 HTTP_RESTFULL_STATUS_CODES.CREATED: 'CREATED',
                 HTTP_RESTFULL_STATUS_CODES.ACCEPTED: 'ACCEPTED',
                 HTTP_RESTFULL_STATUS_CODES.NON_AUTHORITATIVE_INFO:'NON_AUTHORITATIVE_INFO',
                 HTTP_RESTFULL_STATUS_CODES.NO_CONTENT: 'NO_CONTENT',
                 # 3xx: Redirection – Indicates that the client must take some additional action
                 # in order to complete their request.
                 HTTP_RESTFULL_STATUS_CODES.MULTIPLE_CHOICES: 'MULTIPLE_CHOICES',
                 HTTP_RESTFULL_STATUS_CODES.MOVED_PERMANENTLY: 'MOVED_PERMANENTLY',
                 HTTP_RESTFULL_STATUS_CODES.FOUND: 'FOUND',
                 HTTP_RESTFULL_STATUS_CODES.SEE_OTHER: 'SEE_OTHER',
                 HTTP_RESTFULL_STATUS_CODES.NOT_MODIFIED: 'NOT_MODIFIED',
                 HTTP_RESTFULL_STATUS_CODES.TEMPORARY_REDIRECT: 'TEMPORARY_REDIRECT',
                 # 4xx: Client Error – This category of error status codes points the finger at clients.
                 HTTP_RESTFULL_STATUS_CODES.BAD_REQUEST: 'BAD_REQUEST',
                 HTTP_RESTFULL_STATUS_CODES.UNAUTHORIZED: 'UNAUTHORIZED',
                 HTTP_RESTFULL_STATUS_CODES.FORBIDDEN: 'FORBIDDEN',
                 HTTP_RESTFULL_STATUS_CODES.NOT_FOUND: 'NOT_FOUND',
                 HTTP_RESTFULL_STATUS_CODES.METHOD_NOT_ALLOWED: 'METHOD_NOT_ALLOWED',
                 HTTP_RESTFULL_STATUS_CODES.NOT_ACCEPTABLE: 'NOT_ACCEPTABLE',
                 HTTP_RESTFULL_STATUS_CODES.PRECONDITION_FAILED: 'PRECONDITION_FAILED',
                 HTTP_RESTFULL_STATUS_CODES.UNSUPPORTED_MEDIA_TYPE: 'UNSUPPORTED_MEDIA_TYPE',
                 HTTP_RESTFULL_STATUS_CODES.ASSERTION_ERROR: 'ASSERTION_ERROR',
                 # 5xx: Server Error – The server takes responsibility for these error status codes.
                 HTTP_RESTFULL_STATUS_CODES.INTERNAL_SERVER_ERROR: 'INTERNAL_SERVER_ERROR',
                 HTTP_RESTFULL_STATUS_CODES.NOT_IMPLEMENTED: 'NOT_IMPLEMENTED',
                 HTTP_RESTFULL_STATUS_CODES.TRAPPED_UNEXPECTED_ERROR: 'TRAPPED_UNEXPECTED_ERROR'}

        try:
            name_for_level_id = ID_TO_NAME[p_level_id]
        except Exception as e:
            print("Logging error in NameForLevelID!:{}", e)

        return name_for_level_id


    @classmethod
    def CONSTANT_VALUE_LIST(cls):
        return [# < 100 are os error codes
                cls.NOT_SET,
                cls.EXIT_OS_OK,
                cls.EXIT_OS_ERROR1,
                cls.EXIT_OS_ERROR2,
                cls.EXIT_OS_ERROR3,
                # 1xx: Informational – Communicates transfer protocol-level information.
                cls.CONTINUE,
                cls.SWITCHING_PROTOCOL,
                cls.PROCESSING,
                cls.EARLY_HINTS,
                # 2xx: Success – Indicates that the client’s request was accepted successfully.
                cls.OK,
                cls.CREATED,
                cls.ACCEPTED,
                cls.NON_AUTHORITATIVE_INFO,
                cls.NO_CONTENT,
                # 3xx: Redirection – Indicates that the client must take some additional action in order to
                # complete their request.
                cls.MULTIPLE_CHOICES,
                cls.MOVED_PERMANENTLY,
                cls.FOUND,
                cls.SEE_OTHER,
                cls.NOT_MODIFIED,
                cls.TEMPORARY_REDIRECT,
                # 4xx: Client Error – This category of error status codes points the finger at clients.
                cls.BAD_REQUEST,
                cls.UNAUTHORIZED,
                cls.FORBIDDEN,
                cls.NOT_FOUND,
                cls.METHOD_NOT_ALLOWED,
                cls.NOT_ACCEPTABLE,
                cls.PRECONDITION_FAILED,
                cls.UNSUPPORTED_MEDIA_TYPE,
                cls.ASSERTION_ERROR,
                # 5xx: Server Error – The server takes responsibility for these error status codes.
                cls.INTERNAL_SERVER_ERROR,
                cls.NOT_IMPLEMENTED,
                cls.TRAPPED_UNEXPECTED_ERROR]

    @classmethod
    def CONSTANT_NAME_LIST(cls):
        return [# < 100 are os error codes
                'NOT_SET',
                'EXIT_OS_OK',
                'EXIT_OS_ERROR1',
                'EXIT_OS_ERROR2',
                'EXIT_OS_ERROR3',
                # 1xx: Informational – Communicates transfer protocol-level information.
                'CONTINUE',
                'SWITCHING_PROTOCOL',
                'PROCESSING',
                'EARLY_HINTS',
                # 2xx: Success – Indicates that the client’s request was accepted successfully.
                'OK',
                'CREATED',
                'ACCEPTED',
                'NON_AUTHORITATIVE_INFO',
                'NO_CONTENT',
                # 3xx: Redirection – Indicates that the client must take some additional action
                # in order to complete their request.
                'MULTIPLE_CHOICES',
                'MOVED_PERMANENTLY',
                'FOUND',
                'SEE_OTHER',
                'NOT_MODIFIED',
                'TEMPORARY_REDIRECT',
                # 4xx: Client Error – This category of error status codes points the finger at clients.
                'BAD_REQUEST',
                'UNAUTHORIZED',
                'FORBIDDEN',
                'NOT_FOUND',
                'METHOD_NOT_ALLOWED',
                'NOT_ACCEPTABLE',
                'PRECONDITION_FAILED',
                'UNSUPPORTED_MEDIA_TYPE',
                'ASSERTION_ERROR',
                # 5xx: Server Error – The server takes responsibility for these error status codes.
                'INTERNAL_SERVER_ERROR',
                'NOT_IMPLEMENTED',
                'TRAPPED_UNEXPECTED_ERROR']





class HTTP_RESTFULL_STATUS_DESC:

    # < 100 are os error codes
    NOT_SET: str = "If this is returned, No Message Set by handler!: " \
                    "THis is an internal tag reserved to indicate No Status was set!"

    EXIT_OS_OK: str = "OK exit status from a terminal program: " \
                      "On shell programs exit status 0 means no error! "

    EXIT_OS_ERROR1: str = "Custom error exit status 1 from a terminal program: " \
                          "On shell programs exit status 1 is reserved for a custom error! "

    EXIT_OS_ERROR2: str = "Custom error exit status 2 from a terminal program: " \
                          "On shell programs exit status 2 is reserved for a custom error! "

    EXIT_OS_ERROR3: str = "Custom error exit status 3 from a terminal program: " \
                          "On shell programs exit status 3 is reserved for a custom error! "



    """
    1xx: Informational – Communicates transfer protocol-level information.
    2xx: Success – Indicates that the client’s request was accepted successfully.
    3xx: Redirection – Indicates that the client must take some additional action in order to complete their request.
    4xx: Client Error – This category of error status codes points the finger at clients.
    5xx: Server Error – The server takes responsibility for these error status codes.
    """

    # 1xx: Informational – Communicates transfer protocol-level information.

    CONTINUE: str = \
        "Request Received But Has Not Started: " \
        "An interim response. Indicates the client that the initial part of the request has been" \
        "received and has not yet been rejected by the server." \
        "The client SHOULD continue by sending the remainder of the request or, " \
        "if the request has already been completed, ignore this response. " \
        "The server MUST send a final response after the request has been completed. "

    SWITCHING_PROTOCOL: str = \
        "Process In Transition: " \
        "Sent in response to an Upgrade request header from the client, and " \
        "indicates the protocol the server is switching to."

    PROCESSING: str = \
        "Request Received And Is Processing: "\
        "Indicates that the server has received and is processing the request, but no response is available yet."

    EARLY_HINTS: str = \
        "Request Finishing And Preparing Response: " \
        "Primarily intended to be used with the Link header. " \
        "It suggests the user agent start preloading the resources while the server prepares a final response."



    # 2xx: Success – Indicates that the client’s request was accepted successfully.

    OK: str = \
        "Requested Process Completed Successfully And Data Returned: " \
        "Indicates that the REST API successfully carried out whatever action the client " \
        "requested and that no more specific code in the 2xx series is appropriate."

    CREATED: str = \
        "The Requested Resource Was Created: " \
        "inside a collection.There may also be times when a new resource is created as a result of some " \
        "controller action, in which case 201 would also be an appropriate response."

    ACCEPTED: str = \
        "Requested Resource Was Accepted And Is Processing: "\
        "A 202 response is typically used for actions that take a long while to process. " \
        "It indicates that the request has been accepted for processing, but the processing has not been completed. "\
        "The request might or might not be eventually acted upon, or even maybe disallowed when processing occurs."

    NON_AUTHORITATIVE_INFO: str = \
        "Request Was Accepted And Is Being Processed By An External Service: "\
        "A third party service is processing the request with no further information."

    NO_CONTENT: str = \
        "Requested Process Completed Successfully With NO Data Returned: " \
        "An API may also send 204 in conjunction with a GET request to indicate that " \
        "the requested resource exists, but has no state representation to include in the body."



    # 3xx: Redirection – Indicates that the client must take some additional action in order to complete their request.

    MULTIPLE_CHOICES: str = \
        "Not Enough Information To For Fill Request: " \
        "Not enough information to process request or there are too many choices and not enough " \
        "Information to choose one."

    MOVED_PERMANENTLY: str = \
        "An expected dependent API or method signature changed: " \
        "Indicates that the REST API’s resource model has been significantly redesigned, and a new permanent " \
        "URI has been assigned to the client’s requested resource. The REST API should specify the new URI " \
        "in the response’s Location header, and all future requests should be directed to the given URI"

    FOUND: str = \
        "A Redirect To Another Service Was Performed: " \
        "The HTTP response status code 302 Found is a common way of performing URL redirection. " \
        "An HTTP response with this status code will additionally provide a URL in the Location header field. " \
        "The user agent (e.g., a web browser) is invited by a response with this code to make a second. " \
        "Otherwise identical, request to the new URL specified in the location field."


    SEE_OTHER: str = \
        "Request Completed Then A Redirect To Another Service Was Performed: " \
        "A service has finished its work, but instead of sending a potentially unwanted response body, " \
        "it sends the client the URI of a response resource. The response can be the URI of the temporary status "\
        "message, or the URI to some already existing, more permanent, resource. Generally speaking, " \
        "the 303 status code allows a REST API to send a reference to a resource without forcing the client "\
        "to download its state. Instead, the client may send a GET request to the value of the Location header."

    NOT_MODIFIED: str = \
        "Request of Service Not Performed Because It Was Already Performed: " \
        "This status code is similar to 204 (“No Content”) in that the response body must be empty. " \
        "The critical distinction is that 204 is used when there is nothing to send in the body, " \
        "whereas 304 is used when the resource has not been modified since the version specified by " \
        "the request headers If-Modified-Since or If-None-Match."

    TEMPORARY_REDIRECT: str = \
        "Request of Service Temporarily Denied. With alternative returned." \
        "A REST API can use this status code to assign a temporary URI to the client’s requested resource. " \
        " For example, a 307 response can be used to shift a client request over to another host. " \
        "The temporary URI SHOULD be given by the Location field in the response. Unless the request method was HEAD, " \
        "the entity of the response SHOULD contain a short hypertext note with a hyperlink to the new URI(s). " \
        "If the 307 status code is received in response to a request other than GET or HEAD, the user " \
        "agent MUST NOT automatically redirect the request unless it can be confirmed by the user, " \
        "since this might change the conditions under which the request was issued."



    # 4xx: Client Error – This category of error status codes points the finger at clients.
    BAD_REQUEST: str = \
        "Generic User Error Status: " \
        "400 is the generic client-side error status, used when no other 4xx error code is appropriate. " \
        "Errors can be like malformed request syntax, invalid request message parameters, " \
        "or deceptive request routing etc."

    UNAUTHORIZED: str = \
        "Client Unauthorized To Use PROTECTED Service:" \
        "User tried to operate on a protected resource without providing the proper authorization. It may have " \
        "provided the wrong credentials or none at all. The response must include a WWW-Authenticate header " \
        "field containing a challenge applicable to the requested resource."

    FORBIDDEN: str = \
        "Client Unotherized To Use Service:" \
        "A 403 error response indicates that the client’s request is formed correctly, but the REST API refuses " \
        "to honor it, i.e., the user does not have the necessary permissions for the resource. " \
        "A 403 response is not a case of insufficient client credentials; that would be 401 (“Unauthorized”)."

    NOT_FOUND: str = \
        "Endpoint Can Not Be Found: "\
        " The 404 error status code indicates that the REST API can’t map the client’s URI to a resource but " \
        " may be available in the future. Subsequent requests by the client are permissible. No indication is " \
        " given of whether " \
        " the condition is temporary or permanent. The 410 (Gone) status code SHOULD be used if the server knows, " \
        "through some internally configurable mechanism, that an old resource is permanently unavailable " \
        "and has no forwarding address. This status code is commonly used when the server does not wish to reveal " \
        "exactly why the request has been refused, or when no other response is applicable."

    METHOD_NOT_ALLOWED: str = \
        "Invalid Request Type: " \
        "The API responds with a 405 error to indicate that the client tried to use an HTTP method that the " \
        "resource does not allow. For instance, a read-only resource could support only GET and HEAD, " \
        "while a controller resource might allow GET and POST, but not PUT or DELETE."

    NOT_ACCEPTABLE: str = \
        "Request Cannot Be Performed Or Returned The Way Requested: " \
        "preferred media types, as indicated by the Accept request header. " \
        "For example, a client request for data formatted as application/xml will " \
        "receive a 406 response if the API is only willing to format data as application/json."

    PRECONDITION_FAILED: str = \
        "An Assumed Precondition Was Not Met Before Service Requested: " \
        "The 412 error response indicates that the client specified one or more preconditions " \
        " in its request headers, effectively telling the REST API to carry out its request only " \
        "if certain conditions were met. A 412 response indicates that those conditions were not met, "\
        "so instead of carrying out the request, the API sends this status code."

    UNSUPPORTED_MEDIA_TYPE: str = \
        "Format Of Input Parameters Cannot Be Processed: " \
        " indicates that the API is not able to process the client’s supplied media type, " \
        " as indicated by the Content-Type request header. For example, a client request " \
        " including data formatted as application/xml will receive a 415 response if the API " \
        " is only willing to process data formatted as application/json."

    ASSERTION_ERROR: str = \
        "Program Code expected a specified condition that failed: " \
        "This happens when the coder added a logical statement to confirm a specific condition and it failed."

    # 5xx: Server Error – The server takes responsibility for these error status codes.
    INTERNAL_SERVER_ERROR: str = \
        "Generic Unexpected REST API Internal Error: " \
        " A Unexpected Unhandled Server Error. A 500 error is never the client’s fault, and therefore, " \
        " it is reasonable for the client to retry the same request that triggered this response and " \
        " hope to get a different response. The API response is the generic error message, given when an " \
        " unexpected condition was encountered and no more specific message is suitable."


    NOT_IMPLEMENTED: str = \
        "The server either does not recognize the request method, or it cannot fulfill the request. " \
        "Usually, this implies future availability (e.g., a new feature of a web-service API)."

    TRAPPED_UNEXPECTED_ERROR: str = \
        "A programmatic or system error occurred unexpectedly, but was handled: " \
        "THis error happens for some unknown reason and usually needs "



    @classmethod
    def SHORT_DESC(cls, p_desc) -> str:
        return p_desc.split(':')[0]



    @classmethod
    def LONG_DESC(cls, p_desc) -> str:
        return p_desc.split(':')[1]



    @classmethod
    def CONSTANT_NAME_LIST(cls):
        return ['NOT_SET',
                'EXIT_OS_OK',
                'EXIT_OS_ERROR1',
                'EXIT_OS_ERROR2',
                'EXIT_OS_ERROR3',
                # 1xx: Informational – Communicates transfer protocol-level information.
                'CONTINUE',
                'SWITCHING_PROTOCOL',
                'PROCESSING',
                'EARLY_HINTS',
                # 2xx: Success – Indicates that the client’s request was accepted successfully.
                'OK',
                'CREATED',
                'ACCEPTED',
                'NON_AUTHORITATIVE_INFO',
                'NO_CONTENT',
                # 3xx: Redirection – Indicates that the client must take some additional action in order to complete their request.
                'MULTIPLE_CHOICES',
                'MOVED_PERMANENTLY',
                'FOUND',
                'SEE_OTHER',
                'NOT_MODIFIED',
                'TEMPORARY_REDIRECT',
                # 4xx: Client Error – This category of error status codes points the finger at clients.
                'BAD_REQUEST',
                'UNAUTHORIZED',
                'FORBIDDEN',
                'NOT_FOUND',
                'METHOD_NOT_ALLOWED',
                'NOT_ACCEPTABLE',
                'PRECONDITION_FAILED',
                'UNSUPPORTED_MEDIA_TYPE',
                'ASSERTION_ERROR',
                # 5xx: Server Error – The server takes responsibility for these error status codes.
                'INTERNAL_SERVER_ERROR',
                'NOT_IMPLEMENTED'
                'TRAPPED_UNEXPECTED_ERROR']


    @classmethod
    def CONSTANT_VALUE_LIST(cls):
        return [HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.NOT_SET),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.EXIT_OS_OK),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.EXIT_OS_ERROR1),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.EXIT_OS_ERROR2),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.EXIT_OS_ERROR3),
                 # 1xx: Informational – Communicates transfer protocol-level information.
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.CONTINUE),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.SWITCHING_PROTOCOL),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.PROCESSING),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.EARLY_HINTS),
                # 2xx: Success – Indicates that the client’s request was accepted successfully.
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.OK),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.CREATED),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.ACCEPTED),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.NON_AUTHORITATIVE_INFO),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.NO_CONTENT),
                # 3xx: Redirection – Indicates that the client must take some additional action in order to complete their request.
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.MULTIPLE_CHOICES),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.MOVED_PERMANENTLY),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.FOUND),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.SEE_OTHER),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.NOT_MODIFIED),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.TEMPORARY_REDIRECT),
                # 4xx: Client Error – This category of error status codes points the finger at clients.
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.BAD_REQUEST),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.UNAUTHORIZED),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.FORBIDDEN),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.NOT_FOUND),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.METHOD_NOT_ALLOWED),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.NOT_ACCEPTABLE),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.PRECONDITION_FAILED),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.UNSUPPORTED_MEDIA_TYPE),
                # 5xx: Server Error – The server takes responsibility for these error status codes.
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.INTERNAL_SERVER_ERROR),
                HTTP_RESTFULL_STATUS_DESC.SHORT_DESC(cls.NOT_IMPLEMENTED)]