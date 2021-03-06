from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

ds = SupervisedDataSet(2, 1)

# Dormiu e Estudou e Nota 
ds.addSample((0.8, 0.4), (0.7))
ds.addSample((0.6, 0.7), (0.7))
ds.addSample((0.7, 0.7), (0.8))
ds.addSample((0.8, 0.7), (0.95))
ds.addSample((0.5, 0.7), (0.5))
ds.addSample((1.0, 0.8), (0.10))

nn = buildNetwork(2, 4, 1, bias=True)

trainer = BackpropTrainer(nn, ds)

for i in xrange(2000):
    print(trainer.train())

while True:
    dormiu = float(raw_input('Dormiu:\n'))
    estudou = float(raw_input('Estudou:\n'))
    
    z = nn.activate((dormiu, estudou))[0] * 10.0

    print('Previsao de nota: ', str(z))