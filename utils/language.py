from utils.responses import responses


class LanguageDetector:
    responses = responses

    """ Language Detector class to detect language from Headers of Request in View """

    def detect_language(self):
        """ Method to detect language from Headers """

        lang = self.request.META.get('HTTP_ACCEPT_LANGUAGE').upper() \
            if self.request.META.get('HTTP_ACCEPT_LANGUAGE') \
            else 'UZ'

        if lang not in ['RU', 'UZ']:
            lang = 'UZ'

        return lang

    def get_response_message(self, key: str):
        """ Method to return response depending on language and key inserted as argument """
        return self.responses[self.detect_language()][key]
