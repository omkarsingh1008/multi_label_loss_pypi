## In multiple loss package you get two loass functions.
* multilabelloss.
* contrastiveloss.


# multilabelloss
Create a multilabelloss which can help as when we working on multilabel classification model. 
meaning of multilabel classification is that:- 

* develop a single model that will provide binary classification predictions for each of the num_class

* In other words it will predict 'positive' or 'negative' for all class.


how to use tf-multilabelloss

```python
from multiple_loss.multilabelloss import MultilabelLoss
predictions = Dense(len(num_class), activation="sigmoid")(x)
model = Model(inputs=base_model.input, outputs=predictions)
model.compile(optimizer='adam', loss=MultilabelLoss(num_class),metrics=['binary_accuracy'])
```
# contrastiveloss

contrastive loss function use when we are working on Siamese networks.

Siamese networks :- A Siamese networks consists of two identical neural networks, each taking one of the two input images. The last layers of the two networks are then fed to a contrastive loss function , which calculates the similarity between the two images. Each image in the image pair is fed to one of these networks.

if you want to know more about [contrastive](http://yann.lecun.com/exdb/publis/pdf/hadsell-chopra-lecun-06.pdf)

```python
from multiple_loss.contrastive_loss import contrastive_loss_with_margin
rms = RMSprop()
model.compile(loss=contrastive_loss_with_margin(margin=1), optimizer=rms)
history = model.fit([tr_pairs[:,0], tr_pairs[:,1]], tr_y, epochs=20, batch_size=128, validation_data=([ts_pairs[:,0], ts_pairs[:,1]], ts_y))
```
## installation
```bash
pip install multiple-loss==0.0.7
```
