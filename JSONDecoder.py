import json
import sys, getopt

# This JSON decoder decode JSON format file to
# caffe configuration format file
import sys
class JSONDecoder:
  def decodeFromFile(self, file_path, output_path):
    json_data=open(file_path).read()
    caffe_data = self.decode(json_data)
    f = open(output_path,'w+')
    f.write(caffe_data)
    f.close()

  def decodeFromFileAndSet(self, file_path, output_path, dic={}):
    json_data=open(file_path).read()
    caffe_data = self.SetAndDecode(json_data, dic)
    f = open(output_path,'w+')
    f.write(caffe_data)
    f.close()

  def SetAndDecode(self, j='', dic={}):
    if len(j) == 0:
      return
    data = json.loads(j)
    for key, value in dic.iteritems():
      data[key] = value
    return self.decodeRootDictToStr(data, 0)

  def decode(self, j=''):
    if len(j) == 0:
      return
    data = json.loads(j)
    return self.decodeRootDictToStr(data, 0)

  def decodPairToStr(self, key, value):
    res = ""
    res += str(key)
    res += ": "
    if isinstance(value, str):
      if value.isupper():
        res += value
      else:
        res += "\"" + value +"\""
    else:
      res += str(value)
    res +="\n"
    return res

  def decodeValueToStr(self, value):
    res = ""
    if isinstance(value, str):
      if value.isupper():
        res += value
      else:
        res += "\"" + value +"\""
    else:
      res += str(value)
    res +="\n"
    return res

  def decodeRootDictToStr(self, dictionary, tab):
    tabs = "  " * tab
    res = ""
    for key,value in dictionary.iteritems():
      if key == "idx":
        continue
      if isinstance(value, dict):
        res += tabs
        res += key
        res += " "
        res += self.decodeDictToStr(value, tab + 1);
      elif isinstance(value, list): # assume list only contains dicts
        for element in value:
          res += tabs
          res += key
          if isinstance(element, dict):
            res += " "
            res += self.decodeDictToStr(element, tab + 1)
          else:
            res += ": "
            res += self.decodeValueToStr(element)
      else:
        res += tabs
        res += self.decodPairToStr(key, value)
    res += (tab - 1) * "  "
    return res

  def decodeDictToStr(self, dictionary, tab):
    tabs = "  " * tab
    res = "{\n"
    for key,value in dictionary.iteritems():
      if key == "idx":
        continue
      if isinstance(value, dict):
        res += tabs
        res += key
        res += " "
        res += self.decodeDictToStr(value, tab + 1);
      elif isinstance(value, list):
        for element in value:
          res += tabs
          res += key

          if isinstance(element, dict):
            res += " "
            res += self.decodeDictToStr(element, tab + 1)
          else:
            res += ": "
            res += self.decodeValueToStr(element)
      else:
        res += tabs
        res += self.decodPairToStr(key, value)
    res += (tab - 1) * "  "
    res += "}\n"
    return res

'''
-c command (train/test)
-i inputfile
-o outputfile

#extra parameters.
-t number of inter
-n network
'''
def main(argv):
  inputfile = ''
  outputfile = ''
  command = ''
  iter = 3
  decoder = JSONDecoder()
  net = ""
  try:
    opts, args = getopt.getopt(argv,"hc:i:o:t:",["command=","ifile=","ofile=","iter="])
  except getopt.GetoptError:
    print 'test.py -i <inputfile> -o <outputfile>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-o", "--ofile"):
      outputfile = arg
    elif opt in ("-c", "--command"):
      command = arg
    elif opt in ("-t", "--iter"):
      iter = int(arg)
    else:
      sys.exit()

  parameters = {"max_iter":iter}
  if net != "":
    parameters["net"] = net
  if command == "train":
    decoder.decodeFromFileAndSet(inputfile, outputfile, parameters)
  elif command == "test":
    decoder.decodeFromFile(inputfile, outputfile)

if __name__ == "__main__":
  main(sys.argv[1:])