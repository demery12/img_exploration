import pickle
import csv

def main():
   with open('labels.pickle', 'rb') as handle:
      toCSV = pickle.load(handle)
   #print toCSV
   with open('labels.csv', 'wb') as output_file:
      output_file.write('filename,label\n')
      print toCSV
      for entry in toCSV:
         file_name = entry["file_name"]
         label = entry['responses'][0]['labelAnnotations'][0]['description']
         output_file.write(file_name + ',' + label + '\n')
 
   '''
   with open('labels.csv', 'wb') as output_file:
      dict_writer = csv.DictWriter(output_file, keys)
      dict_writer.writeheader()
      dict_writer.writerows(toCSV)
   '''
if __name__ =='__main__':
   main()