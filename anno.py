from presidio_analyzer import AnalyzerEngine, PatternRecognizer
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig
import json

# Set up analyzers and recognizers (do this once, outside the handler for efficiency)
analyzer = AnalyzerEngine()
titles_recognizer = PatternRecognizer(supported_entity="TITLE", deny_list=["Mr.","Mrs.","Miss"])
pronoun_recognizer = PatternRecognizer(supported_entity="PRONOUN", deny_list=["he", "He", "his", "His", "she", "She", "hers", "Hers"])
analyzer.registry.add_recognizer(titles_recognizer)
analyzer.registry.add_recognizer(pronoun_recognizer)
anonymizer = AnonymizerEngine()

def lambda_handler(event, context):
    # Get the text to anonymize from the event
    text_to_anonymize = event.get("text", "")

    print('text_to_anonymize', text_to_anonymize)

    # Analyze for all entities (including phone numbers)
    analyzer_results = analyzer.analyze(
        text=text_to_anonymize,
        language="en"
    )

    # Anonymize the text
    anonymized_results = anonymizer.anonymize(
        text=text_to_anonymize,
        analyzer_results=analyzer_results,
        operators={
            "DEFAULT": OperatorConfig("replace", {"new_value": "<ANONYMIZED PII>"}),
            "PHONE_NUMBER": OperatorConfig("mask", {"type": "mask", "masking_char": "*", "chars_to_mask": 12, "from_end": True}),
            "TITLE": OperatorConfig("replace", {"new_value": "<ANONYMIZED TITLE>"})
        }
    )

    # Prepare the response
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "anonymized_text": anonymized_results.text,
            "details": json.loads(anonymized_results.to_json())
        })
    }
    return response