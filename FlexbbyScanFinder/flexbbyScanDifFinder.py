# coding=utf-8
import clr
import json
import os
import tempfile
import urllib2
import shutil
import collections
from urlparse import urlparse
from os.path import splitext
from io import open as iopen
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# Покдлючаем dll
clr.AddReferenceToFileAndPath(r"D:\Program Files (x86)\ABBYY ScanDifFinder SDK\1.0\ABBYY.ScanDifFinder.dll")
# Импортим основной класс ScanDifFinder
from ABBYY.ScanDifFinder import ScanDifFinder
print('ABBY.ScanDifFinder import seccessfuly')
# Доступ к продукту на основании открытой лицензии.
# finder.SetLocalLicenseFile('./ABBYY ScanDifFinder SDK/1.0/Engine/Bin') # TODO: Уточнить по поводу лцензии!!!
# Массив разрешённых расширений файлов
possible_exts = {'.pdf', '.doc', '.docx', '.jpg', '.png', '.rtf', '.xls', '.xlsx', '.tif'}
class RequestHandler(BaseHTTPRequestHandler):
	def do_POST(self):
		print('---------------')
		# Читаем переданные данные
		content_len = int(self.headers.getheader('content-length', 0))
		post_body = self.rfile.read(content_len)
		# Парсим в словарь
		files_dict = json.loads(post_body)
		# Создаём новый объект ScanDifFinder
		finder = ScanDifFinder()
		# Создаём папку для хранения докумнетов
		dirpath = tempfile.mkdtemp()
		print('Temporary directory' + '\033[92m' + ' created. ' + '\033[0m' + '\033[93m' + 'Path = ' + str(dirpath) + '\033[0m')
		# Обработчик сохранения файла
		def fileDownloader(file_url, file_name):
			try:
				print('\033[93m'+'Download file from ==> '+'\033[0m' + file_url)
				open_file = urllib2.urlopen(file_url)
				parsed = urlparse(file_url)
				root, extension = splitext(parsed.path)
				# Проверка расширения на совпадение из массива
				if extension.lower() in possible_exts:
					# Формируем имя файла с расширением
					doc_name = dirpath + '/' + file_name + extension.lower()
					# Пишем файл
					with iopen(doc_name, 'wb') as file:
						file.write(open_file.read())
						#
						print(str(doc_name) + '\033[92m' + ' download seccessfully' + '\033[0m')
						# Возвращаем имя файла
						return doc_name		
				else:
					return False
			except urllib2.HTTPError, e:
				print("HTTP Error:" + str(e.code) + file_url)
				return False
			except urllib2.URLError, e:
				print ("URL Error:" + str(e.reason) + file_url)
				return False
		# Скачиваем эталонный документ
		original_file = fileDownloader(files_dict['original'], 'original_doc')
		# Скачиваем сравниваемый документ
		user_file = fileDownloader(files_dict['document'], 'user_doc')
		# Вызывает CompareFiles для сравнения документов. (Путь к эталонному документу, путь к документу с которым сравниваем, путь сохранения результата)
		try:
			finder_result = finder.CompareFiles(original_file, user_file,  dirpath)
			print('Compared files' + '\033[92m' + ' seccessfully' + '\033[0m')
			# Создаём переменную, содержащую все изменения
			result = finder_result.AllChanges
			# Создаём массив для хранения обработаных результатов сравнивания
			result_list = []
			# Заполняем массив словарями с данными
			for x in result:
				# Обработчик по координатам прямоугольников несовпадений
				def location(location):	
					# Применяет метод, который возвращает массив координат несовпадений
					position = location.GetRelativeChangePosition()
					# Узнаём длинну массива  
					pos_len = len(position)
					# Создаём массив для хранения обработанных координат
					loc_list = []
					# Обработчик создания словаря координат. Создаёт словарь на каждое несовпадение, который содержит X Y Height Width прямоугольника несовпадения. 
					for z in position:
						# Получаем индекс для обращения в массив с необработанными данными
						index = pos_len - 1
						# Создаём словарь одного несовпадения
						loc_dict = {
							key: float(getattr(position[index], key))
							for key in ('X','Y','Height','Width') 
						}
						# Добавляем словарь в массив
						loc_list.append(loc_dict)
					# Если массив содержит только один словарь, приваиваим ему это значение
					if len(loc_list) == 1:
						loc_list = loc_list[0]
					# Возвращаем массив с обработанными данными
					return loc_list
				# Создаём словарь с информацией одного несовпадения
				result_dict = dict(
					ChangeType=str(x.ChangeType),
					RefLocation=location(x.RefLocation), 
					RefText=x.RefText,
					UserLocation=location(x.UserLocation),
					UserText=x.UserText,
					Description=x.Description,
					EditLength=x.EditLength,
					RefDescription=x.RefDescription,
					UserDescription=x.UserDescription
					)
				# Обработчик инкодинга полученных данных. (https://stackoverflow.com/questions/1254454/fastest-way-to-convert-a-dicts-keys-values-from-unicode-to-str)
				def convert(data):
					if isinstance(data, basestring):
						return data.encode('utf-8')
					elif isinstance(data, collections.Mapping):
						return dict(map(convert, data.iteritems()))
					elif isinstance(data, collections.Iterable):
						return type(data)(map(convert, data))
					else:
						return data
				# Конвертируем словарь
				result_dict = convert(result_dict)
				# Добавляем словарь в массив
				result_list.append(result_dict)
			# Конвертируем в JSON массив
			json_list = json.dumps(result_list)
			print('\033[93m' + 'JSON created' + '\033[0m')	
			# Вывод в консоль
			return json_list			
		finally:
			# Удаляем временную папку
			shutil.rmtree(dirpath)
			print('Temporary directory' + '\033[92m' + ' deleted' + '\033[0m')
			print('---------------')
# Threading HTTP-Server
if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8000), RequestHandler)
    print ('\033[92m'+'Starting server....'+'\033[0m')
    print ('\033[94m'+'Use <Ctrl-C> to STOP'+'\033[0m') 
    server.serve_forever()