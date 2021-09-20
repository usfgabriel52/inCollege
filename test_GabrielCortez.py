import sys
import io
from typing import NoReturn
import pytest

from pytest_mock import mocker
import main
#tests for stories 4,5,6

def test_Main_Menu():
    sys.stdin = io.StringIO('0')
    assert main.display_MainMenu() == None

def test_findJob():
    sys.stdin = io.StringIO('1 \n 0\n')
    
    
    assert main.display_MainMenu() == None

def test_findSomeone():
    sys.stdin = io.StringIO('1 \n 0\n')
    
    
    assert main.display_MainMenu() == None

def test_skillsMenu():
    sys.stdin = io.StringIO('3 \n 1\n2\n3\n4\n5\n0\n0\n')
    
    assert main.display_MainMenu() == None    





