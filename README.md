# tf-multilabelloss

how to use tf-multilabelloss

```python
from multi_label_loss.multilabelloss import MultilabelLoss
predictions = Dense(len(num_class), activation="sigmoid")(x)
model = Model(inputs=base_model.input, outputs=predictions)
model.compile(optimizer='adam', loss=MultilabelLoss(num_class),metrics=['binary_accuracy'])
```
