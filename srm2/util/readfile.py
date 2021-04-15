def readtxt():
    filepath = r'D:\apache-jmeter-5.3\apache-jmeter-5.3\testdata\import.txt'
    with open(filepath,'r') as f:
        filenames = f.readlines()
        # print(filenames)
        for line in filenames:
            filename = line.strip('\n')
            print(filename)
