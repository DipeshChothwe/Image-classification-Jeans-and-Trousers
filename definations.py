import shutil
import os
import requests
import pandas as pd

#Info abt images
def scrap_image_url(driver,page):
  images = driver.find_elements_by_xpath("//img[@class='_3togXc']")
  print(len(images))

  product_data = {}
  product_data['image_url'] = []
  count = 40*page-40
  for image in images:
    source = image.get_attribute('src')
    count = count + 1
    if(count < 101):
      print(count)
      product_data['image_url'].append(source)

  return product_data

#Info abt images
def scrap_image_url_test(driver,page):
  images = driver.find_elements_by_xpath("//img[@class='_3togXc']")
  print(len(images))

  product_data = {}
  product_data['image_url'] = []
  count = 0
  for image in images:
    source = image.get_attribute('src')
    count = count + 1
    if(count < 31):
      print(count)
      product_data['image_url'].append(source)

  return product_data

#making directory to store image
def make_directory(data_use,dirname):
    path = os.path.join('G:\FliproboAssgn', data_use, dirname)
    if not os.path.exists(path):
        os.makedirs(path)

#To save image
def save_images(data, data_use, dirname, page):
    for index, link in enumerate(data['image_url']):
        print("downloading image", index + 1, "of", len(data['image_url']))
        response = requests.get(link)
        with open('{0}/{1}/img_{2}{3}.jpeg'.format(data_use, dirname, page, index), "wb") as file:
            file.write(response.content)
