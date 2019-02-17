from flask import Flask, request

app=Flask(__name__, instance_relative_config=True)

from app import views

app.config.from_object('config')