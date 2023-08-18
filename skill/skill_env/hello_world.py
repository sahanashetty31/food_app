from ask_sdk_core.skill_builder import SkillBuilder
sb = SkillBuilder()

#The following code example shows how to configure a handler to be invoked when the skill receives a LaunchRequest.
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        #type: (HandlerInput) -> bool
        return  is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        #type: (HandlerInput) -> Response
        speech_text = "Welcome to the Alexa Skills Kit, you can say hello!"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Hello World", speech_text)).set.should_end_session(False)
        return handler_input.response_builder.response

#The following code example shows how to configure a handler to be invoked when the skill receives an intent request with the name HelloWorldIntent
class HelloWorldIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        #type: (HandlerInput) -> bool
        return is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        #type: (HandlerInput) -> Response
        speech_text = "Hello World"

        handler_input.response_builder.speak(speech_text).set_card(SimpleCard("Hello World", speech_text)).set_should_end_session(True)
        return handler_input.response_builder.response

#The following code example shows how to configure a handler to be invoked when the skill receives the built-in intent AMAZON.HelpIntent.

class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        #type:(HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        #type: (HandlerInput) -> Response
        speech_text = "You can say hello to me!"

        handler_input.response_builder.speak(speech_text).ask(speech_text).set_card(
            SimpleCard("Hello World", speech_text))
        return handler_input.response_builder.response

#The CancelAndStopIntentHandler is similar to the HelpIntent handler, as it is also triggered by the built-In AMAZON.CancelIntent or AMAZON.StopIntent Intents. The following example uses a single handler to respond to both intents.

class CancelAndStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        #type:(HandlerInput) -> bool
        return is_intent_name("AMAZON.CancelIntent")(handler_input) or is_intent_name("AMAZON.StopIntent")(handler_input)

    def handle(self, handler_input):
        #type: (HandlerInput) -> Response
        speech_text = "Goodbye"

        handler_input.response_builder.speak(speech_text).ask(speech_text).set_card(
            SimpleCard("Hello World", speech_text)).set_should_end_session(True)
        return handler_input.response_builder.response

# Although you cannot return a response with any speech, card or directives after receiving a SessionEndedRequest, the SessionEndedRequestHandler is a good place to put your cleanup logic.

class SessionEndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("SessionEndRequest")(handler_input)


    def handle(self, handler_input):
        #type:(HandlerInput)->Response
        #any cleanup logic goes here

        return handler_input.response_builder.response

#The following sample adds a catch all exception handler to your skill, to ensure the skill returns a meaningful message for all exceptions.

from ask_sdk.core.dispatch_components import AbstractExceptionHandler

class AllExceptionHandler(AbstractExceptionHandler):

    def can_handle(self, handler_input, exception):
        #type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        #Log the exception in CloudWatch Logs
        print(exception)

        speech = "Sorry, I didn't get it. Can you please say it again!!"
        handler_input.response_builder.speak(speech).ask(speech)
        return handler_input.response_builder.response


sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelAndStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_exception_handler(AllExceptionHandler())

handler = sb.lambda_handler()
