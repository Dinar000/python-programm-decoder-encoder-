import hashlib
import time

print("Encoder By Dinar!")
print("YouTube: https://www.youtube.com/channel/UCpPdugSd_OrYesemb2WJHjA")

while True:
	counter = 0
	print()
	print('Функции:')
	time.sleep(0.4)
	print('1. Декодер md5')
	print('2. Зашифровщик md5')
	print('3. Зашифровщик sha256')
	print('4. Зашифровщик sha512')
	print('5. Зашифровщик sha1')
	print()
	time.sleep(0.4)
	menu_select = int(input('Выбор: '))
	if menu_select == 1:
		md5_pass = input("Введи md5 пароль: ")
		md5_file = input("Путь к словарю паролей: ")
		
		try:
			md5_file = open(md5_file, 'r', encoding="utf8")
			print("Идёт подбор пароля, ожидай.. (если словарь очень большой, будет очень долго)")
		except:
			print()
			print('Путь к файлу не найден!')
			
		for password in md5_file:
			hash_obj = hashlib.md5(password.strip().encode('utf-8')).hexdigest()

			if hash_obj == md5_pass:
				print("\nПароль найден! Пароль:", password)
				time.sleep(1)
				break

		else:
			print("\nПароль не найден!")

	elif menu_select == 2:
		input_md5 = input('Текст: ')
		time.sleep(0.4)
		print("Хэш md5:", hashlib.md5(input_md5.encode('UTF-8')).hexdigest())
	elif menu_select == 3:
		input_sha256 = input('Текст: ')
		time.sleep(0.4)
		print("Хэш sha256:", hashlib.sha256(input_sha256.encode('UTF-8')).hexdigest())
		print()
	elif menu_select == 4:
		input_sha512 = input('Текст: ')
		time.sleep(0.4)
		print("Хэш sha512:", hashlib.sha512(input_sha512.encode('UTF-8')).hexdigest())
	elif menu_select == 5:
		input_sha1 = input('Текст: ')
		time.sleep(0.4)
		print("Хэш sha1:", hashlib.sha1(input_sha1.encode('UTF-8')).hexdigest())
	else:
		print("Ошибка!")
		time.sleep(0.4)