import spacy
from google.cloud import translate_v2 as translate

# Initialize spaCy for English language processing
nlp = spacy.load("en_core_web_sm")

# Initialize Google Cloud Translation client
translate_client = translate.Client()

# Function to detect language and translate to English
def translate_to_english(text):
    # Detect the language of the input text
    detected_language = translate_client.detect_language(text)["language"]

    # Translate the text to English if it's not already in English
    if detected_language != "en":
        translation = translate_client.translate(text, target_language="en")
        return translation["translatedText"]
    else:
        return text

# Function to handle different commands
def handle_command(command):
    # Preprocess the command by translating it to English
    command_english = translate_to_english(command)

    # Perform any additional processing on the command as needed
    # For example, you can use spaCy for language understanding and reply generation
    doc = nlp(command_english)

    # Example logic: respond based on the detected verbs
    verbs = [token.text for token in doc if token.pos_ == "VERB"]
    if "greet" in verbs:
        return "Hello! How can I help you?"
    elif "leave" in verbs:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that command."

# Main function to listen for commands and respond
def main():
    print("Welcome! I'm here to assist you.")
    print("You can ask me questions or give me commands in any language.")

    while True:
        user_input = input("Your command: ")
        response = handle_command(user_input)
        print(response)

if __name__ == "__main__":
    main()
