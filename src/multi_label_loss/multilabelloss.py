import tensorflow.keras.backend as k
from tensorflow.keras.losses import Loss
class MultilabelLoss(Loss):
    def __init__(self,num_class):
        super().__init__()
        self.num_class=num_class
    def call(self,y_true,y_pred):
        loss=0
        for i in range(self.num_class):
            loss_pos= -1 * k.mean( y_true[:,i] * k.log(y_pred[:,i]))
            loss_neg= -1 * k.mean(( 1 - y_true[:,i])* k.log(1 - y_pred[:,i]))
            loss+=loss_pos+loss_neg
        return loss