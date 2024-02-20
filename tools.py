import sys
  
def debug(*args, **kwargs):
    print("DEBUG :",*args, **kwargs, file = sys.stder)