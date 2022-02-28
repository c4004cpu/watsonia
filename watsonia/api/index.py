#!/usr/bin/env python3

from flask import Flask, request, jsonify
from ._app import app

@app.route("/", methods=["GET"])
def get_index():
    return jsonify({})
