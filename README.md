# NER_telegram_bot
ner

# Задачи распознования сущностей из текста, новостная лента

raw_dataset = load_dataset('surdan/nerel_short')

tokenizer = AutoTokenizer.from_pretrained("DeepPavlov/rubert-base-cased-sentence")

model = AutoModelForTokenClassification.from_pretrained("DeepPavlov/rubert-base-cased-sentence")

Epoc |	Training Loss |	Validation Loss |	Precision |	Recall |	F1 |	Accuracy
|----------------|:---------:|----------------:|----------------|:---------:|----------------:|----------------|
25 |	0.001300 |	0.895051 |	0.800244 |	0.792887 |	0.796548 |	0.900756

## Пример:

token_classifier("Отвечая на вопрос, кто принял решение о закрытии воздушного пространства Черногории для борта Лаврова, Кривокапич отметил, что формально решение принято правительством и министерством иностранных дел страны.")

# Результат
[{'end': 72,
  'entity_group': 'EVENT',
  'score': 0.99739176,
  'start': 40,
  'word': 'закрытии воздушного пространства'},
 {'end': 83,
  'entity_group': 'COUNTRY',
  'score': 0.9999255,
  'start': 73,
  'word': 'Черногории'},
 {'end': 101,
  'entity_group': 'PERSON',
  'score': 0.99571216,
  'start': 94,
  'word': 'Лаврова'},
 {'end': 113,
  'entity_group': 'PERSON',
  'score': 0.9998565,
  'start': 103,
  'word': 'Кривокапич'},
 {'end': 167,
  'entity_group': 'ORGANIZATION',
  'score': 0.9999411,
  'start': 153,
  'word': 'правительством'},
 {'end': 199,
  'entity_group': 'ORGANIZATION',
  'score': 0.9999304,
  'start': 170,
  'word': 'министерством иностранных дел'}]
  
  

![04](https://user-images.githubusercontent.com/61515881/209784337-d66d7ae5-eb6c-429a-a4ab-2a74e6077a0f.png)

![05](https://user-images.githubusercontent.com/61515881/209784347-7976d0b4-5076-493c-bf25-7ed41a824616.png)
