from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import os
from nonebot.log import logger
import shutil
import asyncio

async def generate_otto(driver, text, original_disk_mode, path):
	textarea = driver.find_element(By.XPATH, '//textarea[@class="el-textarea__inner"]')
	textarea.clear()
	textarea.send_keys(text)

	if original_disk_mode:
		switch_button = driver.find_element(By.CLASS_NAME, "el-switch__input")
		driver.execute_script("arguments[0].click();", switch_button)

	button = driver.find_element(By.XPATH, '//button/span[text()="生成otto鬼叫"]')
	button.click()
	
	await asyncio.sleep(5)
	
	download_button = driver.find_element(By.XPATH, '//button[@class="el-button el-button--primary" and span[text()="下载原音频"]]')
	download_button.click()
	
	driver.quit()
	
	files = await get_files_in_directory(path)
	if files:
		return files[0]
	return None


async def get_files_in_directory(path):
	file_list = []
	for root, dirs, files in os.walk(path):
		for file in files:
			file_list.append(os.path.join(root, file))
	return file_list


async def clear_directory(path):
	for root, dirs, files in os.walk(path):
		for file in files:
			os.remove(os.path.join(root, file))
		for dir in dirs:
			shutil.rmtree(os.path.join(root, dir))


async def call_otto(text, ysdd, path, website):
	await clear_directory(path)
	logger.info("Directory cleaned.")
	
	options = Options()
	options.add_argument("--headless")

	options.set_preference("browser.download.folderList", 2)
	options.set_preference("browser.download.manager.showWhenStarting", False)
	options.set_preference("browser.download.dir", path)
	options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

	driver = webdriver.Firefox(options=options)

	driver.get(website)
	
	first_file = await generate_otto(driver, text, ysdd, path)
	logger.info(f"Executed. File: {first_file}")
	return first_file

