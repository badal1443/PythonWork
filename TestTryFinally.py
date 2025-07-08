def sample():
    try:
        return 1
    finally:
        return 2
    
if __name__=="__main__":
    print(sample())