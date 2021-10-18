#!/usr/bin/python3

import base64
import hashlib
from logging import NullHandler, root
import sys
import os
from Crypto import Random
from Crypto.Cipher import AES
from werkzeug.exceptions import abort
from functools import wraps
from flask import Flask, render_template, request, url_for, flash, redirect, session, make_response, g
import werkzeug
import ssl
import OpenSSL
from OpenSSL import crypto
from certutils import CertInfo, verify_certificate_chain

def validate_certificate(file):
    
    trusted_certs = ['./ca.crt', './app.crt']

    for root_cert in trusted_certs:
        if not os.path.isfile(root_cert):
            raise Exception("Cannot found root certs")

    clientcert = file.stream.read()

    return verify_certificate_chain(clientcert, trusted_certs)


app = Flask(__name__)

app.config['SECRET_KEY'] = 'xxxxxxxxxxxxxxxx'

ROLE_ADMIN = 0
ROLE_USER = 1

@app.route("/flag")
def flag():
    flag = "You are not admin"
    if session["role"] == ROLE_ADMIN:
        flag = "ASCIS{xxxxxx}"
    return flag

# This function only for admin
@app.route("/logincert", methods=('GET', 'POST'))
def logincert():
    if request.method == 'POST':
        username = None
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            split_tup = os.path.splitext(uploaded_file.filename)
            if split_tup[1] != ".pem":
                flash('Cert file is invalid')
                return render_template('logincert.html')
            else:    
                username = validate_certificate(uploaded_file)

        if username is None:
            flash('Login cert is invalid!')
            return render_template('logincert.html')
        else:    
            session["username"] = username
            session["role"] = ROLE_ADMIN

            return redirect(url_for('index'))

    return render_template('logincert.html')

app.run(host="0.0.0.0", port=8100, debug=False)