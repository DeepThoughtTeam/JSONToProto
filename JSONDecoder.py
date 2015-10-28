import simplejson as json

# This JSON decoder decode JSON format file to
# caffe configuration format file

class JSONDecoder:
  def decodeFromFile(self, file_path, output_path):
    json_data=open("data/jsonsample.json").read()
    caffe_data = self.decode(json_data)
    open(output_path,'w').write(caffe_data)

  def decode(self, j=''):
    if len(j) == 0:
      return
    data = json.loads(j)
    return self.decodeDictToStr(data, 0)

  def decodPairToStr(self, key, value):
    res = ""
    res += str(key)
    res += ":"
    if isinstance(value, str) and value != "MAX":
      res += "\"" + value +"\""
    else:
      res += str(value)
    res +="\n"
    return res

  def decodeValueToStr(self, value):
    res = ""
    if isinstance(value, str) and value != "MAX":
      res += "\"" + value +"\""
    else:
      res += str(value)
    res +="\n"
    return res

  def decodeDictToStr(self, dictionary, tab):
    tabs = "  " * tab
    res = "{\n"
    for key,value in dictionary.iteritems():

      if isinstance(value, dict):
        res += tabs
        res += key
        res += ":"
        res += self.decodeDictToStr(value, tab + 1);
      elif isinstance(value, list): # assume list only contains dicts
        for element in value:
          res += tabs
          res += key
          res += ":"
          if isinstance(element, dict):
            res += self.decodeDictToStr(element, tab + 1)
          else:
            res += self.decodeValueToStr(element)
      else:
        res += tabs
        res += self.decodPairToStr(key, value)
    res += tabs
    res += "}\n"
    return res

if __name__ == "__main__":
  decoder = JSONDecoder()
  decoder.decodeFromFile("data/jsonsample.json", "data/jsonsample.prototxt")
