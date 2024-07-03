from model.model import Model

myModel = Model()
myModel.buildGraph(60*60*1000)
print(myModel.getGraphDetails())

myModel.getNodeI(261)
#myModel.getSetAlbum(myModel.getNodeI(1), 261, )
