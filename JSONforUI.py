__author__ = 'laceyliu'
import json
import sys
class Layer:
    def __init__(self, name, id, bottom, up, param = None):
        self.name = name
        self.id = id
        self.bottom = bottom
        self.up = up
        self.lyParam = param
        self.neuronNum = -1

class JSONExtractor:

    def extracFromFile(self, file_path, out_path):
        JSONLayers = []
        json_file = open(file_path).read()
        data = json.loads(json_file)
        layers = data["layer"]
        for layer in layers:
            if "idx" in layer.keys() and "bottom" in layer.keys() and "top" in layer.keys():
                bt = layer["bottom"]
                tp = layer["top"]
                param = None
                for key in layer.keys():
                    if "_param" in key:
                        param = layer[key]

                JSONLayers.append(Layer(layer["name"], layer["idx"], bt, tp, param))


        #print json.dumps(data, indent=4)

    def calculateNeuronNumber(self, layers):

if __name__ == "__main__":
  jsonPath = sys.argv[1]
  protoPath = sys.argv[2]

  decoder = JSONExtractor()
  decoder.extracFromFile(jsonPath, protoPath)