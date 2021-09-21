# tf-multilabelloss
Create a multilabelloss which can help as when we working on multilabel classification model. 
meaning of multilabel classification is that:- 

* develop a single model that will provide binary classification predictions for each of the num_class

* In other words it will predict 'positive' or 'negative' for all class.


how to use tf-multilabelloss

```python
from multi_label_loss.multilabelloss import MultilabelLoss
predictions = Dense(len(num_class), activation="sigmoid")(x)
model = Model(inputs=base_model.input, outputs=predictions)
model.compile(optimizer='adam', loss=MultilabelLoss(num_class),metrics=['binary_accuracy'])
```
## installation
```bash
pip install tf-multilabelloss
```
