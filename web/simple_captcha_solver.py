import pytesseract
import sys
import argparse
from PIL import Image
from subprocess import check_output
import numpy as np
import requests

def resolve(path):
	# check_output(['convert', path, '-resample', '600', path])
	web_img = requests.get('https://example.com')
	if web_img.status_code == 200:
		with open('pew.png', 'wb') as f:
			for chunk in web_img.iter_content(1024):
				f.write(chunk)

	img = Image.open('pew.png')
	# img = img.resize((600,150),1)
	img = img.convert('RGB')
	dat = np.array(img)

	# remove grey stripes
	rgb = dat[:,:,:3]

	grey = [172,172,172]
	white = [255,255,255]
	black = [0,0,0]
	black2 = [10,10,10]

	mask = np.all(rgb >= grey, axis = -1)
	dat[mask] = white

	# make everything except white black
	rgb = dat[:,:,:3]

	mask = np.all(rgb != white, axis = -1)
	dat[mask] = black


	new_img = Image.fromarray(dat)
	new_img.save('bla.png')

	for x in range(0,13):
		try:
			config = '--psm ' + str(x) + ' --oem 3 -c tessedit_char_whitelist=0123456789'
			tst = Image.open('bla.png')
			print(pytesseract.image_to_string(tst,config=config))
			Image.close(tst)
		except:
			print('error on mode: {}'.format(x))

	return pytesseract.image_to_string(Image.open('bla.png'),config='--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789')

if __name__ == "__main__":
	argparser = argparse.ArgumentParser()
	argparser.add_argument('path',help = 'Captcha file path')
	args = argparser.parse_args()
	path = args.path
	print('Resolving Captcha')
	pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
	captcha_text = resolve(path)
	print('Extracted Text',captcha_text)
