# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
import credentials

driver = webdriver.Chrome('chromedriver.exe')

driver.get(url="https://www.instagram.com/accounts/login")

def is_the_page_ready(driver, id):
    try:
        ident = driver.find_element_by_id(id)
        return True
    except:
        return False

def login(driver):
    while is_the_page_ready(driver, 'username') != True:
        sleep(0.5)
    username = driver.find_element_by_name("username")
    username.send_keys(credentials.login)
    password = driver.find_element_by_name("password")
    password.send_keys(credentials.senha)
    button_login = driver.find_element_by_class_name('sqdOP  L3NKy   y3zKF     ')
    button_login.click()
    sleep(10)
    button_confirm = driver.find_element_by_class_name('sqdOP  L3NKy   y3zKF  ').click()
    button_confirm.click()


def find_to_follow(driver):
    sleep(3)
    driver.get(url="https://*****")


def click_follow(driver):
    sleep(5)
    driver.find_element_by_class_name('_5f5mN       jIbKX  _6VtSN     yZn4P   ').click()


def click_unfollow(driver):
    sleep(5)
    driver.find_element_by_class_name('_5f5mN       jIbKX  _6VtSN     yZn4P   ').click()


login(driver)
find_to_follow(driver)
click_follow(driver)
click_unfollow(driver)