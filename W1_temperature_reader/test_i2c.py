#!/usr/bin/env python3
import pytest
import sh_i2c

def test_i2cRead() -> None:
    client = sh_i2c.I2C_client(2, 0x18)
    data = client.readByte()
    assert data == 0x18

def test_i2cWrite1() -> None:
    client = sh_i2c.I2C_client(2, 0x18)
    assert client.WriteByte(0xf0) == True

def test_i2cWrite2() -> None:
    client = sh_i2c.I2C_client(2, 0x18)
    assert client.WriteByte(0xfff) == False

def test_i2cWrite3() -> None:
    client = sh_i2c.I2C_client(2, 0x18)
    assert client.WriteByte(0xe1, 0xf0) == True