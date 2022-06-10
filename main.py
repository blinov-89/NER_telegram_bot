from telegram.ext import Updater, Filters, CommandHandler, MessageHandler
from transformers import pipeline

# load model
model_checkpoint = "./saved_model"
token_classifier = pipeline("token-classification", model=model_checkpoint, aggregation_strategy="simple")


def start(updater, context):
    updater.message.reply_text("Добро пожаловать в телеграм бот по распознованию сущностей из текста новостей")


def help_(updater, context):
    updater.message.reply_text("Отправь текст")


def message(updater, context):
    text = updater.message.text
    answer = token_classifier(text)
    updater.message.reply_text(str(answer))


with open("C:/Users/Dmitry/OneDrive/Рабочий стол/TOKEN_NER.txt", "r") as valuesFile:
    TOKEN = valuesFile.readlines()


def main():
    updater = Updater(TOKEN[0])
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_))
    dispatcher.add_handler(MessageHandler(Filters.text, message))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

# вариант 2
# ru_label_names = ['O', 'I-AGE', 'B-AGE', 'B-AWARD', 'I-AWARD', 'B-CITY', 'I-CITY', 'B-COUNTRY', 'I-COUNTRY', 'B-CRIME', 'I-CRIME', 'B-DATE', 'I-DATE', 'B-DISEASE', 'I-DISEASE', 'B-DISTRICT', 'I-DISTRICT', 'B-EVENT', 'I-EVENT', 'B-FACILITY', 'I-FACILITY', 'B-FAMILY', 'I-FAMILY', 'B-IDEOLOGY', 'I-IDEOLOGY', 'B-LANGUAGE', 'I-LAW', 'B-LAW', 'B-LOCATION', 'I-LOCATION', 'B-MONEY', 'I-MONEY', 'B-NATIONALITY', 'I-NATIONALITY', 'B-NUMBER', 'I-NUMBER', 'B-ORDINAL', 'I-ORDINAL', 'B-ORGANIZATION', 'I-ORGANIZATION', 'B-PENALTY', 'I-PENALTY', 'B-PERCENT', 'I-PERCENT', 'B-PERSON', 'I-PERSON', 'I-PRODUCT', 'B-PRODUCT', 'B-PROFESSION', 'I-PROFESSION', 'B-RELIGION', 'I-RELIGION', 'B-STATE_OR_PROVINCE', 'I-STATE_OR_PROVINCE', 'B-TIME', 'I-TIME', 'B-WORK_OF_ART', 'I-WORK_OF_ART']
#
# test_model = AutoModelForTokenClassification.from_pretrained("./saved_model_3", num_labels=len(ru_label_names))
# ru_tokenizer = AutoTokenizer.from_pretrained("DeepPavlov/rubert-base-cased")
# test_nerpipeline = pipeline('ner', model=test_model, tokenizer=ru_tokenizer)
# test_text = "Новым послом Южной Кореи в России стал бывший посол в Камбодже Чан Хо Чжин, передает Yonhap."
# print(test_nerpipeline(test_text))
