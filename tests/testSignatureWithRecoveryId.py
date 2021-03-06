# coding=utf-8

from unittest.case import TestCase
from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.signature import Signature
from ellipticcurve.utils.compatibility import *


class SignatureTest(TestCase):

    def testDerConversion(self):
        privateKey = PrivateKey()
        message = "This is a text message"

        signature1 = Ecdsa.sign(message, privateKey)

        der = signature1.toDer(withRecoveryId=True)
        signature2 = Signature.fromDer(toBytes(der), recoveryByte=True)

        self.assertEqual(signature1.r, signature2.r)
        self.assertEqual(signature1.s, signature2.s)
        self.assertEqual(signature1.recid, signature2.recid)

    def testBase64Conversion(self):
        privateKey = PrivateKey()
        message = "This is a text message"

        signature1 = Ecdsa.sign(message, privateKey)

        base64 = signature1.toBase64(withRecoveryId=True)

        signature2 = Signature.fromBase64(base64, recoveryByte=True)

        self.assertEqual(signature1.r, signature2.r)
        self.assertEqual(signature1.s, signature2.s)
        self.assertEqual(signature1.recid, signature2.recid)
